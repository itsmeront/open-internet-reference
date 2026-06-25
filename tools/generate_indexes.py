"""Generate machine-readable OIR indexes from Markdown metadata."""

from __future__ import annotations

import json
import os
import re
import shutil
from datetime import date
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - exercised only when setup is incomplete.
    print("PyYAML is required. Install docs dependencies with: python -m pip install -e .[docs]")
    raise SystemExit(2)


ROOT = Path(__file__).resolve().parents[1]
GENERATED_DIR = ROOT / "generated"
WEBSITE_GENERATED_DIR = ROOT / "website" / "generated"
SOURCE_DOCS_DIR = WEBSITE_GENERATED_DIR / "source-docs"
GITHUB_REPO_URL = "https://github.com/itsmeront/open-internet-reference"
SOURCE_CODE_ID_PATTERN = re.compile(r"`(SRC-[A-Z0-9-]+)`")
USED_FOR_ITEM_PATTERN = re.compile(r"^-\s+(.+?)\s*$")
METADATA_ITEM_PATTERN = re.compile(r"^-\s+([^:]+):\s*(.*?)\s*$")
CONTENT_DIRS = {
    "bibliography": ROOT / "bibliography",
    "knowledge": ROOT / "knowledge",
}
URL_IN_BACKTICKS_PATTERN = re.compile(r"`(https?://[^\s`]+)`")


def iter_markdown_files(directory: Path) -> list[Path]:
    if not directory.exists():
        return []
    return sorted(
        path
        for path in directory.rglob("*.md")
        if "_templates" not in path.parts and path.name != "README.md"
    )


def load_front_matter(path: Path) -> dict[str, Any] | None:
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


def markdown_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return text
    try:
        _, _, body = text.split("---\n", 2)
    except ValueError:
        return text
    return body


def used_for_terms(path: Path) -> list[str]:
    terms: list[str] = []
    in_used_for = False

    for line in markdown_body(path).splitlines():
        if line.startswith("## "):
            in_used_for = line.strip().lower() == "## used for"
            continue
        if not in_used_for:
            continue
        match = USED_FOR_ITEM_PATTERN.match(line)
        if match:
            terms.append(match.group(1).strip())

    return terms


def bibliographic_metadata(path: Path) -> dict[str, str]:
    metadata: dict[str, str] = {}
    in_metadata = False

    for line in markdown_body(path).splitlines():
        if line.startswith("## "):
            in_metadata = line.strip().lower() == "## bibliographic metadata"
            continue
        if not in_metadata:
            continue
        match = METADATA_ITEM_PATTERN.match(line)
        if match:
            key = match.group(1).strip().lower()
            value = match.group(2).strip()
            if value:
                metadata[key] = value

    return metadata


def source_doc_path(source_path: str) -> str:
    return f"source-docs/{source_path}"


def record_for(path: Path, metadata: dict[str, Any]) -> dict[str, Any]:
    relative_path = path.relative_to(ROOT).as_posix()
    body_metadata = bibliographic_metadata(path)
    return {
        "id": metadata.get("id"),
        "title": metadata.get("title"),
        "type": metadata.get("type"),
        "status": metadata.get("status"),
        "summary": metadata.get("summary"),
        "tags": metadata.get("tags", []),
        "sources": metadata.get("sources", []),
        "relationships": metadata.get("relationships", []),
        "last_verified": metadata.get("last_verified"),
        "path": relative_path,
        "source_doc_path": source_doc_path(relative_path),
        "used_for": used_for_terms(path),
        "bibliographic_metadata": body_metadata,
    }


def records_from(directory: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in iter_markdown_files(directory):
        metadata = load_front_matter(path)
        if metadata is None:
            continue
        records.append(record_for(path, metadata))
    return sorted(records, key=lambda record: record["id"])


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(json.dumps(record, sort_keys=True) for record in records) + "\n",
        encoding="utf-8",
    )


def markdown_escape(value: Any) -> str:
    text = "" if value is None else str(value)
    return text.replace("|", "\\|")


def markdown_link(label: str, target: str) -> str:
    return f"[`{markdown_escape(label)}`]({target})"


def text_markdown_link(label: str, target: str) -> str:
    return f"[{markdown_escape(label)}]({target})"


