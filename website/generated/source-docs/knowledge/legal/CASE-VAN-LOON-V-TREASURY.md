---
id: CASE-VAN-LOON-V-TREASURY
title: Van Loon v. Department of the Treasury
type: case
status: draft
summary: Van Loon v. Department of the Treasury, No. 23-50669 (5th Cir. Nov. 26, 2024), held that Tornado Cash immutable smart contracts are not “property” under IEEPA and that OFAC exceeded its statutory authority by blocking them.
tags:
  - case
  - sanctions
  - open-source-software
  - censorship-resistance
  - tornado-cash
  - case-studies
sources:
  - SRC-VAN-LOON-5TH-CIR-JUSTIA
  - SRC-TREASURY-TC-AUG-2022
  - SRC-TREASURY-TC-NOV-2022
  - SRC-TREASURY-TC-DELIST-2025
  - SRC-OFAC-TC-REMOVAL-20250321
  - SRC-IEEPA-50-USC-1702-LII
relationships:
  - subject: CASE-VAN-LOON-V-TREASURY
    predicate: cites
    object: SRC-VAN-LOON-5TH-CIR-JUSTIA
    sources:
      - SRC-VAN-LOON-5TH-CIR-JUSTIA
  - subject: CASE-VAN-LOON-V-TREASURY
    predicate: interprets
    object: STAT-IEEPA
    sources:
      - SRC-VAN-LOON-5TH-CIR-JUSTIA
      - SRC-IEEPA-50-USC-1702-LII
  - subject: CASE-VAN-LOON-V-TREASURY
    predicate: related_to
    object: TOPIC-TORNADO-CASH
    sources:
      - SRC-VAN-LOON-5TH-CIR-JUSTIA
  - subject: CASE-VAN-LOON-V-TREASURY
    predicate: related_to
    object: TECH-TORNADO-CASH
    sources:
      - SRC-VAN-LOON-5TH-CIR-JUSTIA
