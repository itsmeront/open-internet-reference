"""Check URLs in OIR source records for accessibility.

Reports broken, redirected, or inaccessible URLs found in bibliography
source records. Designed to be run periodically to detect link rot.

Usage:
    python tools/check_urls.py              # Check all primary URLs
    python tools/check_urls.py --quiet      # Only show problems
    python tools/check_urls.py --archives   # Also check archive URLs
"""

from __future__ import annotations

import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

try:
    import yaml
except ImportError:
    print("PyYAML is required. Install docs dependencies with: python -m pip install -e .[docs]")
    raise SystemExit(2)


ROOT = Path(__file__).resolve().parents[1]
BIBLIOGRAPHY_DIR = ROOT / "bibliography"
PRIMARY_URL_PATTERN = re.compile(r"^-\s+URL:\s*(https?://\S+)", re.IGNORECASE)
ARCHIVE_URL_PATTERN = re.compile(r"^-\s+Archive URL:\s*(https?://\S+)", re.IGNORECASE)
USER_AGENT = "OIR-LinkChecker/1.0 (Open Internet Reference; link verification)"
TIMEOUT = 15  # seconds per request
DEFAULT_DELAY = 1.0  # seconds between requests to avoid rate limiting
MAX_RETRIES = 2  # number of retries on 429

# Per-domain delay overrides (seconds) for rate-limited or sensitive sites
DOMAIN_DELAYS: dict[str, float] = {
    "web.archive.org": 5.0,
    "archive.org": 5.0,
}

# Sites known to block automated requests (403 from these is expected)
BOT_BLOCKING_DOMAINS = {
    "justia.com",
    "supreme.justia.com",
    "law.justia.com",
    "cdt.org",
    "ij.org",
    "opencasebook.org",
}

# Archive domains — skipped by default, checked with --archives flag
ARCHIVE_DOMAINS = {
    "web.archive.org",
    "archive.org",
}


@dataclass
class URLCheckResult:
    path: Path
    record_id: str
    url: str
    status: str  # "ok", "broken", "redirect", "timeout", "error", "rate_limited", "skipped"
    status_code: int | None = None
    detail: str = ""


def iter_source_records() -> list[Path]:
    """Find all source record Markdown files in the bibliography."""
    if not BIBLIOGRAPHY_DIR.exists():
        return []
    return sorted(
        path
        for path in BIBLIOGRAPHY_DIR.rglob("*.md")
        if "_templates" not in path.parts and path.name != "README.md"
    )


def load_front_matter(path: Path) -> dict[str, Any] | None:
    """Extract YAML front matter from a Markdown file."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    try:
        _, raw_metadata, _ = text.split("---\n", 2)
    except ValueError:
        return None
    metadata = yaml.safe_load(raw_metadata)
    if not isinstance(metadata, dict):
        return None
    return metadata


@dataclass
class ExtractedURL:
    url: str
    is_archive: bool


def extract_urls(path: Path) -> list[ExtractedURL]:
    """Extract URLs from a source record's bibliographic metadata section."""
    urls: list[ExtractedURL] = []
    text = path.read_text(encoding="utf-8")
    in_metadata = False

    for line in text.splitlines():
        if line.startswith("## "):
            in_metadata = line.strip().lower() == "## bibliographic metadata"
            continue
        if in_metadata:
            match = PRIMARY_URL_PATTERN.match(line)
            if match:
                urls.append(ExtractedURL(url=match.group(1).rstrip(".,:;"), is_archive=False))
                continue
            match = ARCHIVE_URL_PATTERN.match(line)
            if match:
                url_value = match.group(1).rstrip(".,:;")
                if url_value.lower() not in ("none", "none recorded"):
                    urls.append(ExtractedURL(url=url_value, is_archive=True))

    return urls


def delay_for_domain(url: str) -> float:
    """Return the appropriate delay for a given URL's domain."""
    domain = urlparse(url).netloc
    for known_domain, delay in DOMAIN_DELAYS.items():
        if domain.endswith(known_domain):
            return delay
    return DEFAULT_DELAY


def is_archive_url(url: str) -> bool:
    """Check if URL belongs to an archive domain."""
    domain = urlparse(url).netloc
    return any(domain.endswith(d) for d in ARCHIVE_DOMAINS)


def is_bot_blocked_domain(url: str) -> bool:
    """Check if URL belongs to a known bot-blocking domain."""
    domain = urlparse(url).netloc
    return any(domain.endswith(d) for d in BOT_BLOCKING_DOMAINS)


def check_url(url: str, retries: int = MAX_RETRIES) -> URLCheckResult:
    """Check if a URL is accessible. Handles retries on 429."""
    request = Request(url, method="HEAD")
    request.add_header("User-Agent", USER_AGENT)

    try:
        response = urlopen(request, timeout=TIMEOUT)
        code = response.getcode()
        final_url = response.geturl()

        if final_url != url:
            return URLCheckResult(
                path=Path(),
                record_id="",
                url=url,
                status="redirect",
                status_code=code,
                detail=f"Redirected to {final_url}",
            )
        return URLCheckResult(
            path=Path(),
            record_id="",
            url=url,
            status="ok",
            status_code=code,
        )
    except HTTPError as e:
        # Handle 429 Too Many Requests with retry
        if e.code == 429:
            if retries > 0:
                retry_after = _parse_retry_after(e)
                wait_time = retry_after if retry_after else 30.0
                print(f"    ⏳ Rate limited (429). Waiting {wait_time:.0f}s before retry...")
                time.sleep(wait_time)
                return check_url(url, retries - 1)
            return URLCheckResult(
                path=Path(),
                record_id="",
                url=url,
                status="rate_limited",
                status_code=429,
                detail="Rate limited (429) after retries exhausted",
            )
        # Some servers reject HEAD, try GET
        if e.code == 405:
            return _check_url_get(url, retries)
        return URLCheckResult(
            path=Path(),
            record_id="",
            url=url,
            status="broken",
            status_code=e.code,
            detail=f"HTTP {e.code}: {e.reason}",
        )
    except TimeoutError:
        return URLCheckResult(
            path=Path(),
            record_id="",
            url=url,
            status="timeout",
            detail=f"Timeout after {TIMEOUT}s",
        )
    except URLError as e:
        return URLCheckResult(
            path=Path(),
            record_id="",
            url=url,
            status="error",
            detail=str(e.reason),
        )
    except Exception as e:
        return URLCheckResult(
            path=Path(),
            record_id="",
            url=url,
            status="error",
            detail=str(e),
        )


