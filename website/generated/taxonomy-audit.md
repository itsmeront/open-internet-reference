# Taxonomy Audit Report

Last updated: 2026-07-29 08:20 UTC

This report analyzes tag usage, identifies gaps, and surfaces potential duplicates.

## Summary

| Metric | Count |
|--------|-------|
| Tags declared in TAXONOMY.md | 53 |
| Tags used in content | 51 |
| Total tag applications | 1182 |
| Orphan tags (declared but unused) | 16 |
| Undeclared tags (used but not in TAXONOMY.md) | 14 |
| Similar tag pairs (possible duplicates) | 0 |
| Content without tags | 0 |

## Tag Usage Frequency

| Tag | Uses | Status |
|-----|------|--------|
| `source` | 169 | ✓ |
| `digital-rights` | 139 | ✓ |
| `privacy` | 82 | ✓ |
| `organization` | 78 | ✓ |
| `open-source-software` | 69 | ✓ |
| `person` | 64 | ⚠️ undeclared |
| `first-amendment` | 58 | ✓ |
| `outreach` | 53 | ⚠️ undeclared |
| `internet-governance` | 45 | ✓ |
| `case` | 36 | ✓ |
| `attorney` | 35 | ✓ |
| `copyright` | 32 | ✓ |
| `cryptography` | 31 | ✓ |
| `surveillance` | 24 | ✓ |
| `computer-crime` | 22 | ✓ |
| `internet-architecture` | 22 | ✓ |
| `speech-and-code` | 20 | ✓ |
| `sanctions` | 19 | ✓ |
| `fourth-amendment` | 17 | ✓ |
| `civil-society` | 15 | ✓ |
| `open-source-risk` | 13 | ✓ |
| `case-studies` | 12 | ✓ |
| `statute` | 11 | ✓ |
| `safe-harbor` | 10 | ✓ |
| `intermediary-liability` | 10 | ✓ |
| `case-law` | 10 | ⚠️ undeclared |
| `developer-rights` | 7 | ✓ |
| `network-protocols` | 7 | ✓ |
| `tornado-cash` | 6 | ✓ |
| `censorship-resistance` | 6 | ✓ |
| `secure-messaging` | 6 | ✓ |
| `constitutional-law` | 5 | ✓ |
| `export-control` | 5 | ✓ |
| `border-search` | 5 | ⚠️ undeclared |
| `technology-law` | 4 | ⚠️ undeclared |
| `distributed-systems` | 4 | ✓ |
| `civil-liberties` | 3 | ⚠️ undeclared |
| `technology` | 3 | ✓ |
| `technical` | 3 | ⚠️ undeclared |
| `imported-source` | 3 | ⚠️ undeclared |
| `project-governance` | 3 | ⚠️ undeclared |
| `technical-standard` | 3 | ⚠️ undeclared |
| `privacy-preserving-systems` | 2 | ✓ |
| `historical-event` | 2 | ✓ |
| `peer-to-peer-networking` | 2 | ✓ |
| `distributed-hash-tables` | 2 | ✓ |
| `example-tag` | 1 | ⚠️ undeclared |
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
| `border-search` | `knowledge/legal/CASE-US-V-TUNICK.md`, `knowledge/legal/STAT-18-USC-2232.md`, `knowledge/technical/TECH-GRAPHENEOS.md` +2 more |
| `case-law` | `bibliography/legal/SRC-RENO-V-ACLU-LOC.md`, `bibliography/legal/SRC-BROWN-V-EMA-GOVINFO.md`, `bibliography/legal/SRC-VAN-BUREN-LII.md` +7 more |
| `civil-liberties` | `knowledge/organizations/ORG-ACLU.md`, `bibliography/organizations/SRC-ACLU-HISTORY.md`, `bibliography/organizations/SRC-ACLU-CONTACT.md` |
| `example-tag` | `knowledge/_templates/knowledge-page.md` |
| `imported-source` | `bibliography/imported/SRC-OIR-ROADMAP-DOCX.md`, `bibliography/imported/SRC-OIR-BOOTSTRAP-PROMPT.md`, `bibliography/imported/SRC-OIR-PROJECT-CHARTER-DOCX.md` |
| `onion-routing` | `bibliography/academic/SRC-TOR-DESIGN-PAPER.md` |
| `outreach` | `knowledge/organizations/ORG-KNIGHT-FIRST-AMENDMENT.md`, `knowledge/organizations/ORG-WILSON-SONSINI.md`, `knowledge/organizations/ORG-RCFP.md` +50 more |
| `person` | `knowledge/people/PERSON-THOMAS-MASSIE.md`, `knowledge/people/PERSON-JANE-FONDA.md`, `knowledge/people/PERSON-WHITFIELD-DIFFIE.md` +61 more |
| `project-governance` | `bibliography/imported/SRC-OIR-ROADMAP-DOCX.md`, `bibliography/imported/SRC-OIR-BOOTSTRAP-PROMPT.md`, `bibliography/imported/SRC-OIR-PROJECT-CHARTER-DOCX.md` |
| `technical` | `knowledge/technical/TOPIC-ONION-ROUTING.md`, `bibliography/technical/SRC-SIGNAL-DOUBLE-RATCHET.md`, `bibliography/technical/SRC-SIGNAL-X3DH.md` |
| `technical-standard` | `bibliography/technical/SRC-RFC-1034.md`, `bibliography/technical/SRC-RFC-9293.md`, `bibliography/technical/SRC-RFC-8446.md` |
| `technology-law` | `knowledge/legal/CASE-VAN-BUREN-V-US.md`, `knowledge/legal/TOPIC-COMPUTER-FRAUD.md`, `bibliography/legal/SRC-VAN-BUREN-LII.md` +1 more |

**Action:** Add these to TAXONOMY.md or replace with existing tags.
