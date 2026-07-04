"""Add per-claim footnotes and research-debt items to knowledge pages.

Implements RESEARCH_STANDARDS.md and CITATION_GUIDE.md rules:
- Every Verified Facts bullet gets a Markdown footnote to a source ID.
- Historical Context bullets get footnotes when present.
- Self-reported biography/about sources trigger corroboration research debt.

Usage:
    python tools/add_fact_citations.py            # update pages in place
    python tools/add_fact_citations.py --dry-run  # print planned changes
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("PyYAML is required. Install docs dependencies with: python -m pip install -e .[docs]")
    raise SystemExit(2)


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = ROOT / "knowledge"
BIBLIOGRAPHY_DIR = ROOT / "bibliography"

FOOTNOTE_REF_PATTERN = re.compile(r"\[\^[^\]]+\]")
FOOTNOTE_DEF_PATTERN = re.compile(r"^\[\^[^\]]+\]:")
FOOTNOTE_DEF_PARSE_PATTERN = re.compile(
    r"^\[\^(\d+)\]:\s*`(SRC-[A-Z0-9-]+)`\s*—\s*(.+)$"
)
SOURCE_ITEM_PATTERN = re.compile(
    r"^(?:\d+\.\s*)?`?(SRC-[A-Z0-9-]+)`?\s*:\s*(.+)$"
)
SOURCE_ID_PATTERN = re.compile(r"`(SRC-[A-Z0-9-]+)`")
SECTION_PATTERN = re.compile(r"^## (.+)$")

CITATION_SECTIONS = {"Verified Facts", "Historical Context"}

LITIGATION_KEYWORDS = (
    "litigat",
    "argued",
    "counsel",
    "supreme court",
    "held that",
    "compelled",
    "forced",
    "landmark",
    "case",
    "v.",
    " v ",
    "docket",
    "amicus",
)

SELF_REPORTED_DEBT = (
    "Corroborate self-reported biography or about-page claims with independent "
    "sources (institutional profile, court docket, case page, or reputable journalism)."
)

LITIGATION_DEBT = (
    "Add primary or secondary sources for major litigation and impact claims "
    "(dockets, case pages, official court records, or reputable journalism)."
)

MAPPING_DEBT = (
    "Review per-fact footnote-to-source mapping; multiple sources are cited on this page."
)


@dataclass
class SourceInfo:
    source_id: str
    title: str
    summary: str
    body: str
    reliability: str
    reliability_note: str


def load_yaml_front_matter(path: Path) -> tuple[dict[str, Any], str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text, text
    try:
        _, raw_metadata, body = text.split("---\n", 2)
    except ValueError:
        return {}, text, text
    metadata = yaml.safe_load(raw_metadata)
    if not isinstance(metadata, dict):
        metadata = {}
    return metadata, raw_metadata, body


def rebuild_file(raw_metadata: str, body: str) -> str:
    return f"---\n{raw_metadata.rstrip()}\n---\n{body}"


def parse_source_body(body: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in body.splitlines():
        if line.startswith("- ") and ": " in line:
            key, value = line[2:].split(": ", 1)
            fields[key.strip()] = value.strip()
    return fields


def classify_source(source_id: str, title: str, summary: str, body: str) -> tuple[str, str]:
    haystack = " ".join([source_id, title, summary, body]).lower()
    fields = parse_source_body(body)
    url = fields.get("URL", "").lower()

    if any(token in haystack for token in ("justia", "govinfo", "lii", "court opinion", "rfc ", "usc ", "u.s.c.")):
        return "primary", "Primary authority."
    if "rfc-" in url:
        return "primary", "Primary technical standard."
    if any(token in haystack for token in ("docket", "court filing", "statute", "regulation")):
        return "primary", "Primary legal authority."

    if any(token in haystack for token in ("contact page", "contact record", "annual report")):
        return "official", "Official organizational record."

    if any(
        token in haystack
        for token in (
            "staff biography",
            "staff profile",
            "staff bio",
            "attorney biography",
            "firm biography",
            "official biography",
            "bio page",
            "/bio/",
            "/bios/",
            "/staff/",
            "about us page",
            "about page",
        )
    ) or any(token in url for token in ("/bio", "/bios/", "/staff/", "/about", "about-us", "about-me")):
        if "contact" in haystack and "about" not in haystack:
            return "official", "Official contact page."
        return "self_reported", "Self-reported profile; corroboration pending."

    if "contact" in haystack:
        return "official", "Official organizational record."

    if any(token in haystack for token in ("press release", "news", "journalism", "paper", "scholar")):
        return "secondary", "Secondary reporting or scholarship."

    return "official", "Official source; review reliability tier."


def load_source_info(source_id: str) -> SourceInfo | None:
    matches = list(BIBLIOGRAPHY_DIR.rglob(f"{source_id}.md"))
    if not matches:
        return None
    path = matches[0]
    metadata, _, body = load_yaml_front_matter(path)
    title = str(metadata.get("title") or source_id)
    summary = str(metadata.get("summary") or "")
    reliability, reliability_note = classify_source(source_id, title, summary, body)
    return SourceInfo(
        source_id=source_id,
        title=title,
        summary=summary,
        body=body,
        reliability=reliability,
        reliability_note=reliability_note,
    )


def source_title_from_page(body: str, source_id: str) -> str | None:
    for line in body.splitlines():
        stripped = line.strip()
        match = SOURCE_ITEM_PATTERN.match(stripped.lstrip("- "))
        if match and match.group(1) == source_id:
            return match.group(2).strip().rstrip(".")
    return None


def extract_footnote_map(body: str) -> dict[int, str]:
    mapping: dict[int, str] = {}
    for line in body.splitlines():
        match = FOOTNOTE_DEF_PARSE_PATTERN.match(line.strip())
        if match:
            mapping[int(match.group(1))] = match.group(2)
    return mapping


def extract_sources_titles(body: str) -> dict[str, str]:
    titles: dict[str, str] = {}
    in_section = False
    for line in body.splitlines():
        if line.startswith("## "):
            in_section = line.strip() == "## Sources"
            continue
        if not in_section:
            continue
        stripped = line.strip()
        if not stripped or stripped.lower().startswith("additional sources"):
            continue
        match = SOURCE_ITEM_PATTERN.match(stripped.lstrip("- "))
        if match:
            titles[match.group(1)] = match.group(2).strip().rstrip(".")
    return titles


def format_numbered_source(num: int, source_id: str, title: str) -> str:
    return f"{num}. `{source_id}`: {title.rstrip('.')}."


def sync_sources_section(
    body: str,
    footnote_map: dict[int, str],
    front_matter_sources: list[str],
    source_infos: dict[str, SourceInfo],
) -> str:
    if not footnote_map:
        return body

    existing_titles = extract_sources_titles(body)
    lines = body.splitlines()
    output: list[str] = []
    in_section = False
    replaced = False
    i = 0

    while i < len(lines):
        line = lines[i]
        if line.startswith("## "):
            if in_section and not replaced:
                for num in sorted(footnote_map):
                    source_id = footnote_map[num]
                    title = (
                        existing_titles.get(source_id)
                        or source_title_from_page(body, source_id)
                        or (source_infos[source_id].title if source_id in source_infos else source_id)
                    )
                    output.append(format_numbered_source(num, source_id, title))

                footnoted_ids = set(footnote_map.values())
                extras = [
                    source_id
                    for source_id in front_matter_sources
                    if source_id not in footnoted_ids
                ]
                if extras:
                    output.append("")
                    output.append("Additional sources (not yet cited in footnotes):")
                    output.append("")
                    for source_id in extras:
                        title = (
                            existing_titles.get(source_id)
                            or (source_infos[source_id].title if source_id in source_infos else source_id)
                        )
                        output.append(f"- `{source_id}`: {title.rstrip('.')}.")
                if output and output[-1].strip():
                    output.append("")
                replaced = True
                in_section = False

            in_section = line.strip() == "## Sources"
            output.append(line)
            if in_section:
                output.append("")
            i += 1
            continue

        if in_section:
            i += 1
            while i < len(lines) and lines[i].startswith("  "):
                i += 1
            continue

        output.append(line)
        i += 1

    if in_section and not replaced:
        for num in sorted(footnote_map):
            source_id = footnote_map[num]
            title = (
                existing_titles.get(source_id)
                or (source_infos[source_id].title if source_id in source_infos else source_id)
            )
            output.append(format_numbered_source(num, source_id, title))

    return "\n".join(output).rstrip() + "\n"


def choose_source_for_bullet(bullet: str, sources: list[str], source_infos: dict[str, SourceInfo]) -> str:
    bullet_lower = bullet.lower()

    if "about page" in bullet_lower or "about:" in bullet_lower or "mission" in bullet_lower or "what we do" in bullet_lower:
        for source_id in sources:
            info = source_infos.get(source_id)
            if info and (
                "about" in source_id.lower()
                or "what-we-do" in source_id.lower()
                or "about" in info.title.lower()
                or "what we do" in info.title.lower()
            ):
                return source_id

    if "contact page" in bullet_lower or "contact:" in bullet_lower or "hotline" in bullet_lower:
        for source_id in sources:
            info = source_infos.get(source_id)
            if info and ("contact" in source_id.lower() or "contact" in info.title.lower()):
                return source_id

    if "phone" in bullet_lower or "email" in bullet_lower or "mailing address" in bullet_lower:
        for source_id in sources:
            if "contact" in source_id.lower():
                return source_id

    for source_id in sources:
        sid_lower = source_id.lower()
        tokens = [token for token in re.split(r"[-_]", sid_lower.removeprefix("src-")) if len(token) > 3]
        if any(token in bullet_lower for token in tokens):
            return source_id

    if "official" in bullet_lower:
        for source_id in sources:
            info = source_infos.get(source_id)
            if info and info.reliability in {"self_reported", "official"}:
                return source_id

    for source_id in sources:
        info = source_infos.get(source_id)
        if info and info.reliability == "primary":
            return source_id

    return sources[0]


def is_placeholder_bullet(line: str) -> bool:
    stripped = line.strip()
    if not stripped.startswith("- "):
        return True
    lower = stripped.lower()
    return any(
        phrase in lower
        for phrase in (
            "has not yet been drafted",
            "has not yet been",
            "not yet drafted",
            "future work",
            "add context",
            "add sourced facts",
        )
    )


def format_footnote_def(source_id: str, label_num: int, title: str, note: str) -> str:
    return f"[^{label_num}]: `{source_id}` — {title}. {note}"


def extract_research_debt_items(body: str) -> list[str]:
    items: list[str] = []
    in_section = False
    for line in body.splitlines():
        if line.startswith("## "):
            in_section = line.strip() == "## Research Debt"
            continue
        if in_section and line.strip().startswith("- "):
            items.append(line.strip()[2:].strip())
    return items


def replace_research_debt(body: str, new_items: list[str]) -> str:
    lines = body.splitlines()
    output: list[str] = []
    in_section = False
    replaced = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("## "):
            if in_section and not replaced:
                for item in new_items:
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
        for item in new_items:
            output.append(f"- {item}")

    return "\n".join(output).rstrip() + "\n"


def strip_footnote_defs(lines: list[str]) -> list[str]:
    cleaned: list[str] = []
    for line in lines:
        if FOOTNOTE_DEF_PATTERN.match(line):
            continue
        cleaned.append(line)
    while cleaned and cleaned[-1].strip() == "":
        cleaned.pop()
    return cleaned


def citation_sections_fully_footnoted(body: str, sources: list[str]) -> bool:
    if not sources:
        return False
    lines = body.splitlines()
    in_section = False
    has_bullet = False
    for line in lines:
        if line.startswith("## "):
            in_section = line.strip() in {f"## {name}" for name in CITATION_SECTIONS}
            continue
        if not in_section:
            continue
        if line.strip().startswith("- ") and not is_placeholder_bullet(line):
            has_bullet = True
            if not FOOTNOTE_REF_PATTERN.search(line):
                return False
    if not has_bullet:
        return False
    defs = [line for line in lines if FOOTNOTE_DEF_PATTERN.match(line)]
    return len(defs) >= 1


def process_page(path: Path, dry_run: bool = False, sync_sources_only: bool = False) -> bool:
    metadata, raw_metadata, body = load_yaml_front_matter(path)
    sources = metadata.get("sources") or []
    if not sources:
        return False

    source_infos = {sid: info for sid in sources if (info := load_source_info(sid)) is not None}
    if not source_infos:
        return False

    if sync_sources_only:
        footnote_map = extract_footnote_map(body)
        if not footnote_map:
            return False
        synced_body = sync_sources_section(body, footnote_map, sources, source_infos)
        if synced_body.rstrip() == body.rstrip():
            return False
        if not dry_run:
            path.write_text(rebuild_file(raw_metadata, synced_body), encoding="utf-8")
        return True

    if citation_sections_fully_footnoted(body, sources):
        footnote_map = extract_footnote_map(body)
        if not footnote_map:
            return False
        synced_body = sync_sources_section(body, footnote_map, sources, source_infos)
        if synced_body.rstrip() == body.rstrip():
            return False
        if not dry_run:
            path.write_text(rebuild_file(raw_metadata, synced_body), encoding="utf-8")
        return True

    lines = strip_footnote_defs(body.splitlines())
    output: list[str] = []
    current_section: str | None = None
    section_lines: list[str] = []
    changed = False

    label_for_source: dict[str, int] = {}
    next_label = 1
    mapped_sources: set[str] = set()
    has_litigation_claim = False
    has_self_reported = any(info.reliability == "self_reported" for info in source_infos.values())

    def label_for(source_id: str) -> int:
        nonlocal next_label
        if source_id not in label_for_source:
            label_for_source[source_id] = next_label
            next_label += 1
        return label_for_source[source_id]

    def process_citation_lines(raw_lines: list[str]) -> list[str]:
        nonlocal changed, has_litigation_claim
        processed: list[str] = []
        for line in raw_lines:
            if not line.strip().startswith("- ") or is_placeholder_bullet(line):
                processed.append(line)
                continue

            bullet_text = FOOTNOTE_REF_PATTERN.sub("", line).rstrip()
            if any(keyword in bullet_text.lower() for keyword in LITIGATION_KEYWORDS):
                has_litigation_claim = True

            source_id = choose_source_for_bullet(bullet_text, sources, source_infos)
            mapped_sources.add(source_id)
            num = label_for(source_id)
            new_line = f"{bullet_text}[^{num}]"
            if new_line != line.rstrip():
                changed = True
            processed.append(new_line)

        return processed

    def flush_section() -> None:
        nonlocal section_lines
        if current_section in CITATION_SECTIONS:
            output.extend(process_citation_lines(section_lines))
        else:
            output.extend(section_lines)
        section_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]
        section_match = SECTION_PATTERN.match(line)
        if section_match:
            flush_section()
            current_section = section_match.group(1).strip()
            output.append(line)
            i += 1
            continue

        if current_section in CITATION_SECTIONS:
            section_lines.append(line)
            i += 1
            continue

        output.append(line)
        i += 1

    flush_section()

    if label_for_source:
        insert_at = len(output)
        for idx, out_line in enumerate(output):
            if out_line.startswith("## ") and idx > 0:
                prev_sections = [l.strip() for l in output[:idx] if l.startswith("## ")]
                if any(name in prev_sections for name in ("## Verified Facts", "## Historical Context")):
                    if out_line.strip() not in ("## Verified Facts", "## Historical Context"):
                        insert_at = idx
                        break

        defs: list[str] = [""]
        for source_id, num in sorted(label_for_source.items(), key=lambda item: item[1]):
            info = source_infos[source_id]
            title = source_title_from_page(body, source_id) or info.title
            defs.append(format_footnote_def(source_id, num, title, info.reliability_note))
        defs.append("")
        if insert_at == len(output):
            output.extend(defs)
        else:
            output[insert_at:insert_at] = defs

    new_body = "\n".join(output)
    if not new_body.endswith("\n"):
        new_body += "\n"

    debt_items = extract_research_debt_items(new_body)
    additions: list[str] = []
    if has_self_reported:
        additions.append(SELF_REPORTED_DEBT)
    if has_litigation_claim and has_self_reported:
        additions.append(LITIGATION_DEBT)
    if len(sources) > 1:
        additions.append(MAPPING_DEBT)

    for item in additions:
        if item not in debt_items:
            debt_items.append(item)
            changed = True

    if additions:
        new_body = replace_research_debt(new_body, debt_items)

    footnote_map = extract_footnote_map(new_body)
    if footnote_map:
        synced_body = sync_sources_section(new_body, footnote_map, sources, source_infos)
        if synced_body.rstrip() != new_body.rstrip():
            new_body = synced_body
            changed = True

    if new_body.rstrip() != body.rstrip():
        changed = True

    if changed and not dry_run:
        path.write_text(rebuild_file(raw_metadata, new_body), encoding="utf-8")

    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Add per-claim footnotes to knowledge pages.")
    parser.add_argument("--dry-run", action="store_true", help="Report files that would change without writing.")
    parser.add_argument(
        "--sync-sources",
        action="store_true",
        help="Only renumber the Sources section to match existing footnotes.",
    )
    args = parser.parse_args()

    paths = sorted(
        path
        for path in KNOWLEDGE_DIR.rglob("*.md")
        if "_templates" not in path.parts and path.name != "README.md"
    )

    changed_files: list[str] = []
    skipped_no_sources = 0
    for path in paths:
        metadata, _, _ = load_yaml_front_matter(path)
        if not metadata.get("sources"):
            skipped_no_sources += 1
            continue
        if process_page(path, dry_run=args.dry_run, sync_sources_only=args.sync_sources):
            changed_files.append(str(path.relative_to(ROOT)))

    mode = "Would update" if args.dry_run else "Updated"
    print(f"{mode} {len(changed_files)} knowledge page(s).")
    if changed_files:
        for name in changed_files:
            print(f"  - {name}")
    print(f"Skipped {skipped_no_sources} page(s) without sources.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
