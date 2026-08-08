# Taxonomy Audit Report

Last updated: 2026-08-08 13:45 UTC

This report analyzes tag usage, identifies gaps, and surfaces potential duplicates.

## Summary

| Metric | Count |
|--------|-------|
| Tags declared in TAXONOMY.md | 54 |
| Tags used in content | 55 |
| Total tag applications | 1400 |
| Orphan tags (declared but unused) | 14 |
| Undeclared tags (used but not in TAXONOMY.md) | 15 |
| Similar tag pairs (possible duplicates) | 0 |
| Content without tags | 0 |

## Tag Usage Frequency

| Tag | Uses | Status |
|-----|------|--------|
| `source` | 198 | ✓ |
| `digital-rights` | 160 | ✓ |
| `privacy` | 107 | ✓ |
| `organization` | 91 | ✓ |
| `open-source-software` | 76 | ✓ |
| `person` | 68 | ⚠️ undeclared |
| `first-amendment` | 62 | ✓ |
| `outreach` | 56 | ⚠️ undeclared |
| `internet-governance` | 45 | ✓ |
| `attorney` | 41 | ✓ |
| `case` | 36 | ✓ |
| `copyright` | 32 | ✓ |
| `cryptography` | 31 | ✓ |
| `surveillance` | 31 | ✓ |
| `censorship-resistance` | 26 | ✓ |
| `fourth-amendment` | 22 | ✓ |
| `computer-crime` | 22 | ✓ |
| `internet-architecture` | 22 | ✓ |
| `speech-and-code` | 20 | ✓ |
| `case-studies` | 20 | ✓ |
| `sanctions` | 19 | ✓ |
| `civil-society` | 19 | ✓ |
| `intermediary-liability` | 18 | ✓ |
| `peer-to-peer-networking` | 17 | ✓ |
| `secure-messaging` | 14 | ✓ |
| `open-source-risk` | 13 | ✓ |
| `case-law` | 12 | ⚠️ undeclared |
| `statute` | 11 | ✓ |
| `safe-harbor` | 10 | ✓ |
| `historical-event` | 9 | ✓ |
| `developer-rights` | 7 | ✓ |
| `network-protocols` | 7 | ✓ |
| `technology` | 7 | ✓ |
| `tornado-cash` | 6 | ✓ |
| `border-search` | 6 | ⚠️ undeclared |
| `encryption-law` | 6 | ✓ |
| `export-control` | 5 | ✓ |
| `constitutional-law` | 5 | ✓ |
| `distributed-systems` | 5 | ✓ |
| `technology-law` | 4 | ⚠️ undeclared |
| `content-moderation` | 4 | ✓ |
| `civil-liberties` | 3 | ⚠️ undeclared |
| `researcher` | 3 | ✓ |
| `technical` | 3 | ⚠️ undeclared |
| `academic-paper` | 3 | ⚠️ undeclared |
| `imported-source` | 3 | ⚠️ undeclared |
| `project-governance` | 3 | ⚠️ undeclared |
| `technical-standard` | 3 | ⚠️ undeclared |
| `privacy-preserving-systems` | 2 | ✓ |
| `distributed-hash-tables` | 2 | ✓ |
| `software-distribution` | 1 | ✓ |
| `example-tag` | 1 | ⚠️ undeclared |
| `academic` | 1 | ⚠️ undeclared |
| `onion-routing` | 1 | ⚠️ undeclared |
| `commentary` | 1 | ⚠️ undeclared |

## Orphan Tags

These tags are declared in `TAXONOMY.md` but never used in any content:

- `axona`
- `consensus`
- `content-addressing`
- `court`
- `cryptographic-signatures`
- `due-process`
- `key-management`
- `paper`
- `prior-restraint`
- `protocol`
- `public-policy`
- `regulation`
- `routing`
- `software-publication`

**Action:** Either add content using these tags or remove them from TAXONOMY.md.

## Undeclared Tags

These tags are used in content but not listed in `TAXONOMY.md`:

| Tag | Used in |
|-----|---------|
| `academic` | `bibliography\academic\SRC-TOR-DESIGN-PAPER.md` |
| `academic-paper` | `bibliography\academic\SRC-CLARKE-DDISRS-1999.md`, `bibliography\academic\SRC-CLARKE-FREENET-PAPER-2001.md`, `bibliography\academic\SRC-KADEMLIA-PAPER.md` |
| `border-search` | `knowledge\legal\CASE-US-V-TUNICK.md`, `knowledge\legal\STAT-18-USC-2232.md`, `knowledge\technical\TECH-GRAPHENEOS.md` +3 more |
| `case-law` | `bibliography\legal\SRC-BROWN-V-EMA-GOVINFO.md`, `bibliography\legal\SRC-CARPENTER-GOVINFO.md`, `bibliography\legal\SRC-CARPENTER-LII.md` +9 more |
| `civil-liberties` | `knowledge\organizations\ORG-ACLU.md`, `bibliography\organizations\SRC-ACLU-CONTACT.md`, `bibliography\organizations\SRC-ACLU-HISTORY.md` |
| `commentary` | `bibliography\legal\SRC-HILL-MARLOW-REVERSE-WARRANTS-2026.md` |
| `example-tag` | `knowledge\_templates\knowledge-page.md` |
| `imported-source` | `bibliography\imported\SRC-OIR-BOOTSTRAP-PROMPT.md`, `bibliography\imported\SRC-OIR-PROJECT-CHARTER-DOCX.md`, `bibliography\imported\SRC-OIR-ROADMAP-DOCX.md` |
| `onion-routing` | `bibliography\academic\SRC-TOR-DESIGN-PAPER.md` |
| `outreach` | `knowledge\organizations\ORG-ACLU.md`, `knowledge\organizations\ORG-CDT.md`, `knowledge\organizations\ORG-COMMITTEE-FOR-THE-FIRST-AMENDMENT.md` +53 more |
| `person` | `knowledge\people\PERSON-ALAN-KAY.md`, `knowledge\people\PERSON-ANDREW-RUSSELL.md`, `knowledge\people\PERSON-BRUCE-SCHNEIER.md` +65 more |
| `project-governance` | `bibliography\imported\SRC-OIR-BOOTSTRAP-PROMPT.md`, `bibliography\imported\SRC-OIR-PROJECT-CHARTER-DOCX.md`, `bibliography\imported\SRC-OIR-ROADMAP-DOCX.md` |
| `technical` | `knowledge\technical\TOPIC-ONION-ROUTING.md`, `bibliography\technical\SRC-SIGNAL-DOUBLE-RATCHET.md`, `bibliography\technical\SRC-SIGNAL-X3DH.md` |
| `technical-standard` | `bibliography\technical\SRC-RFC-1034.md`, `bibliography\technical\SRC-RFC-8446.md`, `bibliography\technical\SRC-RFC-9293.md` |
| `technology-law` | `knowledge\legal\CASE-VAN-BUREN-V-US.md`, `knowledge\legal\TOPIC-COMPUTER-FRAUD.md`, `bibliography\legal\SRC-VAN-BUREN-GOVINFO.md` +1 more |

**Action:** Add these to TAXONOMY.md or replace with existing tags.
