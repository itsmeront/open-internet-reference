"""Audit knowledge pages for unlinked court case mentions.

When Verified Facts or Historical Context mention a case by name, each mention
should either link to an existing CASE-* page (with a primary-source footnote)
or appear in Research Debt until a case page is created.

Usage:
    python tools/audit_case_mentions.py            # add missing research debt
    python tools/audit_case_mentions.py --dry-run  # report only
    python tools/audit_case_mentions.py --json     # machine-readable report
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("PyYAML is required. Install docs dependencies with: python -m pip install -e .[docs]")
    raise SystemExit(2)


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = ROOT / "knowledge"

CASE_LINE_PATTERN = re.compile(
    r"(?<![A-Za-z/])([A-Z][A-Za-z0-9'.&-]+(?:\s+[A-Za-z0-9'.&-]+){0,5}\s+v\.?\s+[A-Z][A-Za-z0-9'.&-]+(?:\s+[A-Za-z0-9'.&-]+){0,5})"
)


def normalize_case_name(name: str) -> str:
    cleaned = name.strip().rstrip(".,;:")
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned


def is_plausible_case_name(name: str) -> bool:
    if len(name) > 80:
        return False
    if any(token in name for token in ("She ", "He ", "The ", "including ", "challenge")):
        return False
    return " v. " in name or " v " in name
CASE_LINK_PATTERN = re.compile(r"\]\(\.{0,2}/legal/(CASE-[A-Z0-9-]+)\.md\)")
CASE_ID_PATTERN = re.compile(r"`(CASE-[A-Z0-9-]+)`")
FOOTNOTE_DEF_PATTERN = re.compile(r"^\[\^[^\]]+\]:")
SECTIONS = {"Verified Facts", "Historical Context"}

# Short names and variants -> CASE-* id
CASE_ALIASES: dict[str, str] = {
    "Bernstein v. United States Department of Justice": "CASE-BERNSTEIN-V-DOJ",
    "Bernstein v. Dept. of Justice": "CASE-BERNSTEIN-V-DOJ",
    "Bernstein v. DOJ": "CASE-BERNSTEIN-V-DOJ",
    "Brown v. Entertainment Merchants Assn.": "CASE-BROWN-V-ENTERTAINMENT-MERCHANTS",
    "Brown v. Entertainment Merchants Association": "CASE-BROWN-V-ENTERTAINMENT-MERCHANTS",
    "EMA v. Brown": "CASE-BROWN-V-ENTERTAINMENT-MERCHANTS",
    "Carpenter v. United States": "CASE-CARPENTER-V-US",
    "Google LLC v. Oracle America, Inc.": "CASE-GOOGLE-V-ORACLE",
    "Google v. Oracle": "CASE-GOOGLE-V-ORACLE",
    "Junger v. Daley": "CASE-JUNGER-V-DALEY",
    "Packingham v. North Carolina": "CASE-PACKINGHAM-V-NC",
    "Perfect 10, Inc. v. CCBill LLC": "CASE-PERFECT10-V-CCBILL",
    "Perfect 10 v. CCBill": "CASE-PERFECT10-V-CCBILL",
    "Reno v. American Civil Liberties Union": "CASE-RENO-V-ACLU",
    "Reno v. ACLU": "CASE-RENO-V-ACLU",
    "Universal City Studios v. Corley": "CASE-UNIVERSAL-V-CORLEY",
    "Van Buren v. United States": "CASE-VAN-BUREN-V-US",
}


@dataclass
class CaseMention:
    page_path: str
    page_id: str
    section: str
    case_name: str
    case_id: str | None
    linked: bool
    footnoted: bool
    line: str


def load_front_matter(path: Path) -> tuple[dict[str, Any], str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text, text
    try:
        _, raw_metadata, body = text.split("---\n", 2)
    except ValueError:
        return {}, text, text
    metadata = yaml.safe_load(raw_metadata) or {}
    if not isinstance(metadata, dict):
        metadata = {}
    return metadata, raw_metadata, body


def rebuild_file(raw_metadata: str, body: str) -> str:
    return f"---\n{raw_metadata.rstrip()}\n---\n{body}"


def load_case_registry() -> dict[str, str]:
    registry = dict(CASE_ALIASES)
    legal_dir = KNOWLEDGE_DIR / "legal"
    for path in legal_dir.glob("CASE-*.md"):
        metadata, _, _ = load_front_matter(path)
        case_id = metadata.get("id")
        title = metadata.get("title")
        if isinstance(case_id, str):
            if isinstance(title, str):
                registry[title] = case_id
            registry[case_id.replace("CASE-", "").replace("-", " ")] = case_id
    return registry


def resolve_case_id(name: str, registry: dict[str, str]) -> str | None:
    cleaned = name.strip().rstrip(".")
    if cleaned in registry:
        return registry[cleaned]
    lowered = cleaned.lower()
    for alias, case_id in registry.items():
        if alias.lower() == lowered:
            return case_id
    return None


def extract_research_debt(body: str) -> list[str]:
    items: list[str] = []
    in_section = False
    for line in body.splitlines():
        if line.startswith("## "):
            in_section = line.strip() == "## Research Debt"
            continue
        if in_section and line.strip().startswith("- "):
            items.append(line.strip()[2:].strip())
    return items


def replace_research_debt(body: str, items: list[str]) -> str:
    lines = body.splitlines()
    output: list[str] = []
    in_section = False
    replaced = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("## "):
            if in_section and not replaced:
                for item in items:
                    output.append(f"- {item}")
                replaced = True
            in_section = line.strip() == "## Research Debt"
            output.append(line)
            i += 1
            continue
        if in_section and line.strip().startswith("- "):
            i += 1
            while i < len(lines) and lines[i].startswith("  "):
                i += 1
            continue
        output.append(line)
        i += 1
    if in_section and not replaced:
        for item in items:
            output.append(f"- {item}")
    return "\n".join(output).rstrip() + "\n"


def debt_item_for(case_name: str, case_id: str | None) -> str:
    if case_id:
        return (
            f"Link mentioned case `{case_name}` to `{case_id}` with a primary-source footnote "
            f"(opinion, docket, or official case page)."
        )
    return f"Create `CASE-*` page and primary source for mentioned case `{case_name}`."


def line_is_linked(line: str, case_id: str | None) -> bool:
    if CASE_LINK_PATTERN.search(line):
        return True
    if case_id and case_id in line:
        return True
    return bool(CASE_ID_PATTERN.search(line))


def line_is_footnoted(line: str) -> bool:
    return "[^" in line


def audit_page(path: Path, registry: dict[str, str]) -> list[CaseMention]:
    metadata, _, body = load_front_matter(path)
    page_id = str(metadata.get("id") or path.stem)
    mentions: list[CaseMention] = []
    current_section: str | None = None

    for line in body.splitlines():
        if line.startswith("## "):
            section = line.strip()[3:]
            current_section = section if section in SECTIONS else None
            continue
        if not current_section or FOOTNOTE_DEF_PATTERN.match(line):
            continue
        if not line.strip().startswith("- "):
            continue
        for match in CASE_LINE_PATTERN.finditer(line):
            case_name = normalize_case_name(match.group(1))
            if not is_plausible_case_name(case_name):
                continue
            case_id = resolve_case_id(case_name, registry)
            mentions.append(
                CaseMention(
                    page_path=str(path.relative_to(ROOT)),
                    page_id=page_id,
                    section=current_section,
                    case_name=case_name,
                    case_id=case_id,
                    linked=line_is_linked(line, case_id),
                    footnoted=line_is_footnoted(line),
                    line=line.strip(),
                )
            )
    return mentions


def apply_debt(path: Path, mentions: list[CaseMention], dry_run: bool) -> bool:
    unresolved = [m for m in mentions if not (m.linked and m.footnoted)]
    if not unresolved:
        return False

    _, raw_metadata, body = load_front_matter(path)
    debt = extract_research_debt(body)
    changed = False
    for mention in unresolved:
        item = debt_item_for(mention.case_name, mention.case_id)
        if item not in debt:
            debt.append(item)
            changed = True
    if changed and not dry_run:
        path.write_text(rebuild_file(raw_metadata, replace_research_debt(body, debt)), encoding="utf-8")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit case mentions in knowledge pages.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    registry = load_case_registry()
    paths = sorted(
        path
        for path in KNOWLEDGE_DIR.rglob("*.md")
        if "_templates" not in path.parts and path.name != "README.md"
    )

    all_mentions: list[CaseMention] = []
    changed_files: list[str] = []
    for path in paths:
        mentions = audit_page(path, registry)
        all_mentions.extend(mentions)
        if apply_debt(path, mentions, dry_run=args.dry_run):
            changed_files.append(str(path.relative_to(ROOT)))

    unresolved = [m for m in all_mentions if not (m.linked and m.footnoted)]

    if args.json:
        print(json.dumps({"mentions": [asdict(m) for m in all_mentions], "changed_files": changed_files}, indent=2))
        return 0

    print(f"Found {len(all_mentions)} case mention(s); {len(unresolved)} need link or primary-source footnote.")
    mode = "Would update" if args.dry_run else "Updated"
    print(f"{mode} {len(changed_files)} file(s) with research debt.")
    for name in changed_files:
        print(f"  - {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
