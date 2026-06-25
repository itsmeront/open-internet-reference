# Roadmap

## Current Sprint

### Sprint 8: First Public Release Candidate

Goal: tag and document the first public OIR release after Sprint 7 analysis and policy work.

Milestones:

- [ ] Finalize `CHANGELOG.md` for `v0.1.0` and update release label from Unreleased.
- [ ] Run full CI validation and strict site build on a clean checkout.
- [ ] Create git commit and `v0.1.0` tag when the repository owner approves.
- [ ] Publish generated site to the chosen hosting target.
- [ ] Close remaining high-priority research debt items blocking release notes.

Exit criteria:

- `CHANGELOG.md` contains a dated `v0.1.0` section matching repository contents.
- CI passes on the release candidate branch or commit.
- Public site and handbook reflect the release version label.
- Release process in `PUBLISHING.md` is exercised at least once locally.

## Planned Sprint

### Sprint 9: Collaboration & Editorial Workflow

Goal: enable structured public suggestions and domain-expert review while keeping Git as the canonical source of truth.

Architecture: **Git-first near term**; **authenticated admin UI that opens PRs or commits** medium term. No database-only CMS that bypasses audit history.

#### Phase A: Git-native collaboration

Milestones:

- [x] Document roles, permissions, intake rules, and phased plan in `EDITORIAL_WORKFLOW.md`.
- [x] Add GitHub issue templates for edit suggestions, intake proposals, and topic/taxonomy requests.
- [x] Add pull request template aligned with validation requirements.
- [x] Add `CODEOWNERS` scaffold for domain review paths.
- [ ] Configure real code owners and branch protection on the hosting repository.
- [ ] Add public “propose change” links from generated pages to repository contribution paths.

Exit criteria:

- Contributors can file structured suggestions without write access.
- Pull requests prompt evidence and validation checks.
- Domain review paths are documented and ready to enforce.

#### Phase B: Editorial tooling on Git

Milestones:

- [ ] Add taxonomy and topic audit reports (tag usage, orphans, duplicate candidates).
- [ ] Add intake helper that creates draft bibliography or intake queue entries from structured input.
- [ ] Extend review metadata for assignment and editorial queues.
- [ ] Surface assignment and stale verification work in generated dashboards.

Exit criteria:

- Maintainers can audit topics and tags without manual repo-wide searches.
- Intake proposals can become auditable files without a custom CMS.

#### Phase C: Authenticated admin UI

Milestones:

- [ ] Authenticated admin for topic lifecycle, taxonomy merge, and relationship editing.
- [ ] Topic browser showing related sources, pages, and research debt.
- [ ] Intake submission UI with mandatory provenance fields.
- [ ] All admin actions produce commits or pull requests; CI runs before merge.

Exit criteria:

- Domain experts can maintain topics and relationships through a UI without losing Git audit history.
- No direct path from intake submission to `verified` without editor approval.

## Completed Sprints

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

## Earlier Completed Sprints

### Sprint 6: Primary Source Deepening and Case Analysis

Goal: strengthen legal seed records with official primary sources and begin substantive case and constitutional analysis.

Milestones:

- [x] Add official GovInfo and U.S. Reports source records for priority legal authorities.
- [x] Summarize `CASE-RENO-V-ACLU` holding from official reporter materials.
- [x] Add Fourth Amendment seed topic with constitutional source record.
- [x] Record governance alignment outcomes for imported charter and roadmap materials.
- [x] Add case law sources for safe harbor, CFAA, and Fourth Amendment digital privacy topics.
- [x] Add onion routing and Signal Protocol primary technical sources.

Exit criteria:

- Priority case and statute records cite at least one official government source.
- At least one seed case record includes syllabus-level verified facts from primary materials.
- Research debt backlog reflects completed and remaining verification tasks.
- Root governance docs are identified as authoritative over imported `.docx` materials.

### Sprint 5: Knowledge Expansion and Review Readiness

Goal: grow the verified seed knowledge graph and prepare OIR for broader external review.

Milestones:

