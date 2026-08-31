# Taxonomy Audit Report

Last updated: 2026-08-31 12:10 UTC

This report analyzes tag usage, identifies gaps, and surfaces potential duplicates.

## Summary

| Metric | Count |
|--------|-------|
| Tags declared in TAXONOMY.md | 56 |
| Tags used in content | 58 |
| Total tag applications | 1655 |
| Orphan tags (declared but unused) | 13 |
| Undeclared tags (used but not in TAXONOMY.md) | 15 |
| Similar tag pairs (possible duplicates) | 0 |
| Content without tags | 0 |

## Tag Usage Frequency

| Tag | Uses | Status |
|-----|------|--------|
| `source` | 233 | ✓ |
| `digital-rights` | 187 | ✓ |
| `privacy` | 114 | ✓ |
| `organization` | 91 | ✓ |
| `open-source-software` | 78 | ✓ |
| `first-amendment` | 75 | ✓ |
| `case` | 74 | ✓ |
| `copyright` | 68 | ✓ |
| `person` | 68 | ⚠️ undeclared |
| `outreach` | 56 | ⚠️ undeclared |
| `internet-governance` | 49 | ✓ |
| `attorney` | 41 | ✓ |
| `artificial-intelligence` | 40 | ✓ |
| `cryptography` | 33 | ✓ |
| `surveillance` | 32 | ✓ |
| `case-studies` | 27 | ✓ |
| `censorship-resistance` | 26 | ✓ |
| `fourth-amendment` | 23 | ✓ |
| `computer-crime` | 23 | ✓ |
| `internet-architecture` | 22 | ✓ |
| `speech-and-code` | 21 | ✓ |
| `intermediary-liability` | 20 | ✓ |
| `sanctions` | 19 | ✓ |
| `civil-society` | 19 | ✓ |
| `peer-to-peer-networking` | 17 | ✓ |
| `statute` | 16 | ✓ |
| `secure-messaging` | 15 | ✓ |
| `open-source-risk` | 14 | ✓ |
| `age-verification` | 14 | ✓ |
| `case-law` | 12 | ⚠️ undeclared |
| `public-policy` | 10 | ✓ |
| `safe-harbor` | 10 | ✓ |
| `historical-event` | 9 | ✓ |
| `technology` | 9 | ✓ |
| `developer-rights` | 8 | ✓ |
| `border-search` | 7 | ⚠️ undeclared |
| `encryption-law` | 7 | ✓ |
| `network-protocols` | 7 | ✓ |
| `tornado-cash` | 6 | ✓ |
| `export-control` | 6 | ✓ |
| `constitutional-law` | 5 | ✓ |
| `distributed-systems` | 5 | ✓ |
| `technology-law` | 4 | ⚠️ undeclared |
| `content-moderation` | 4 | ✓ |
| `privacy-preserving-systems` | 3 | ✓ |
| `civil-liberties` | 3 | ⚠️ undeclared |
| `researcher` | 3 | ✓ |
| `technical` | 3 | ⚠️ undeclared |
| `imported-source` | 3 | ⚠️ undeclared |
| `project-governance` | 3 | ⚠️ undeclared |
| `technical-standard` | 3 | ⚠️ undeclared |
| `academic-paper` | 3 | ⚠️ undeclared |
| `distributed-hash-tables` | 2 | ✓ |
| `software-distribution` | 1 | ✓ |
| `example-tag` | 1 | ⚠️ undeclared |
| `commentary` | 1 | ⚠️ undeclared |
| `academic` | 1 | ⚠️ undeclared |
| `onion-routing` | 1 | ⚠️ undeclared |

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
- `regulation`
- `routing`
- `software-publication`

**Action:** Either add content using these tags or remove them from TAXONOMY.md.

## Undeclared Tags

These tags are used in content but not listed in `TAXONOMY.md`:

| Tag | Used in |
|-----|---------|
| `academic` | `bibliography/academic/SRC-TOR-DESIGN-PAPER.md` |
| `academic-paper` | `bibliography/academic/SRC-CLARKE-DDISRS-1999.md`, `bibliography/academic/SRC-CLARKE-FREENET-PAPER-2001.md`, `bibliography/academic/SRC-KADEMLIA-PAPER.md` |
| `border-search` | `knowledge/legal/STAT-18-USC-2232.md`, `knowledge/legal/TOPIC-DEVICE-SEARCH.md`, `knowledge/legal/CASE-US-V-TUNICK.md` +4 more |
| `case-law` | `bibliography/legal/SRC-VAN-BUREN-GOVINFO.md`, `bibliography/legal/SRC-RENO-V-ACLU-JUSTIA.md`, `bibliography/legal/SRC-CARPENTER-LII.md` +9 more |
| `civil-liberties` | `knowledge/organizations/ORG-ACLU.md`, `bibliography/organizations/SRC-ACLU-HISTORY.md`, `bibliography/organizations/SRC-ACLU-CONTACT.md` |
| `commentary` | `bibliography/legal/SRC-HILL-MARLOW-REVERSE-WARRANTS-2026.md` |
| `example-tag` | `knowledge/_templates/knowledge-page.md` |
| `imported-source` | `bibliography/imported/SRC-OIR-ROADMAP-DOCX.md`, `bibliography/imported/SRC-OIR-PROJECT-CHARTER-DOCX.md`, `bibliography/imported/SRC-OIR-BOOTSTRAP-PROMPT.md` |
| `onion-routing` | `bibliography/academic/SRC-TOR-DESIGN-PAPER.md` |
| `outreach` | `knowledge/organizations/ORG-EFF.md`, `knowledge/organizations/ORG-OSI.md`, `knowledge/organizations/ORG-PUBLIC-KNOWLEDGE.md` +53 more |
| `person` | `knowledge/people/PERSON-RON-WYDEN.md`, `knowledge/people/PERSON-ROBERT-KAHN.md`, `knowledge/people/PERSON-TIM-BERNERS-LEE.md` +65 more |
| `project-governance` | `bibliography/imported/SRC-OIR-ROADMAP-DOCX.md`, `bibliography/imported/SRC-OIR-PROJECT-CHARTER-DOCX.md`, `bibliography/imported/SRC-OIR-BOOTSTRAP-PROMPT.md` |
| `technical` | `knowledge/technical/TOPIC-ONION-ROUTING.md`, `bibliography/technical/SRC-SIGNAL-DOUBLE-RATCHET.md`, `bibliography/technical/SRC-SIGNAL-X3DH.md` |
| `technical-standard` | `bibliography/technical/SRC-RFC-9293.md`, `bibliography/technical/SRC-RFC-1034.md`, `bibliography/technical/SRC-RFC-8446.md` |
| `technology-law` | `knowledge/legal/CASE-VAN-BUREN-V-US.md`, `knowledge/legal/TOPIC-COMPUTER-FRAUD.md`, `bibliography/legal/SRC-VAN-BUREN-GOVINFO.md` +1 more |

**Action:** Add these to TAXONOMY.md or replace with existing tags.