def anchor_for(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "item"


def citation_source_ids(record: dict[str, Any]) -> set[str]:
    source_ids = set(record.get("sources", []))
    for relationship in record.get("relationships", []):
        if not isinstance(relationship, dict):
            continue
        source_ids.update(relationship.get("sources", []))
    return source_ids


def citation_backlinks(
    source_id: str,
    citing_records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    return [
        record
        for record in citing_records
        if source_id in citation_source_ids(record)
    ]


def citation_usages(
    source_id: str,
    citing_records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    usages: list[dict[str, Any]] = []
    for record in citing_records:
        if source_id in set(record.get("sources", [])):
            usages.append(
                {
                    "record_id": record["id"],
                    "record_title": record["title"],
                    "usage": "page_source",
                }
            )

        for relationship in record.get("relationships", []):
            if not isinstance(relationship, dict):
                continue
            if source_id not in set(relationship.get("sources", [])):
                continue
            usages.append(
                {
                    "record_id": record["id"],
                    "record_title": record["title"],
                    "usage": "relationship_source",
                    "subject": relationship.get("subject"),
                    "predicate": relationship.get("predicate"),
                    "object": relationship.get("object"),
                }
            )

    return sorted(
        usages,
        key=lambda usage: (
            str(usage.get("record_id")),
            str(usage.get("usage")),
            str(usage.get("subject")),
            str(usage.get("predicate")),
            str(usage.get("object")),
        ),
    )


def link_for_record(record_id: str, records_by_id: dict[str, dict[str, Any]], from_path: Path) -> str:
    record = records_by_id[record_id]
    target_path = WEBSITE_GENERATED_DIR / record["source_doc_path"]
    return os.path.relpath(target_path, from_path.parent).replace("\\", "/")


def link_for_id(record_id: str, records_by_id: dict[str, dict[str, Any]], from_path: Path) -> str:
    if record_id in records_by_id:
        return markdown_link(record_id, link_for_record(record_id, records_by_id, from_path))
    return f"`{markdown_escape(record_id)}`"


def runtime_pretty_url(markdown_path: str) -> str:
    if markdown_path.endswith(".md"):
        return f"../{markdown_path[:-3]}/"
    return f"../{markdown_path}"


def used_for_link_for(
    term: str,
    from_path: Path,
    records_by_title: dict[str, dict[str, Any]],
) -> str:
    matching_record = records_by_title.get(term.lower())
    if matching_record:
        target_path = WEBSITE_GENERATED_DIR / matching_record["source_doc_path"]
        target = os.path.relpath(target_path, from_path.parent).replace("\\", "/")
        return text_markdown_link(term, target)

    used_for_path = WEBSITE_GENERATED_DIR / "used-for.md"
    relative_path = os.path.relpath(used_for_path, from_path.parent).replace("\\", "/")
    return text_markdown_link(term, f"{relative_path}#{anchor_for(term)}")


def record_section(
    record: dict[str, Any],
    citing_records: list[dict[str, Any]] | None = None,
) -> str:
    tags = ", ".join(record.get("tags", []))
    parts = [
        f"## `{record['id']}`: {markdown_escape(record['title'])} {{ #{record['id']} }}",
        "",
        f"- Type: `{markdown_escape(record['type'])}`",
        f"- Status: `{markdown_escape(record['status'])}`",
        f"- Path: {markdown_link(record['path'], record['source_doc_path'])}",
    ]
    if tags:
        parts.append(f"- Tags: {markdown_escape(tags)}")
    summary = record.get("summary")
    if summary:
        parts.extend(["", markdown_escape(summary)])
    if citing_records is not None:
        backlinks = citation_backlinks(record["id"], citing_records)
        parts.extend(["", "### Cited By"])
        if backlinks:
            for backlink in backlinks:
                link = markdown_link(
                    f"{backlink['id']}: {backlink['title']}",
                    backlink["source_doc_path"],
                )
                parts.append(f"- {link}")
        else:
            parts.append("- No citing knowledge records yet.")
    return "\n".join(parts)


def write_bibliography_markdown(
    records: list[dict[str, Any]],
    citing_records: list[dict[str, Any]],
) -> None:
    lines = [
        "# Generated Bibliography",
        "",
        "This page is generated from bibliography metadata. Do not edit it manually.",
        "",
        f"Record count: {len(records)}",
        "",
    ]

    for record in records:
        lines.append(record_section(record, citing_records))
        lines.append("")

    write_markdown(WEBSITE_GENERATED_DIR / "bibliography.md", lines)


def citation_index_payload(
    source_records: list[dict[str, Any]],
    citing_records: list[dict[str, Any]],
) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "description": "Generated citation usage index.",
        "sources": [
            {
                "source_id": source["id"],
                "source_title": source["title"],
                "usages": citation_usages(source["id"], citing_records),
            }
            for source in source_records
        ],
    }


def usage_line(
    usage: dict[str, Any],
    records_by_id: dict[str, dict[str, Any]],
    citation_path: Path,
) -> str:
    record = link_for_id(str(usage["record_id"]), records_by_id, citation_path)
    if usage["usage"] == "page_source":
        return f"- Page source in {record}"

    subject = link_for_id(str(usage["subject"]), records_by_id, citation_path)
    obj = link_for_id(str(usage["object"]), records_by_id, citation_path)
    predicate = markdown_escape(usage["predicate"])
    return f"- Relationship source in {record}: {subject} `{predicate}` {obj}"


def write_citation_index_markdown(
    source_records: list[dict[str, Any]],
    citing_records: list[dict[str, Any]],
    records_by_id: dict[str, dict[str, Any]],
) -> None:
    citation_path = WEBSITE_GENERATED_DIR / "citations.md"
    lines = [
        "# Generated Citation Index",
        "",
        "This page is generated from `sources` and relationship source metadata. Do not edit it manually.",
        "",
        f"Source count: {len(source_records)}",
        "",
    ]

    for source in source_records:
        source_link = link_for_id(source["id"], records_by_id, citation_path)
        lines.extend([f"## {source_link}: {markdown_escape(source['title'])}", ""])
        usages = citation_usages(source["id"], citing_records)
        if usages:
            for usage in usages:
                lines.append(usage_line(usage, records_by_id, citation_path))
        else:
            lines.append("- No citation usages yet.")
        lines.append("")

    write_markdown(citation_path, lines)


def write_glossary_markdown(records: list[dict[str, Any]]) -> None:
    lines = [
        "# Generated Glossary",
        "",
        "This page is generated from knowledge metadata. Do not edit it manually.",
        "",
        f"Record count: {len(records)}",
        "",
    ]

    for record in records:
        lines.append(record_section(record))
        lines.append("")

    write_markdown(WEBSITE_GENERATED_DIR / "glossary.md", lines)


def used_for_index(records: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    index: dict[str, list[dict[str, Any]]] = {}
    for record in records:
        for term in record.get("used_for", []):
            index.setdefault(term, []).append(record)
    return {
        term: sorted(term_records, key=lambda record: record["id"])
        for term, term_records in sorted(index.items(), key=lambda item: item[0].lower())
    }


def write_used_for_markdown(records: list[dict[str, Any]]) -> None:
    index = used_for_index(records)
    used_for_path = WEBSITE_GENERATED_DIR / "used-for.md"
    lines = [
        "# Generated Used For Index",
        "",
        "This page is generated from `Used For` sections in source records. Do not edit it manually.",
        "",
        f"Term count: {len(index)}",
        "",
    ]

    for term, term_records in index.items():
        lines.extend([f"## {markdown_escape(term)} {{ #{anchor_for(term)} }}", ""])
        for record in term_records:
            target_path = WEBSITE_GENERATED_DIR / record["source_doc_path"]
            target = os.path.relpath(target_path, used_for_path.parent).replace("\\", "/")
            label = f"{record['id']}: {record['title']}"
            lines.append(f"- {markdown_link(label, target)}")
        lines.append("")

    write_markdown(used_for_path, lines)


def count_by(records: list[dict[str, Any]], field: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for record in records:
        value = str(record.get(field) or "unknown")
        counts[value] = counts.get(value, 0) + 1
    return dict(sorted(counts.items()))


def records_missing_last_verified(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        record
        for record in records
        if record.get("last_verified") in (None, "")
    ]


def records_needing_review(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        record
        for record in records
        if record.get("status") in {"draft", "needs_sources", "in_review"}
    ]


def record_link_line(record: dict[str, Any], from_path: Path) -> str:
    target_path = WEBSITE_GENERATED_DIR / record["source_doc_path"]
    target = os.path.relpath(target_path, from_path.parent).replace("\\", "/")
    label = f"{record['id']}: {record['title']}"
    return f"- {markdown_link(label, target)}"


def write_count_section(lines: list[str], title: str, counts: dict[str, int]) -> None:
    lines.extend([f"## {title}", ""])
    if not counts:
        lines.extend(["No records.", ""])
        return
    for key, value in counts.items():
        slug = key.lower().replace(" ", "-").replace("_", "-")
        anchor = f"#{slug}-records"
        lines.append(f"- [`{markdown_escape(key)}`]({anchor}): {value}")
    lines.append("")


def write_record_list_section(
    lines: list[str],
    title: str,
    records: list[dict[str, Any]],
    dashboard_path: Path,
) -> None:
    lines.extend([f"## {title}", ""])
    if not records:
        lines.extend(["No records.", ""])
        return
    for record in sorted(records, key=lambda item: item["id"]):
        lines.append(record_link_line(record, dashboard_path))
    lines.append("")


def review_status_payload(records: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "description": "Generated review status dashboard.",
        "totals": {
            "records": len(records),
            "missing_last_verified": len(records_missing_last_verified(records)),
            "needing_review": len(records_needing_review(records)),
        },
        "by_status": count_by(records, "status"),
        "by_type": count_by(records, "type"),
        "missing_last_verified": [
            record["id"]
            for record in records_missing_last_verified(records)
        ],
        "needing_review": [
            record["id"]
            for record in records_needing_review(records)
        ],
    }


def write_review_status_markdown(records: list[dict[str, Any]]) -> None:
    dashboard_path = WEBSITE_GENERATED_DIR / "review-status.md"
    payload = review_status_payload(records)
    lines = [
        "# Generated Review Status Dashboard",
        "",
        "This page is generated from OIR metadata. Do not edit it manually.",
        "",
        "## Totals",
        "",
        f"- Records: {payload['totals']['records']}",
        f"- Records needing review: {payload['totals']['needing_review']}",
        f"- Records missing `last_verified`: {payload['totals']['missing_last_verified']}",
        "",
    ]
    write_count_section(lines, "By Status", payload["by_status"])
    write_count_section(lines, "By Type", payload["by_type"])
    write_record_list_section(
        lines,
        "Records Needing Review",
        records_needing_review(records),
        dashboard_path,
    )
    write_record_list_section(
        lines,
        "Records Missing Verification Date",
        records_missing_last_verified(records),
        dashboard_path,
    )

    # Per-status filtered sections
    for status_value in sorted(payload["by_status"].keys()):
        section_records = [r for r in records if r.get("status") == status_value]
        slug = status_value.lower().replace(" ", "-").replace("_", "-")
        section_title = f"{status_value} Records"
        lines.extend([f"## {section_title} {{ #{slug}-records }}", ""])
        for record in sorted(section_records, key=lambda r: r["id"]):
            lines.append(record_link_line(record, dashboard_path))
        lines.append("")

    # Per-type filtered sections
    for type_value in sorted(payload["by_type"].keys()):
        section_records = [r for r in records if r.get("type") == type_value]
        slug = type_value.lower().replace(" ", "-").replace("_", "-")
        section_title = f"{type_value} Records"
        lines.extend([f"## {section_title} {{ #{slug}-records }}", ""])
        for record in sorted(section_records, key=lambda r: r["id"]):
            lines.append(record_link_line(record, dashboard_path))
        lines.append("")

    write_markdown(dashboard_path, lines)


def outreach_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        [
            record
            for record in records
            if "outreach" in set(record.get("tags", []))
        ],
        key=lambda record: (str(record.get("type")), record["id"]),
    )


def outreach_payload(records: list[dict[str, Any]]) -> dict[str, Any]:
    outreach_items = outreach_records(records)
    return {
        "schema_version": 1,
        "description": "Generated outreach CRM prototype from outreach-tagged metadata records.",
        "record_count": len(outreach_items),
        "records": [
            {
                "id": record["id"],
                "title": record["title"],
                "type": record["type"],
                "status": record["status"],
                "summary": record.get("summary"),
                "tags": record.get("tags", []),
                "sources": record.get("sources", []),
                "path": record["path"],
                "source_doc_path": record["source_doc_path"],
                "last_verified": record.get("last_verified"),
            }
            for record in outreach_items
        ],
    }


def write_outreach_markdown(
    records: list[dict[str, Any]],
    records_by_id: dict[str, dict[str, Any]],
) -> None:
    outreach_path = WEBSITE_GENERATED_DIR / "outreach.md"
    outreach_items = outreach_records(records)
    lines = [
        "# Generated Outreach CRM",
        "",
        "This page is generated from records tagged `outreach`. Do not edit it manually.",
        "",
        "This is a prototype index, not a verified contact database. Contact details should be checked against official public sources before use.",
        "",
        f"Record count: {len(outreach_items)}",
        "",
    ]

    for record in outreach_items:
        record_link = link_for_id(record["id"], records_by_id, outreach_path)
        lines.extend(
            [
                f"## {record_link}: {markdown_escape(record['title'])}",
                "",
                f"- Type: `{markdown_escape(record['type'])}`",
                f"- Status: `{markdown_escape(record['status'])}`",
            ]
        )
        if record.get("last_verified"):
            lines.append(f"- Last verified: `{markdown_escape(record['last_verified'])}`")
        if record.get("sources"):
            source_links = [
                link_for_id(str(source), records_by_id, outreach_path)
                for source in record["sources"]
            ]
            lines.append(f"- Sources: {', '.join(source_links)}")
        if record.get("summary"):
            lines.extend(["", markdown_escape(record["summary"])])
        lines.append("")

    write_markdown(outreach_path, lines)


def handbook_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        [
            record
            for record in records
            if record.get("type") != "source"
        ],
        key=lambda record: (str(record.get("type")), record["id"]),
    )


def handbook_payload(records: list[dict[str, Any]]) -> dict[str, Any]:
    items = handbook_records(records)
    return {
        "schema_version": 1,
        "description": "Generated linear handbook prototype from knowledge metadata.",
        "record_count": len(items),
        "records": [
            {
                "id": record["id"],
                "title": record["title"],
                "type": record["type"],
                "status": record["status"],
                "summary": record.get("summary"),
                "sources": record.get("sources", []),
                "path": record["path"],
                "source_doc_path": record["source_doc_path"],
            }
            for record in items
        ],
    }


def read_project_version() -> str:
    pyproject_path = ROOT / "pyproject.toml"
    if not pyproject_path.exists():
        return "0.0.0"
    match = re.search(r'^version\s*=\s*"([^"]+)"', pyproject_path.read_text(encoding="utf-8"), re.MULTILINE)
    return match.group(1) if match else "0.0.0"


def read_release_status() -> str:
    changelog_path = ROOT / "CHANGELOG.md"
    if not changelog_path.exists():
        return "Unreleased"
    changelog = changelog_path.read_text(encoding="utf-8")
    if "## Unreleased" in changelog:
        return "Unreleased"
    match = re.search(r"^## (\d+\.\d+\.\d+)\s*$", changelog, re.MULTILINE)
    return match.group(1) if match else "Unreleased"


def handbook_publication_metadata(
    items: list[dict[str, Any]],
    cited_source_ids: list[str],
) -> dict[str, str | int]:
    version = read_project_version()
    release_status = read_release_status()
    release_label = f"{version} ({release_status})" if release_status == "Unreleased" else version
    return {
        "version": version,
        "release_status": release_status,
        "release_label": release_label,
        "generated_date": date.today().isoformat(),
        "record_count": len(items),
        "source_count": len(cited_source_ids),
    }


def handbook_cover_lines(publication: dict[str, str | int]) -> list[str]:
    return [
        '<div class="oir-print-cover" markdown="0">',
        '  <div class="oir-print-cover__frame">',
        '    <img class="oir-print-cover__logo" src="../../assets/images/oir-logo-v5-fullmesh.svg" alt="Open Internet Reference" />',
        '    <p class="oir-print-cover__edition">Handbook Edition</p>',
        '    <p class="oir-print-cover__motto">Evidence over assertion. Knowledge over opinion.</p>',
        '    <dl class="oir-print-cover__meta">',
        "      <div>",
        "        <dt>Release</dt>",
        f"        <dd>{markdown_escape(str(publication['release_label']))}</dd>",
        "      </div>",
        "      <div>",
        "        <dt>Generated</dt>",
        f"        <dd>{markdown_escape(str(publication['generated_date']))}</dd>",
        "      </div>",
        "      <div>",
        "        <dt>Knowledge records</dt>",
        f"        <dd>{publication['record_count']}</dd>",
        "      </div>",
        "      <div>",
        "        <dt>Sources referenced</dt>",
        f"        <dd>{publication['source_count']}</dd>",
        "      </div>",
        "      <div>",
        "        <dt>Document type</dt>",
        "        <dd>Generated handbook prototype</dd>",
        "      </div>",
        "      <div>",
        "        <dt>Publisher</dt>",
        "        <dd>Open Internet Reference</dd>",
        "      </div>",
        "    </dl>",
        '    <p class="oir-print-cover__note">This edition is generated automatically from repository metadata. Formal public releases will be tagged in version control and recorded in CHANGELOG.md.</p>',
        "  </div>",
        "</div>",
        "",
    ]


def handbook_cited_source_ids(items: list[dict[str, Any]]) -> list[str]:
    cited: set[str] = set()
    for record in items:
        cited.update(str(source) for source in record.get("sources", []))
    return sorted(cited)


def handbook_context_lines(*, for_print: bool) -> list[str]:
    lines = [
        "## About Open Internet Reference",
        "",
        "**Open Internet Reference (OIR)** is an evidence-based knowledge base documenting the legal, constitutional, historical, technical, and public policy landscape surrounding the open internet.",
        "",
        "**Motto:** Evidence over assertion. Knowledge over opinion.",
        "",
        "OIR covers internet architecture, distributed systems, peer-to-peer networking, cryptography, open source software, privacy, constitutional law, internet governance, and digital rights. It is intended for technologists, researchers, attorneys, policymakers, journalists, and civil society organizations.",
        "",
        "OIR follows strict research standards: significant claims should be independently verifiable, primary sources are preferred, and review statuses such as `draft` and `verified` indicate editorial progress.",
        "",
        "## How to Read This Handbook",
        "",
        "This document is a **linear reading view** generated automatically from OIR knowledge metadata. It is a prototype handbook, not yet a polished narrative edition.",
        "",
        "- **Index** — every knowledge record in this edition, grouped by type, with links to each entry.",
        "- **Glossary** — quick-reference definitions for each record.",
        "- **Knowledge Records** — the main handbook content.",
        "- **Sources Referenced** — primary sources cited by the records above.",
        "",
        "**Bibliography note:** Each knowledge record lists its own sources. This handbook includes a compact **Sources Referenced** appendix rather than the full OIR bibliography, because the full catalog contains many source records not cited here and would largely repeat information already shown per entry.",
        "",
    ]
    if for_print:
        lines.extend(
            [
                "Readers with web access can consult the complete OIR bibliography, relationship graph, timeline, and review-status indexes for broader repository navigation.",
                "",
            ]
        )
    else:
        lines.extend(
            [
                "For the complete source catalog, see the [Generated Bibliography](bibliography.md).",
                "",
            ]
        )
    return lines


def handbook_index_lines(
    items: list[dict[str, Any]],
    records_by_id: dict[str, dict[str, Any]],
    from_path: Path,
    *,
    internal_links: bool,
) -> list[str]:
    lines = [
        "## Index",
        "",
        "Knowledge records included in this handbook, grouped by type.",
        "",
    ]
    current_type = None
    for record in items:
        record_type = str(record.get("type") or "unknown")
        if record_type != current_type:
            if current_type is not None:
                lines.append("")
            current_type = record_type
            lines.extend([f"### {markdown_escape(record_type.replace('_', ' ').title())}", ""])

        if internal_links:
            lines.append(
                f"- {text_markdown_link(record['title'], f'#{record['id']}')} "
                f"(`{markdown_escape(record['id'])}`)"
            )
        else:
            record_link = link_for_id(record["id"], records_by_id, from_path)
            lines.append(f"- {record_link}: {markdown_escape(record['title'])}")
    lines.append("")
    return lines


def handbook_glossary_lines(items: list[dict[str, Any]]) -> list[str]:
    lines = [
        "## Glossary",
        "",
        "Quick reference for knowledge records included in this handbook.",
        "",
    ]
    for record in sorted(items, key=lambda item: str(item.get("title", "")).lower()):
        lines.extend([f"### {markdown_escape(record['title'])} {{ #{record['id']}-glossary }}", ""])
        lines.append(f"- **Record ID:** `{markdown_escape(record['id'])}`")
        lines.append(f"- **Type:** {markdown_escape(str(record.get('type') or 'unknown'))}")
        lines.append(f"- **Status:** {markdown_escape(str(record.get('status') or 'unknown'))}")
        if record.get("tags"):
            tag_list = ", ".join(markdown_escape(str(tag)) for tag in record["tags"])
            lines.append(f"- **Tags:** {tag_list}")
        if record.get("summary"):
            lines.extend(["", markdown_escape(record["summary"])])
        lines.append("")
    return lines


def handbook_knowledge_record_lines(
    items: list[dict[str, Any]],
    records_by_id: dict[str, dict[str, Any]],
    from_path: Path,
    *,
    web_links: bool,
    print_style: bool,
) -> list[str]:
    lines = ["## Knowledge Records", ""]
    current_type = None
    for record in items:
        record_type = str(record.get("type") or "unknown")
        if record_type != current_type:
            current_type = record_type
            lines.extend([f"### {markdown_escape(record_type.replace('_', ' ').title())}", ""])

        if web_links:
            record_link = link_for_id(record["id"], records_by_id, from_path)
            lines.extend(
                [
                    f"#### {record_link}: {markdown_escape(record['title'])} {{ #{record['id']} }}",
                    "",
                    f"- Status: `{markdown_escape(record['status'])}`",
                ]
            )
            if record.get("sources"):
                source_links = [
                    link_for_id(str(source), records_by_id, from_path)
                    for source in record["sources"]
                ]
                lines.append(f"- Sources: {', '.join(source_links)}")
        else:
            lines.extend([f"#### {markdown_escape(record['title'])} {{ #{record['id']} }}", ""])
            lines.append(f"- **Record ID:** `{markdown_escape(record['id'])}`")
            lines.append(f"- **Status:** {markdown_escape(str(record.get('status') or 'unknown'))}")
            if record.get("sources"):
                source_refs = [
                    print_source_reference(str(source), records_by_id)
                    for source in record["sources"]
                ]
                lines.append(f"- **Sources:** {', '.join(source_refs)}")
            if record.get("tags"):
                tag_list = ", ".join(markdown_escape(str(tag)) for tag in record["tags"])
                lines.append(f"- **Tags:** {tag_list}")

        if record.get("summary"):
            lines.extend(["", markdown_escape(record["summary"])])

        if print_style:
            lines.extend(["", "---", ""])
        else:
            lines.append("")

    return lines


def handbook_sources_appendix_lines(
    cited_source_ids: list[str],
    records_by_id: dict[str, dict[str, Any]],
    from_path: Path,
    *,
    web_links: bool,
    print_style: bool,
) -> list[str]:
    lines = [
        "## Sources Referenced in This Handbook",
        "",
        "Primary sources cited by knowledge records in this edition. This appendix is not the full OIR bibliography.",
        "",
    ]
    for source_id in cited_source_ids:
        source_record = records_by_id.get(source_id)
        if not source_record:
            lines.append(f"- `{markdown_escape(source_id)}`")
            continue

        if web_links:
            source_link = link_for_id(source_id, records_by_id, from_path)
            lines.append(
                f"- {source_link}: {markdown_escape(source_record['title'])} "
                f"(`{markdown_escape(str(source_record.get('status') or 'unknown'))}`)"
            )
            continue

        lines.extend([f"### {markdown_escape(source_record['title'])}", ""])
        lines.append(f"- **Source ID:** `{markdown_escape(source_id)}`")
        lines.append(f"- **Status:** {markdown_escape(str(source_record.get('status') or 'unknown'))}")
        summary = source_record.get("summary")
        if summary:
            lines.extend(["", markdown_escape(summary)])
        if print_style:
            lines.extend(["", "---", ""])
        else:
            lines.append("")

    if not cited_source_ids:
        lines.append("- No cited sources yet.")
        lines.append("")

    return lines


def write_handbook_markdown(
    records: list[dict[str, Any]],
    records_by_id: dict[str, dict[str, Any]],
) -> None:
    handbook_path = WEBSITE_GENERATED_DIR / "handbook.md"
    items = handbook_records(records)
    cited_source_ids = handbook_cited_source_ids(items)
    publication = handbook_publication_metadata(items, cited_source_ids)
    lines = [
        "# Generated Handbook",
        "",
        "This page is generated from knowledge metadata. Do not edit it manually.",
        "",
        f"**Release:** {publication['release_label']} | **Generated:** {publication['generated_date']} | "
        f"**Records:** {publication['record_count']} | **Sources referenced:** {publication['source_count']}",
        "",
        '<div class="oir-handbook" markdown="1">',
        "",
    ]
    lines.extend(handbook_context_lines(for_print=False))
    lines.extend(handbook_index_lines(items, records_by_id, handbook_path, internal_links=True))
    lines.extend(handbook_glossary_lines(items))
    lines.extend(
        handbook_knowledge_record_lines(
            items,
            records_by_id,
            handbook_path,
            web_links=True,
            print_style=False,
        )
    )
    lines.extend(
        handbook_sources_appendix_lines(
            cited_source_ids,
            records_by_id,
            handbook_path,
            web_links=True,
            print_style=False,
        )
    )
    lines.extend(["</div>", ""])

    write_markdown(handbook_path, lines)


def print_source_reference(
    source_id: str,
    records_by_id: dict[str, dict[str, Any]],
) -> str:
    source_record = records_by_id.get(source_id)
    if source_record and source_record.get("title"):
        return (
            f"{markdown_escape(str(source_record['title']))} "
            f"(`{markdown_escape(source_id)}`)"
        )
    return f"`{markdown_escape(source_id)}`"


def write_print_handbook_markdown(
    records: list[dict[str, Any]],
    records_by_id: dict[str, dict[str, Any]],
) -> None:
    print_path = WEBSITE_GENERATED_DIR / "print-handbook.md"
    items = handbook_records(records)
    cited_source_ids = handbook_cited_source_ids(items)
    publication = handbook_publication_metadata(items, cited_source_ids)
    lines = [
        "# Print Handbook",
        "",
        '<p class="oir-print-screen-note">This page is generated from knowledge metadata. Use your browser\'s '
        "<strong>Print</strong> dialog and choose <strong>Save as PDF</strong> for a portable copy.</p>",
        "",
    ]
    lines.extend(handbook_cover_lines(publication))
    lines.extend(
        [
            '<div class="oir-print-handbook" markdown="1">',
            "",
        ]
    )
    lines.extend(handbook_context_lines(for_print=True))
    lines.extend(handbook_index_lines(items, records_by_id, print_path, internal_links=True))
    lines.extend(handbook_glossary_lines(items))
    lines.extend(
        handbook_knowledge_record_lines(
            items,
            records_by_id,
            print_path,
            web_links=False,
            print_style=True,
        )
    )
    lines.extend(
        handbook_sources_appendix_lines(
            cited_source_ids,
            records_by_id,
            print_path,
            web_links=False,
            print_style=True,
        )
    )
    lines.extend(["</div>", ""])
    write_markdown(print_path, lines)


def retrieval_text(record: dict[str, Any]) -> str:
    parts = [
        str(record.get("title") or ""),
        str(record.get("summary") or ""),
        " ".join(record.get("tags", [])),
        " ".join(record.get("used_for", [])),
    ]
    return "\n".join(part for part in parts if part).strip()


def retrieval_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    dataset: list[dict[str, Any]] = []
    for record in records:
        dataset.append(
            {
                "id": record["id"],
                "title": record["title"],
                "type": record["type"],
                "status": record["status"],
                "summary": record.get("summary"),
                "tags": record.get("tags", []),
                "sources": record.get("sources", []),
                "relationships": record.get("relationships", []),
                "last_verified": record.get("last_verified"),
                "path": record["path"],
                "source_doc_path": record["source_doc_path"],
                "text": retrieval_text(record),
            }
        )
    return sorted(dataset, key=lambda item: item["id"])


def retrieval_payload(records: list[dict[str, Any]]) -> dict[str, Any]:
    dataset = retrieval_records(records)
    return {
        "schema_version": 1,
        "description": "Generated AI retrieval dataset manifest.",
        "record_count": len(dataset),
        "jsonl_path": "generated/retrieval.jsonl",
    }


def timeline_date_from_record(record: dict[str, Any]) -> str | None:
    body_metadata = record.get("bibliographic_metadata", {})
    if not isinstance(body_metadata, dict):
        return None
    publication_date = body_metadata.get("publication date")
    if publication_date and publication_date.lower() != "unknown":
        return publication_date
    return None


def timeline_events(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    for record in records:
        publication_date = timeline_date_from_record(record)
        if publication_date:
            events.append(
                {
                    "date": publication_date,
                    "event_type": "publication",
                    "record_id": record["id"],
                    "record_title": record["title"],
                    "description": f"Publication date for {record['title']}.",
                }
            )
        if record.get("last_verified"):
            events.append(
                {
                    "date": str(record["last_verified"]),
                    "event_type": "verification",
                    "record_id": record["id"],
                    "record_title": record["title"],
                    "description": f"Last verified date for {record['title']}.",
                }
            )

    return sorted(
        events,
        key=lambda event: (
            event["date"],
            event["event_type"],
            event["record_id"],
        ),
    )


def timeline_payload(records: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "description": "Generated timeline from explicit publication and verification dates.",
        "events": timeline_events(records),
    }


def write_timeline_markdown(
    records: list[dict[str, Any]],
    records_by_id: dict[str, dict[str, Any]],
) -> None:
    timeline_path = WEBSITE_GENERATED_DIR / "timeline.md"
    events = timeline_events(records)
    lines = [
        "# Generated Timeline",
        "",
        "This page is generated from explicit publication and verification dates. Do not edit it manually.",
        "",
        f"Event count: {len(events)}",
        "",
    ]

    current_date = None
    for event in events:
        if event["date"] != current_date:
            current_date = event["date"]
            if lines[-1] != "":
                lines.append("")
            lines.extend([f"## {markdown_escape(current_date)}", ""])
        record_link = link_for_id(event["record_id"], records_by_id, timeline_path)
        lines.append(
            f"- `{markdown_escape(event['event_type'])}`: {record_link} - {markdown_escape(event['description'])}"
        )

    write_markdown(timeline_path, lines)


def relationship_edges(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    edges: list[dict[str, Any]] = []
    for record in records:
        for relationship in record.get("relationships", []):
            if not isinstance(relationship, dict):
                continue
            edges.append(
                {
                    "declared_in": record["id"],
                    "subject": relationship.get("subject"),
                    "predicate": relationship.get("predicate"),
                    "object": relationship.get("object"),
                    "sources": relationship.get("sources", []),
                    "notes": relationship.get("notes"),
                }
            )
    return sorted(
        edges,
        key=lambda edge: (
            str(edge.get("subject")),
            str(edge.get("predicate")),
            str(edge.get("object")),
        ),
    )


def relationship_line(edge: dict[str, Any], records_by_id: dict[str, dict[str, Any]]) -> str:
    graph_path = WEBSITE_GENERATED_DIR / "relationships.md"
    subject = link_for_id(str(edge["subject"]), records_by_id, graph_path)
    obj = link_for_id(str(edge["object"]), records_by_id, graph_path)
    declared_in = link_for_id(str(edge["declared_in"]), records_by_id, graph_path)
    sources = [
        link_for_id(str(source), records_by_id, graph_path)
        for source in edge.get("sources", [])
    ]
    parts = [
        f"## {subject} `{markdown_escape(edge['predicate'])}` {obj}",
        "",
        f"- Declared in: {declared_in}",
    ]
    if sources:
        parts.append(f"- Sources: {', '.join(sources)}")
    if edge.get("notes"):
        parts.extend(["", markdown_escape(edge["notes"])])
    return "\n".join(parts)


def write_relationships_markdown(
    edges: list[dict[str, Any]],
    records_by_id: dict[str, dict[str, Any]],
) -> None:
    lines = [
        "# Generated Relationship Graph",
        "",
        "This page is generated from relationship metadata. Do not edit it manually.",
        "",
        f"Edge count: {len(edges)}",
        "",
    ]

    for edge in edges:
        lines.append(relationship_line(edge, records_by_id))
        lines.append("")

    write_markdown(WEBSITE_GENERATED_DIR / "relationships.md", lines)


def write_relationship_visual_markdown(
    edges: list[dict[str, Any]],
    records_by_id: dict[str, dict[str, Any]],
) -> None:
    graph_path = WEBSITE_GENERATED_DIR / "relationship-graph.md"
    node_ids = sorted(
        {
            str(edge.get("subject"))
            for edge in edges
        }
        | {
            str(edge.get("object"))
            for edge in edges
        }
    )
    graph_payload = {
        "nodes": [
            {
                "id": record_id,
                "title": records_by_id.get(record_id, {}).get("title", record_id),
                "type": records_by_id.get(record_id, {}).get("type", "unknown"),
                "href": runtime_pretty_url(link_for_record(record_id, records_by_id, graph_path))
                if record_id in records_by_id
                else "#",
            }
            for record_id in node_ids
        ],
        "edges": [
            {
                "subject": str(edge.get("subject")),
                "predicate": str(edge.get("predicate")),
                "object": str(edge.get("object")),
            }
            for edge in edges
        ],
    }
    lines = [
        "# Generated Relationship Graph Visualization",
        "",
        "This page is generated from relationship metadata. Do not edit it manually.",
        "",
        "The visual graph is an interactive rendering of the same source-backed edges listed in [Relationship Graph](relationships.md).",
        "",
        '<div class="oir-relationship-graph">',
        '  <div class="oir-relationship-graph__toolbar">',
        '    <div class="oir-relationship-graph__toolbar-group">',
        '      <button class="oir-relationship-graph__button" type="button" data-graph-zoom-in>Zoom In</button>',
        '      <button class="oir-relationship-graph__button" type="button" data-graph-zoom-out>Zoom Out</button>',
        '      <button class="oir-relationship-graph__button" type="button" data-graph-fit>Fit</button>',
        '      <button class="oir-relationship-graph__button" type="button" data-graph-reset>Reset</button>',
        "    </div>",
        '    <div class="oir-relationship-graph__hint">Drag to pan. Use the mouse wheel or buttons to zoom. Click a node to open its record.</div>',
        "  </div>",
        '  <div class="oir-relationship-graph__viewport"></div>',
        '  <script type="application/json">',
        json.dumps(graph_payload, sort_keys=True),
        "  </script>",
        "</div>",
        "",
        '<script src="../../assets/js/relationship-graph.js"></script>',
        "",
        f"Edge count: {len(edges)}",
    ]

    write_markdown(WEBSITE_GENERATED_DIR / "relationship-graph.md", lines)


def write_markdown(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def clean_source_docs() -> None:
    if SOURCE_DOCS_DIR.exists():
        shutil.rmtree(SOURCE_DOCS_DIR)
    SOURCE_DOCS_DIR.mkdir(parents=True, exist_ok=True)


def bibliography_link_for(source_id: str, from_path: Path) -> str:
    bibliography_path = WEBSITE_GENERATED_DIR / "bibliography.md"
    relative_path = os.path.relpath(bibliography_path, from_path.parent).replace("\\", "/")
    return f"{relative_path}#{source_id}"


def external_url_for_source(source_record: dict[str, Any]) -> str | None:
    body_metadata = source_record.get("bibliographic_metadata", {})
    if not isinstance(body_metadata, dict):
        return None
    url_or_citation = body_metadata.get("url or citation")
    if isinstance(url_or_citation, str) and url_or_citation.startswith(("http://", "https://")):
        return url_or_citation
    return None


def source_link_for(
    source_id: str,
    source_records_by_id: dict[str, dict[str, Any]],
    from_path: Path,
) -> str:
    source_record = source_records_by_id[source_id]
    external_url = external_url_for_source(source_record)
    if external_url:
        return external_url
    return bibliography_link_for(source_id, from_path)


def link_source_ids(
    line: str,
    source_records_by_id: dict[str, dict[str, Any]],
    from_path: Path,
) -> str:
    def replace(match: re.Match[str]) -> str:
        source_id = match.group(1)
        if source_id not in source_records_by_id:
            return match.group(0)
        return markdown_link(source_id, source_link_for(source_id, source_records_by_id, from_path))

    return SOURCE_CODE_ID_PATTERN.sub(replace, line)


def link_used_for_terms(
    lines: list[str],
    from_path: Path,
    records_by_title: dict[str, dict[str, Any]],
) -> list[str]:
    linked_lines: list[str] = []
    in_used_for = False

    for line in lines:
        if line.startswith("## "):
            in_used_for = line.strip().lower() == "## used for"
            linked_lines.append(line)
            continue
        if in_used_for:
            match = USED_FOR_ITEM_PATTERN.match(line)
            if match:
                term = match.group(1).strip()
                linked_lines.append(f"- {used_for_link_for(term, from_path, records_by_title)}")
                continue
        linked_lines.append(line)

    return linked_lines


def link_source_doc_body(
    lines: list[str],
    from_path: Path,
    source_records_by_id: dict[str, dict[str, Any]],
    records_by_title: dict[str, dict[str, Any]],
) -> list[str]:
    source_linked_lines = [
        link_backtick_urls(link_source_ids(line, source_records_by_id, from_path))
        for line in lines
    ]
    return link_used_for_terms(source_linked_lines, from_path, records_by_title)


def link_backtick_urls(line: str) -> str:
    """Convert backtick-wrapped URLs into clickable Markdown autolinks."""
    return URL_IN_BACKTICKS_PATTERN.sub(r"<\1>", line)


def _research_debt_count(body: str) -> int:
    """Count the number of research debt items in a page body."""
    count = 0
    in_debt = False
    for line in body.splitlines():
        if line.startswith("## "):
            in_debt = line.strip().lower() == "## research debt"
            continue
        if in_debt and line.strip().startswith("- "):
            count += 1
    return count


def _page_status_banner(record: dict[str, Any], body: str) -> list[str]:
    """Generate a status banner for the top of a source-doc mirror page."""
    status = record.get("status", "unknown")
    sources_count = len(record.get("sources", []))
    relationships_count = len(record.get("relationships", []))
    debt_count = _research_debt_count(body)
    last_verified = record.get("last_verified") or "Never"

    # Determine completeness level
    if status == "verified" and debt_count == 0:
        completeness = "Complete"
        icon = "✅"
    elif status == "verified" and debt_count > 0:
        completeness = "Verified with open research items"
        icon = "☑️"
    elif status == "in_review":
        completeness = "Under review"
        icon = "🔍"
    elif status == "needs_sources":
        completeness = "Needs additional sources"
        icon = "📎"
    elif status == "draft" and sources_count > 0:
        completeness = "Draft — sourced but not yet reviewed"
        icon = "📝"
    elif status == "draft":
        completeness = "Early draft — needs sources and review"
        icon = "🚧"
    elif status == "deprecated":
        completeness = "Deprecated — retained for history"
        icon = "🗄️"
    else:
        completeness = "Unknown status"
        icon = "❓"

    banner = [
        f"!!! info \"{icon} Page Status: {completeness}\"",
        "",
        f"    - **Status**: `{status}`",
        f"    - **Sources**: {sources_count}",
        f"    - **Relationships**: {relationships_count}",
        f"    - **Research debt items**: {debt_count}",
        f"    - **Last verified**: {last_verified}",
        "",
    ]
    return banner


def write_source_doc_mirror(
    record: dict[str, Any],
    source_records_by_id: dict[str, dict[str, Any]],
    records_by_title: dict[str, dict[str, Any]],
) -> None:
    source_path = ROOT / record["path"]
    target_path = WEBSITE_GENERATED_DIR / record["source_doc_path"]
    original = source_path.read_text(encoding="utf-8")

    # Extract body for analysis
    if original.startswith("---\n"):
        _, _, raw_body = original.split("---\n", 2)
    else:
        raw_body = original

    status_banner = _page_status_banner(record, raw_body)

    edit_url = f"{GITHUB_REPO_URL}/edit/main/{record['path']}"
    issue_url = f"{GITHUB_REPO_URL}/issues/new?template=suggest-edit.yml&title=Edit+suggestion:+{record['id']}"

    notice = [
        "# Generated Source Mirror",
        "",
        "This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.",
        "",
        f"- Source path: `{record['path']}`",
        f"- Source ID: `{record['id']}`",
        f"- [**Edit this page**]({edit_url}) | [**Suggest a change**]({issue_url})",
        "",
        *status_banner,
        "---",
        "",
    ]

    if original.startswith("---\n"):
        _, raw_metadata, body = original.split("---\n", 2)
        body_lines = link_source_doc_body(
            body.lstrip().splitlines(),
            target_path,
            source_records_by_id,
            records_by_title,
        )
        lines = ["---", *raw_metadata.rstrip().splitlines(), "---", "", *notice, *body_lines]
    else:
        lines = [
            *notice,
            *link_source_doc_body(
                original.splitlines(),
                target_path,
                source_records_by_id,
                records_by_title,
            ),
        ]

    write_markdown(target_path, lines)


def write_source_doc_mirrors(
    records: list[dict[str, Any]],
    source_records_by_id: dict[str, dict[str, Any]],
    records_by_title: dict[str, dict[str, Any]],
) -> None:
    clean_source_docs()
    for record in records:
        write_source_doc_mirror(record, source_records_by_id, records_by_title)


def main() -> int:
    bibliography_records = records_from(CONTENT_DIRS["bibliography"])
    knowledge_records = records_from(CONTENT_DIRS["knowledge"])
    all_records = bibliography_records + knowledge_records
    records_by_id = {record["id"]: record for record in all_records}
    records_by_title = {record["title"].lower(): record for record in all_records}
    relationship_records = relationship_edges(all_records)
    used_for_records = used_for_index(bibliography_records)

    bibliography_payload = {
        "schema_version": 1,
        "description": "Generated bibliography source index.",
        "records": bibliography_records,
    }
    glossary_payload = {
        "schema_version": 1,
        "description": "Generated glossary-style index of non-source knowledge records.",
        "records": [
            record
            for record in knowledge_records
            if record.get("type") != "source"
        ],
    }
    relationships_payload = {
        "schema_version": 1,
        "description": "Generated relationship graph edge index.",
        "edges": relationship_records,
    }
    used_for_payload = {
        "schema_version": 1,
        "description": "Generated index of Used For terms from source records.",
        "terms": [
            {
                "term": term,
                "sources": [record["id"] for record in records],
            }
            for term, records in used_for_records.items()
        ],
    }
    review_payload = review_status_payload(all_records)
    citations_payload = citation_index_payload(bibliography_records, glossary_payload["records"])
    timeline_index_payload = timeline_payload(all_records)
    retrieval_index_payload = retrieval_payload(all_records)
    retrieval_dataset = retrieval_records(all_records)
    outreach_index_payload = outreach_payload(all_records)
    handbook_index_payload = handbook_payload(all_records)

    write_json(GENERATED_DIR / "bibliography.json", bibliography_payload)
    write_json(GENERATED_DIR / "citations.json", citations_payload)
    write_json(GENERATED_DIR / "glossary.json", glossary_payload)
    write_json(GENERATED_DIR / "handbook.json", handbook_index_payload)
    write_json(GENERATED_DIR / "relationships.json", relationships_payload)
    write_json(GENERATED_DIR / "retrieval.json", retrieval_index_payload)
    write_jsonl(GENERATED_DIR / "retrieval.jsonl", retrieval_dataset)
    write_json(GENERATED_DIR / "outreach.json", outreach_index_payload)
    write_json(GENERATED_DIR / "timeline.json", timeline_index_payload)
    write_json(GENERATED_DIR / "used-for.json", used_for_payload)
    write_json(GENERATED_DIR / "review-status.json", review_payload)
    write_source_doc_mirrors(
        bibliography_records + glossary_payload["records"],
        {record["id"]: record for record in bibliography_records},
        records_by_title,
    )
    write_bibliography_markdown(bibliography_records, glossary_payload["records"])
    write_citation_index_markdown(
        bibliography_records,
        glossary_payload["records"],
        records_by_id,
    )
    write_glossary_markdown(glossary_payload["records"])
    write_handbook_markdown(all_records, records_by_id)
    write_print_handbook_markdown(all_records, records_by_id)
    write_relationships_markdown(relationship_records, records_by_id)
    write_relationship_visual_markdown(relationship_records, records_by_id)
    write_outreach_markdown(all_records, records_by_id)
    write_timeline_markdown(all_records, records_by_id)
    write_used_for_markdown(bibliography_records)
    write_review_status_markdown(all_records)

    print(f"Generated bibliography index with {len(bibliography_records)} records.")
    print(f"Generated citation index with {len(citations_payload['sources'])} sources.")
    print(f"Generated glossary index with {len(glossary_payload['records'])} records.")
    print(f"Generated handbook prototype with {handbook_index_payload['record_count']} records.")
    print(f"Generated print handbook with {handbook_index_payload['record_count']} records.")
    print(f"Generated relationship graph with {len(relationship_records)} edges.")
    print(f"Generated retrieval dataset with {len(retrieval_dataset)} records.")
    print(f"Generated outreach CRM prototype with {outreach_index_payload['record_count']} records.")
    print(f"Generated timeline with {len(timeline_index_payload['events'])} events.")
    print(f"Generated Used For index with {len(used_for_records)} terms.")
    print(f"Generated review status dashboard with {len(all_records)} records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
