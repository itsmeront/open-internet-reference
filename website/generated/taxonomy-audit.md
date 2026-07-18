# Taxonomy Audit Report

Last updated: 2026-07-11 14:37 UTC

This report analyzes tag usage, identifies gaps, and surfaces potential duplicates.

## Summary

| Metric | Count |
|--------|-------|
| Tags declared in TAXONOMY.md | 51 |
| Tags used in content | 42 |
| Total tag applications | 849 |
| Orphan tags (declared but unused) | 22 |
| Undeclared tags (used but not in TAXONOMY.md) | 13 |
| Similar tag pairs (possible duplicates) | 0 |
| Content without tags | 0 |

## Tag Usage Frequency

| Tag | Uses | Status |
|-----|------|--------|
| `source` | 117 | ✓ |
| `digital-rights` | 107 | ✓ |
| `organization` | 71 | ✓ |
| `privacy` | 58 | ✓ |
| `open-source-software` | 53 | ✓ |
| `outreach` | 50 | ⚠️ undeclared |
| `first-amendment` | 49 | ✓ |
| `person` | 49 | ⚠️ undeclared |
| `internet-governance` | 39 | ✓ |
| `attorney` | 35 | ✓ |
| `cryptography` | 25 | ✓ |
| `internet-architecture` | 22 | ✓ |
| `speech-and-code` | 17 | ✓ |
| `copyright` | 17 | ✓ |
| `surveillance` | 13 | ✓ |
| `fourth-amendment` | 12 | ✓ |
| `civil-society` | 12 | ✓ |
| `case` | 11 | ✓ |
| `computer-crime` | 10 | ✓ |
| `intermediary-liability` | 9 | ✓ |
| `case-law` | 8 | ⚠️ undeclared |
| `safe-harbor` | 7 | ✓ |
| `network-protocols` | 7 | ✓ |
| `secure-messaging` | 6 | ✓ |
| `constitutional-law` | 5 | ✓ |
| `technology-law` | 4 | ⚠️ undeclared |
| `distributed-systems` | 4 | ✓ |
| `statute` | 4 | ✓ |
| `civil-liberties` | 3 | ⚠️ undeclared |
| `technical` | 3 | ⚠️ undeclared |
| `imported-source` | 3 | ⚠️ undeclared |
| `project-governance` | 3 | ⚠️ undeclared |
| `technical-standard` | 3 | ⚠️ undeclared |
| `export-control` | 2 | ✓ |
| `censorship-resistance` | 2 | ✓ |
| `peer-to-peer-networking` | 2 | ✓ |
| `distributed-hash-tables` | 2 | ✓ |
| `software-distribution` | 1 | ✓ |
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
- `software-publication`
- `technology`

**Action:** Either add content using these tags or remove them from TAXONOMY.md.

## Undeclared Tags

These tags are used in content but not listed in `TAXONOMY.md`:

| Tag | Used in |
|-----|---------|
| `academic` | `bibliography\academic\SRC-TOR-DESIGN-PAPER.md` |
| `academic-paper` | `bibliography\academic\SRC-KADEMLIA-PAPER.md` |
| `case-law` | `bibliography\legal\SRC-CARPENTER-GOVINFO.md`, `bibliography\legal\SRC-CARPENTER-LII.md`, `bibliography\legal\SRC-PERFECT10-V-CCBILL-JUSTIA.md` +5 more |
| `civil-liberties` | `knowledge\organizations\ORG-ACLU.md`, `bibliography\organizations\SRC-ACLU-CONTACT.md`, `bibliography\organizations\SRC-ACLU-HISTORY.md` |
| `example-tag` | `knowledge\_templates\knowledge-page.md` |
| `imported-source` | `bibliography\imported\SRC-OIR-BOOTSTRAP-PROMPT.md`, `bibliography\imported\SRC-OIR-PROJECT-CHARTER-DOCX.md`, `bibliography\imported\SRC-OIR-ROADMAP-DOCX.md` |
| `onion-routing` | `bibliography\academic\SRC-TOR-DESIGN-PAPER.md` |
| `outreach` | `knowledge\organizations\ORG-ACLU.md`, `knowledge\organizations\ORG-CDT.md`, `knowledge\organizations\ORG-COOLEY.md` +47 more |
| `person` | `knowledge\people\PERSON-ALAN-KAY.md`, `knowledge\people\PERSON-ANDREW-RUSSELL.md`, `knowledge\people\PERSON-BRUCE-SCHNEIER.md` +46 more |
| `project-governance` | `bibliography\imported\SRC-OIR-BOOTSTRAP-PROMPT.md`, `bibliography\imported\SRC-OIR-PROJECT-CHARTER-DOCX.md`, `bibliography\imported\SRC-OIR-ROADMAP-DOCX.md` |
| `technical` | `knowledge\technical\TOPIC-ONION-ROUTING.md`, `bibliography\technical\SRC-SIGNAL-DOUBLE-RATCHET.md`, `bibliography\technical\SRC-SIGNAL-X3DH.md` |
| `technical-standard` | `bibliography\technical\SRC-RFC-1034.md`, `bibliography\technical\SRC-RFC-8446.md`, `bibliography\technical\SRC-RFC-9293.md` |
| `technology-law` | `knowledge\legal\CASE-VAN-BUREN-V-US.md`, `knowledge\legal\TOPIC-COMPUTER-FRAUD.md`, `bibliography\legal\SRC-VAN-BUREN-GOVINFO.md` +1 more |

**Action:** Add these to TAXONOMY.md or replace with existing tags.
