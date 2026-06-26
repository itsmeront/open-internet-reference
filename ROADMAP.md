# Roadmap

## Current Sprint

### Sprint 10: Content Depth, MCP Server, and Debt Resolution

Goal: expand the knowledge base with actionable content, build the MCP server for AI integration, and systematically resolve research debt.

Milestones:

- [ ] Add law firms known for defending open source companies (Perkins Coie, Wilson Sonsini, Cooley, Fenwick, etc.).
- [ ] Add policymakers with track records supporting digital rights (Wyden, Paul, Khanna, Lofgren, etc.).
- [ ] Add additional legal cases and precedent from candidate lists.
- [ ] Build MCP server with `query_knowledge`, `get_research_debt`, and `verify_source` tools.
- [ ] Resolve high-priority research debt items (cases, attorneys, organizations).
- [ ] Add Viacom v. YouTube, Oracle v. Google, and other significant tech law cases.

Exit criteria:

- At least 10 additional knowledge pages added with sources.
- MCP server operational with at least 3 tools functional.
- Research debt reduced by 20+ items.
- All new content passes metadata validation.

## Completed Sprints

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
- [x] Design MCP server architecture (`MCP_SERVER.md`) for AI agent integration.
- [x] Deploy site publicly at `openinternetresearch.com` (Oracle Cloud, Docker nginx, Let's Encrypt).
- [x] Add `RestartAndUpdateOIR.sh` for one-command server updates.
- [x] Add webhook handler for auto-deploy on GitHub push.
- [x] Add cron jobs for periodic URL checking and research debt reporting.

Exit criteria:

- ✅ Site live at `https://openinternetresearch.com`.
- ✅ Contributors can file structured suggestions via GitHub Issues.
- ✅ Decap CMS provides Wikipedia-like editing interface.
- ✅ MCP server design documented and ready for implementation.
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
- ✅ Tools available for URL checking and debt tracking.
- ✅ Public site deployed and accessible.

### Sprint 7: Case Analysis Depth and Release Readiness

Goal: deepen case and topic analysis, close remaining primary-source gaps, and prepare for the first public repository release.

Milestones:

- [x] Summarize full reasoning for priority seed cases beyond syllabus-level facts.
- [x] Add official GovInfo records for Van Buren, Carpenter, and additional appellate cases where available.
- [x] Decompose Axona manual claims into auditable verification tasks.
- [x] Update stale public status copy and prepare first release notes.
- [x] Decide outreach contact record requirements before creating `contacts/` entries.

Exit criteria:

- At least three seed case records include holding plus one additional reasoning or procedural fact from primary sources.
- Research debt backlog reflects Sprint 6 completions and Sprint 7 priorities.
- Public site copy matches current sprint state.
- Repository is ready for an initial tagged release candidate.

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
- Full MCP server with all 6 tools (suggest_edit, submit_intake, resolve_debt_item).
- Non-GitHub authentication for public wiki-style editing.
- Real-time collaboration features.
