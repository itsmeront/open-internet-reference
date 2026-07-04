# Roadmap

OIR development is organized in sprints. The full plan lives in [`ROADMAP.md`](https://github.com/itsmeront/open-internet-reference/blob/main/ROADMAP.md) at the repository root.

## Current Sprint: MCP Security and Write Tools

We are hardening the MCP server and closing remaining content gaps:

- **MCP authentication and rate limiting** before any public HTTP endpoint
- **Write tools** (`suggest_edit`, `submit_intake`, `resolve_debt_item`) that open labeled PRs for human review
- **GitHub App integration** for AI-proposed changes
- **Viacom v. YouTube** case page and high-priority research debt resolution
- **Technical expert pages** for litigation consultation — Cerf, Vixie, Diffie, Zimmermann, Zittrain added; Kahn, Crocker, Berners-Lee remain in intake queue

### MCP access model

| Use case | How to connect | Public URL needed? |
|----------|----------------|--------------------|
| **Cursor (local dev)** | `.cursor/mcp.json` — stdio mode | No |
| **Production server** | `oir-mcp` on `127.0.0.1:8080` | No (localhost only) |
| **Remote AI agents (future)** | HTTPS at `/mcp/` with API keys | Yes — after auth ships |

The MCP server is **intentionally not public** today. Current tools are read-only; exposing HTTP without authentication would allow unauthenticated querying and abuse of URL verification. See [`MCP_SERVER.md`](https://github.com/itsmeront/open-internet-reference/blob/main/MCP_SERVER.md) for details.

## Recently Completed

### Sprint 11 — Editorial workflow, Decap CMS, and MCP read path

- Moderation queue, taxonomy audit, GitHub labels, and scheduled report workflows
- Decap CMS at `/admin/` with GitHub OAuth on production
- OAuth env-file pattern for server secrets (no credentials in shell history)
- MCP server with 9 read-only tools; Cursor project config (`.cursor/mcp.json`)
- Production `oir-mcp` service on localhost

### Sprint 10 — Content depth

- Law firms (Perkins Coie, Wilson Sonsini, Cooley, Fenwick)
- Policymakers (Wyden, Paul, Khanna, Lofgren)
- Additional cases and topics (Google v. Oracle, Section 230, intermediary liability)

### Sprint 9 — Public deployment

- Site live at [openinternetresearch.com](https://openinternetresearch.com)
- GitHub issue/PR templates, `CODEOWNERS`, editorial workflow docs
- Auto-deploy via webhook and `RestartAndUpdateOIR.sh`

## Foundation in Place

- 50+ knowledge pages, bibliography, contacts, and generated indexes
- Metadata validation, link checking, relationship graph, handbook, and CI
- Tools for URL health, research debt, moderation reports, and label sync
- Documented publishing, OAuth, and MCP setup guides

## Backlog

- Curated timeline narratives and advanced citation analytics
- Advanced outreach synchronization and contact lifecycle tracking
- Automated PDF rendering beyond browser print
- Advanced AI retrieval chunking and embeddings
- Zensical migration (when MkDocs successor is production-ready)
