---
id: TOPIC-DEVELOPER-SOFTWARE-LIABILITY
title: Documented Proceedings Involving Software Authors and Operators
type: topic
status: draft
summary: Inventory of documented U.S. and selected foreign proceedings in which people who wrote, published, or operated software faced criminal investigation, prosecution, civil injunction, or OFAC sanctions — organized by legal tool and outcome.
tags:
  - developer-rights
  - open-source-risk
  - case-studies
  - computer-crime
  - sanctions
  - speech-and-code
  - copyright
  - export-control
  - cryptography
  - digital-rights
sources:
  - SRC-IRS-SAMOURAI-PLEA-2025
  - SRC-IRS-SAMOURAI-SENTENCE-2025
  - SRC-DOJ-STORM-INDICTMENT
  - SRC-DOJ-STORM-CONVICTION-2025
  - SRC-PERTSEV-ECLI-2024
  - SRC-TREASURY-BLENDER-2022
  - SRC-TREASURY-TC-AUG-2022
  - SRC-VAN-LOON-5TH-CIR-JUSTIA
  - SRC-ZIMMERMANN-DECLINATION-1996
  - SRC-DOJ-SKLYAROV-INDICTMENT-2001
  - SRC-DOJ-SKLYAROV-AGREE-2001
  - SRC-BERNSTEIN-JUSTIA
  - SRC-JUNGER-CMU
  - SRC-CORLEY-LII
relationships:
  - subject: TOPIC-DEVELOPER-SOFTWARE-LIABILITY
    predicate: cites
    object: SRC-IRS-SAMOURAI-SENTENCE-2025
    sources:
      - SRC-IRS-SAMOURAI-SENTENCE-2025
  - subject: TOPIC-DEVELOPER-SOFTWARE-LIABILITY
    predicate: related_to
    object: CASE-US-V-RODRIGUEZ
    sources:
      - SRC-IRS-SAMOURAI-PLEA-2025
  - subject: TOPIC-DEVELOPER-SOFTWARE-LIABILITY
    predicate: related_to
    object: CASE-US-V-STORM
    sources:
      - SRC-DOJ-STORM-INDICTMENT
  - subject: TOPIC-DEVELOPER-SOFTWARE-LIABILITY
    predicate: related_to
    object: CASE-NL-V-PERTSEV
    sources:
      - SRC-PERTSEV-ECLI-2024
  - subject: TOPIC-DEVELOPER-SOFTWARE-LIABILITY
    predicate: related_to
    object: TOPIC-TORNADO-CASH
    sources:
      - SRC-VAN-LOON-5TH-CIR-JUSTIA
  - subject: TOPIC-DEVELOPER-SOFTWARE-LIABILITY
    predicate: related_to
    object: EVENT-OFAC-BLENDER-2022
    sources:
      - SRC-TREASURY-BLENDER-2022
  - subject: TOPIC-DEVELOPER-SOFTWARE-LIABILITY
    predicate: related_to
    object: EVENT-ZIMMERMANN-PGP-INVESTIGATION
    sources:
      - SRC-ZIMMERMANN-DECLINATION-1996
  - subject: TOPIC-DEVELOPER-SOFTWARE-LIABILITY
    predicate: related_to
    object: CASE-US-V-SKLYAROV
    sources:
      - SRC-DOJ-SKLYAROV-AGREE-2001
  - subject: TOPIC-DEVELOPER-SOFTWARE-LIABILITY
    predicate: related_to
    object: CASE-BERNSTEIN-V-DOJ
    sources:
      - SRC-BERNSTEIN-JUSTIA
  - subject: TOPIC-DEVELOPER-SOFTWARE-LIABILITY
    predicate: related_to
    object: CASE-UNIVERSAL-V-CORLEY
    sources:
      - SRC-CORLEY-LII
  - subject: TOPIC-DEVELOPER-SOFTWARE-LIABILITY
    predicate: related_to
    object: TOPIC-CODE-AS-SPEECH
    sources:
      - SRC-BERNSTEIN-JUSTIA
last_verified: "2026-07-23"
---

# Documented Proceedings Involving Software Authors and Operators

## Summary

This page inventories documented U.S. and selected foreign proceedings in which people who wrote, published, or operated software faced criminal investigation, prosecution, civil injunction, or OFAC sanctions. Entries record the software category, legal authority cited by the government or court, and documented outcome.

## Verified Facts

### Money transmitting / mixer criminal cases

