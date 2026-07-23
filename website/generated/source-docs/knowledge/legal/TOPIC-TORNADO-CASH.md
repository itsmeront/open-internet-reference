---
id: TOPIC-TORNADO-CASH
title: Tornado Cash Sanctions and Developer Prosecutions
type: topic
status: draft
summary: Tornado Cash is an open-source Ethereum mixing protocol that was designated by OFAC in 2022, challenged in civil litigation culminating in Van Loon (5th Cir. 2024), delisted in 2025, and remains the subject of developer criminal cases in the United States and the Netherlands.
tags:
  - tornado-cash
  - case-studies
  - sanctions
  - open-source-software
  - censorship-resistance
  - privacy-preserving-systems
  - developer-rights
  - open-source-risk
  - digital-rights
sources:
  - SRC-TREASURY-TC-AUG-2022
  - SRC-TREASURY-TC-NOV-2022
  - SRC-TREASURY-TC-DELIST-2025
  - SRC-OFAC-FAQ-1076
  - SRC-VAN-LOON-5TH-CIR-JUSTIA
  - SRC-COIN-CENTER-YELLEN-NDFLA-2023
  - SRC-DOJ-STORM-INDICTMENT
  - SRC-DOJ-STORM-CONVICTION-2025
  - SRC-TREASURY-SEMENOV-2023
  - SRC-PERTSEV-ECLI-2024
  - SRC-PERTSEV-RECHTSPRAAK-EN-2024
  - SRC-IEEPA-50-USC-1702-LII
relationships:
  - subject: TOPIC-TORNADO-CASH
    predicate: cites
    object: SRC-VAN-LOON-5TH-CIR-JUSTIA
    sources:
      - SRC-VAN-LOON-5TH-CIR-JUSTIA
  - subject: TOPIC-TORNADO-CASH
    predicate: related_to
    object: TECH-TORNADO-CASH
    sources:
      - SRC-VAN-LOON-5TH-CIR-JUSTIA
  - subject: TOPIC-TORNADO-CASH
    predicate: related_to
    object: CASE-VAN-LOON-V-TREASURY
    sources:
      - SRC-VAN-LOON-5TH-CIR-JUSTIA
  - subject: TOPIC-TORNADO-CASH
    predicate: related_to
    object: CASE-COIN-CENTER-V-YELLEN
    sources:
      - SRC-COIN-CENTER-YELLEN-NDFLA-2023
  - subject: TOPIC-TORNADO-CASH
    predicate: related_to
    object: CASE-US-V-STORM
    sources:
      - SRC-DOJ-STORM-INDICTMENT
  - subject: TOPIC-TORNADO-CASH
    predicate: related_to
    object: CASE-NL-V-PERTSEV
    sources:
      - SRC-PERTSEV-ECLI-2024
  - subject: TOPIC-TORNADO-CASH
    predicate: related_to
    object: STAT-IEEPA
    sources:
      - SRC-VAN-LOON-5TH-CIR-JUSTIA
      - SRC-IEEPA-50-USC-1702-LII
