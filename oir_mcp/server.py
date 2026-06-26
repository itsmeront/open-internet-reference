"""OIR MCP Server.

Provides tools for AI agents to query the Open Internet Reference knowledge base,
check research debt, and verify sources.

Usage:
    # stdio mode (for Claude Desktop, Kiro, etc.)
    python -m oir_mcp

    # HTTP mode (for remote access)
    python -m oir_mcp --transport streamable-http --port 8080

    # Development mode
    mcp dev oir_mcp/server.py
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML is required: pip install pyyaml")

from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP(
    "oir-knowledge-base",
    version="0.1.0",
    description="Open Internet Reference knowledge base - query organizations, lawyers, cases, and research debt for digital rights and software freedom.",
)

# Repository root (auto-detect)
ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = ROOT / "knowledge"
BIBLIOGRAPHY_DIR = ROOT / "bibliography"
CONTACTS_DIR = ROOT / "contacts"


# ─── Helpers ───────────────────────────────────────────────────────────────────


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


def load_body(path: Path) -> str:
    """Extract the body (after front matter) from a Markdown file."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return text
    try:
        _, _, body = text.split("---\n", 2)
    except ValueError:
        return text
    return body.strip()


def iter_content_files() -> list[Path]:
    """Find all content Markdown files."""
    files: list[Path] = []
    for content_dir in [KNOWLEDGE_DIR, BIBLIOGRAPHY_DIR, CONTACTS_DIR]:
        if not content_dir.exists():
            continue
        files.extend(
            path
            for path in content_dir.rglob("*.md")
            if "_templates" not in path.parts and path.name != "README.md"
        )
    return sorted(files)


def load_all_records() -> list[dict[str, Any]]:
    """Load all records with their metadata and paths."""
    records = []
    for path in iter_content_files():
        metadata = load_front_matter(path)
        if metadata is None:
            continue
        metadata["_path"] = str(path.relative_to(ROOT))
        metadata["_body"] = load_body(path)
        records.append(metadata)
    return records


def extract_research_debt(body: str) -> list[str]:
    """Extract research debt items from a page body."""
    items = []
    in_debt = False
    for line in body.splitlines():
        if line.startswith("## "):
            in_debt = line.strip().lower() == "## research debt"
            continue
        if in_debt and line.strip().startswith("- "):
            items.append(line.strip()[2:].strip())
    return items


def matches_query(record: dict[str, Any], query: str) -> bool:
    """Check if a record matches a search query (case-insensitive)."""
    query_lower = query.lower()
    searchable = " ".join([
        str(record.get("id", "")),
        str(record.get("title", "")),
        str(record.get("summary", "")),
        " ".join(record.get("tags", [])),
        record.get("_body", ""),
    ]).lower()
    return query_lower in searchable


# ─── Tools ─────────────────────────────────────────────────────────────────────


@mcp.tool()
def query_knowledge(
    query: str,
    type: str | None = None,
    limit: int = 10,
) -> str:
    """Search the OIR knowledge base for organizations, lawyers, cases, topics, or any content.

    Args:
        query: Natural language search query or entity ID (e.g., "EFF", "Bernstein", "CASE-BERNSTEIN-V-DOJ")
        type: Optional filter by type: case, organization, attorney, person, topic, source, statute
        limit: Maximum results to return (default 10)

    Returns:
        Matching records with metadata and summaries.
    """
    records = load_all_records()

    # Filter by type if specified
    if type:
        records = [r for r in records if r.get("type") == type]

    # Search
    matches = [r for r in records if matches_query(r, query)]

    if not matches:
        return f"No results found for '{query}'" + (f" (type={type})" if type else "")

    # Format results
    results = []
    for record in matches[:limit]:
        result = f"## {record.get('id', 'Unknown')} — {record.get('title', 'Untitled')}\n"
        result += f"- **Type**: {record.get('type', 'unknown')}\n"
        result += f"- **Status**: {record.get('status', 'unknown')}\n"
        result += f"- **Summary**: {record.get('summary', 'No summary')}\n"
        result += f"- **Tags**: {', '.join(record.get('tags', []))}\n"
        result += f"- **Sources**: {', '.join(record.get('sources', []))}\n"
        result += f"- **Path**: {record.get('_path', 'unknown')}\n"
        result += f"- **Last verified**: {record.get('last_verified', 'Never')}\n"

        # Include body excerpt
        body = record.get("_body", "")
        if body:
            # Take first 500 chars of body
            excerpt = body[:500]
            if len(body) > 500:
                excerpt += "..."
            result += f"\n{excerpt}\n"

        results.append(result)

    header = f"Found {len(matches)} result(s) for '{query}'"
    if type:
        header += f" (type={type})"
    if len(matches) > limit:
        header += f" (showing first {limit})"

    return header + "\n\n" + "\n---\n".join(results)


