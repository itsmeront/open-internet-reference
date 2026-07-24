# Taxonomy Audit Report

Last updated: 2026-07-24 08:08 UTC

This report analyzes tag usage, identifies gaps, and surfaces potential duplicates.

## Summary

| Metric | Count |
|--------|-------|
| Tags declared in TAXONOMY.md | 53 |
| Tags used in content | 50 |
| Total tag applications | 1136 |
| Orphan tags (declared but unused) | 16 |
| Undeclared tags (used but not in TAXONOMY.md) | 13 |
| Similar tag pairs (possible duplicates) | 0 |
| Content without tags | 0 |

## Tag Usage Frequency

| Tag | Uses | Status |
|-----|------|--------|
| `source` | 162 | ✓ |
| `digital-rights` | 136 | ✓ |
| `organization` | 78 | ✓ |
| `privacy` | 74 | ✓ |
| `person` | 64 | ⚠️ undeclared |
| `open-source-software` | 62 | ✓ |
| `first-amendment` | 58 | ✓ |
| `outreach` | 53 | ⚠️ undeclared |
| `internet-governance` | 45 | ✓ |
| `attorney` | 35 | ✓ |
| `copyright` | 31 | ✓ |
| `case` | 30 | ✓ |
| `cryptography` | 29 | ✓ |
| `surveillance` | 24 | ✓ |
| `internet-architecture` | 22 | ✓ |
| `computer-crime` | 22 | ✓ |
| `speech-and-code` | 20 | ✓ |
| `sanctions` | 19 | ✓ |
| `fourth-amendment` | 15 | ✓ |
| `civil-society` | 15 | ✓ |
| `open-source-risk` | 13 | ✓ |
| `case-studies` | 11 | ✓ |
| `safe-harbor` | 10 | ✓ |
| `intermediary-liability` | 10 | ✓ |
| `case-law` | 10 | ⚠️ undeclared |
| `statute` | 9 | ✓ |
| `network-protocols` | 7 | ✓ |
| `developer-rights` | 7 | ✓ |
| `censorship-resistance` | 6 | ✓ |
| `tornado-cash` | 6 | ✓ |
| `secure-messaging` | 6 | ✓ |
| `constitutional-law` | 5 | ✓ |
| `export-control` | 5 | ✓ |
| `distributed-systems` | 4 | ✓ |
| `technology-law` | 4 | ⚠️ undeclared |
| `technical` | 3 | ⚠️ undeclared |
| `civil-liberties` | 3 | ⚠️ undeclared |
| `technical-standard` | 3 | ⚠️ undeclared |
| `imported-source` | 3 | ⚠️ undeclared |
| `project-governance` | 3 | ⚠️ undeclared |
| `peer-to-peer-networking` | 2 | ✓ |
| `distributed-hash-tables` | 2 | ✓ |
| `privacy-preserving-systems` | 2 | ✓ |
| `historical-event` | 2 | ✓ |
| `example-tag` | 1 | ⚠️ undeclared |
| `technology` | 1 | ✓ |
| `software-distribution` | 1 | ✓ |
| `academic` | 1 | ⚠️ undeclared |
| `onion-routing` | 1 | ⚠️ undeclared |
| `academic-paper` | 1 | ⚠️ undeclared |

## Orphan Tags

These tags are declared in `TAXONOMY.md` but never used in any content:

- `axona`
- `consensus`
- `content-addressing`
- `court`
- `cryptographic-signatures`
- `due-process`
- `encryption-law`
- `key-management`
- `paper`
- `prior-restraint`
- `protocol`
- `public-policy`
- `regulation`
- `researcher`
- `routing`
- `software-publication`

**Action:** Either add content using these tags or remove them from TAXONOMY.md.

## Undeclared Tags

These tags are used in content but not listed in `TAXONOMY.md`:

| Tag | Used in |
|-----|---------|
| `academic` | `bibliography/academic/SRC-TOR-DESIGN-PAPER.md` |
| `academic-paper` | `bibliography/academic/SRC-KADEMLIA-PAPER.md` |
| `case-law` | `bibliography/legal/SRC-BROWN-V-EMA-GOVINFO.md`, `bibliography/legal/SRC-RENO-V-ACLU-LOC.md`, `bibliography/legal/SRC-RENO-V-ACLU-JUSTIA.md` +7 more |
| `civil-liberties` | `knowledge/organizations/ORG-ACLU.md`, `bibliography/organizations/SRC-ACLU-HISTORY.md`, `bibliography/organizations/SRC-ACLU-CONTACT.md` |
| `example-tag` | `knowledge/_templates/knowledge-page.md` |
| `imported-source` | `bibliography/imported/SRC-OIR-BOOTSTRAP-PROMPT.md`, `bibliography/imported/SRC-OIR-PROJECT-CHARTER-DOCX.md`, `bibliography/imported/SRC-OIR-ROADMAP-DOCX.md` |
| `onion-routing` | `bibliography/academic/SRC-TOR-DESIGN-PAPER.md` |
| `outreach` | `knowledge/organizations/ORG-SFLC.md`, `knowledge/organizations/ORG-COOLEY.md`, `knowledge/organizations/ORG-ACLU.md` +50 more |
| `person` | `knowledge/people/PERSON-THOMAS-MASSIE.md`, `knowledge/people/PERSON-RON-WYDEN.md`, `knowledge/people/PERSON-BRUCE-SCHNEIER.md` +61 more |
| `project-governance` | `bibliography/imported/SRC-OIR-BOOTSTRAP-PROMPT.md`, `bibliography/imported/SRC-OIR-PROJECT-CHARTER-DOCX.md`, `bibliography/imported/SRC-OIR-ROADMAP-DOCX.md` |
| `technical` | `knowledge/technical/TOPIC-ONION-ROUTING.md`, `bibliography/technical/SRC-SIGNAL-DOUBLE-RATCHET.md`, `bibliography/technical/SRC-SIGNAL-X3DH.md` |
| `technical-standard` | `bibliography/technical/SRC-RFC-1034.md`, `bibliography/technical/SRC-RFC-9293.md`, `bibliography/technical/SRC-RFC-8446.md` |
| `technology-law` | `knowledge/legal/TOPIC-COMPUTER-FRAUD.md`, `knowledge/legal/CASE-VAN-BUREN-V-US.md`, `bibliography/legal/SRC-VAN-BUREN-LII.md` +1 more |

**Action:** Add these to TAXONOMY.md or replace with existing tags.
