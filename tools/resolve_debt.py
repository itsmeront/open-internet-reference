"""Scan, prioritize, and track research debt across OIR pages.

Reports all research debt items from knowledge and bibliography pages,
prioritized by page type and status. Can output a summary report or
detailed per-page breakdown.

Usage:
    python tools/resolve_debt.py              # Full report
    python tools/resolve_debt.py --summary    # Counts only
    python tools/resolve_debt.py --by-type    # Group by page type
    python tools/resolve_debt.py --json       # Machine-readable output
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("PyYAML is required. Install docs dependencies with: python -m pip install -e .[docs]")
    raise SystemExit(2)


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIRS = [
    ROOT / "knowledge",
    ROOT / "bibliography",
    ROOT / "contacts",
]

# Priority order: higher priority types get resolved first
TYPE_PRIORITY = {
    "case": 1,
    "attorney": 2,
    "organization": 3,
    "person": 4,
    "statute": 5,
    "topic": 6,
    "technology": 7,
    "protocol": 8,
    "source": 9,
}

STATUS_PRIORITY = {
    "needs_sources": 1,
    "in_review": 2,
    "draft": 3,
    "verified": 4,
    "deprecated": 5,
}


@dataclass
class DebtItem:
    text: str
    page_id: str
    page_title: str
    page_type: str
    page_status: str
    page_path: str
    sources_count: int
    last_verified: str | None


@dataclass
class DebtReport:
    total_items: int = 0
    total_pages_with_debt: int = 0
    total_pages_scanned: int = 0
    by_type: dict[str, int] = field(default_factory=dict)
    by_status: dict[str, int] = field(default_factory=dict)
    items: list[DebtItem] = field(default_factory=list)


def iter_markdown_files() -> list[Path]:
    """Find all content Markdown files."""
    files: list[Path] = []
    for content_dir in CONTENT_DIRS:
        if not content_dir.exists():
            continue
        files.extend(
            path
            for path in content_dir.rglob("*.md")
            if "_templates" not in path.parts and path.name != "README.md"
        )
    return sorted(files)


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


def extract_research_debt(path: Path) -> list[str]:
    """Extract research debt items from a page's Research Debt section."""
    text = path.read_text(encoding="utf-8")
    items: list[str] = []
    in_debt = False

    for line in text.splitlines():
        if line.startswith("## "):
            in_debt = line.strip().lower() == "## research debt"
            continue
        if in_debt and line.strip().startswith("- "):
            item_text = line.strip()[2:].strip()
            if item_text:
                items.append(item_text)

    return items


def priority_key(item: DebtItem) -> tuple[int, int, str]:
    """Sort key: type priority, then status priority, then page ID."""
    type_pri = TYPE_PRIORITY.get(item.page_type, 99)
    status_pri = STATUS_PRIORITY.get(item.page_status, 99)
    return (type_pri, status_pri, item.page_id)


def scan_debt() -> DebtReport:
    """Scan all pages and collect research debt items."""
    report = DebtReport()
    files = iter_markdown_files()
    report.total_pages_scanned = len(files)

    for path in files:
        metadata = load_front_matter(path)
        if metadata is None:
            continue

        debt_items = extract_research_debt(path)
        if not debt_items:
            continue

        page_id = metadata.get("id", path.stem)
        page_title = metadata.get("title", path.stem)
        page_type = metadata.get("type", "unknown")
        page_status = metadata.get("status", "unknown")
        sources_count = len(metadata.get("sources", []))
        last_verified = metadata.get("last_verified")
        page_path = str(path.relative_to(ROOT))

        report.total_pages_with_debt += 1
        report.by_type[page_type] = report.by_type.get(page_type, 0) + len(debt_items)
        report.by_status[page_status] = report.by_status.get(page_status, 0) + len(debt_items)

        for item_text in debt_items:
            report.total_items += 1
            report.items.append(DebtItem(
                text=item_text,
                page_id=page_id,
                page_title=page_title,
                page_type=page_type,
                page_status=page_status,
                page_path=page_path,
                sources_count=sources_count,
                last_verified=last_verified,
            ))

    # Sort by priority
    report.items.sort(key=priority_key)
    return report


def print_summary(report: DebtReport) -> None:
    """Print a summary of research debt."""
    print("═" * 60)
    print("  OIR RESEARCH DEBT REPORT")
    print("═" * 60)
    print()
    print(f"  Pages scanned:        {report.total_pages_scanned}")
    print(f"  Pages with debt:      {report.total_pages_with_debt}")
    print(f"  Total debt items:     {report.total_items}")
    print()

    if report.by_type:
        print("  By page type:")
        for type_name, count in sorted(report.by_type.items(), key=lambda x: TYPE_PRIORITY.get(x[0], 99)):
            print(f"    {type_name:20s} {count:3d} items")
        print()

    if report.by_status:
        print("  By page status:")
        for status_name, count in sorted(report.by_status.items(), key=lambda x: STATUS_PRIORITY.get(x[0], 99)):
            print(f"    {status_name:20s} {count:3d} items")
        print()


def print_by_type(report: DebtReport) -> None:
    """Print debt items grouped by page type."""
    current_type = None
    for item in report.items:
        if item.page_type != current_type:
            current_type = item.page_type
            print(f"\n{'─' * 60}")
            print(f"  {current_type.upper()} ({report.by_type.get(current_type, 0)} items)")
            print(f"{'─' * 60}")

        print(f"\n  [{item.page_id}] {item.page_title}")
        print(f"    Status: {item.page_status} | Sources: {item.sources_count} | Verified: {item.last_verified or 'Never'}")
        print(f"    → {item.text}")


def print_full_report(report: DebtReport) -> None:
    """Print the full prioritized debt report."""
    print_summary(report)
    print("─" * 60)
    print("  PRIORITIZED DEBT ITEMS (by type → status → page)")
    print("─" * 60)

    current_page = None
    for item in report.items:
        if item.page_id != current_page:
            current_page = item.page_id
            print(f"\n  [{item.page_type}] {item.page_id}: {item.page_title}")
            print(f"  Status: {item.page_status} | Sources: {item.sources_count} | Verified: {item.last_verified or 'Never'}")
            print(f"  Path: {item.page_path}")

        print(f"    • {item.text}")

    print(f"\n{'═' * 60}")
    print(f"  {report.total_items} items across {report.total_pages_with_debt} pages")
    print(f"{'═' * 60}")


def print_json(report: DebtReport) -> None:
    """Print machine-readable JSON output."""
    output = {
        "total_items": report.total_items,
        "total_pages_with_debt": report.total_pages_with_debt,
        "total_pages_scanned": report.total_pages_scanned,
        "by_type": report.by_type,
        "by_status": report.by_status,
        "items": [asdict(item) for item in report.items],
    }
    print(json.dumps(output, indent=2))


def main() -> int:
    report = scan_debt()

    if "--json" in sys.argv:
        print_json(report)
    elif "--summary" in sys.argv:
        print_summary(report)
    elif "--by-type" in sys.argv:
        print_summary(report)
        print_by_type(report)
    else:
        print_full_report(report)

    return 0 if report.total_items == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