- In [United States v. Rodriguez (Samourai Wallet)](CASE-US-V-RODRIGUEZ.md), co-founders of Samourai Wallet pled guilty to conspiracy to operate a money transmitting business knowing it transmitted crime proceeds and received sentences of five years and four years.[^1][^2]
- In [United States v. Storm](CASE-US-V-STORM.md), a Tornado Cash co-founder was charged with conspiracies including money laundering, unlicensed money transmitting, and IEEPA violations; the USAO reported an August 2025 conviction for conspiring to operate an unlicensed money transmitting business.[^3][^4]
- In [Netherlands v. Pertsev (Tornado Cash)](CASE-NL-V-PERTSEV.md), a Dutch court convicted a Tornado Cash developer of money laundering and imposed a 64-month sentence (ECLI:NL:RBOBR:2024:2069).[^5]

### OFAC sanctions on mixing software / services

- On May 6, 2022, Treasury announced OFAC’s designation of [Blender.io](EVENT-OFAC-BLENDER-2022.md), described as the first sanctions action against a virtual currency mixer, under E.O. 13694.[^6]
- On August 8, 2022, Treasury announced OFAC’s designation of Tornado Cash under E.O. 13694; see [TOPIC-TORNADO-CASH](TOPIC-TORNADO-CASH.md).[^7]
- In [Van Loon v. Department of the Treasury](CASE-VAN-LOON-V-TREASURY.md), the Fifth Circuit held that Tornado Cash immutable smart contracts are not “property” under IEEPA and that OFAC exceeded its authority by blocking them.[^8]

### Encryption publication investigation (no indictment)

- In the [Zimmermann / PGP investigation](EVENT-ZIMMERMANN-PGP-INVESTIGATION.md), the U.S. Attorney for the Northern District of California declined prosecution in January 1996 and closed the investigation into the June 1991 USENET posting of Pretty Good Privacy.[^9]

### Circumvention software — criminal DMCA

- In [United States v. Sklyarov / Elcomsoft](CASE-US-V-SKLYAROV.md), a programmer and company were indicted under 17 U.S.C. § 1201 for trafficking in ebook circumvention software; Sklyarov entered a deferred-prosecution agreement in December 2001.[^10][^11]

### Circumvention software — civil injunction; code treated as speech

- In [Universal City Studios v. Corley](CASE-UNIVERSAL-V-CORLEY.md), the Second Circuit upheld a DMCA anti-circumvention injunction against distribution of DeCSS code while recognizing that computer code is speech entitled to First Amendment scrutiny.[^12]

### Encryption source-code publication — civil constitutional challenges

- In [Bernstein v. DOJ](CASE-BERNSTEIN-V-DOJ.md), the Ninth Circuit held that software source code is protected speech and that challenged encryption export regulations constituted an unconstitutional prior restraint.[^13]
- In [Junger v. Daley](CASE-JUNGER-V-DALEY.md), the Sixth Circuit held that computer source code is protected by the First Amendment because of its expressiveness.[^14]

## Historical Context

Proceedings in this inventory span export-control investigations of encryption software in the 1990s, DMCA anti-circumvention enforcement in the early 2000s, and 2020s OFAC mixer designations plus criminal cases alleging money-transmitting or money-laundering theories against people associated with cryptocurrency privacy software. Outcomes include declination of prosecution, deferred prosecution, civil injunction, SDN designation, guilty plea with prison sentence, trial conviction, and appellate invalidation of an OFAC blocking theory for immutable smart contracts.


[^1]: `SRC-IRS-SAMOURAI-PLEA-2025` — IRS-CI Samourai Wallet Founders Plead Guilty (July 30, 2025). Official government announcement.
[^2]: `SRC-IRS-SAMOURAI-SENTENCE-2025` — IRS-CI Samourai Wallet Founders Sentenced (Nov. 2025). Official government announcement.
[^3]: `SRC-DOJ-STORM-INDICTMENT` — United States v. Storm / Semenov Indictment (S.D.N.Y. Aug. 2023). Charging instrument.
[^4]: `SRC-DOJ-STORM-CONVICTION-2025` — SDNY National Security Page — Roman Storm Conviction Note (Aug. 2025). Official USAO summary.
[^5]: `SRC-PERTSEV-ECLI-2024` — ECLI:NL:RBOBR:2024:2069 (May 14, 2024). Primary Dutch judgment.
[^6]: `SRC-TREASURY-BLENDER-2022` — Treasury Blender.io Designation (May 6, 2022). Official government press release.
[^7]: `SRC-TREASURY-TC-AUG-2022` — Treasury Tornado Cash Designation (Aug. 8, 2022). Official government press release.
[^8]: `SRC-VAN-LOON-5TH-CIR-JUSTIA` — Van Loon v. Department of the Treasury, No. 23-50669 (5th Cir. Nov. 26, 2024). Primary authority.
[^9]: `SRC-ZIMMERMANN-DECLINATION-1996` — Zimmermann PGP Investigation Closed (Jan. 1996). Republished declination.
[^10]: `SRC-DOJ-SKLYAROV-INDICTMENT-2001` — DOJ First DMCA Indictment (Aug. 28, 2001). Archived official press release.
[^11]: `SRC-DOJ-SKLYAROV-AGREE-2001` — DOJ Sklyarov Agreement (Dec. 13, 2001). Official archived press release.
[^12]: `SRC-CORLEY-LII` — Universal City Studios v. Corley (Cornell LII / related Corley source). Primary authority cross-check on CASE page.
[^13]: `SRC-BERNSTEIN-JUSTIA` — Bernstein v. DOJ, 176 F.3d 1132 (9th Cir. 1999). Primary authority.
[^14]: `SRC-JUNGER-CMU` — Junger v. Daley Opinion Text (CMU). Primary authority.

