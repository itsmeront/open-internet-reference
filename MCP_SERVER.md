# OIR MCP Server Design

## Overview

The OIR MCP (Model Context Protocol) server provides tools for AI agents to interact with the Open Internet Reference knowledge base. AI contributions follow the same editorial workflow as human contributions — all changes go through pull requests and require human approval.

## Principles

1. **AI as contributor, not authority** — AI proposes; humans verify and approve.
2. **Transparency** — AI-generated content is always labeled as such.
3. **Same pipeline** — AI uses the same Git workflow (PRs, validation, review) as humans.
4. **Evidence-first** — AI must cite sources, not training data assertions.
5. **Research debt awareness** — AI should prioritize resolving existing debt over generating new content.

## Tools

### `query_knowledge`

Query the OIR knowledge base for information about a topic, organization, case, or person.

**Parameters:**
- `query` (string) — Natural language query or entity ID
- `type` (optional) — Filter by type: case, organization, attorney, topic, source
- `include_debt` (optional, boolean) — Include research debt items in response

**Returns:** Matching records with metadata, verified facts, and relationships.

### `get_research_debt`

Get prioritized research debt items that need resolution.

**Parameters:**
- `type` (optional) — Filter by page type
- `limit` (optional, integer) — Maximum items to return
- `priority` (optional) — "high", "medium", "low"

**Returns:** Prioritized list of research debt items with page context.

### `suggest_edit`

Propose an edit to an existing knowledge page.

**Parameters:**
- `page_id` (string) — The ID of the page to edit (e.g., "PERSON-CINDY-COHN")
- `section` (string) — Which section to modify (e.g., "verified_facts", "research_debt")
- `content` (string) — The proposed new content for that section
- `sources` (list of strings) — Source IDs or URLs supporting the edit
- `rationale` (string) — Why this edit should be made

**Returns:** PR URL or draft ID for the proposed change.

**Behavior:**
- Creates a branch named `ai/edit-{page_id}-{timestamp}`
- Commits the change with author `OIR-AI <ai@oir.example>`
- Opens a PR with the `ai-generated` label
- PR description includes rationale and source references

### `submit_intake`

Propose new content for the knowledge base.

**Parameters:**
- `type` (string) — Entity type: "organization", "attorney", "case", "topic", "source"
- `title` (string) — Proposed title
- `summary` (string) — One-sentence neutral summary
- `content` (string) — Full Markdown body
- `sources` (list) — Source URLs or references
- `tags` (list of strings) — Proposed taxonomy tags

**Returns:** PR URL for the proposed new page.

**Behavior:**
- Generates appropriate ID from type + title
- Creates full Markdown file with proper front matter
- Validates against `DATA_MODEL.md` requirements
- Opens a PR with `ai-generated` and `needs-review` labels

### `verify_source`

Check if a source URL is still accessible and retrieve its current content.

**Parameters:**
- `source_id` (string) — The SRC-* ID to check
- `url` (optional, string) — Override URL to check instead

**Returns:** HTTP status, accessibility, content summary, and archive URL if available.

### `resolve_debt_item`

Propose resolution for a specific research debt item.

**Parameters:**
- `page_id` (string) — Page containing the debt item
- `debt_text` (string) — The debt item text to resolve
- `resolution` (string) — How it was resolved (new facts, sources, etc.)
- `sources` (list) — Sources supporting the resolution

**Returns:** PR URL for the proposed resolution.

## Authentication

The MCP server authenticates AI agents via:
- API key for server-to-server communication
- GitHub App token for creating branches and PRs
- All actions are attributed to the AI agent's identity

## Rate Limiting

- Maximum 10 PRs per hour per AI agent
- Maximum 100 queries per minute
- Source verification: maximum 5 URL checks per minute (respects domain delays)

## Git Author Convention

All AI-generated commits use:

```
Author: OIR-AI-Worker <ai-worker@oir.example>
Committer: OIR-AI-Worker <ai-worker@oir.example>
```

PR descriptions include:

```markdown
> 🤖 This change was proposed by an AI agent and requires human review before merging.
> 
> **Agent:** [agent name/version]
> **Confidence:** [high/medium/low]
> **Sources consulted:** [list]
```

## Implementation Status

- [ ] Core MCP server framework
- [ ] `query_knowledge` tool
- [ ] `get_research_debt` tool
- [ ] `suggest_edit` tool
- [ ] `submit_intake` tool
- [ ] `verify_source` tool
- [ ] `resolve_debt_item` tool
- [ ] GitHub App integration for PR creation
- [ ] Authentication and rate limiting
- [ ] AI agent identity management

## Future Considerations

- Multi-agent coordination (avoid duplicate work)
- Confidence scoring for AI-generated content
- Automated re-verification scheduling
- Integration with Decap CMS for unified editing experience
