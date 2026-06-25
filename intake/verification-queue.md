# Verification Queue

This queue turns imported candidates into research tasks.

No item is considered resolved until the relevant claim, entity, contact path, or topic is supported by a primary or high-confidence source record.

## Priority 1: External Source Foundation

Create verified source records for authorities that can support the first seed knowledge pages.

Status: initial seed set created.

Initial source categories:

- Court opinions involving software, code, encryption, speech, privacy, and internet rights
- Statutes and regulations relevant to open source, computer crime, copyright, surveillance, export controls, and encryption
- RFCs and official standards for core internet architecture topics
- Canonical papers for peer-to-peer networking, distributed hash tables, cryptography, and secure messaging
- Official organization pages for outreach and civil society entities

Expected output:

- Bibliography records under `bibliography/`
- Draft knowledge pages only after source records exist

Initial records created:

- `bibliography/technical/SRC-RFC-9293.md`
- `bibliography/technical/SRC-RFC-8446.md`
- `bibliography/technical/SRC-RFC-1034.md`
- `bibliography/legal/SRC-RENO-V-ACLU-JUSTIA.md`
- `bibliography/legal/SRC-USC-17-512-LII.md`
- `bibliography/legal/SRC-USC-18-1030-LII.md`
- `bibliography/academic/SRC-KADEMLIA-PAPER.md`
- `bibliography/organizations/SRC-EFF-CONTACT.md`
- `bibliography/organizations/SRC-ACLU-CONTACT.md`
- `bibliography/organizations/SRC-TOR-PROJECT-CONTACT.md`
- `bibliography/organizations/SRC-SIGNAL-HOME.md`
- `bibliography/organizations/SRC-SIGNAL-DOCS.md`

## Priority 2: Outreach Verification

Verify candidate outreach entities before creating contact records.

Status: in progress. EFF, ACLU, Tor Project, and Signal organization pages were reverified on 2026-06-19. Signal `/about/` remains unavailable; homepage and docs page are the current official sources.

Tasks:

- Confirm official websites for each candidate organization.
- Confirm public contact or intake pages.
- Confirm current names, affiliations, and roles.
- Remove or mark stale any contact path that cannot be verified.
- Avoid adding private or inferred contact information.

Expected output:

- Verified contact records under `contacts/`
- Organization knowledge pages for entities that warrant durable reference coverage

## Priority 3: Technical Topic Verification

Select a small number of technical seed topics that can be sourced from standards or canonical papers.

Status: in progress. Onion routing topic page added from Tor Project history source on 2026-06-19.

Good first candidates:

- TCP/IP
- DNS
- Distributed hash tables
- Kademlia
- Public key cryptography
- Digital signatures
- Content addressing

Expected output:

- Verified source records
- Draft topic pages under `knowledge/`
- Relationship records only where evidence exists

## Priority 4: Legal Topic Verification

Select a small number of legal seed topics that can be sourced from primary legal authorities.

Status: in progress. First Amendment, safe harbor, computer fraud, code as speech, and intermediary liability topic pages added on 2026-06-19.

Good first candidates:

- First Amendment
- Code as speech
- Export control and encryption
- Fourth Amendment and digital privacy
- Copyright safe harbor

Expected output:

- Court case records
- Statute records
- Draft legal topic pages under `knowledge/`

## Priority 5: Governance Alignment

Compare imported project governance materials against root repository docs.

Status: triaged and partially resolved on 2026-06-19. Root `PROJECT_CHARTER.md` and `ROADMAP.md` are authoritative; see `RESEARCH_DEBT.md` for recorded outcomes.

Tasks:

- Identify any useful concepts missing from `PROJECT_CHARTER.md`.
- Identify any data model ideas missing from `DATA_MODEL.md`.
- Identify any roadmap concepts missing from `ROADMAP.md`.
- Mark superseded imported governance language where root docs intentionally differ.

Expected output:

- Small root documentation updates
- No duplicate governance sources
