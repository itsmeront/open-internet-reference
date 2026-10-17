"""List open cases that are due for a docket check.

Case pages opt in with `monitor: true`. This report is the periodic chore.
It does not add research debt and it does not edit case pages.

Usage:
    python tools/monitor_cases.py
    python tools/monitor_cases.py --due-days 14 --output generated/case-monitor.md
"""

from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("PyYAML is required. Install docs dependencies with: python -m pip install -e .[docs]")
    raise SystemExit(2)


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = ROOT / "knowledge"
DEFAULT_DUE_DAYS = 14
MARKER = "<!-- oir-case-monitor -->"
HINT_MARKERS = (
    "update after",
    "when it issues",
    "when issued",
    "when one issues",
    "later ",
    "appeal",
    "merits",
    "settlement",
    "certiorari",
    "track the",
    "docket",
)
PRIMARY_HINTS = (
    "update after",
    "when it issues",
    "when issued",
    "when one issues",
    "track the",
)


@dataclass(frozen=True)
class MonitoredCase:
    page_id: str
    title: str
    path: Path
    last_verified: date | None
    hint: str

    @property
    def days_since_check(self) -> int | None:
        if self.last_verified is None:
            return None
        return (date.today() - self.last_verified).days

    def is_due(self, due_days: int) -> bool:
        days = self.days_since_check
        return days is None or days >= due_days


def load_front_matter(path: Path) -> tuple[dict[str, Any] | None, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, text
    try:
        _, raw_metadata, body = text.split("---\n", 2)
    except ValueError:
        return None, text
    metadata = yaml.safe_load(raw_metadata)
    if not isinstance(metadata, dict):
        return None, body
    return metadata, body


def parse_verified_date(value: Any) -> date | None:
    if value in (None, ""):
        return None
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if not isinstance(value, str):
        return None
    try:
        return date.fromisoformat(value[:10])
    except ValueError:
        return None


def research_debt_lines(body: str) -> list[str]:
    items: list[str] = []
    in_debt = False
    for line in body.splitlines():
        if line.startswith("## "):
            in_debt = line.strip().lower() == "## research debt"
            continue
        if in_debt and line.startswith("- "):
            items.append(line[2:].strip())
    return items


def hint_for(items: list[str]) -> str:
    scored: list[tuple[int, int, str]] = []
    for index, item in enumerate(items):
        lower = item.lower()
        if any(marker in lower for marker in PRIMARY_HINTS):
            scored.append((2, index, item))
        elif any(marker in lower for marker in HINT_MARKERS):
            scored.append((1, index, item))
    scored.sort(key=lambda row: (-row[0], row[1]))
    chosen = [row[2] for row in scored[:2]] or items[:1]
    text = " ".join(chosen)
    if len(text) > 220:
        return text[:217].rstrip() + "..."
    return text


def iter_monitored_cases() -> list[MonitoredCase]:
    cases: list[MonitoredCase] = []
    if not KNOWLEDGE_DIR.exists():
        return cases
    for path in sorted(KNOWLEDGE_DIR.rglob("CASE-*.md")):
        if "_templates" in path.parts or path.name == "README.md":
            continue
        metadata, body = load_front_matter(path)
        if not metadata or metadata.get("type") != "case" or metadata.get("monitor") is not True:
            continue
        page_id = metadata.get("id")
        title = metadata.get("title")
        cases.append(
            MonitoredCase(
                page_id=page_id if isinstance(page_id, str) else path.stem,
                title=title if isinstance(title, str) else path.stem,
                path=path,
                last_verified=parse_verified_date(metadata.get("last_verified")),
                hint=hint_for(research_debt_lines(body)),
            )
        )
    return cases


def cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def page_url(path: Path) -> str:
    repo = os.environ.get("GITHUB_REPOSITORY", "itsmeront/open-internet-reference")
    server = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
    relative = path.relative_to(ROOT).as_posix()
    return f"{server}/{repo}/blob/main/{relative}"


def format_verified(case: MonitoredCase) -> str:
    if case.last_verified is None:
        return "missing"
    return case.last_verified.isoformat()


def format_days(case: MonitoredCase) -> str:
    days = case.days_since_check
    if days is None:
        return "—"
    return str(days)


def render_table(cases: list[MonitoredCase]) -> list[str]:
    lines = [
        "| Case | Last verified | Days | Waiting on |",
        "| --- | --- | ---: | --- |",
    ]
    for case in cases:
        link = f"[`{case.page_id}`]({page_url(case.path)})"
        lines.append(
            f"| {link} {cell(case.title)} | {format_verified(case)} | {format_days(case)} | {cell(case.hint) or '—'} |"
        )
    return lines


def render_report(cases: list[MonitoredCase], due_days: int) -> str:
    due = [case for case in cases if case.is_due(due_days)]
    current = [case for case in cases if not case.is_due(due_days)]
    due.sort(key=lambda case: (case.days_since_check is not None, -(case.days_since_check or 0), case.page_id))
    current.sort(key=lambda case: case.page_id)
    today = date.today().isoformat()

    lines = [
        MARKER,
        "",
        "# Open case monitor",
        "",
        "Weekly docket check for case pages with `monitor: true`. "
        "This issue is the chore. Do not copy it into a page's research debt.",
        "",
        f"Generated {today}. A case is due when `last_verified` is missing or older than {due_days} days.",
        "",
        "## What to do",
        "",
        "1. For each due case, check the court docket for a new order, appeal, settlement, or dismissal.",
        "2. If the record changed, add a source and update the facts. Remove `monitor` when the case is concluded.",
        "3. If nothing material changed, set `last_verified` to the check date.",
        "4. Opt a case in with `monitor: true` in its front matter. Opt out by removing the field or setting `monitor: false`.",
        "",
        f"## Due ({len(due)})",
        "",
    ]
    if due:
        lines.extend(render_table(due))
    else:
        lines.append("None.")
    lines.extend(["", f"## Checked within {due_days} days ({len(current)})", ""])
    if current:
        lines.extend(render_table(current))
    else:
        lines.append("None.")
    if not cases:
        lines.extend(
            [
                "",
                "No case page sets `monitor: true` yet. Add it to a case whose outcome can still change.",
            ]
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="List open cases due for a docket check.")
    parser.add_argument(
        "--due-days",
        type=int,
        default=DEFAULT_DUE_DAYS,
        help="Cases last verified at least this many days ago are due (default: 14).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Write the report to this path. The report is always printed to stdout.",
    )
    args = parser.parse_args()
    if args.due_days < 0:
        print("--due-days must be zero or greater", file=sys.stderr)
        return 2

    report = render_report(iter_monitored_cases(), args.due_days)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
    sys.stdout.write(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