last_verified: "2026-07-23"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/legal/CASE-VAN-LOON-V-TREASURY.md`
- Source ID: `CASE-VAN-LOON-V-TREASURY`
- [**Edit this page**](https://github.com/itsmeront/open-internet-reference/edit/main/knowledge/legal/CASE-VAN-LOON-V-TREASURY.md) | [**Suggest a change**](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml&title=Edit+suggestion:+CASE-VAN-LOON-V-TREASURY)

!!! info "📝 Page Status: Draft — sourced but not yet reviewed"

    - **Status**: `draft`
    - **Sources**: 6
    - **Relationships**: 4
    - **Research debt items**: 5
    - **Last verified**: 2026-07-23

---

# Van Loon v. Department of the Treasury

## Summary

Van Loon v. Department of the Treasury, No. 23-50669 (5th Cir. Nov. 26, 2024), held that Tornado Cash immutable smart contracts are not “property” under the International Emergency Economic Powers Act (IEEPA) and that OFAC exceeded its statutory authority by blocking them.

## Verified Facts

- The appeal is captioned Joseph Van Loon; Tyler Almeida; Alexander Fisher; Preston Van Loon; Kevin Vitale; Nate Welch v. Department of the Treasury; Office of Foreign Assets Control; Janet Yellen; Andrea M. Gacki, No. 23-50669 (5th Cir.).[^1]
- The panel was Circuit Judges Jones, Willett, and Engelhardt; Judge Willett authored the opinion.[^1]
- The case arose from OFAC’s designation of Tornado Cash on the Specially Designated Nationals and Blocked Persons List after late-2022 sanctions actions.[^1]
- Plaintiffs were users of Tornado Cash who challenged the designation as exceeding OFAC’s statutory authority.[^1]
- The United States District Court for the Western District of Texas had granted summary judgment to the Department; the Fifth Circuit reversed.[^1]
- The Fifth Circuit held that Tornado Cash’s immutable smart contracts are not the “property” of a foreign national or entity under IEEPA, cannot be blocked under IEEPA on that theory, and that OFAC overstepped its congressionally defined authority.[^1]
- The Fifth Circuit reversed and remanded with instructions to grant the plaintiffs’ motion for partial summary judgment based on the Administrative Procedure Act.[^1]
- The opinion describes Tornado Cash as an open-source crypto transaction software protocol that facilitates anonymous transactions by obfuscating origins and destinations of digital asset transfers, and describes immutable smart contracts as unownable, uncontrollable, and unchangeable—even by creators.[^1]
- On August 8, 2022, Treasury announced OFAC’s designation of Tornado Cash pursuant to Executive Order 13694, as amended.[^2]
- On November 8, 2022, Treasury announced that OFAC delisted and simultaneously redesignated Tornado Cash under Executive Order 13722 and Executive Order 13694, as amended, and that the August 8, 2022 designation was wholly replaced.[^3]
- On March 21, 2025, Treasury announced that it had exercised discretion to remove economic sanctions against Tornado Cash, referencing a filing in Van Loon v. Department of the Treasury.[^4]
- OFAC’s March 21, 2025 recent-actions notice records removal of Tornado Cash SDN list entries.[^5]
- IEEPA, at 50 U.S.C. § 1702, authorizes the President to investigate, regulate, or prohibit transactions involving property in which any foreign country or a national thereof has any interest, among other powers, when a national emergency has been declared.[^6]

## Historical Context

OFAC first designated Tornado Cash in August 2022 and redesignated it in November 2022. Users filed suit in the Western District of Texas. After the district court upheld the designation, the Fifth Circuit reversed on the statutory meaning of “property,” limiting its holding to immutable smart contracts. Treasury later announced delisting of Tornado Cash in March 2025.


[^1]: [`SRC-VAN-LOON-5TH-CIR-JUSTIA`](../../../bibliography.md#SRC-VAN-LOON-5TH-CIR-JUSTIA) — Van Loon v. Department of the Treasury, No. 23-50669 (5th Cir. Nov. 26, 2024) (Justia). Primary authority.
[^2]: [`SRC-TREASURY-TC-AUG-2022`](../../../bibliography.md#SRC-TREASURY-TC-AUG-2022) — U.S. Treasury Sanctions Notorious Virtual Currency Mixer Tornado Cash (Aug. 8, 2022). Official government press release.
[^3]: [`SRC-TREASURY-TC-NOV-2022`](../../../bibliography.md#SRC-TREASURY-TC-NOV-2022) — Treasury Designates DPRK Weapons Representatives; Tornado Cash Redesignation (Nov. 8, 2022). Official government press release.
[^4]: [`SRC-TREASURY-TC-DELIST-2025`](../../../bibliography.md#SRC-TREASURY-TC-DELIST-2025) — Tornado Cash Delisting (Mar. 21, 2025). Official government press release.
[^5]: [`SRC-OFAC-TC-REMOVAL-20250321`](../../../bibliography.md#SRC-OFAC-TC-REMOVAL-20250321) — OFAC Recent Actions — Cyber-related Designation Removal (Mar. 21, 2025). Official OFAC notice.
[^6]: [`SRC-IEEPA-50-USC-1702-LII`](../../../bibliography.md#SRC-IEEPA-50-USC-1702-LII) — 50 U.S.C. § 1702 (Cornell LII). Statute text.

## Legal Analysis

Jurisdiction: U.S. Court of Appeals for the Fifth Circuit. Authority level: published federal appellate opinion binding within the Fifth Circuit unless overruled. The dispositive holding concerns the meaning of “property” under IEEPA as applied to immutable smart contracts; the court did not rest the reverse-and-remand disposition on alternate entity-status or interest questions once the property requirement failed. The opinion notes that Congress may update IEEPA to address technologies such as crypto-mixing software.

## Relationships

- `CASE-VAN-LOON-V-TREASURY` cites [`SRC-VAN-LOON-5TH-CIR-JUSTIA`](../../../bibliography.md#SRC-VAN-LOON-5TH-CIR-JUSTIA).
- `CASE-VAN-LOON-V-TREASURY` interprets `STAT-IEEPA`.
- `CASE-VAN-LOON-V-TREASURY` related_to `TOPIC-TORNADO-CASH`.
- `CASE-VAN-LOON-V-TREASURY` related_to `TECH-TORNADO-CASH`.

## Sources

1. [`SRC-VAN-LOON-5TH-CIR-JUSTIA`](../../../bibliography.md#SRC-VAN-LOON-5TH-CIR-JUSTIA): Van Loon v. Department of the Treasury, No. 23-50669 (5th Cir. Nov. 26, 2024) (Justia).
2. [`SRC-TREASURY-TC-AUG-2022`](../../../bibliography.md#SRC-TREASURY-TC-AUG-2022): U.S. Treasury Sanctions Notorious Virtual Currency Mixer Tornado Cash (Aug. 8, 2022).
3. [`SRC-TREASURY-TC-NOV-2022`](../../../bibliography.md#SRC-TREASURY-TC-NOV-2022): Treasury Designates DPRK Weapons Representatives; Tornado Cash Redesignation (Nov. 8, 2022).
4. [`SRC-TREASURY-TC-DELIST-2025`](../../../bibliography.md#SRC-TREASURY-TC-DELIST-2025): Tornado Cash Delisting (Mar. 21, 2025).
5. [`SRC-OFAC-TC-REMOVAL-20250321`](../../../bibliography.md#SRC-OFAC-TC-REMOVAL-20250321): OFAC Recent Actions — Cyber-related Designation Removal (Mar. 21, 2025).
6. [`SRC-IEEPA-50-USC-1702-LII`](../../../bibliography.md#SRC-IEEPA-50-USC-1702-LII): 50 U.S.C. § 1702 (Cornell LII).

## Research Debt

- Add the Western District of Texas district-court opinion and docket number as a dedicated source record.
- Add counsel listings from the official opinion PDF or PACER/RECAP filings.
- Confirm Westlaw/LEXIS or F.4th reporter citation when assigned.
- Document post-remand district-court judgment text.
- Review First Amendment arguments raised below that the Fifth Circuit did not decide.
