"""Check URLs in OIR source records for accessibility.

Reports broken, redirected, or inaccessible URLs found in bibliography
source records. Designed to be run periodically to detect link rot.

Usage:
    python tools/check_urls.py          # Check all source records
    python tools/check_urls.py --quiet  # Only show problems
"""

from __future__ import annotations

import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

try:
    import yaml
except ImportError:
    print("PyYAML is required. Install docs dependencies with: python -m pip install -e .[docs]")
    raise SystemExit(2)


ROOT = Path(__file__).resolve().parents[1]
BIBLIOGRAPHY_DIR = ROOT / "bibliography"
URL_PATTERN = re.compile(r"https?://[^\s>)\]\"']+")
METADATA_URL_PATTERN = re.compile(r"^-\s+(?:URL|Archive URL|Access date):\s*(https?://\S+)", re.IGNORECASE)
USER_AGENT = "OIR-LinkChecker/1.0 (Open Internet Reference; link verification)"
TIMEOUT = 15  # seconds per request
DELAY = 1.0  # seconds between requests to avoid rate limiting

# Sites known to block automated requests (403 from these is expected)
BOT_BLOCKING_DOMAINS = {
    "justia.com",
    "supreme.justia.com",
    "law.justia.com",
    "cdt.org",
    "ij.org",
    "opencasebook.org",
}


@dataclass
class URLCheckResult:
    path: Path
    record_id: str
    url: str
    status: str  # "ok", "broken", "redirect", "timeout", "error"
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


def extract_urls(path: Path) -> list[str]:
    """Extract all URLs from a source record's bibliographic metadata section."""
    urls: list[str] = []
    text = path.read_text(encoding="utf-8")
    in_metadata = False

    for line in text.splitlines():
        if line.startswith("## "):
            in_metadata = line.strip().lower() == "## bibliographic metadata"
            continue
        if in_metadata:
            match = METADATA_URL_PATTERN.match(line)
            if match:
                urls.append(match.group(1).rstrip(".,:;"))

    return urls


def check_url(url: str) -> URLCheckResult:
    """Check if a URL is accessible. Returns status information."""
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
        # Some servers reject HEAD, try GET
        if e.code == 405:
            return _check_url_get(url)
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


def _check_url_get(url: str) -> URLCheckResult:
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
    source_files = iter_source_records()

    if not source_files:
        print("No source records found.")
        return 0

    results: list[URLCheckResult] = []
    checked = 0
    problems = 0

    print(f"Checking URLs in {len(source_files)} source records...\n")

    for path in source_files:
        metadata = load_front_matter(path)
        if metadata is None:
            continue

        record_id = metadata.get("id", path.stem)
        urls = extract_urls(path)

        for url in urls:
            time.sleep(DELAY)
            result = check_url(url)
            result.path = path
            result.record_id = record_id
            results.append(result)
            checked += 1

            if result.status == "ok":
                if not quiet:
                    print(f"  ✓ {record_id}: {url}")
            elif result.status == "redirect":
                print(f"  → {record_id}: {url}")
                print(f"    Redirected: {result.detail}")
            else:
                # Check if this is a known bot-blocking domain
                from urllib.parse import urlparse
                domain = urlparse(url).netloc
                is_bot_blocked = any(domain.endswith(d) for d in BOT_BLOCKING_DOMAINS)

                if is_bot_blocked and result.status_code == 403:
                    if not quiet:
                        print(f"  ? {record_id}: {url}")
                        print(f"    Bot-blocked (403) — likely accessible in browser")
                else:
                    problems += 1
                    print(f"  ✗ {record_id}: {url}")
                    print(f"    {result.status.upper()}: {result.detail}")

    print(f"\n{'─' * 60}")
    print(f"Checked {checked} URLs in {len(source_files)} source records.")
    print(f"  OK: {checked - problems}")
    print(f"  Problems: {problems}")

    if problems > 0:
        print(f"\n⚠ {problems} URL(s) need attention. See RESEARCH_DEBT.md or update source records.")
        print("\nNote: Some 403 responses are from bot-blocking (Justia, CDT, IJ, etc.)")
        print("and may still be accessible in a browser. Verify manually before marking broken.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
