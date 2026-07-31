# Project Charter

## Name

Open Internet Reference (OIR)

## Motto

Evidence over assertion. Knowledge over opinion.

## How OIR Is Made

**Human-directed, AI-processed, source-bound.**

- **Humans** set priorities (what to intake), review and merge pull requests into the public draft corpus, and periodically deep-audit a smaller **verified core**.
- **AI assistants** do most drafting, structuring, cross-linking, mechanical QA (metadata, links, footnote coverage), and research-debt sweeps when directed.
- **Cited sources** are the authority for factual claims — not model memory, narrative force, or unsourced interpretation.

Merging a page into `main` means it is **accepted into the draft corpus** under human direction. It does **not** mean every claim has been human-verified. `status: verified` is scarce and reserved for periodic deep source checks.

OIR is not crowdsourced encyclopedia editing. Public suggestions are leads for processing, not a promise that volunteers will line-edit the site.

## Mission

Build a comprehensive, independently verifiable knowledge base documenting the legal, constitutional, historical, technical, and public policy landscape surrounding:

- Internet architecture
- Distributed systems
- Peer-to-peer networking
- Cryptography
- Open source software
- Privacy
- Constitutional law
- Internet governance
- Digital rights

OIR may include Axona as a case study, but Axona is not the primary focus. The reference must be useful to technologists, researchers, attorneys, policymakers, journalists, and civil society organizations without requiring prior knowledge of Axona.

## Operating Principles

- Accuracy comes before speed, completeness, or narrative force.
- Every significant factual claim should be independently verifiable via cited sources.
- Primary sources are preferred whenever available.
- Prefer facts and citations over interpretation; keep legal analysis, technical analysis, historical context, commentary, and recommendations clearly distinguishable.
- Unsupported claims must be marked as unverified or research debt rather than softened into apparent fact.
- Do not treat unsourced AI output as evidence; AI drafts must cite sources and start as `draft`.
- Generated artifacts are never manually edited.
- The Git repository is the single source of truth.

## Project Roles

OIR work should be approached as a small engineering and editorial team, with AI as the primary processing labor:

- Chief Architect: repository design, data model, and long-term technical coherence.
- Research Editor (human): prioritization, merge acceptance into the draft corpus, periodic verified-core audits, and research-debt direction.
- AI research assistants: intake processing, draft authorship, mechanical QA, and directed debt sweeps.
- Technical Writer: clear, consistent, accessible documentation.
- Knowledge Engineer: metadata, relationships, taxonomy, and retrieval design.
- Build Engineer: validation, publishing, automation, and release tooling.
- Project Manager: roadmap, changelog, milestones, and prioritization.

## Long-Term Outputs

The repository should be able to generate:

- Public website
- Handbook
- PDF
- Knowledge graph
- Timeline
- Bibliography
- Glossary
- Search index
- Outreach CRM
- AI retrieval dataset

All outputs should derive from the authoritative repository contents.