def _parse_retry_after(error: HTTPError) -> float | None:
    """Parse Retry-After header from a 429 response."""
    try:
        retry_header = error.headers.get("Retry-After")
        if retry_header is None:
            return None
        # Retry-After can be seconds (integer) or an HTTP date
        try:
            return float(retry_header)
        except ValueError:
            # Could be an HTTP date; default to 30 seconds
            return 30.0
    except Exception:
        return None


def _check_url_get(url: str, retries: int = MAX_RETRIES) -> URLCheckResult:
    """Fallback GET request for servers that reject HEAD."""
    request = Request(url)
    request.add_header("User-Agent", USER_AGENT)

    try:
        response = urlopen(request, timeout=TIMEOUT)
        code = response.getcode()
        return URLCheckResult(
            path=Path(),
            record_id="",
            url=url,
            status="ok",
            status_code=code,
        )
    except HTTPError as e:
        if e.code == 429:
            if retries > 0:
                retry_after = _parse_retry_after(e)
                wait_time = retry_after if retry_after else 30.0
                print(f"    ⏳ Rate limited (429). Waiting {wait_time:.0f}s before retry...")
                time.sleep(wait_time)
                return _check_url_get(url, retries - 1)
            return URLCheckResult(
                path=Path(),
                record_id="",
                url=url,
                status="rate_limited",
                status_code=429,
                detail="Rate limited (429) after retries exhausted",
            )
        return URLCheckResult(
            path=Path(),
            record_id="",
            url=url,
            status="broken",
            status_code=e.code,
            detail=f"HTTP {e.code}: {e.reason}",
        )
    except Exception as e:
        return URLCheckResult(
            path=Path(),
            record_id="",
            url=url,
            status="error",
            detail=str(e),
        )


def main() -> int:
    quiet = "--quiet" in sys.argv or "-q" in sys.argv
    check_archives = "--archives" in sys.argv
    source_files = iter_source_records()

    if not source_files:
        print("No source records found.")
        return 0

    results: list[URLCheckResult] = []
    checked = 0
    skipped = 0
    problems = 0
    bot_blocked = 0
    rate_limited = 0

    print(f"Checking URLs in {len(source_files)} source records...")
    if not check_archives:
        print("  (Skipping archive URLs — use --archives to include them)")
    print()

    for path in source_files:
        metadata = load_front_matter(path)
        if metadata is None:
            continue

        record_id = metadata.get("id", path.stem)
        extracted = extract_urls(path)

        for item in extracted:
            url = item.url

            # Skip archive URLs unless --archives flag is set
            if item.is_archive and not check_archives:
                skipped += 1
                if not quiet:
                    print(f"  ⊘ {record_id}: {url} (archive — skipped)")
                continue

            # Apply per-domain delay
            delay = delay_for_domain(url)
            time.sleep(delay)

            result = check_url(url)
            result.path = path
            result.record_id = record_id
            results.append(result)
            checked += 1

            if result.status == "ok":
                if not quiet:
                    print(f"  ✓ {record_id}: {url}")
            elif result.status == "redirect":
                if not quiet:
                    print(f"  → {record_id}: {url}")
                    print(f"    Redirected: {result.detail}")
            elif result.status == "rate_limited":
                rate_limited += 1
                print(f"  ⏳ {record_id}: {url}")
                print(f"    Rate limited — try again later or use --archives sparingly")
            else:
                # Check if this is a known bot-blocking domain
                if is_bot_blocked_domain(url) and result.status_code == 403:
                    bot_blocked += 1
                    if not quiet:
                        print(f"  ? {record_id}: {url}")
                        print(f"    Bot-blocked (403) — likely accessible in browser")
                else:
                    problems += 1
                    print(f"  ✗ {record_id}: {url}")
                    print(f"    {result.status.upper()}: {result.detail}")

    print(f"\n{'─' * 60}")
    print(f"Checked {checked} URLs in {len(source_files)} source records.")
    print(f"  OK:           {checked - problems - bot_blocked - rate_limited}")
    print(f"  Bot-blocked:  {bot_blocked} (likely fine in browser)")
    print(f"  Rate-limited: {rate_limited} (retry later)")
    print(f"  Problems:     {problems}")
    if skipped:
        print(f"  Skipped:      {skipped} archive URLs (use --archives to check)")

    if problems > 0:
        print(f"\n⚠ {problems} URL(s) need attention.")
        print("  Update source records with archive URLs or mark as research debt.")
        return 1

    if rate_limited > 0:
        print(f"\n⚠ {rate_limited} URL(s) were rate-limited. Try again later.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
