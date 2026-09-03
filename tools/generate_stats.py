"""Generate anonymous usage statistics for OIR.

Reads nginx access logs and MCP request logs to produce a summary
statistics page with traffic classification. No personal data (IPs,
user agents) is stored or displayed — only aggregate counts.

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
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
WEBSITE_GENERATED_DIR = ROOT / "website" / "generated"
STATS_FILE = WEBSITE_GENERATED_DIR / "stats.md"
MCP_STATS_FILE = ROOT / "generated" / "mcp-stats.json"

# Default log locations on the server
DEFAULT_NGINX_LOG = "/var/log/nginx/access.log"
DEFAULT_MCP_LOG = "/opt/oir/mcp-requests.log"

# ---------------------------------------------------------------------------
# Nginx log parsing — extracts date, method, path, status, and user-agent.
# IP addresses are intentionally NOT stored.
# ---------------------------------------------------------------------------

# Full nginx combined log format (with optional trailing X-Forwarded-For)
NGINX_PATTERN = re.compile(
    r'\S+ - \S+ \[([^\]]+)\] "(\w+) ([^\s"]+)[^"]*" (\d+) \S+ "[^"]*" "([^"]*)".*'
)

# Fallback for logs without user-agent field (old common format)
NGINX_PATTERN_BASIC = re.compile(
    r'\S+ - \S+ \[([^\]]+)\] "(\w+) ([^\s]+) [^"]*" (\d+) \d+'
)

# ---------------------------------------------------------------------------
# Path filters — exclude assets; also exclude non-OIR paths from page counts
# ---------------------------------------------------------------------------

ASSET_PATTERN = re.compile(
    r"^/assets/|^/admin/config\.yml$|^/favicon\.ico$|^/sitemap\.xml$"
    r"|^/search/|\.(css|js|png|jpg|jpeg|gif|ico|svg|woff|woff2|map)$"
)

# Allowlist: paths that belong to the OIR site.
# Everything else (other apps, attack probes, random scans) is excluded.
OIR_PATH = re.compile(
    r"^/$"                               # homepage
    r"|^/generated/"                      # all generated pages
    r"|^/knowledge/"                      # knowledge base direct links
    r"|^/bibliography/"                   # bibliography
    r"|^/about/"                          # about pages
    r"|^/contacts/"                       # contacts
    r"|^/admin/"                          # Decap CMS admin
    r"|^/robots\.txt$"                    # robots.txt
    r"|^/404\.html$"                      # error page
    r"|^/index\.html$",                   # homepage variant
    re.I,
)

# ---------------------------------------------------------------------------
# User-agent classification patterns
# ---------------------------------------------------------------------------

# AI training and retrieval crawlers
AI_CRAWLER_RE = re.compile(
    r"GPTBot|ChatGPT-User|OAI-SearchBot"
    r"|ClaudeBot|Claude-Web|anthropic-ai"
    r"|Google-Extended"
    r"|CCBot|Bytespider|cohere-ai|PerplexityBot|YouBot"
    r"|Meta-ExternalAgent|Meta-ExternalFetcher"
    r"|Amazonbot|AI2Bot|Diffbot|Timpibot|ImagesiftBot"
    r"|Omgili|DataForSeo|peer39|Webz\.io",
    re.I,
)

# AI crawler → friendly display name
AI_LABELS: list[tuple[re.Pattern, str]] = [
    (re.compile(r"ChatGPT-User", re.I), "ChatGPT (OpenAI)"),
    (re.compile(r"OAI-SearchBot", re.I), "SearchGPT (OpenAI)"),
    (re.compile(r"GPTBot", re.I), "GPTBot (OpenAI)"),
    (re.compile(r"ClaudeBot|Claude-Web|anthropic", re.I), "ClaudeBot (Anthropic)"),
    (re.compile(r"Google-Extended", re.I), "Google-Extended (Gemini)"),
    (re.compile(r"PerplexityBot", re.I), "PerplexityBot"),
    (re.compile(r"Bytespider", re.I), "Bytespider (ByteDance)"),
    (re.compile(r"CCBot", re.I), "CCBot (Common Crawl)"),
    (re.compile(r"Meta-External", re.I), "Meta AI"),
    (re.compile(r"Amazonbot", re.I), "Amazonbot"),
    (re.compile(r"cohere-ai", re.I), "Cohere"),
    (re.compile(r"YouBot", re.I), "YouBot (You.com)"),
    (re.compile(r"AI2Bot", re.I), "AI2Bot (Allen AI)"),
    (re.compile(r"Diffbot", re.I), "Diffbot"),
]

# Search-engine crawlers (not AI training)
SE_CRAWLER_RE = re.compile(
    r"Googlebot|Bingbot|Slurp|DuckDuckBot|Baiduspider|YandexBot|Sogou"
    r"|Applebot|BingPreview|facebookexternalhit|Twitterbot|LinkedInBot"
    r"|Pinterestbot|Slackbot|WhatsApp"
    r"|AhrefsBot|SemrushBot|MJ12bot|DotBot|PetalBot",
    re.I,
)

# Automated scanners, security probes, generic bots
BOT_RE = re.compile(
    r"zgrab|CensysInspect|SecurityResearch|Palo Alto|visionheight"
    r"|internet-measurement|shodan|masscan|nmap|ModatScanner"
    r"|libredtail|Go-http-client|python-requests|python-urllib"
    r"|curl/|wget/|Java/|libwww|Scrapy|Nutch|heritrix|okhttp"
    r"|axios|node-fetch|Faraday|got-scraping|HTTPClient",
    re.I,
)

EMPTY_UA_RE = re.compile(r"^-?$")


# ---------------------------------------------------------------------------
# Traffic classification
# ---------------------------------------------------------------------------

def classify_ua(ua: str) -> str:
    """Classify a user-agent string into a traffic category."""
    if AI_CRAWLER_RE.search(ua):
        return "ai"
    if SE_CRAWLER_RE.search(ua):
        return "crawler"
    if BOT_RE.search(ua) or EMPTY_UA_RE.match(ua):
        return "bot"
    return "human"


def ai_label(ua: str) -> str:
    """Return a friendly AI crawler name, or 'Other AI' as fallback."""
    for pattern, label in AI_LABELS:
        if pattern.search(ua):
            return label
    return "Other AI"


# ---------------------------------------------------------------------------
# Log parsing
# ---------------------------------------------------------------------------

def parse_nginx_log(log_path: str) -> list[dict[str, str]]:
    """Parse nginx access log, extracting date, path, status, and traffic class.

    IP addresses are intentionally never stored.
    """
    entries: list[dict[str, str]] = []
    path = Path(log_path)

    if not path.exists():
        return entries

    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        # Try combined format first (has user-agent)
        match = NGINX_PATTERN.match(line)
        if match:
            date_str, method, request_path, status, ua = match.groups()
        else:
            # Fallback: basic format without user-agent
            match = NGINX_PATTERN_BASIC.match(line)
            if not match:
                continue
            date_str, method, request_path, status = match.groups()
            ua = "-"

        # Only count GET requests with 200 status
        if method != "GET" or status != "200":
            continue

        # Exclude static assets
        if ASSET_PATTERN.search(request_path):
            continue

        # Only count OIR pages (allowlist); skip other apps and attack probes
        if not OIR_PATH.search(request_path):
            continue

        # Parse date
        try:
            dt = datetime.strptime(date_str.split()[0], "%d/%b/%Y:%H:%M:%S")
            date_key = dt.strftime("%Y-%m-%d")
        except ValueError:
            continue

        traffic_class = classify_ua(ua)

        entry: dict[str, str] = {
            "date": date_key,
            "path": request_path,
            "class": traffic_class,
        }
        # For AI traffic, also record the specific crawler
        if traffic_class == "ai":
            entry["ai_name"] = ai_label(ua)

        entries.append(entry)

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


# ---------------------------------------------------------------------------
# Statistics computation
# ---------------------------------------------------------------------------

def compute_page_stats(entries: list[dict[str, str]]) -> dict[str, Any]:
    """Compute aggregate page view statistics with traffic breakdown."""
    if not entries:
        return {
            "total_views": 0,
            "days": 0,
            "top_pages": [],
            "daily_views": {},
            "traffic_breakdown": {},
            "ai_breakdown": {},
            "daily_human": {},
        }

    daily_views: Counter[str] = Counter()
    daily_human: Counter[str] = Counter()
    page_views: Counter[str] = Counter()
    traffic_breakdown: Counter[str] = Counter()
    ai_breakdown: Counter[str] = Counter()

    for entry in entries:
        date = entry["date"]
        daily_views[date] += 1
        traffic_class = entry.get("class", "human")
        traffic_breakdown[traffic_class] += 1

        if traffic_class == "human":
            page_views[entry["path"]] += 1
            daily_human[date] += 1

        if traffic_class == "ai":
            ai_breakdown[entry.get("ai_name", "Other AI")] += 1

    # Top pages — only human traffic
    top_pages = [
        (path.rstrip("/") or "/", count)
        for path, count in page_views.most_common(20)
    ]

    total = len(entries)
    human_total = traffic_breakdown.get("human", 0)

    return {
        "total_views": total,
        "human_views": human_total,
        "days": len(daily_views),
        "avg_daily": human_total // max(len(daily_human) or 1, 1),
        "top_pages": top_pages,
        "daily_views": dict(sorted(daily_views.items())[-30:]),
        "daily_human": dict(sorted(daily_human.items())[-30:]),
        "traffic_breakdown": dict(traffic_breakdown.most_common()),
        "ai_breakdown": dict(ai_breakdown.most_common()),
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


# ---------------------------------------------------------------------------
# Chart rendering
# ---------------------------------------------------------------------------

def _nice_axis_max(value: int) -> int:
    """Round a chart maximum up to a readable axis bound."""
    if value <= 0:
        return 1
    magnitude = 10 ** (len(str(value)) - 1)
    return int(((value + magnitude - 1) // magnitude) * magnitude)


def render_daily_traffic_chart(
    daily_views: dict[str, int],
    title: str = "### Daily Traffic (last 30 days)",
    bar_color: str = "#4051b5",
    aria_label: str = "Daily page views for the last 30 days",
) -> list[str]:
    """Render the last 30 days of traffic as an inline SVG bar chart."""
    items = list(daily_views.items())[-30:]
    if not items:
        return []

    width = 920
    height = 320
    margin_left = 56
    margin_right = 16
    margin_top = 20
    margin_bottom = 52
    chart_width = width - margin_left - margin_right
    chart_height = height - margin_top - margin_bottom
    max_value = max(count for _, count in items)
    axis_max = _nice_axis_max(max_value)
    bar_gap = 3
    bar_width = (chart_width - bar_gap * (len(items) - 1)) / len(items)

    lines = [
        title,
        "",
        f'<div class="oir-daily-traffic-chart" role="img" '
        f'aria-label="{aria_label}">',
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        'preserveAspectRatio="xMidYMid meet">',
        f'<rect x="0" y="0" width="{width}" height="{height}" fill="transparent" />',
    ]

    for tick in range(5):
        fraction = tick / 4
        y = margin_top + chart_height - (chart_height * fraction)
        value = int(axis_max * fraction)
        lines.append(
            f'<line x1="{margin_left}" y1="{y:.1f}" x2="{width - margin_right}" '
            f'y2="{y:.1f}" stroke="rgba(63, 81, 181, 0.15)" stroke-width="1" />'
        )
        lines.append(
            f'<text x="{margin_left - 8}" y="{y + 4:.1f}" text-anchor="end" '
            f'font-size="11" fill="currentColor">{value:,}</text>'
        )

    for index, (date, count) in enumerate(items):
        bar_height = (count / axis_max) * chart_height if axis_max else 0
        x = margin_left + index * (bar_width + bar_gap)
        y = margin_top + chart_height - bar_height
        label = date[5:]  # MM-DD
        show_label = index == 0 or index == len(items) - 1 or index % 5 == 0
        lines.extend([
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_width:.1f}" '
            f'height="{bar_height:.1f}" fill="{bar_color}" rx="2">',
            f"<title>{date}: {count:,} views</title>",
            "</rect>",
        ])
        if show_label:
            lines.append(
                f'<text x="{x + bar_width / 2:.1f}" y="{height - 18}" text-anchor="middle" '
                f'font-size="11" fill="currentColor">{label}</text>'
            )

    lines.extend([
        "</svg>",
        "</div>",
        "",
    ])
    return lines


# ---------------------------------------------------------------------------
# Markdown page generation
# ---------------------------------------------------------------------------

TRAFFIC_CLASS_LABELS = {
    "human": "Human visitors",
    "ai": "AI crawlers",
    "crawler": "Search-engine crawlers",
    "bot": "Bots (scanners, automated, unknown)",
}

TRAFFIC_CLASS_ORDER = ["human", "ai", "crawler", "bot"]


def generate_stats_page(
    page_stats: dict[str, Any],
    mcp_stats: dict[str, Any],
) -> str:
    """Generate the Markdown stats page."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# Usage Statistics",
        "",
        f"Last updated: {now}",
        "",
        "These statistics are collected anonymously — no personal information "
        "(IP addresses, user agents, or identifiers) is tracked or stored.",
        "",
    ]

    # ------------------------------------------------------------------
    # Traffic breakdown
    # ------------------------------------------------------------------
    breakdown = page_stats.get("traffic_breakdown", {})
    total = page_stats.get("total_views", 0)
    human_total = page_stats.get("human_views", 0)

    if total > 0:
        lines.extend([
            "## Traffic Overview",
            "",
            f"Over **{page_stats['days']}** days of tracking, OIR received "
            f"**{total:,}** classified requests (GET 200, excluding assets and "
            f"non-OIR paths). The breakdown by visitor type:",
            "",
            "| Visitor type | Requests | Share |",
            "|---|---:|---:|",
        ])

        for cls in TRAFFIC_CLASS_ORDER:
            count = breakdown.get(cls, 0)
            pct = f"{100 * count / total:.1f}%" if total else "0%"
            label = TRAFFIC_CLASS_LABELS.get(cls, cls)
            lines.append(f"| {label} | {count:,} | {pct} |")

        lines.extend([
            "",
            f"> Of {total:,} total OIR requests, **{human_total:,}** came from "
            f"human visitors. The remaining traffic is automated.",
            "",
        ])

        # AI breakdown detail
        ai_breakdown = page_stats.get("ai_breakdown", {})
        if ai_breakdown:
            lines.extend([
                "### AI Crawlers",
                "",
                "These AI systems are reading OIR content, likely for training "
                "data or retrieval-augmented generation:",
                "",
                "| AI system | Requests |",
                "|---|---:|",
            ])
            for name, count in ai_breakdown.items():
                lines.append(f"| {name} | {count:,} |")
            lines.append("")

    # ------------------------------------------------------------------
    # Human page views
    # ------------------------------------------------------------------
    lines.extend([
        "## Site Traffic (Human Visitors)",
        "",
    ])

    if human_total > 0:
        lines.extend([
            f"- **Human page views**: {human_total:,}",
            f"- **Days tracked**: {page_stats['days']}",
            f"- **Average daily views**: {page_stats['avg_daily']:,}",
            "",
        ])

        if page_stats["top_pages"]:
            lines.extend(["### Most Visited Pages", ""])
            lines.append("| Page | Views |")
            lines.append("|---|---:|")
            for path, count in page_stats["top_pages"][:15]:
                display_path = path if len(path) <= 60 else path[:57] + "..."
                lines.append(f"| `{display_path}` | {count:,} |")
            lines.append("")

        daily_human = page_stats.get("daily_human", {})
        if daily_human:
            lines.extend(render_daily_traffic_chart(
                daily_human,
                title="### Daily Human Traffic (last 30 days)",
                bar_color="#4051b5",
                aria_label="Daily human page views for the last 30 days",
            ))
    else:
        lines.extend([
            "*No human page view data available yet. Statistics will appear "
            "after the site receives traffic.*",
            "",
        ])

    # ------------------------------------------------------------------
    # MCP usage
    # ------------------------------------------------------------------
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
            lines.append("|---|---:|")
            for tool, count in mcp_stats["tool_usage"].items():
                lines.append(f"| `{tool}` | {count:,} |")
            lines.append("")
    else:
        lines.extend([
            "*No MCP request data available yet. Statistics will appear "
            "after AI agents connect.*",
            "",
        ])

    # ------------------------------------------------------------------
    # Methodology
    # ------------------------------------------------------------------
    lines.extend([
        "## About These Statistics",
        "",
        "- **Scope**: Only requests to OIR pages are counted; traffic to other "
        "applications on the shared server is excluded",
        "- **Human page views**: GET requests returning 200, after filtering "
        "out assets, attack probes, and all identified bot/crawler/AI traffic",
        "- **AI crawlers**: Identified by user-agent strings of known AI "
        "training and retrieval systems (GPTBot, ClaudeBot, Google-Extended, etc.)",
        "- **Search-engine crawlers**: Googlebot, Bingbot, and similar "
        "indexing bots",
        "- **Bots**: Vulnerability scanners, automated scripts, monitoring "
        "services, and requests with empty or unrecognized automated "
        "user-agent strings",
        "- **Privacy**: No IP addresses, user agents, cookies, or personal "
        "identifiers are stored — only aggregate counts",
        "- Statistics are regenerated periodically by a scheduled job",
        "- Traffic growth increases hosting load; optional tips are accepted "
        "on the [Support OIR](../about/support.md) page (not tax-deductible)",
        "",
    ])

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Generate OIR usage statistics")
    parser.add_argument(
        "--nginx-log", default=DEFAULT_NGINX_LOG,
        help="Path to nginx access log",
    )
    parser.add_argument(
        "--mcp-log", default=DEFAULT_MCP_LOG,
        help="Path to MCP request log",
    )
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

    # Summary
    breakdown = page_stats.get("traffic_breakdown", {})
    print(f"Generated stats page: {STATS_FILE}")
    print(f"  Total OIR requests: {page_stats['total_views']:,} "
          f"across {page_stats['days']} days")
    print(f"  Human page views:   {page_stats.get('human_views', 0):,}")
    print(f"  AI crawlers:        {breakdown.get('ai', 0):,}")
    print(f"  Search crawlers:    {breakdown.get('crawler', 0):,}")
    print(f"  Bots:               {breakdown.get('bot', 0):,}")
    print(f"  MCP requests:       {mcp_stats['total_requests']:,}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