last_verified: "2026-07-23"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/legal/TOPIC-TORNADO-CASH.md`
- Source ID: `TOPIC-TORNADO-CASH`
- [**Edit this page**](https://github.com/itsmeront/open-internet-reference/edit/main/knowledge/legal/TOPIC-TORNADO-CASH.md) | [**Suggest a change**](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml&title=Edit+suggestion:+TOPIC-TORNADO-CASH)

!!! info "📝 Page Status: Draft — sourced but not yet reviewed"

    - **Status**: `draft`
    - **Sources**: 12
    - **Relationships**: 7
    - **Research debt items**: 5
    - **Last verified**: 2026-07-23

---

# Tornado Cash Sanctions and Developer Prosecutions

## Summary

Tornado Cash is an open-source Ethereum mixing protocol that was designated by OFAC in 2022, challenged in U.S. civil litigation including Van Loon v. Department of the Treasury (5th Cir. 2024), removed from the SDN list in 2025, and remains the subject of developer criminal cases in the United States and the Netherlands.

## Verified Facts

- Treasury announced on August 8, 2022 that OFAC sanctioned Tornado Cash under Executive Order 13694, as amended, stating the mixer had been used to launder more than $7 billion in virtual currency since 2019, including over $455 million stolen by the Lazarus Group.[^1]
- Treasury announced on November 8, 2022 that OFAC delisted and simultaneously redesignated Tornado Cash under Executive Order 13722 and Executive Order 13694, as amended, wholly replacing the August 8, 2022 designation.[^2]
- OFAC FAQ 1076 states SDN identifiers included virtual currency wallet addresses and the Tornado Cash website URL; that the website had been deleted from the Internet but remained available in archives; and that interacting with open-source code without a prohibited transaction with Tornado Cash is not prohibited.[^3]
- [Van Loon v. Department of the Treasury](CASE-VAN-LOON-V-TREASURY.md) held that Tornado Cash immutable smart contracts are not IEEPA “property” and that OFAC exceeded its authority by blocking them.[^4]
- [Coin Center v. Yellen](CASE-COIN-CENTER-V-YELLEN.md) granted summary judgment to Treasury in the Northern District of Florida on October 30, 2023.[^5]
- Treasury announced on March 21, 2025 that it removed economic sanctions against Tornado Cash, referencing a filing in Van Loon.[^6]
- [United States v. Storm](CASE-US-V-STORM.md) concerns SDNY charges against Roman Storm and Roman Semenov; Treasury reported the August 23, 2023 charging and Storm’s arrest; the USAO reported Storm’s August 2025 conviction for conspiring to operate an unlicensed money transmitting business.[^7][^8][^9]
- [Netherlands v. Pertsev (Tornado Cash)](CASE-NL-V-PERTSEV.md) is the East Brabant District Court judgment ECLI:NL:RBOBR:2024:2069 (May 14, 2024) imposing a 64-month sentence for money laundering related to Tornado Cash; English judiciary news identifies Alexey Pertsev.[^10][^11]
- [TECH-TORNADO-CASH](../technical/TECH-TORNADO-CASH.md) records the Fifth Circuit’s description of mutable versus immutable smart contracts and automatic mixing without human intervention.[^4]
- 50 U.S.C. § 1702 is the IEEPA provision authorizing regulation of property in which foreign countries or nationals have interests under declared national emergency conditions; see [STAT-IEEPA](STAT-IEEPA.md).[^12]

## Historical Context

OFAC’s 2022 designations produced immediate compliance actions against listed identifiers and related access surfaces described in OFAC materials (including the project website URL). Civil plaintiffs challenged whether immutable smart-contract code could be blocked as “property” under IEEPA. The Fifth Circuit answered that question in the negative for immutable contracts in November 2024. Treasury delisted Tornado Cash in March 2025. Criminal cases against alleged developers continued on separate tracks under U.S. and Dutch criminal law.


[^1]: [`SRC-TREASURY-TC-AUG-2022`](../../../bibliography.md#SRC-TREASURY-TC-AUG-2022) — U.S. Treasury Sanctions Notorious Virtual Currency Mixer Tornado Cash (Aug. 8, 2022). Official government press release.
[^2]: [`SRC-TREASURY-TC-NOV-2022`](../../../bibliography.md#SRC-TREASURY-TC-NOV-2022) — Treasury Designates DPRK Weapons Representatives; Tornado Cash Redesignation (Nov. 8, 2022). Official government press release.
[^3]: [`SRC-OFAC-FAQ-1076`](../../../bibliography.md#SRC-OFAC-FAQ-1076) — OFAC FAQ 1076. Official OFAC FAQ.
[^4]: [`SRC-VAN-LOON-5TH-CIR-JUSTIA`](../../../bibliography.md#SRC-VAN-LOON-5TH-CIR-JUSTIA) — Van Loon v. Department of the Treasury, No. 23-50669 (5th Cir. Nov. 26, 2024) (Justia). Primary authority.
[^5]: [`SRC-COIN-CENTER-YELLEN-NDFLA-2023`](../../../bibliography.md#SRC-COIN-CENTER-YELLEN-NDFLA-2023) — Coin Center v. Yellen, No. 3:22-cv-20375 (N.D. Fla. Oct. 30, 2023). Primary authority.
[^6]: [`SRC-TREASURY-TC-DELIST-2025`](../../../bibliography.md#SRC-TREASURY-TC-DELIST-2025) — Tornado Cash Delisting (Mar. 21, 2025). Official government press release.
[^7]: [`SRC-TREASURY-SEMENOV-2023`](../../../bibliography.md#SRC-TREASURY-SEMENOV-2023) — Treasury Designates Roman Semenov (Aug. 23, 2023). Official government press release.
[^8]: [`SRC-DOJ-STORM-INDICTMENT`](../../../bibliography.md#SRC-DOJ-STORM-INDICTMENT) — United States v. Storm / Semenov Indictment (S.D.N.Y. Aug. 2023). Charging instrument.
[^9]: [`SRC-DOJ-STORM-CONVICTION-2025`](../../../bibliography.md#SRC-DOJ-STORM-CONVICTION-2025) — SDNY National Security Page — Roman Storm Conviction Note (Aug. 2025). Official USAO summary.
[^10]: [`SRC-PERTSEV-ECLI-2024`](../../../bibliography.md#SRC-PERTSEV-ECLI-2024) — ECLI:NL:RBOBR:2024:2069 (May 14, 2024). Primary authority.
[^11]: [`SRC-PERTSEV-RECHTSPRAAK-EN-2024`](../../../bibliography.md#SRC-PERTSEV-RECHTSPRAAK-EN-2024) — Dutch Judiciary English News — Tornado Cash Developer Jail Sentence (May 2024). Official court news summary.
[^12]: [`SRC-IEEPA-50-USC-1702-LII`](../../../bibliography.md#SRC-IEEPA-50-USC-1702-LII) — 50 U.S.C. § 1702 (Cornell LII). Statute text.

## Technical Analysis

On-chain immutable contracts, as described in Van Loon, cannot be altered by developers after immutability. Application-layer and intermediary surfaces (websites, hosting, repositories, issuer-controlled tokens, RPC access) remain subject to operator control and sanctions-compliance actions. OIR’s [PROTOCOL-TCP](../technical/PROTOCOL-TCP.md) page documents the Transmission Control Protocol as an internet transport standard; any comparison between immutable application-layer contracts and transport-layer protocols is architectural analysis and is not a holding of Van Loon.

## Legal Analysis

Three legal tracks appear in the record: (1) civil APA/IEEPA challenges to OFAC designations ([CASE-VAN-LOON-V-TREASURY](CASE-VAN-LOON-V-TREASURY.md), [CASE-COIN-CENTER-V-YELLEN](CASE-COIN-CENTER-V-YELLEN.md)); (2) U.S. criminal prosecution of alleged developers ([CASE-US-V-STORM](CASE-US-V-STORM.md)); and (3) Dutch criminal prosecution ([CASE-NL-V-PERTSEV](CASE-NL-V-PERTSEV.md)). Civil delisting does not, by itself, terminate criminal cases. Van Loon’s holding is limited to immutable smart contracts as IEEPA “property” within the Fifth Circuit’s decision.

## Relationships

- `TOPIC-TORNADO-CASH` cites [`SRC-VAN-LOON-5TH-CIR-JUSTIA`](../../../bibliography.md#SRC-VAN-LOON-5TH-CIR-JUSTIA).
- `TOPIC-TORNADO-CASH` related_to `TECH-TORNADO-CASH`.
- `TOPIC-TORNADO-CASH` related_to `CASE-VAN-LOON-V-TREASURY`.
- `TOPIC-TORNADO-CASH` related_to `CASE-COIN-CENTER-V-YELLEN`.
- `TOPIC-TORNADO-CASH` related_to `CASE-US-V-STORM`.
- `TOPIC-TORNADO-CASH` related_to `CASE-NL-V-PERTSEV`.
- `TOPIC-TORNADO-CASH` related_to `STAT-IEEPA`.

## Sources

1. [`SRC-TREASURY-TC-AUG-2022`](../../../bibliography.md#SRC-TREASURY-TC-AUG-2022): U.S. Treasury Sanctions Notorious Virtual Currency Mixer Tornado Cash (Aug. 8, 2022).
2. [`SRC-TREASURY-TC-NOV-2022`](../../../bibliography.md#SRC-TREASURY-TC-NOV-2022): Treasury Designates DPRK Weapons Representatives; Tornado Cash Redesignation (Nov. 8, 2022).
3. [`SRC-OFAC-FAQ-1076`](../../../bibliography.md#SRC-OFAC-FAQ-1076): OFAC FAQ 1076.
4. [`SRC-VAN-LOON-5TH-CIR-JUSTIA`](../../../bibliography.md#SRC-VAN-LOON-5TH-CIR-JUSTIA): Van Loon v. Department of the Treasury, No. 23-50669 (5th Cir. Nov. 26, 2024) (Justia).
5. [`SRC-COIN-CENTER-YELLEN-NDFLA-2023`](../../../bibliography.md#SRC-COIN-CENTER-YELLEN-NDFLA-2023): Coin Center v. Yellen, No. 3:22-cv-20375 (N.D. Fla. Oct. 30, 2023).
6. [`SRC-TREASURY-TC-DELIST-2025`](../../../bibliography.md#SRC-TREASURY-TC-DELIST-2025): Tornado Cash Delisting (Mar. 21, 2025).
7. [`SRC-TREASURY-SEMENOV-2023`](../../../bibliography.md#SRC-TREASURY-SEMENOV-2023): Treasury Designates Roman Semenov (Aug. 23, 2023).
8. [`SRC-DOJ-STORM-INDICTMENT`](../../../bibliography.md#SRC-DOJ-STORM-INDICTMENT): United States v. Storm / Semenov Indictment (S.D.N.Y. Aug. 2023).
9. [`SRC-DOJ-STORM-CONVICTION-2025`](../../../bibliography.md#SRC-DOJ-STORM-CONVICTION-2025): SDNY National Security Page — Roman Storm Conviction Note (Aug. 2025).
10. [`SRC-PERTSEV-ECLI-2024`](../../../bibliography.md#SRC-PERTSEV-ECLI-2024): ECLI:NL:RBOBR:2024:2069 (May 14, 2024).
11. [`SRC-PERTSEV-RECHTSPRAAK-EN-2024`](../../../bibliography.md#SRC-PERTSEV-RECHTSPRAAK-EN-2024): Dutch Judiciary English News — Tornado Cash Developer Jail Sentence (May 2024).
12. [`SRC-IEEPA-50-USC-1702-LII`](../../../bibliography.md#SRC-IEEPA-50-USC-1702-LII): 50 U.S.C. § 1702 (Cornell LII).

Additional sources (not yet cited in footnotes):

- [`SRC-OFAC-TC-REMOVAL-20250321`](../../../bibliography.md#SRC-OFAC-TC-REMOVAL-20250321): OFAC Recent Actions — Cyber-related Designation Removal (Mar. 21, 2025).
- [`SRC-FBI-SEMENOV`](../../../bibliography.md#SRC-FBI-SEMENOV): FBI Wanted — Roman Semenov.

## Research Debt

- Add primary sources for intermediary compliance events (GitHub, Circle/USDC, RPC providers).
- Add Eleventh Circuit primary disposition of Coin Center appeal after delisting.
- Add docket-verified outcomes for non-convicted counts in United States v. Storm.
- Add relationship to `TOPIC-CODE-AS-SPEECH` only if First Amendment holdings or preserved claims are sourced (Van Loon did not decide First Amendment).
- Human research-editor review required before any status promotion beyond `draft` (AI-assisted intake).