@mcp.tool()
def get_research_debt(
    type: str | None = None,
    limit: int = 20,
    priority: str = "high",
) -> str:
    """Get prioritized research debt items that need resolution.

    Research debt items are unresolved verification needs, missing sources,
    or incomplete analysis documented in the knowledge base.

    Args:
        type: Optional filter by page type: case, organization, attorney, person, topic
        limit: Maximum items to return (default 20)
        priority: Priority level - "high" (cases/attorneys first), "medium", or "all"

    Returns:
        Prioritized list of research debt items with page context.
    """
    TYPE_PRIORITY = {
        "case": 1, "attorney": 2, "organization": 3,
        "person": 4, "statute": 5, "topic": 6,
        "technology": 7, "protocol": 8, "source": 9,
    }

    records = load_all_records()

    # Collect debt items
    debt_items = []
    for record in records:
        if type and record.get("type") != type:
            continue

        items = extract_research_debt(record.get("_body", ""))
        for item_text in items:
            debt_items.append({
                "text": item_text,
                "page_id": record.get("id", "unknown"),
                "page_title": record.get("title", "Untitled"),
                "page_type": record.get("type", "unknown"),
                "page_status": record.get("status", "unknown"),
                "sources_count": len(record.get("sources", [])),
                "path": record.get("_path", "unknown"),
            })

    if not debt_items:
        return "No research debt items found" + (f" (type={type})" if type else "")

    # Sort by priority
    debt_items.sort(key=lambda x: (TYPE_PRIORITY.get(x["page_type"], 99), x["page_id"]))

    # Apply priority filter
    if priority == "high":
        debt_items = [d for d in debt_items if TYPE_PRIORITY.get(d["page_type"], 99) <= 4]
    elif priority == "medium":
        debt_items = [d for d in debt_items if TYPE_PRIORITY.get(d["page_type"], 99) <= 6]

    if not debt_items:
        return f"No research debt items at priority='{priority}'" + (f" (type={type})" if type else "")

    # Format output
    results = []
    current_page = None
    count = 0

    for item in debt_items:
        if count >= limit:
            break

        if item["page_id"] != current_page:
            current_page = item["page_id"]
            results.append(f"\n### [{item['page_type']}] {item['page_id']}: {item['page_title']}")
            results.append(f"Status: {item['page_status']} | Sources: {item['sources_count']} | Path: {item['path']}")

        results.append(f"  - {item['text']}")
        count += 1

    header = f"Research debt: {count} item(s)"
    if type:
        header += f" (type={type})"
    header += f" (priority={priority})"
    header += f"\nTotal debt items in knowledge base: {len(debt_items)}"

    return header + "\n" + "\n".join(results)


@mcp.tool()
def verify_source(
    source_id: str,
) -> str:
    """Check the status of a source record — whether its URL is accessible and its metadata is current.

    Args:
        source_id: The SRC-* identifier of the source to check (e.g., "SRC-EFF-ABOUT")

    Returns:
        Source record details including URL, accessibility status, and metadata.
    """
    import urllib.request
    import urllib.error

    records = load_all_records()
    record = next((r for r in records if r.get("id") == source_id), None)

    if not record:
        return f"Source '{source_id}' not found in the knowledge base."

    body = record.get("_body", "")

    # Extract URL from bibliographic metadata
    url = None
    archive_url = None
    for line in body.splitlines():
        if line.strip().lower().startswith("- url:"):
            url = line.split(":", 1)[1].strip() if ":" in line else None
            # Handle "- URL: https://..." format
            url_match = re.search(r"https?://\S+", line)
            if url_match:
                url = url_match.group(0).rstrip(".,:;")
        elif line.strip().lower().startswith("- archive url:"):
            archive_match = re.search(r"https?://\S+", line)
            if archive_match:
                archive_url = archive_match.group(0).rstrip(".,:;")

    result = f"## Source: {source_id}\n"
    result += f"- **Title**: {record.get('title', 'Untitled')}\n"
    result += f"- **Type**: {record.get('type', 'unknown')}\n"
    result += f"- **Status**: {record.get('status', 'unknown')}\n"
    result += f"- **Summary**: {record.get('summary', 'No summary')}\n"
    result += f"- **Last verified**: {record.get('last_verified', 'Never')}\n"
    result += f"- **Path**: {record.get('_path', 'unknown')}\n"
    result += f"- **URL**: {url or 'Not found in record'}\n"
    result += f"- **Archive URL**: {archive_url or 'None recorded'}\n"

    # Check URL accessibility
    if url and url.startswith("http"):
        try:
            req = urllib.request.Request(url, method="HEAD")
            req.add_header("User-Agent", "OIR-MCP-Server/0.1 (link verification)")
            response = urllib.request.urlopen(req, timeout=10)
            result += f"\n### URL Check: ✅ Accessible (HTTP {response.getcode()})\n"
        except urllib.error.HTTPError as e:
            result += f"\n### URL Check: ❌ HTTP {e.code} ({e.reason})\n"
            if archive_url:
                result += f"  Archive available at: {archive_url}\n"
        except Exception as e:
            result += f"\n### URL Check: ⚠️ Error ({e})\n"
    else:
        result += "\n### URL Check: ⊘ No URL to check\n"

    # Show what pages use this source
    used_by = []
    for r in records:
        if source_id in r.get("sources", []):
            used_by.append(f"{r.get('id', 'unknown')}: {r.get('title', 'Untitled')}")

    if used_by:
        result += f"\n### Used by ({len(used_by)} pages):\n"
        for page in used_by:
            result += f"  - {page}\n"

    return result


