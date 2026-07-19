# Taxonomy Audit Report

Last updated: 2026-07-19 07:59 UTC

This report analyzes tag usage, identifies gaps, and surfaces potential duplicates.

## Summary

| Metric | Count |
|--------|-------|
| Tags declared in TAXONOMY.md | 51 |
| Tags used in content | 42 |
| Total tag applications | 925 |
| Orphan tags (declared but unused) | 22 |
| Undeclared tags (used but not in TAXONOMY.md) | 13 |
| Similar tag pairs (possible duplicates) | 0 |
| Content without tags | 0 |

## Tag Usage Frequency

| Tag | Uses | Status |
|-----|------|--------|
| `source` | 128 | ✓ |
| `digital-rights` | 118 | ✓ |
| `organization` | 75 | ✓ |
| `privacy` | 69 | ✓ |
| `person` | 62 | ⚠️ undeclared |
| `first-amendment` | 56 | ✓ |
| `open-source-software` | 53 | ✓ |
| `outreach` | 51 | ⚠️ undeclared |
| `internet-governance` | 43 | ✓ |
| `attorney` | 35 | ✓ |
| `cryptography` | 25 | ✓ |
| `internet-architecture` | 22 | ✓ |
| `surveillance` | 22 | ✓ |
| `copyright` | 17 | ✓ |
| `speech-and-code` | 17 | ✓ |
| `civil-society` | 15 | ✓ |
| `fourth-amendment` | 14 | ✓ |
| `case` | 11 | ✓ |
| `computer-crime` | 10 | ✓ |
| `intermediary-liability` | 9 | ✓ |
| `case-law` | 8 | ⚠️ undeclared |
| `network-protocols` | 7 | ✓ |
| `safe-harbor` | 7 | ✓ |
| `secure-messaging` | 6 | ✓ |
| `constitutional-law` | 5 | ✓ |
| `distributed-systems` | 4 | ✓ |
| `technology-law` | 4 | ⚠️ undeclared |
| `statute` | 4 | ✓ |
| `technical` | 3 | ⚠️ undeclared |
| `civil-liberties` | 3 | ⚠️ undeclared |
| `technical-standard` | 3 | ⚠️ undeclared |
| `imported-source` | 3 | ⚠️ undeclared |
| `project-governance` | 3 | ⚠️ undeclared |
| `censorship-resistance` | 2 | ✓ |
| `peer-to-peer-networking` | 2 | ✓ |
| `distributed-hash-tables` | 2 | ✓ |
| `export-control` | 2 | ✓ |
| `example-tag` | 1 | ⚠️ undeclared |
| `software-distribution` | 1 | ✓ |
| `academic` | 1 | ⚠️ undeclared |
| `onion-routing` | 1 | ⚠️ undeclared |
| `academic-paper` | 1 | ⚠️ undeclared |

## Orphan Tags

These tags are declared in `TAXONOMY.md` but never used in any content:

- `axona`
- `case-studies`
- `consensus`
- `content-addressing`
- `court`
- `cryptographic-signatures`
- `developer-rights`
- `due-process`
- `encryption-law`
- `historical-event`
- `key-management`
- `open-source-risk`
- `paper`
- `prior-restraint`
- `privacy-preserving-systems`
- `protocol`
- `public-policy`
- `regulation`
- `researcher`
- `routing`
- `software-publication`
- `technology`

**Action:** Either add content using these tags or remove them from TAXONOMY.md.

## Undeclared Tags

These tags are used in content but not listed in `TAXONOMY.md`:

| Tag | Used in |
|-----|---------|
| `academic` | `bibliography/academic/SRC-TOR-DESIGN-PAPER.md` |
| `academic-paper` | `bibliography/academic/SRC-KADEMLIA-PAPER.md` |
| `case-law` | `bibliography/legal/SRC-RENO-V-ACLU-LOC.md`, `bibliography/legal/SRC-RENO-V-ACLU-JUSTIA.md`, `bibliography/legal/SRC-CARPENTER-GOVINFO.md` +5 more |
| `civil-liberties` | `knowledge/organizations/ORG-ACLU.md`, `bibliography/organizations/SRC-ACLU-HISTORY.md`, `bibliography/organizations/SRC-ACLU-CONTACT.md` |
| `example-tag` | `knowledge/_templates/knowledge-page.md` |
| `imported-source` | `bibliography/imported/SRC-OIR-BOOTSTRAP-PROMPT.md`, `bibliography/imported/SRC-OIR-PROJECT-CHARTER-DOCX.md`, `bibliography/imported/SRC-OIR-ROADMAP-DOCX.md` |
| `onion-routing` | `bibliography/academic/SRC-TOR-DESIGN-PAPER.md` |
| `outreach` | `knowledge/organizations/ORG-SFLC.md`, `knowledge/organizations/ORG-COOLEY.md`, `knowledge/organizations/ORG-ACLU.md` +48 more |
| `person` | `knowledge/people/PERSON-THOMAS-MASSIE.md`, `knowledge/people/PERSON-RON-WYDEN.md`, `knowledge/people/PERSON-BRUCE-SCHNEIER.md` +59 more |
| `project-governance` | `bibliography/imported/SRC-OIR-BOOTSTRAP-PROMPT.md`, `bibliography/imported/SRC-OIR-PROJECT-CHARTER-DOCX.md`, `bibliography/imported/SRC-OIR-ROADMAP-DOCX.md` |
| `technical` | `knowledge/technical/TOPIC-ONION-ROUTING.md`, `bibliography/technical/SRC-SIGNAL-DOUBLE-RATCHET.md`, `bibliography/technical/SRC-SIGNAL-X3DH.md` |
| `technical-standard` | `bibliography/technical/SRC-RFC-1034.md`, `bibliography/technical/SRC-RFC-9293.md`, `bibliography/technical/SRC-RFC-8446.md` |
| `technology-law` | `knowledge/legal/TOPIC-COMPUTER-FRAUD.md`, `knowledge/legal/CASE-VAN-BUREN-V-US.md`, `bibliography/legal/SRC-VAN-BUREN-LII.md` +1 more |

**Action:** Add these to TAXONOMY.md or replace with existing tags.