## Legal Analysis

Documented theories in this inventory include: (1) conspiracy to operate an unlicensed or crime-proceeds money transmitting business; (2) money laundering; (3) IEEPA / OFAC sanctions violations and SDN designation of mixers; (4) Arms Export Control Act / encryption export investigation (declined); (5) criminal DMCA anti-circumvention trafficking; and (6) civil DMCA injunction with First Amendment scrutiny of code. Authority levels differ (investigation closed; plea; trial conviction; appellate statutory holding; district injunction). This page does not state whether any particular future project is lawful or unlawful.

## Relationships

- `TOPIC-DEVELOPER-SOFTWARE-LIABILITY` cites `SRC-IRS-SAMOURAI-SENTENCE-2025`.
- `TOPIC-DEVELOPER-SOFTWARE-LIABILITY` related_to `CASE-US-V-RODRIGUEZ`.
- `TOPIC-DEVELOPER-SOFTWARE-LIABILITY` related_to `CASE-US-V-STORM`.
- `TOPIC-DEVELOPER-SOFTWARE-LIABILITY` related_to `CASE-NL-V-PERTSEV`.
- `TOPIC-DEVELOPER-SOFTWARE-LIABILITY` related_to `TOPIC-TORNADO-CASH`.
- `TOPIC-DEVELOPER-SOFTWARE-LIABILITY` related_to `EVENT-OFAC-BLENDER-2022`.
- `TOPIC-DEVELOPER-SOFTWARE-LIABILITY` related_to `EVENT-ZIMMERMANN-PGP-INVESTIGATION`.
- `TOPIC-DEVELOPER-SOFTWARE-LIABILITY` related_to `CASE-US-V-SKLYAROV`.
- `TOPIC-DEVELOPER-SOFTWARE-LIABILITY` related_to `CASE-BERNSTEIN-V-DOJ`.
- `TOPIC-DEVELOPER-SOFTWARE-LIABILITY` related_to `CASE-UNIVERSAL-V-CORLEY`.
- `TOPIC-DEVELOPER-SOFTWARE-LIABILITY` related_to `TOPIC-CODE-AS-SPEECH`.

## Sources

1. `SRC-IRS-SAMOURAI-PLEA-2025`: IRS-CI — Samourai Wallet Founders Plead Guilty (July 30, 2025).
2. `SRC-IRS-SAMOURAI-SENTENCE-2025`: IRS-CI — Samourai Wallet Founders Sentenced (Nov. 2025).
3. `SRC-DOJ-STORM-INDICTMENT`: United States v. Storm / Semenov Indictment (S.D.N.Y. Aug. 2023).
4. `SRC-DOJ-STORM-CONVICTION-2025`: SDNY National Security Page — Roman Storm Conviction Note (Aug. 2025).
5. `SRC-PERTSEV-ECLI-2024`: ECLI:NL:RBOBR:2024:2069 (May 14, 2024).
6. `SRC-TREASURY-BLENDER-2022`: Treasury Blender.io Designation (May 6, 2022).
7. `SRC-TREASURY-TC-AUG-2022`: Treasury Tornado Cash Designation (Aug. 8, 2022).
8. `SRC-VAN-LOON-5TH-CIR-JUSTIA`: Van Loon v. Department of the Treasury (5th Cir. Nov. 26, 2024).
9. `SRC-ZIMMERMANN-DECLINATION-1996`: Zimmermann PGP Investigation Closed (Jan. 1996).
10. `SRC-DOJ-SKLYAROV-INDICTMENT-2001`: DOJ First DMCA Indictment (Aug. 28, 2001).
11. `SRC-DOJ-SKLYAROV-AGREE-2001`: DOJ Sklyarov Agreement (Dec. 13, 2001).
12. `SRC-CORLEY-LII`: Universal City Studios v. Corley source record.
13. `SRC-BERNSTEIN-JUSTIA`: Bernstein v. DOJ (Justia).
14. `SRC-JUNGER-CMU`: Junger v. Daley Opinion Text (CMU).

## Research Debt

- Add Helix / Bitcoin Fog primary plea and judgment sources (custodial mixer contrast).
- Add FinCEN FIN-2019-G001 as a statute/guidance source on anonymizing software providers.
- Human research-editor review before status promotion beyond `draft`.
