# Changelog

All notable changes to OIR will be recorded in this file.

The project uses human-readable milestone entries during the foundation phase. Formal semantic versioning can begin once the repository has its first public release.

## Unreleased

### Added

- Created Sprint 1 repository foundation documentation.
- Added project charter, roadmap, research standards, style guide, citation guide, data model, taxonomy, contribution guide, and README.
- Added MkDocs Material publishing scaffold.
- Added knowledge page template and directory structure.
- Added metadata validation tooling scaffold.
- Added source-intake records for imported project materials.
- Added `SOURCE_INTAKE.md` and `RESEARCH_DEBT.md` to track imported files, verification needs, and research debt.
- Updated the roadmap to make Sprint 2 source intake the current sprint.
- Added `intake/` queues for candidate topics, candidate entities, and verification tasks extracted from imported documents.
- Added initial external bibliography records for RFCs, statutes, case law, official organization pages, and the Kademlia academic paper.
- Advanced the roadmap to Sprint 3 seed knowledge graph work.
- Added initial seed knowledge pages for technical protocols, Kademlia, legal authorities, and organizations.
- Exposed the seed knowledge page set in the MkDocs site.
- Added hardened metadata graph validation for duplicate IDs, source references, relationship endpoints, and predicates.
- Added local Markdown link validation tooling.
- Added GitHub Actions validation workflow.
- Added `PUBLISHING.md` for local preview, validation, build output, CI, and release notes.
- Added generated bibliography and glossary JSON prototype tooling.
- Tuned MkDocs search indexing for English knowledge-base content and hyphenated identifiers.
- Added generated MkDocs bibliography and glossary pages to site navigation.
- Added generated source mirror pages and clickable Path links from generated bibliography and glossary entries.
- Added site behavior that opens external links in a new tab.
- Added generated relationship graph JSON and MkDocs page with clickable subject, object, source, and declaration links.
- Added generated Used For index and clickable Used For terms in source mirror pages.
- Added generated review status dashboard for metadata status, type, verification date, and review queues.
- Added generated citation index showing page-level and relationship-level source usage.
- Added generated timeline JSON and MkDocs page from explicit publication and verification dates.
- Added generated AI retrieval dataset manifest and JSONL export.
- Updated generated source mirrors so `SRC-*` links prefer external source URLs when available.
- Added generated outreach CRM prototype and Contacts section.
- Added generated handbook prototype from knowledge metadata.
- Added generated Mermaid relationship graph visualization.
- Added generated print-ready handbook page and print stylesheet for browser PDF export.
- Added interactive relationship graph visualization with zoom, pan, and clickable nodes.
- Added canonical SVG brand assets for the site header, handbook cover, and favicon generation.
- Added `tools/render_brand_assets.py` for favicon rasterization from the header logo SVG.
- Advanced the roadmap to Sprint 5 knowledge expansion and review readiness.
- Added First Amendment and safe harbor topic pages with Cornell LII and case/statute relationships.
- Added official about and history source records for EFF, ACLU, and Tor Project outreach verification.
- Added computer fraud, code as speech, intermediary liability, and onion routing topic pages with cross-links to existing seed records.
- Added Signal protocol documentation source record and reverified `ORG-SIGNAL`.
- Triaged research debt into concrete verification tasks in `RESEARCH_DEBT.md`.
- Fixed relationship graph Fit button to center graph content in the viewport.
- Advanced the roadmap to Sprint 6 primary source deepening and case analysis.
- Added official GovInfo and U.S. Reports source records for Reno v. ACLU and U.S. Code § 512 and § 1030.
- Summarized `CASE-RENO-V-ACLU` syllabus-level holding from official United States Reports materials.
- Added Fourth Amendment seed topic and Cornell LII constitutional source record.
- Recorded governance alignment outcomes: root charter and roadmap docs supersede imported `.docx` materials.
- Added `tools/serve.py` for local preview with index regeneration.
- Added Van Buren, Carpenter, and Perfect 10 v. CCBill case records with primary source links.
- Added Tor design paper and Signal X3DH and Double Ratchet specification source records.
- Added GovInfo source records for Van Buren and Carpenter.
- Expanded legal analysis for Reno, Van Buren, and Carpenter seed case records.
- Added `intake/axona-claim-queue.md` for auditable Axona manual decomposition.
- Documented contact record policy in `contacts/README.md`.
- Added `StartLocalServer.bat` and `StartLocalServer.sh` root launchers for local preview.
- Updated root and site status copy for Sprint 7 completion and release readiness.
- Added `EDITORIAL_WORKFLOW.md` and Sprint 9 collaboration plan (Git-first Phases A–C).
- Added GitHub issue templates, pull request template, and `CODEOWNERS` scaffold for editorial workflow.
