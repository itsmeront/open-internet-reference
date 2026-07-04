# Roadmap

## Current Sprint

### Sprint 12: MCP Security, Write Tools, and Content Gaps

Goal: harden the MCP server for optional public access, implement AI write paths through the editorial pipeline, and close remaining Sprint 10 content gaps.

Milestones:

- [ ] Add Viacom v. YouTube case page with primary sources.
- [ ] Resolve 20+ high-priority research debt items (cases, attorneys, organizations).
- [x] Add technical expert pages for litigation consultation (Cerf, Zittrain, Vixie, Diffie, Zimmermann) and publish Experts navigation page.
- [ ] Add remaining expert candidates (Kahn, Crocker, Berners-Lee, Rivest) with testimony/deposition sources where available.
- [ ] Add MCP authentication (API keys for HTTP/streamable-http mode).
- [ ] Add MCP rate limiting (query volume, `verify_source` URL checks).
- [ ] Expose MCP via nginx at `/mcp/` behind TLS and auth (only after auth + rate limits are implemented).
- [ ] Implement write MCP tools: `suggest_edit`, `submit_intake`, `resolve_debt_item`.
- [ ] GitHub App integration for AI-proposed PRs (branch creation, labels, human review queue).
- [ ] AI agent identity management and attribution in PR descriptions.

Exit criteria:

- Write tools create labeled PRs; nothing merges without human review.
- Public MCP endpoint remains disabled until auth and rate limits pass review.
- Cursor developers use local stdio (`.cursor/mcp.json`); remote agents use authenticated HTTP when enabled.
- Viacom case and debt-resolution targets met or explicitly deferred with documented rationale.

## Completed Sprints

### Sprint 11: Editorial Workflow, Production CMS, and MCP Read Path

Goal: enable moderation automation, deploy Decap CMS with GitHub OAuth, and ship a read-only MCP server for Cursor and localhost HTTP access.

Milestones:

- [x] Add moderation queue dashboard (`tools/moderation_queue.py`) and taxonomy audit (`tools/taxonomy_audit.py`).
- [x] Add GitHub label definitions (`.github/labels.yml`) and sync tooling (`tools/sync_labels.py`).
- [x] Add moderation and stale PR workflows (`.github/workflows/moderation.yml`, `moderation-reports.yml`, `stale.yml`).
- [x] Fix moderation-reports for branch-protected `main` (open PR instead of direct push).
- [x] Document branch protection and automation bypass (`.github/BRANCH_PROTECTION.md`).
- [x] Deploy Decap CMS at `/admin/` with GitHub OAuth on production (`oir-oauth` container, nginx `/api/auth/`).
- [x] Document OAuth setup and production troubleshooting (`.github/DECAP_CMS_OAUTH.md`).
- [x] Use OAuth env-file pattern on server to avoid secrets in shell history.
- [x] Add non-GitHub contribution path (`website/about/contributing-without-github.md`).
- [x] Build MCP server with 9 read-only tools (`oir_mcp/server.py`).
- [x] Deploy production MCP service (`oir-mcp` systemd, localhost `:8080`).
- [x] Add Cursor project MCP config (`.cursor/mcp.json`, `.cursor/README.md`).
- [x] Document MCP public-vs-private policy and production deployment (`MCP_SERVER.md`, `deploy/README.md`).

Exit criteria:

- ✅ Moderation labels and report tooling operational in CI.
- ✅ Decap CMS login and editing work at `https://openinternetresearch.com/admin/`.
- ✅ MCP read tools available in Cursor via stdio and on server via localhost HTTP.
- ✅ MCP intentionally not public until authentication is implemented.

### Sprint 10: Content Depth and Knowledge Expansion

Goal: expand the knowledge base with actionable content and systematically resolve research debt.

Milestones:

- [x] Add law firms known for defending open source companies (Perkins Coie, Wilson Sonsini, Cooley, Fenwick).
- [x] Add policymakers with track records supporting digital rights (Wyden, Paul, Khanna, Lofgren).
- [x] Add additional legal cases and precedent (Google v. Oracle, Perfect 10 v. CCBill, Section 230 statute page).
- [x] Add technical and legal topic depth (intermediary liability, code as speech, onion routing, Signal sources).
- [x] Design MCP server architecture (`MCP_SERVER.md`).

Exit criteria:

- ✅ 50+ knowledge pages with metadata validation.
- ✅ Actionable contact and organization coverage for legal and policy outreach.
- ⏭ Viacom v. YouTube and bulk debt resolution deferred to Sprint 12.

### Sprint 9: Collaboration, Editorial Workflow, and Public Deployment

Goal: enable structured public contributions, deploy the site publicly, and establish AI integration architecture.

Milestones:

