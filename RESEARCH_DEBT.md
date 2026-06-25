# Research Debt

Research debt tracks useful leads that should not yet be treated as verified OIR knowledge.

## Current Debt Categories

### Imported Manual Claims

The file `Axona Constitutional & Public Policy Reference Manual.docx` should be decomposed into individual candidate claims and topics. Each claim needs external verification before being reused.

Initial verification targets:

- Legal authorities related to software publication and protected expression
- Constitutional doctrines relevant to code, encryption, privacy, and open source software
- Technical claims about peer-to-peer, decentralized, censorship-resistant, and serverless systems
- Public policy claims about internet governance and digital rights
- Historical claims about cryptography, distributed systems, and internet architecture

### Outreach Contacts

The outreach files contain candidate organizations, law firms, academics, policymakers, and public contacts. These require verification before outreach use.

Initial verification targets:

- Official organization websites
- Public contact pages
- Public professional biographies
- Current role and affiliation
- Relevance to digital rights, open source, constitutional law, privacy, cryptography, or internet governance

### Project Governance Alignment

The imported charter and roadmap documents are retained as provenance under `bibliography/imported/`. Root repository docs are authoritative for current project governance:

- `PROJECT_CHARTER.md` supersedes `Open Internet Reference Project Charter.docx` for mission, principles, and roles.
- `ROADMAP.md` supersedes `Open Internet Reference Roadmap.docx` for sprint planning and milestones.
- `RESEARCH_STANDARDS.md`, `DATA_MODEL.md`, and `TAXONOMY.md` are the live conventions for research workflow and metadata.

Imported `.docx` materials should be consulted for historical context only, not as verified external knowledge.

## Debt Resolution Rules

- Resolve research debt by linking to verified source records or by removing unsupported claims.
- Do not resolve an item merely by copying language from an internal draft.
- Prefer small, auditable changes over large content imports.
- Record unresolved uncertainty directly on the relevant page.

## Verification Task Backlog

The following concrete tasks were triaged from intake queues on 2026-06-19. Each item should produce a source record, a knowledge page update, or a documented deferral.

### Legal and Policy

| Task | Status | Next action |
| --- | --- | --- |
| Summarize `CASE-RENO-V-ACLU` holding and reasoning | Partial | Syllabus-level holding added from U.S. Reports; full reasoning summary still open |
| Add official U.S. Code sources for § 512 and § 1030 | Done | GovInfo source records added; statute pages updated |
| Expand intermediary liability beyond copyright safe harbor | Partial | `CASE-PERFECT10-V-CCBILL` added for § 512; non-copyright doctrines still open |
| Fourth Amendment and digital privacy topic | Partial | `CASE-CARPENTER-V-US` added; additional digital privacy case law still open |
| Export control and encryption law topic | Open | Add primary regulatory or case sources before drafting |

### Technical

| Task | Status | Next action |
| --- | --- | --- |
| Onion routing primary papers | Partial | `SRC-TOR-DESIGN-PAPER` added; earlier NRL papers still open |
| Signal Protocol specification sources | Partial | X3DH and Double Ratchet source records added |
| Public key cryptography topic | Open | Add RFC or canonical paper source before drafting |
| Content addressing topic | Open | Add IPFS, CID, or other standards source before drafting |

### Outreach and Organizations

| Task | Status | Next action |
| --- | --- | --- |
| Signal governance or foundation page | Open | `/about/` unavailable; monitor for stable official page |
| EFF, ACLU, Tor independent history sources | Open | Supplement official pages with third-party sources where analysis requires |
| Contact records under `contacts/` | Deferred | Policy recorded in `contacts/README.md`; create records only after outreach use case is defined |

### Governance Alignment

| Task | Status | Next action |
| --- | --- | --- |
| Compare imported charter to `PROJECT_CHARTER.md` | Done | Root `PROJECT_CHARTER.md` is authoritative; imported `.docx` retained as provenance only |
| Compare imported roadmap to `ROADMAP.md` | Done | Root `ROADMAP.md` sprint structure supersedes imported roadmap language |
| Decompose Axona manual into candidate claims | Partial | `intake/axona-claim-queue.md` created with auditable tasks on 2026-06-19 |