- [x] Refresh public-facing project status and navigation copy.
- [x] Document brand asset generation and favicon workflow.
- [x] Verify outreach records against official organization pages.
- [x] Add the next batch of source-backed knowledge pages from intake queues (First Amendment and safe harbor topics; four supporting source records).
- [x] Expand legal and technical seed coverage where primary sources already exist (computer fraud, code as speech, intermediary liability, onion routing).
- [x] Triage research debt items into concrete verification tasks.

Exit criteria:

- Public site copy reflects the current publishing and handbook capabilities.
- CI validates brand asset generation alongside metadata, links, and site builds.
- At least five additional verified knowledge or source records are added, or equivalent research debt is closed with documented outcomes.
- Review status and outreach dashboards reflect current verification state.

## Earlier Completed Sprints

### Sprint 4: Publishing Hardening

Goal: make the public website reliable enough for review and collaboration.

Milestones:

- [x] Add CI validation.
- [x] Add local Markdown link checking.
- [x] Add site search tuning.
- [x] Add generated bibliography and glossary prototypes.
- [x] Add generated relationship graph prototype.
- [x] Document release and versioning workflow.
- [x] Add interactive relationship graph visualization.
- [x] Add generated handbook and print-ready handbook export.
- [x] Add canonical SVG brand assets for site header, cover, and favicons.

Exit criteria:

- CI validates metadata, local links, and site builds.
- Publishing workflow is documented.
- Generated indexes can be produced without manual editing.
- The public site is ready for broader review.
- Public bibliography and glossary index pages are generated from metadata.
- Public citation index pages are generated from metadata.
- Public relationship graph index pages are generated from metadata.
- Public relationship graph visualization is generated from metadata.
- Public review status dashboard is generated from metadata.
- Public timeline pages are generated from explicit metadata dates.
- AI retrieval dataset exports are generated from metadata.
- Outreach CRM prototype is generated from outreach-tagged metadata.
- Handbook prototype is generated from knowledge metadata.
- Print-ready handbook source is generated for browser PDF export.

## Earlier Sprints

### Sprint 3: Seed Knowledge Graph

Goal: create the first small set of verified knowledge pages and evidence-backed relationships.

Milestones:

- [x] Create seed pages for major topic areas.
- [x] Create seed pages for a limited number of organizations, cases, statutes, technologies, and protocols.
- [x] Add relationship records only where evidence exists.
- [x] Validate metadata and cross-links.

Exit criteria:

- Seed pages cite verified source records.
- Relationships include source-backed evidence.
- Metadata validation passes.
- The website exposes the seed knowledge pages.

### Sprint 2: Source Intake and Verification

Goal: convert imported notes and documents into traceable source records without treating unverified material as fact.

Milestones:

- [x] Inventory all imported documents.
- [x] Classify each document by source type, provenance, confidence, and verification needs.
- [x] Create source-intake records for imported project materials.
- [x] Establish research debt tracking.
- [x] Extract candidate entities, claims, and topics from imported documents.
- [x] Create bibliography records for primary sources, statutes, cases, organizations, technical standards, and academic materials.

Exit criteria:

- Imported materials have source records.
- Candidate claims and entities are separated from verified facts.
- Research debt is tracked explicitly.
- First external source records are ready to support seed knowledge pages.

### Sprint 1: Repository Foundation

Goal: establish the repository as a durable, evidence-first open-source research platform before writing substantive content.

Milestones:

- [x] Create root project documentation.
- [x] Define initial repository structure.
- [x] Configure MkDocs Material publishing scaffold.
- [x] Define initial metadata model.
- [x] Define initial taxonomy.
- [x] Add knowledge page templates.
- [x] Add validation tooling scaffold.
- [x] Review imported source documents and classify them as source material.

Exit criteria:

- The repository has stable conventions for research, metadata, citations, style, and contribution workflow.
- New knowledge pages can be created from templates.
- Metadata validation can run locally.
- The website can be served locally with MkDocs Material.

## Backlog

- Interactive graph exploration beyond current zoom and pan.
- Curated timeline narratives.
- Advanced citation analytics.
- Advanced outreach synchronization and contact lifecycle tracking.
- Curated handbook editorial workflow.
- Automated PDF rendering beyond browser print.
- Advanced AI retrieval chunking and embeddings.

Editorial workflow and topic administration are tracked in **Sprint 9** (`EDITORIAL_WORKFLOW.md`).