- [x] Document roles, permissions, intake rules, and phased plan in `EDITORIAL_WORKFLOW.md`.
- [x] Add GitHub issue templates for edit suggestions, intake proposals, and topic/taxonomy requests.
- [x] Add pull request template aligned with validation requirements.
- [x] Add `CODEOWNERS` scaffold for domain review paths.
- [x] Add `CONTRIBUTING.md` with paths for humans and AI agents.
- [x] Add public "Edit this page" and "Suggest a change" links on all generated pages.
- [x] Add Decap CMS configuration (`/admin/`) for Git-backed editing with editorial workflow.
- [x] Deploy site publicly at `openinternetresearch.com` (Oracle Cloud, Docker nginx, Let's Encrypt).
- [x] Add `RestartAndUpdateOIR.sh` for one-command server updates.
- [x] Add webhook handler for auto-deploy on GitHub push.
- [x] Add cron jobs for periodic URL checking and research debt reporting.

Exit criteria:

- ✅ Site live at `https://openinternetresearch.com`.
- ✅ Contributors can file structured suggestions via GitHub Issues.
- ✅ Auto-deploy pipeline: merge → webhook → rebuild → live.

### Sprint 8: First Public Release Candidate

Goal: expand content to make OIR useful as a resource for contacting lawyers and organizations that help open source companies, and prepare for public release.

Milestones:

- [x] Add 7 organization knowledge pages (Knight First Amendment Institute, Software Freedom Conservancy, FSF, CDT, OSI, SFLC, Institute for Justice).
- [x] Add 7 attorney/person pages (Cindy Cohn, Eben Moglen, Jennifer Granick, Lawrence Lessig, Mitch Stoltz, Kit Walsh, Corynne McSherry).
- [x] Add 4 landmark case pages (Bernstein v. DOJ, Junger v. Daley, Universal City Studios v. Corley, Packingham v. NC).
- [x] Add 9 actionable contact records with intake paths for legal help.
- [x] Add 28+ bibliography source records backing all new content.
- [x] Reorganize site navigation: replace "Seed Pages" with Organizations, Lawyers, Law sections.
- [x] Fix non-clickable URLs in generated pages (add `link_backtick_urls()` to generator).
- [x] Add `CONTACT-` prefix to ID validator and data model.
- [x] Add URL health checker tool (`tools/check_urls.py`) with rate limiting and archive handling.
- [x] Add research debt scanner (`tools/resolve_debt.py`) with prioritized reporting.
- [x] Make review-status dashboard filters clickable with per-category sections.
- [x] Add page status banners to all generated source-doc pages.
- [x] Resolve key debt items (Cindy Cohn departure, Bernstein practical impact, NSA outcomes).
- [x] Update homepage with mission statement and clickable category navigation.
- [x] Fix project name consistency (Open Internet Reference throughout).
- [x] Publish generated site to hosting target.

Exit criteria:

- ✅ 116+ validated pages across knowledge, bibliography, and contacts.
- ✅ CI passes (metadata validation, link checking, strict MkDocs build).
- ✅ Site reorganized with clear entry points for finding help.
- ✅ Public site deployed and accessible.

### Sprint 7: Case Analysis Depth and Release Readiness

Goal: deepen case and topic analysis, close remaining primary-source gaps, and prepare for the first public repository release.

Milestones:

- [x] Summarize full reasoning for priority seed cases beyond syllabus-level facts.
- [x] Add official GovInfo records for Van Buren, Carpenter, and additional appellate cases where available.
- [x] Decompose Axona manual claims into auditable verification tasks.
- [x] Update stale public status copy and prepare first release notes.
- [x] Decide outreach contact record requirements before creating `contacts/` entries.

### Sprint 6: Primary Source Deepening and Case Analysis

Goal: strengthen legal seed records with official primary sources and begin substantive case and constitutional analysis.

Milestones:

- [x] Add official GovInfo and U.S. Reports source records for priority legal authorities.
- [x] Summarize `CASE-RENO-V-ACLU` holding from official reporter materials.
- [x] Add Fourth Amendment seed topic with constitutional source record.
- [x] Record governance alignment outcomes for imported charter and roadmap materials.
- [x] Add case law sources for safe harbor, CFAA, and Fourth Amendment digital privacy topics.
- [x] Add onion routing and Signal Protocol primary technical sources.

### Sprint 5: Knowledge Expansion and Review Readiness

Goal: grow the verified seed knowledge graph and prepare OIR for broader external review.

Milestones:

- [x] Refresh public-facing project status and navigation copy.
- [x] Document brand asset generation and favicon workflow.
- [x] Verify outreach records against official organization pages.
- [x] Add the next batch of source-backed knowledge pages from intake queues.
- [x] Expand legal and technical seed coverage where primary sources already exist.
- [x] Triage research debt items into concrete verification tasks.

### Sprint 4: Publishing Hardening

Goal: make the public website reliable enough for review and collaboration.

Milestones:

- [x] Add CI validation, local link checking, site search tuning.
- [x] Add generated bibliography, glossary, relationship graph, timeline, and handbook prototypes.
- [x] Document release and versioning workflow.
- [x] Add interactive relationship graph visualization.
- [x] Add canonical SVG brand assets for site header, cover, and favicons.

### Sprint 3: Seed Knowledge Graph

Goal: create the first small set of verified knowledge pages and evidence-backed relationships.

### Sprint 2: Source Intake and Verification

Goal: convert imported notes and documents into traceable source records without treating unverified material as fact.

### Sprint 1: Repository Foundation

Goal: establish the repository as a durable, evidence-first open-source research platform before writing substantive content.

## Backlog

- Interactive graph exploration beyond current zoom and pan.
- Curated timeline narratives.
- Advanced citation analytics.
- Advanced outreach synchronization and contact lifecycle tracking.
- Curated handbook editorial workflow.
- Automated PDF rendering beyond browser print.
- Advanced AI retrieval chunking and embeddings.
- Zensical migration (when MkDocs 1.x successor is production-ready).
- Non-GitHub authentication for public wiki-style editing.
- Real-time collaboration features.
