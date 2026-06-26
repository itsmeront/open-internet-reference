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
)

# Repository root (auto-detect)
ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = ROOT / "knowledge"
BIBLIOGRAPHY_DIR = ROOT / "bibliography"
CONTACTS_DIR = ROOT / "contacts"
MCP_LOG_FILE = Path("/opt/oir/mcp-requests.log")


def _log_request(tool_name: str) -> None:
    """Log an MCP tool request (anonymous — no user info)."""
    import json
    try:
        entry = {
            "date": __import__("datetime").datetime.utcnow().strftime("%Y-%m-%d"),
            "time": __import__("datetime").datetime.utcnow().strftime("%H:%M:%S"),
            "tool": tool_name,
        }
        with open(MCP_LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception:
        pass  # Don't let logging failures break the server


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
    _log_request("query_knowledge")
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
    _log_request("get_research_debt")
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
    _log_request("verify_source")
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
    _log_request("list_pages")
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
    _log_request("get_page")
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


# ─── Advisor Tools ─────────────────────────────────────────────────────────────


# Topic keywords mapped to relevant tags for intelligent matching
TOPIC_KEYWORDS = {
    "censorship": ["first-amendment", "speech-and-code", "digital-rights"],
    "dmca": ["copyright", "intermediary-liability", "safe-harbor"],
    "copyright": ["copyright", "intermediary-liability"],
    "encryption": ["cryptography", "privacy", "fourth-amendment"],
    "backdoor": ["cryptography", "privacy", "surveillance"],
    "surveillance": ["surveillance", "privacy", "fourth-amendment"],
    "privacy": ["privacy", "fourth-amendment", "surveillance"],
    "code": ["speech-and-code", "first-amendment", "open-source-software"],
    "open source": ["open-source-software", "copyright"],
    "license": ["open-source-software", "copyright"],
    "gpl": ["open-source-software", "copyright"],
    "cfaa": ["computer-crime"],
    "hacking": ["computer-crime"],
    "scraping": ["computer-crime"],
    "takedown": ["copyright", "intermediary-liability", "safe-harbor"],
    "platform": ["intermediary-liability", "safe-harbor", "internet-governance"],
    "section 230": ["intermediary-liability", "internet-governance"],
    "free speech": ["first-amendment", "speech-and-code", "digital-rights"],
    "export": ["cryptography", "export-control", "speech-and-code"],
    "warrant": ["fourth-amendment", "privacy", "surveillance"],
    "data": ["privacy", "fourth-amendment"],
    "internet": ["internet-governance", "digital-rights"],
    "api": ["copyright", "speech-and-code", "open-source-software"],
    "interoperability": ["copyright", "open-source-software"],
}


def _find_relevant_tags(situation: str) -> list[str]:
    """Find relevant taxonomy tags based on a situation description."""
    situation_lower = situation.lower()
    relevant_tags: set[str] = set()

    for keyword, tags in TOPIC_KEYWORDS.items():
        if keyword in situation_lower:
            relevant_tags.update(tags)

    # If no keywords matched, try broader matching
    if not relevant_tags:
        relevant_tags = {"digital-rights", "first-amendment", "open-source-software"}

    return list(relevant_tags)


def _extract_contact_info(body: str) -> str:
    """Extract contact information section from a page body."""
    lines = []
    in_contact = False
    in_engage = False

    for line in body.splitlines():
        if line.startswith("## "):
            heading = line.strip().lower()
            in_contact = "contact" in heading
            in_engage = "how to engage" in heading or "how to engage for legal help" in heading
            if in_contact or in_engage:
                lines.append(line)
            continue
        if in_contact or in_engage:
            if line.startswith("## "):
                break
            lines.append(line)

    return "\n".join(lines).strip()


@mcp.tool()
def find_help(
    situation: str,
) -> str:
    """Find organizations, lawyers, and legal precedent relevant to a specific situation.

    Describe your problem and this tool will identify who can help, what legal
    precedent supports you, and how to make contact.

    Args:
        situation: Description of your situation (e.g., "My open source project received a DMCA takedown", "Government demanding we add encryption backdoor", "Prosecuted under CFAA for security research")

    Returns:
        Relevant organizations with contact info, lawyers who handle similar cases, applicable legal precedent, and policymakers who've legislated on the issue.
    """
    _log_request("find_help")
    records = load_all_records()
    relevant_tags = _find_relevant_tags(situation)

    # Find matching records by tag relevance
    def relevance_score(record: dict[str, Any]) -> int:
        record_tags = set(record.get("tags", []))
        return len(record_tags.intersection(relevant_tags))

    # Gather organizations that can help
    orgs = [r for r in records if r.get("type") == "organization" and relevance_score(r) > 0]
    orgs.sort(key=relevance_score, reverse=True)

    # Gather attorneys
    attorneys = [r for r in records if r.get("type") == "attorney" and relevance_score(r) > 0]
    attorneys.sort(key=relevance_score, reverse=True)

    # Gather relevant cases
    cases = [r for r in records if r.get("type") == "case" and relevance_score(r) > 0]
    cases.sort(key=relevance_score, reverse=True)

    # Gather policymakers
    policymakers = [r for r in records if r.get("type") == "person" and "person" in r.get("tags", []) and relevance_score(r) > 0]
    policymakers.sort(key=relevance_score, reverse=True)

    # Gather contacts
    contacts = [r for r in records if r.get("id", "").startswith("CONTACT-") and relevance_score(r) > 0]
    contacts.sort(key=relevance_score, reverse=True)

    # Build response
    result = f"# Help for: {situation}\n\n"
    result += f"Matched topics: {', '.join(relevant_tags)}\n\n"

    # Organizations
    if orgs:
        result += "## Organizations That Can Help\n\n"
        for org in orgs[:5]:
            result += f"### {org.get('title')}\n"
            result += f"{org.get('summary', 'No summary')}\n\n"

    # Contacts with intake info
    if contacts:
        result += "## How to Make Contact\n\n"
        for contact in contacts[:5]:
            result += f"### {contact.get('title')}\n"
            contact_info = _extract_contact_info(contact.get("_body", ""))
            if contact_info:
                result += f"{contact_info}\n\n"
            else:
                result += f"{contact.get('summary', '')}\n\n"

    # Attorneys
    if attorneys:
        result += "## Lawyers Who Handle These Issues\n\n"
        for att in attorneys[:5]:
            result += f"- **{att.get('title')}** — {att.get('summary', 'No summary')}\n"
        result += "\n"

    # Cases
    if cases:
        result += "## Relevant Legal Precedent\n\n"
        for case in cases[:5]:
            result += f"- **{case.get('title')}** — {case.get('summary', 'No summary')}\n"
        result += "\n"

    # Policymakers
    if policymakers:
        result += "## Policymakers Active on This Issue\n\n"
        for pm in policymakers[:4]:
            result += f"- **{pm.get('title')}** — {pm.get('summary', 'No summary')}\n"
        result += "\n"

    if not orgs and not attorneys and not cases:
        result += "\n⚠️ No strong matches found. Try describing your situation differently, or use `query_knowledge` to search by specific terms.\n"

    return result


@mcp.tool()
def find_precedent(
    legal_issue: str,
    jurisdiction: str = "US federal",
) -> str:
    """Find court cases and statutes relevant to a specific legal issue.

    Args:
        legal_issue: Description of the legal issue (e.g., "source code as protected speech", "API copyright fair use", "warrantless cell phone tracking")
        jurisdiction: Jurisdiction context (default "US federal")

    Returns:
        Relevant cases with holdings, statutes, and their significance for the issue.
    """
    _log_request("find_precedent")
    records = load_all_records()
    relevant_tags = _find_relevant_tags(legal_issue)

    # Find cases and statutes
    def relevance_score(record: dict[str, Any]) -> int:
        score = len(set(record.get("tags", [])).intersection(relevant_tags))
        # Boost if the issue text appears in summary or body
        searchable = (record.get("summary", "") + " " + record.get("_body", "")).lower()
        for word in legal_issue.lower().split():
            if len(word) > 3 and word in searchable:
                score += 1
        return score

    cases = [r for r in records if r.get("type") == "case"]
    statutes = [r for r in records if r.get("type") == "statute"]
    topics = [r for r in records if r.get("type") == "topic" and relevance_score(r) > 0]

    # Score and sort
    scored_cases = [(relevance_score(c), c) for c in cases]
    scored_cases = [(s, c) for s, c in scored_cases if s > 0]
    scored_cases.sort(key=lambda x: x[0], reverse=True)

    scored_statutes = [(relevance_score(s), s) for s in statutes]
    scored_statutes = [(s, st) for s, st in scored_statutes if s > 0]
    scored_statutes.sort(key=lambda x: x[0], reverse=True)

    result = f"# Legal Precedent: {legal_issue}\n\n"
    result += f"Jurisdiction: {jurisdiction}\n"
    result += f"Matched topics: {', '.join(relevant_tags)}\n\n"

    if scored_cases:
        result += "## Relevant Cases\n\n"
        for score, case in scored_cases[:8]:
            result += f"### {case.get('title')} (relevance: {score})\n"
            result += f"**Summary**: {case.get('summary', 'No summary')}\n\n"

            # Extract key sections from body
            body = case.get("_body", "")

            # Get significance section if available
            for section_name in ["## Significance", "## Practical Impact", "## Legal Analysis"]:
                if section_name in body:
                    section_start = body.index(section_name)
                    section_content = body[section_start:]
                    # Find next ## heading
                    next_heading = section_content.find("\n## ", 1)
                    if next_heading > 0:
                        section_content = section_content[:next_heading]
                    result += f"{section_content.strip()}\n\n"
                    break

    if scored_statutes:
        result += "## Relevant Statutes\n\n"
        for score, statute in scored_statutes[:4]:
            result += f"- **{statute.get('title')}** — {statute.get('summary', 'No summary')}\n"
        result += "\n"

    if topics:
        result += "## Related Legal Topics\n\n"
        for topic in topics[:4]:
            result += f"- **{topic.get('title')}** — {topic.get('summary', 'No summary')}\n"
        result += "\n"

    if not scored_cases and not scored_statutes:
        result += "\n⚠️ No cases or statutes found matching this issue. Try broader terms or use `query_knowledge` to explore.\n"

    return result


@mcp.tool()
def get_contacts_for(
    topic: str,
) -> str:
    """Get actionable contact information for organizations and lawyers relevant to a topic.

    Args:
        topic: The topic area (e.g., "CFAA", "encryption", "copyright", "open source licensing", "surveillance", "free speech")

    Returns:
        Contact records with intake paths, organized by type (pro bono organizations, commercial law firms, policymakers).
    """
    _log_request("get_contacts_for")
    records = load_all_records()
    relevant_tags = _find_relevant_tags(topic)

    # Find contacts
    contacts = [r for r in records if r.get("id", "").startswith("CONTACT-")]
    orgs = [r for r in records if r.get("type") == "organization" and not r.get("id", "").startswith("CONTACT-")]

    def relevance_score(record: dict[str, Any]) -> int:
        score = len(set(record.get("tags", [])).intersection(relevant_tags))
        searchable = (record.get("summary", "") + " " + record.get("_body", "")).lower()
        if topic.lower() in searchable:
            score += 2
        return score

    relevant_contacts = [(relevance_score(c), c) for c in contacts]
    relevant_contacts = [(s, c) for s, c in relevant_contacts if s > 0]
    relevant_contacts.sort(key=lambda x: x[0], reverse=True)

    result = f"# Contacts for: {topic}\n\n"
    result += f"Matched topics: {', '.join(relevant_tags)}\n\n"

    # Separate pro bono from commercial
    pro_bono = []
    commercial = []

    for score, contact in relevant_contacts:
        body = contact.get("_body", "").lower()
        if "commercial law firm" in body or "paid legal representation" in body:
            commercial.append((score, contact))
        else:
            pro_bono.append((score, contact))

    if pro_bono:
        result += "## Pro Bono / Nonprofit Organizations\n\n"
        result += "*These organizations may provide free legal assistance:*\n\n"
        for score, contact in pro_bono[:5]:
            result += f"### {contact.get('title')}\n"
            result += f"{contact.get('summary', '')}\n\n"
            contact_info = _extract_contact_info(contact.get("_body", ""))
            if contact_info:
                result += f"{contact_info}\n\n"
            result += "---\n\n"

    if commercial:
        result += "## Commercial Law Firms\n\n"
        result += "*These firms provide paid representation for technology companies:*\n\n"
        for score, contact in commercial[:5]:
            result += f"### {contact.get('title')}\n"
            result += f"{contact.get('summary', '')}\n\n"
            contact_info = _extract_contact_info(contact.get("_body", ""))
            if contact_info:
                result += f"{contact_info}\n\n"
            result += "---\n\n"

    if not relevant_contacts:
        result += "\n⚠️ No contacts found for this topic. Try broader terms like 'digital rights', 'open source', or 'privacy'.\n"

    return result


@mcp.tool()
def summarize_landscape(
    topic: str,
) -> str:
    """Get a complete overview of the legal and organizational landscape for a topic area.

    Provides a comprehensive summary including: relevant cases, organizations, attorneys,
    policymakers, statutes, current legislative status, and how to get help.

    Args:
        topic: Topic area (e.g., "code as speech", "encryption rights", "CFAA reform", "open source licensing", "internet censorship")

    Returns:
        Complete landscape overview organized by category.
    """
    _log_request("summarize_landscape")
    records = load_all_records()
    relevant_tags = _find_relevant_tags(topic)

    def relevance_score(record: dict[str, Any]) -> int:
        score = len(set(record.get("tags", [])).intersection(relevant_tags))
        searchable = (record.get("summary", "") + " " + record.get("_body", "")).lower()
        for word in topic.lower().split():
            if len(word) > 3 and word in searchable:
                score += 1
        return score

    # Gather all relevant records by type
    cases = sorted([(relevance_score(r), r) for r in records if r.get("type") == "case" and relevance_score(r) > 0], key=lambda x: -x[0])
    orgs = sorted([(relevance_score(r), r) for r in records if r.get("type") == "organization" and relevance_score(r) > 0], key=lambda x: -x[0])
    attorneys = sorted([(relevance_score(r), r) for r in records if r.get("type") == "attorney" and relevance_score(r) > 0], key=lambda x: -x[0])
    policymakers = sorted([(relevance_score(r), r) for r in records if r.get("type") == "person" and "person" in r.get("tags", []) and relevance_score(r) > 0], key=lambda x: -x[0])
    statutes = sorted([(relevance_score(r), r) for r in records if r.get("type") == "statute" and relevance_score(r) > 0], key=lambda x: -x[0])
    topics = sorted([(relevance_score(r), r) for r in records if r.get("type") == "topic" and relevance_score(r) > 0], key=lambda x: -x[0])

    result = f"# Landscape: {topic}\n\n"
    result += f"Matched topics: {', '.join(relevant_tags)}\n\n"

    # Summary stats
    total = len(cases) + len(orgs) + len(attorneys) + len(policymakers) + len(statutes) + len(topics)
    result += f"**{total} relevant records found**: {len(cases)} cases, {len(orgs)} organizations, "
    result += f"{len(attorneys)} attorneys, {len(policymakers)} policymakers, {len(statutes)} statutes, {len(topics)} topics\n\n"

    # Key legal principles
    if topics:
        result += "## Key Legal Principles\n\n"
        for _, t in topics[:4]:
            result += f"- **{t.get('title')}** — {t.get('summary', '')}\n"
        result += "\n"

    # Landmark cases
    if cases:
        result += "## Landmark Cases\n\n"
        for _, case in cases[:6]:
            result += f"- **{case.get('title')}** — {case.get('summary', '')}\n"
        result += "\n"

    # Statutes
    if statutes:
        result += "## Relevant Statutes\n\n"
        for _, statute in statutes[:4]:
            result += f"- **{statute.get('title')}** — {statute.get('summary', '')}\n"
        result += "\n"

    # Organizations
    if orgs:
        result += "## Organizations\n\n"
        for _, org in orgs[:6]:
            result += f"- **{org.get('title')}** — {org.get('summary', '')}\n"
        result += "\n"

    # Attorneys
    if attorneys:
        result += "## Attorneys & Legal Experts\n\n"
        for _, att in attorneys[:5]:
            result += f"- **{att.get('title')}** — {att.get('summary', '')}\n"
        result += "\n"

    # Policymakers and legislation
    if policymakers:
        result += "## Policymakers & Legislation\n\n"
        for _, pm in policymakers[:4]:
            result += f"- **{pm.get('title')}** — {pm.get('summary', '')}\n"
        result += "\n"

    # How to get help
    result += "## How to Get Help\n\n"
    result += "Use `get_contacts_for(\"" + topic + "\")` to get specific contact information and intake paths.\n"
    result += "Use `find_help(\"describe your specific situation\")` for tailored recommendations.\n"

    return result


# ─── Entry Point ───────────────────────────────────────────────────────────────

def main():
    """Run the MCP server."""
    import sys

    transport = "stdio"
    port = 8080

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--transport" and i + 1 < len(args):
            transport = args[i + 1]
            i += 2
        elif args[i] == "--port" and i + 1 < len(args):
            port = int(args[i + 1])
            i += 2
        else:
            i += 1

    if transport == "stdio":
        mcp.run()
    else:
        mcp.run(transport=transport)


if __name__ == "__main__":
    main()
