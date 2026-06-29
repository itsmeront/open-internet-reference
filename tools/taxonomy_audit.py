"""Taxonomy and topic audit — analyze tag usage across OIR content.

Reports:
- Tag usage frequency across all content
- Orphan tags (defined in TAXONOMY.md but never used)
- Undeclared tags (used in content but not in TAXONOMY.md)
- Duplicate/similar tag candidates (Levenshtein distance)
- Topic page coverage (topics with no linked content)
- Content without tags

Usage:
    python tools/taxonomy_audit.py                  # Generate audit report
    python tools/taxonomy_audit.py --json           # Output JSON
    python tools/taxonomy_audit.py --fix-orphans    # Suggest fixes for orphan tags

Output:
    website/generated/taxonomy-audit.md — generated audit report
    generated/taxonomy-audit.json — machine-readable audit data
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TAXONOMY_FILE = ROOT / "TAXONOMY.md"
WEBSITE_GENERATED_DIR = ROOT / "website" / "generated"
AUDIT_PAGE = WEBSITE_GENERATED_DIR / "taxonomy-audit.md"
AUDIT_JSON = ROOT / "generated" / "taxonomy-audit.json"

# Content directories to scan
CONTENT_DIRS = [
    ROOT / "knowledge",
    ROOT / "bibliography",
    ROOT / "contacts",
    ROOT / "intake",
]


def parse_taxonomy() -> set[str]:
    """Extract all declared tags from TAXONOMY.md."""
    tags: set[str] = set()

    if not TAXONOMY_FILE.exists():
        return tags

    content = TAXONOMY_FILE.read_text(encoding="utf-8")

    # Match lines like "- `tag-name`" or "- tag-name"
    for match in re.finditer(r"^- `?([a-z0-9-]+)`?", content, re.MULTILINE):
        tags.add(match.group(1))

    return tags


def scan_content_tags() -> tuple[Counter[str], dict[str, list[str]]]:
    """Scan all content files for tags used in front matter.

    Returns:
        - Counter of tag usage
        - Dict mapping tags to list of files using them
    """
    tag_counter: Counter[str] = Counter()
    tag_files: dict[str, list[str]] = defaultdict(list)
    
    try:
        import yaml
    except ImportError:
        print("Warning: PyYAML not available. Install with: pip install pyyaml")
        return tag_counter, tag_files

    for content_dir in CONTENT_DIRS:
        if not content_dir.exists():
            continue

        for md_file in content_dir.rglob("*.md"):
            try:
                text = md_file.read_text(encoding="utf-8")
                if not text.startswith("---"):
                    continue

                end_idx = text.index("---", 3)
                front = yaml.safe_load(text[3:end_idx])

                if not front or not isinstance(front, dict):
                    continue

                tags = front.get("tags", [])
                if isinstance(tags, list):
                    rel_path = str(md_file.relative_to(ROOT))
                    for tag in tags:
                        tag_str = str(tag).lower().strip()
                        if tag_str:
                            tag_counter[tag_str] += 1
                            tag_files[tag_str].append(rel_path)

            except (ValueError, Exception):
                continue

    return tag_counter, tag_files


def scan_untagged_content() -> list[dict[str, str]]:
    """Find content files with no tags or empty tag lists."""
    untagged: list[dict[str, str]] = []

    try:
        import yaml
    except ImportError:
        return untagged

    for content_dir in CONTENT_DIRS:
        if not content_dir.exists():
            continue

        for md_file in content_dir.rglob("*.md"):
            try:
                text = md_file.read_text(encoding="utf-8")
                if not text.startswith("---"):
                    continue

                end_idx = text.index("---", 3)
                front = yaml.safe_load(text[3:end_idx])

                if not front or not isinstance(front, dict):
                    continue

                tags = front.get("tags", [])
                if not tags or (isinstance(tags, list) and len(tags) == 0):
                    rel_path = str(md_file.relative_to(ROOT))
                    untagged.append({
                        "path": rel_path,
                        "id": front.get("id", ""),
                        "title": front.get("title", md_file.stem),
                    })
            except (ValueError, Exception):
                continue

    return untagged


def find_similar_tags(tags: set[str], threshold: int = 2) -> list[tuple[str, str, int]]:
    """Find tags that might be duplicates using edit distance."""
    similar: list[tuple[str, str, int]] = []
    tag_list = sorted(tags)

    for i, tag1 in enumerate(tag_list):
        for tag2 in tag_list[i + 1:]:
            dist = levenshtein_distance(tag1, tag2)
            if 0 < dist <= threshold:
                similar.append((tag1, tag2, dist))

    return sorted(similar, key=lambda x: x[2])


def levenshtein_distance(s1: str, s2: str) -> int:
    """Compute the Levenshtein distance between two strings."""
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    prev_row = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        curr_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = prev_row[j + 1] + 1
            deletions = curr_row[j] + 1
            substitutions = prev_row[j] + (c1 != c2)
            curr_row.append(min(insertions, deletions, substitutions))
        prev_row = curr_row

    return prev_row[-1]


def generate_audit_page(
    declared_tags: set[str],
    tag_usage: Counter[str],
    tag_files: dict[str, list[str]],
    orphan_tags: set[str],
    undeclared_tags: set[str],
    similar_pairs: list[tuple[str, str, int]],
    untagged: list[dict[str, str]],
) -> str:
    """Generate the Markdown audit report."""
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# Taxonomy Audit Report",
        "",
        f"Last updated: {now}",
        "",
        "This report analyzes tag usage, identifies gaps, and surfaces potential duplicates.",
        "",
    ]

    # Summary
    all_tags = declared_tags | set(tag_usage.keys())
    lines.extend([
        "## Summary",
        "",
        f"| Metric | Count |",
        f"|--------|-------|",
        f"| Tags declared in TAXONOMY.md | {len(declared_tags)} |",
        f"| Tags used in content | {len(tag_usage)} |",
        f"| Total tag applications | {sum(tag_usage.values())} |",
        f"| Orphan tags (declared but unused) | {len(orphan_tags)} |",
        f"| Undeclared tags (used but not in TAXONOMY.md) | {len(undeclared_tags)} |",
        f"| Similar tag pairs (possible duplicates) | {len(similar_pairs)} |",
        f"| Content without tags | {len(untagged)} |",
        "",
    ])

    # Tag usage frequency
    lines.extend([
        "## Tag Usage Frequency",
        "",
        "| Tag | Uses | Status |",
        "|-----|------|--------|",
    ])

    for tag, count in tag_usage.most_common():
        status = "✓" if tag in declared_tags else "⚠️ undeclared"
        lines.append(f"| `{tag}` | {count} | {status} |")
    lines.append("")

    # Orphan tags
    if orphan_tags:
        lines.extend([
            "## Orphan Tags",
            "",
            "These tags are declared in `TAXONOMY.md` but never used in any content:",
            "",
        ])
        for tag in sorted(orphan_tags):
            lines.append(f"- `{tag}`")
        lines.extend([
            "",
            "**Action:** Either add content using these tags or remove them from TAXONOMY.md.",
            "",
        ])

    # Undeclared tags
    if undeclared_tags:
        lines.extend([
            "## Undeclared Tags",
            "",
            "These tags are used in content but not listed in `TAXONOMY.md`:",
            "",
            "| Tag | Used in |",
            "|-----|---------|",
        ])
        for tag in sorted(undeclared_tags):
            files = tag_files.get(tag, [])
            file_list = ", ".join(f"`{f}`" for f in files[:3])
            if len(files) > 3:
                file_list += f" +{len(files) - 3} more"
            lines.append(f"| `{tag}` | {file_list} |")
        lines.extend([
            "",
            "**Action:** Add these to TAXONOMY.md or replace with existing tags.",
            "",
        ])

    # Similar/duplicate candidates
    if similar_pairs:
        lines.extend([
            "## Possible Duplicate Tags",
            "",
            "Tags with similar names that may represent the same concept:",
            "",
            "| Tag A | Tag B | Edit Distance |",
            "|-------|-------|---------------|",
        ])
        for tag1, tag2, dist in similar_pairs[:20]:
            lines.append(f"| `{tag1}` | `{tag2}` | {dist} |")
        lines.extend([
            "",
            "**Action:** Review and merge duplicates if they represent the same concept.",
            "",
        ])

    # Untagged content
    if untagged:
        lines.extend([
            "## Content Without Tags",
            "",
            f"Found {len(untagged)} content files with no tags:",
            "",
            "| ID | Title | Path |",
            "|---|-------|------|",
        ])
        for item in untagged[:20]:
            lines.append(f"| `{item['id']}` | {item['title'][:40]} | `{item['path']}` |")
        lines.append("")
        if len(untagged) > 20:
            lines.append(f"*...and {len(untagged) - 20} more*\n")

    return "\n".join(lines)


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Run taxonomy audit on OIR content")
    parser.add_argument("--json", action="store_true", help="Output JSON only")
    parser.add_argument("--fix-orphans", action="store_true", help="Suggest fixes for orphan tags")
    args = parser.parse_args()

    print("Running taxonomy audit...")

    # Parse taxonomy
    declared_tags = parse_taxonomy()
    print(f"  Declared tags: {len(declared_tags)}")

    # Scan content
    tag_usage, tag_files = scan_content_tags()
    print(f"  Tags in use: {len(tag_usage)}")

    used_tags = set(tag_usage.keys())

    # Compute analysis
    orphan_tags = declared_tags - used_tags
    undeclared_tags = used_tags - declared_tags
    all_tags = declared_tags | used_tags
    similar_pairs = find_similar_tags(all_tags)
    untagged = scan_untagged_content()

    print(f"  Orphan tags: {len(orphan_tags)}")
    print(f"  Undeclared tags: {len(undeclared_tags)}")
    print(f"  Similar pairs: {len(similar_pairs)}")
    print(f"  Untagged content: {len(untagged)}")

    # Build audit data
    audit_data = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "summary": {
            "declared_tags": len(declared_tags),
            "used_tags": len(tag_usage),
            "total_applications": sum(tag_usage.values()),
            "orphan_tags": len(orphan_tags),
            "undeclared_tags": len(undeclared_tags),
            "similar_pairs": len(similar_pairs),
            "untagged_content": len(untagged),
        },
        "tag_usage": dict(tag_usage.most_common()),
        "orphan_tags": sorted(orphan_tags),
        "undeclared_tags": sorted(undeclared_tags),
        "similar_pairs": [
            {"tag_a": a, "tag_b": b, "distance": d}
            for a, b, d in similar_pairs
        ],
        "untagged_content": untagged,
    }

    # Write JSON
    AUDIT_JSON.parent.mkdir(parents=True, exist_ok=True)
    AUDIT_JSON.write_text(json.dumps(audit_data, indent=2), encoding="utf-8")

    if args.json:
        print(json.dumps(audit_data, indent=2))
        return 0

    # Generate report page
    content = generate_audit_page(
        declared_tags, tag_usage, tag_files,
        orphan_tags, undeclared_tags, similar_pairs, untagged,
    )
    AUDIT_PAGE.parent.mkdir(parents=True, exist_ok=True)
    AUDIT_PAGE.write_text(content, encoding="utf-8")

    print(f"\nGenerated audit report: {AUDIT_PAGE}")
    print(f"Generated audit JSON: {AUDIT_JSON}")

    if args.fix_orphans and orphan_tags:
        print("\nOrphan tag suggestions:")
        for tag in sorted(orphan_tags):
            print(f"  - Remove `{tag}` from TAXONOMY.md or create content using it")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
