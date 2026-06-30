# Taxonomy Audit Report

Last updated: 2026-06-30 08:57 UTC

This report analyzes tag usage, identifies gaps, and surfaces potential duplicates.

## Summary

| Metric | Count |
|--------|-------|
| Tags declared in TAXONOMY.md | 51 |
| Tags used in content | 41 |
| Total tag applications | 601 |
| Orphan tags (declared but unused) | 23 |
| Undeclared tags (used but not in TAXONOMY.md) | 13 |
| Similar tag pairs (possible duplicates) | 0 |
| Content without tags | 0 |

## Tag Usage Frequency

| Tag | Uses | Status |
|-----|------|--------|
| `source` | 84 | ✓ |
| `digital-rights` | 76 | ✓ |
| `organization` | 56 | ✓ |
| `open-source-software` | 42 | ✓ |
| `outreach` | 39 | ⚠️ undeclared |
| `privacy` | 36 | ✓ |
| `first-amendment` | 31 | ✓ |
| `internet-governance` | 23 | ✓ |
| `person` | 19 | ⚠️ undeclared |
| `cryptography` | 18 | ✓ |
| `copyright` | 17 | ✓ |
| `speech-and-code` | 17 | ✓ |
| `attorney` | 15 | ✓ |
| `computer-crime` | 10 | ✓ |
| `fourth-amendment` | 10 | ✓ |
| `surveillance` | 10 | ✓ |
| `case` | 10 | ✓ |
| `intermediary-liability` | 9 | ✓ |
| `civil-society` | 8 | ✓ |
| `case-law` | 8 | ⚠️ undeclared |
| `safe-harbor` | 7 | ✓ |
| `secure-messaging` | 6 | ✓ |
| `constitutional-law` | 5 | ✓ |
| `technology-law` | 4 | ⚠️ undeclared |
| `internet-architecture` | 4 | ✓ |
| `network-protocols` | 4 | ✓ |
| `statute` | 4 | ✓ |
| `technical` | 3 | ⚠️ undeclared |
| `civil-liberties` | 3 | ⚠️ undeclared |
| `technical-standard` | 3 | ⚠️ undeclared |
| `imported-source` | 3 | ⚠️ undeclared |
| `project-governance` | 3 | ⚠️ undeclared |
| `export-control` | 2 | ✓ |
| `censorship-resistance` | 2 | ✓ |
| `peer-to-peer-networking` | 2 | ✓ |
| `distributed-systems` | 2 | ✓ |
| `distributed-hash-tables` | 2 | ✓ |
| `example-tag` | 1 | ⚠️ undeclared |
| `academic-paper` | 1 | ⚠️ undeclared |
| `academic` | 1 | ⚠️ undeclared |
| `onion-routing` | 1 | ⚠️ undeclared |

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
- `software-distribution`
- `software-publication`
- `technology`

**Action:** Either add content using these tags or remove them from TAXONOMY.md.

## Undeclared Tags

These tags are used in content but not listed in `TAXONOMY.md`:

| Tag | Used in |
|-----|---------|
| `academic` | `bibliography/academic/SRC-TOR-DESIGN-PAPER.md` |
| `academic-paper` | `bibliography/academic/SRC-KADEMLIA-PAPER.md` |
| `case-law` | `bibliography/legal/SRC-RENO-V-ACLU-JUSTIA.md`, `bibliography/legal/SRC-PERFECT10-V-CCBILL-JUSTIA.md`, `bibliography/legal/SRC-VAN-BUREN-GOVINFO.md` +5 more |
| `civil-liberties` | `knowledge/organizations/ORG-ACLU.md`, `bibliography/organizations/SRC-ACLU-HISTORY.md`, `bibliography/organizations/SRC-ACLU-CONTACT.md` |
| `example-tag` | `knowledge/_templates/knowledge-page.md` |
| `imported-source` | `bibliography/imported/SRC-OIR-BOOTSTRAP-PROMPT.md`, `bibliography/imported/SRC-OIR-PROJECT-CHARTER-DOCX.md`, `bibliography/imported/SRC-OIR-ROADMAP-DOCX.md` |
| `onion-routing` | `bibliography/academic/SRC-TOR-DESIGN-PAPER.md` |
| `outreach` | `knowledge/organizations/ORG-TOR-PROJECT.md`, `knowledge/organizations/ORG-EFF.md`, `knowledge/organizations/ORG-FENWICK.md` +36 more |
| `person` | `knowledge/people/PERSON-LAWRENCE-LESSIG.md`, `knowledge/people/PERSON-MATT-BLAZE.md`, `knowledge/people/PERSON-RAND-PAUL.md` +16 more |
| `project-governance` | `bibliography/imported/SRC-OIR-BOOTSTRAP-PROMPT.md`, `bibliography/imported/SRC-OIR-PROJECT-CHARTER-DOCX.md`, `bibliography/imported/SRC-OIR-ROADMAP-DOCX.md` |
| `technical` | `knowledge/technical/TOPIC-ONION-ROUTING.md`, `bibliography/technical/SRC-SIGNAL-DOUBLE-RATCHET.md`, `bibliography/technical/SRC-SIGNAL-X3DH.md` |
| `technical-standard` | `bibliography/technical/SRC-RFC-1034.md`, `bibliography/technical/SRC-RFC-9293.md`, `bibliography/technical/SRC-RFC-8446.md` |
| `technology-law` | `knowledge/legal/CASE-VAN-BUREN-V-US.md`, `knowledge/legal/TOPIC-COMPUTER-FRAUD.md`, `bibliography/legal/SRC-VAN-BUREN-GOVINFO.md` +1 more |

**Action:** Add these to TAXONOMY.md or replace with existing tags.