@mcp.tool()
def list_pages(
    type: str | None = None,
    status: str | None = None,
    tag: str | None = None,
    limit: int = 50,
) -> str:
    """List pages in the knowledge base with optional filters.

    Args:
        type: Filter by type: case, organization, attorney, person, topic, source, statute, protocol
        status: Filter by status: draft, needs_sources, in_review, verified, deprecated
        tag: Filter by tag (e.g., "first-amendment", "open-source-software", "privacy")
        limit: Maximum results (default 50)

    Returns:
        List of matching pages with ID, title, type, and status.
    """
    records = load_all_records()

    if type:
        records = [r for r in records if r.get("type") == type]
    if status:
        records = [r for r in records if r.get("status") == status]
    if tag:
        records = [r for r in records if tag in r.get("tags", [])]

    if not records:
        filters = []
        if type: filters.append(f"type={type}")
        if status: filters.append(f"status={status}")
        if tag: filters.append(f"tag={tag}")
        return "No pages found" + (f" ({', '.join(filters)})" if filters else "")

    # Sort by type then ID
    records.sort(key=lambda r: (r.get("type", ""), r.get("id", "")))

    results = [f"Found {len(records)} page(s):\n"]
    for record in records[:limit]:
        results.append(
            f"- **{record.get('id')}** — {record.get('title')} "
            f"[{record.get('type')}, {record.get('status')}]"
        )

    if len(records) > limit:
        results.append(f"\n... and {len(records) - limit} more")

    return "\n".join(results)


@mcp.tool()
def get_page(page_id: str) -> str:
    """Get the full content of a specific page by its ID.

    Args:
        page_id: The page identifier (e.g., "CASE-BERNSTEIN-V-DOJ", "ORG-EFF", "PERSON-CINDY-COHN")

    Returns:
        Full page content including metadata and body.
    """
    records = load_all_records()
    record = next((r for r in records if r.get("id") == page_id), None)

    if not record:
        # Try partial match
        partial = [r for r in records if page_id.upper() in r.get("id", "").upper()]
        if partial:
            suggestions = ", ".join(r.get("id", "") for r in partial[:5])
            return f"Page '{page_id}' not found. Did you mean: {suggestions}?"
        return f"Page '{page_id}' not found in the knowledge base."

    result = f"# {record.get('title', 'Untitled')}\n\n"
    result += f"- **ID**: {record.get('id')}\n"
    result += f"- **Type**: {record.get('type')}\n"
    result += f"- **Status**: {record.get('status')}\n"
    result += f"- **Tags**: {', '.join(record.get('tags', []))}\n"
    result += f"- **Sources**: {', '.join(record.get('sources', []))}\n"
    result += f"- **Last verified**: {record.get('last_verified', 'Never')}\n"
    result += f"- **Path**: {record.get('_path')}\n"

    relationships = record.get("relationships", [])
    if relationships:
        result += f"\n## Relationships ({len(relationships)})\n"
        for rel in relationships:
            if isinstance(rel, dict):
                result += f"- {rel.get('subject')} → {rel.get('predicate')} → {rel.get('object')}\n"

    result += f"\n## Content\n\n{record.get('_body', 'No content')}"

    return result


# ─── Entry Point ───────────────────────────────────────────────────────────────

def main():
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
