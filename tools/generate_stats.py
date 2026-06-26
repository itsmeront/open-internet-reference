"""Generate anonymous usage statistics for OIR.

Reads nginx access logs and MCP request logs to produce a summary
statistics page. No personal data (IPs, user agents) is stored or
displayed — only aggregate counts.

Usage:
    python tools/generate_stats.py                    # Generate stats page
    python tools/generate_stats.py --nginx-log FILE   # Custom nginx log path
    python tools/generate_stats.py --mcp-log FILE     # Custom MCP log path

Output:
    website/generated/stats.md — generated statistics page for the site
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
WEBSITE_GENERATED_DIR = ROOT / "website" / "generated"
STATS_FILE = WEBSITE_GENERATED_DIR / "stats.md"
MCP_STATS_FILE = ROOT / "generated" / "mcp-stats.json"

# Default log locations on the server
DEFAULT_NGINX_LOG = "/var/log/nginx/access.log"
DEFAULT_MCP_LOG = "/opt/oir/mcp-requests.log"

# Nginx log pattern (common log format)
# We only extract: date, method, path, status — NO IP addresses stored
NGINX_PATTERN = re.compile(
    r'\S+ - \S+ \[([^\]]+)\] "(\w+) ([^\s]+) [^"]*" (\d+) \d+'
)

# Pages to exclude from stats (assets, admin internals)
EXCLUDE_PATTERNS = [
    r"^/assets/",
    r"^/admin/config\.yml",
    r"^/favicon\.ico",
    r"^/sitemap\.xml",
    r"^/search/",
    r"\.(css|js|png|jpg|jpeg|gif|ico|svg|woff|woff2|map)$",
]


def parse_nginx_log(log_path: str) -> list[dict[str, str]]:
    """Parse nginx access log, extracting only date, path, and status. No IPs."""
    entries = []
    path = Path(log_path)

    if not path.exists():
        return entries

    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        match = NGINX_PATTERN.match(line)
        if not match:
            continue

        date_str, method, request_path, status = match.groups()

        # Only count GET requests with 200 status
        if method != "GET" or status != "200":
            continue

        # Exclude asset requests
        if any(re.match(pattern, request_path) for pattern in EXCLUDE_PATTERNS):
            continue

        # Parse date (format: "25/Jun/2026:21:17:26 +0000")
        try:
            dt = datetime.strptime(date_str.split()[0], "%d/%b/%Y:%H:%M:%S")
            date_key = dt.strftime("%Y-%m-%d")
        except ValueError:
            continue

        entries.append({
            "date": date_key,
            "path": request_path,
        })

    return entries


def parse_mcp_log(log_path: str) -> list[dict[str, str]]:
    """Parse MCP request log for tool usage stats."""
    entries = []
    path = Path(log_path)

    if not path.exists():
        return entries

    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        try:
            entry = json.loads(line)
            entries.append(entry)
        except json.JSONDecodeError:
            continue

    return entries


def compute_page_stats(entries: list[dict[str, str]]) -> dict[str, Any]:
    """Compute aggregate page view statistics."""
    if not entries:
        return {"total_views": 0, "days": 0, "top_pages": [], "daily_views": {}}

    daily_views: Counter[str] = Counter()
    page_views: Counter[str] = Counter()

    for entry in entries:
        daily_views[entry["date"]] += 1
        page_views[entry["path"]] += 1

    # Top pages (clean up paths for display)
    top_pages = [
        (path.rstrip("/") or "/", count)
        for path, count in page_views.most_common(20)
    ]

    return {
        "total_views": len(entries),
        "days": len(daily_views),
        "avg_daily": len(entries) // max(len(daily_views), 1),
        "top_pages": top_pages,
        "daily_views": dict(sorted(daily_views.items())[-30:]),  # Last 30 days
    }


def compute_mcp_stats(entries: list[dict[str, str]]) -> dict[str, Any]:
    """Compute aggregate MCP usage statistics."""
    if not entries:
        return {"total_requests": 0, "tool_usage": {}, "topic_queries": []}

    tool_usage: Counter[str] = Counter()
    daily_requests: Counter[str] = Counter()

    for entry in entries:
        tool_usage[entry.get("tool", "unknown")] += 1
        date = entry.get("date", "unknown")
        daily_requests[date] += 1

    return {
        "total_requests": len(entries),
        "days": len(daily_requests),
        "tool_usage": dict(tool_usage.most_common()),
        "daily_requests": dict(sorted(daily_requests.items())[-30:]),
    }


def generate_stats_page(
    page_stats: dict[str, Any],
    mcp_stats: dict[str, Any],
) -> str:
    """Generate the Markdown stats page."""
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# Usage Statistics",
        "",
        f"Last updated: {now}",
        "",
        "These statistics are collected anonymously — no personal information (IP addresses, user agents, or identifiers) is tracked or stored.",
        "",
        "## Site Traffic",
        "",
    ]

    if page_stats["total_views"] > 0:
        lines.extend([
            f"- **Total page views**: {page_stats['total_views']:,}",
            f"- **Days tracked**: {page_stats['days']}",
            f"- **Average daily views**: {page_stats['avg_daily']:,}",
            "",
        ])

        if page_stats["top_pages"]:
            lines.extend(["### Most Visited Pages", ""])
            lines.append("| Page | Views |")
            lines.append("|---|---|")
            for path, count in page_stats["top_pages"][:15]:
                display_path = path if len(path) <= 60 else path[:57] + "..."
                lines.append(f"| `{display_path}` | {count:,} |")
            lines.append("")

        if page_stats["daily_views"]:
            lines.extend(["### Daily Traffic (last 30 days)", ""])
            lines.append("| Date | Views |")
            lines.append("|---|---|")
            for date, count in list(page_stats["daily_views"].items())[-14:]:
                lines.append(f"| {date} | {count:,} |")
            lines.append("")
    else:
        lines.extend([
            "*No page view data available yet. Statistics will appear after the site receives traffic.*",
            "",
        ])

    lines.extend([
        "## AI Agent Usage (MCP Server)",
        "",
    ])

    if mcp_stats["total_requests"] > 0:
        lines.extend([
            f"- **Total MCP requests**: {mcp_stats['total_requests']:,}",
            f"- **Days with activity**: {mcp_stats['days']}",
            "",
        ])

        if mcp_stats["tool_usage"]:
            lines.extend(["### Tool Usage", ""])
            lines.append("| Tool | Requests |")
            lines.append("|---|---|")
            for tool, count in mcp_stats["tool_usage"].items():
                lines.append(f"| `{tool}` | {count:,} |")
            lines.append("")
    else:
        lines.extend([
            "*No MCP request data available yet. Statistics will appear after AI agents connect.*",
            "",
        ])

    lines.extend([
        "## About These Statistics",
        "",
        "- Page views are counted from nginx access logs (200 responses to HTML pages only)",
        "- Asset requests (CSS, JS, images, fonts) are excluded",
        "- MCP requests are counted from the MCP server request log",
        "- No IP addresses, user agents, cookies, or personal identifiers are stored",
        "- Statistics are regenerated periodically by a scheduled job",
        "",
    ])

    return "\n".join(lines)


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Generate OIR usage statistics")
    parser.add_argument("--nginx-log", default=DEFAULT_NGINX_LOG, help="Path to nginx access log")
    parser.add_argument("--mcp-log", default=DEFAULT_MCP_LOG, help="Path to MCP request log")
    args = parser.parse_args()

    # Parse logs
    page_entries = parse_nginx_log(args.nginx_log)
    mcp_entries = parse_mcp_log(args.mcp_log)

    # Compute stats
    page_stats = compute_page_stats(page_entries)
    mcp_stats = compute_mcp_stats(mcp_entries)

    # Generate page
    content = generate_stats_page(page_stats, mcp_stats)
    STATS_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATS_FILE.write_text(content, encoding="utf-8")

    # Save MCP stats as JSON for API access
    MCP_STATS_FILE.parent.mkdir(parents=True, exist_ok=True)
    MCP_STATS_FILE.write_text(
        json.dumps({"page_stats": page_stats, "mcp_stats": mcp_stats}, indent=2),
        encoding="utf-8",
    )

    print(f"Generated stats page: {STATS_FILE}")
    print(f"  Page views: {page_stats['total_views']:,} across {page_stats['days']} days")
    print(f"  MCP requests: {mcp_stats['total_requests']:,}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
