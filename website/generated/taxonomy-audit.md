# Taxonomy Audit Report

Last updated: 2026-09-05 09:39 UTC

This report analyzes tag usage, identifies gaps, and surfaces potential duplicates.

## Summary

| Metric | Count |
|--------|-------|
| Tags declared in TAXONOMY.md | 56 |
| Tags used in content | 58 |
| Total tag applications | 1855 |
| Orphan tags (declared but unused) | 13 |
| Undeclared tags (used but not in TAXONOMY.md) | 15 |
| Similar tag pairs (possible duplicates) | 0 |
| Content without tags | 0 |

## Tag Usage Frequency

| Tag | Uses | Status |
|-----|------|--------|
| `source` | 264 | ✓ |
| `digital-rights` | 210 | ✓ |
| `case` | 121 | ✓ |
| `privacy` | 114 | ✓ |
| `copyright` | 99 | ✓ |
| `organization` | 91 | ✓ |
| `artificial-intelligence` | 88 | ✓ |
| `open-source-software` | 81 | ✓ |
| `first-amendment` | 80 | ✓ |
| `person` | 68 | ⚠️ undeclared |
| `outreach` | 56 | ⚠️ undeclared |
| `internet-governance` | 49 | ✓ |
| `attorney` | 41 | ✓ |
| `cryptography` | 33 | ✓ |
| `surveillance` | 32 | ✓ |
| `case-studies` | 28 | ✓ |
| `intermediary-liability` | 27 | ✓ |
| `censorship-resistance` | 26 | ✓ |
| `computer-crime` | 23 | ✓ |
| `fourth-amendment` | 23 | ✓ |
| `internet-architecture` | 22 | ✓ |
| `speech-and-code` | 21 | ✓ |
| `sanctions` | 19 | ✓ |
| `civil-society` | 19 | ✓ |
| `peer-to-peer-networking` | 17 | ✓ |
| `statute` | 16 | ✓ |
| `secure-messaging` | 15 | ✓ |
| `open-source-risk` | 14 | ✓ |
| `public-policy` | 14 | ✓ |
| `age-verification` | 14 | ✓ |
| `case-law` | 12 | ⚠️ undeclared |
| `safe-harbor` | 10 | ✓ |
| `technology` | 9 | ✓ |
| `historical-event` | 9 | ✓ |
| `developer-rights` | 8 | ✓ |
| `network-protocols` | 7 | ✓ |
| `border-search` | 7 | ⚠️ undeclared |
| `encryption-law` | 7 | ✓ |
| `tornado-cash` | 6 | ✓ |
| `export-control` | 6 | ✓ |
| `distributed-systems` | 5 | ✓ |
| `constitutional-law` | 5 | ✓ |
| `content-moderation` | 4 | ✓ |
| `technology-law` | 4 | ⚠️ undeclared |
| `privacy-preserving-systems` | 3 | ✓ |
| `technical` | 3 | ⚠️ undeclared |
| `civil-liberties` | 3 | ⚠️ undeclared |
| `researcher` | 3 | ✓ |
| `technical-standard` | 3 | ⚠️ undeclared |
| `academic-paper` | 3 | ⚠️ undeclared |
| `imported-source` | 3 | ⚠️ undeclared |
| `project-governance` | 3 | ⚠️ undeclared |
| `distributed-hash-tables` | 2 | ✓ |
| `example-tag` | 1 | ⚠️ undeclared |
| `software-distribution` | 1 | ✓ |
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
- `regulation`
- `routing`
- `software-publication`

**Action:** Either add content using these tags or remove them from TAXONOMY.md.

## Undeclared Tags

These tags are used in content but not listed in `TAXONOMY.md`:

| Tag | Used in |
|-----|---------|
| `academic` | `bibliography/academic/SRC-TOR-DESIGN-PAPER.md` |
| `academic-paper` | `bibliography/academic/SRC-KADEMLIA-PAPER.md`, `bibliography/academic/SRC-CLARKE-DDISRS-1999.md`, `bibliography/academic/SRC-CLARKE-FREENET-PAPER-2001.md` |
| `border-search` | `knowledge/technical/TECH-GRAPHENEOS.md`, `knowledge/legal/STAT-18-USC-2232.md`, `knowledge/legal/CASE-US-V-TUNICK.md` +4 more |
| `case-law` | `bibliography/legal/SRC-CHATRIE-SCOTUS-PDF.md`, `bibliography/legal/SRC-VAN-BUREN-LII.md`, `bibliography/legal/SRC-VAN-BUREN-GOVINFO.md` +9 more |
| `civil-liberties` | `knowledge/organizations/ORG-ACLU.md`, `bibliography/organizations/SRC-ACLU-HISTORY.md`, `bibliography/organizations/SRC-ACLU-CONTACT.md` |
| `commentary` | `bibliography/legal/SRC-HILL-MARLOW-REVERSE-WARRANTS-2026.md` |
| `example-tag` | `knowledge/_templates/knowledge-page.md` |
| `imported-source` | `bibliography/imported/SRC-OIR-PROJECT-CHARTER-DOCX.md`, `bibliography/imported/SRC-OIR-BOOTSTRAP-PROMPT.md`, `bibliography/imported/SRC-OIR-ROADMAP-DOCX.md` |
| `onion-routing` | `bibliography/academic/SRC-TOR-DESIGN-PAPER.md` |
| `outreach` | `knowledge/organizations/ORG-RCFP.md`, `knowledge/organizations/ORG-SFLC.md`, `knowledge/organizations/ORG-KNIGHT-FIRST-AMENDMENT.md` +53 more |
| `person` | `knowledge/people/PERSON-BRUCE-SCHNEIER.md`, `knowledge/people/PERSON-PAUL-VIXIE.md`, `knowledge/people/PERSON-MIKE-LEE.md` +65 more |
| `project-governance` | `bibliography/imported/SRC-OIR-PROJECT-CHARTER-DOCX.md`, `bibliography/imported/SRC-OIR-BOOTSTRAP-PROMPT.md`, `bibliography/imported/SRC-OIR-ROADMAP-DOCX.md` |
| `technical` | `knowledge/technical/TOPIC-ONION-ROUTING.md`, `bibliography/technical/SRC-SIGNAL-DOUBLE-RATCHET.md`, `bibliography/technical/SRC-SIGNAL-X3DH.md` |
| `technical-standard` | `bibliography/technical/SRC-RFC-8446.md`, `bibliography/technical/SRC-RFC-9293.md`, `bibliography/technical/SRC-RFC-1034.md` |
| `technology-law` | `knowledge/legal/TOPIC-COMPUTER-FRAUD.md`, `knowledge/legal/CASE-VAN-BUREN-V-US.md`, `bibliography/legal/SRC-VAN-BUREN-LII.md` +1 more |

**Action:** Add these to TAXONOMY.md or replace with existing tags.
