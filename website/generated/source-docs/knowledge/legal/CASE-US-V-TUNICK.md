---
id: CASE-US-V-TUNICK
title: United States v. Tunick
type: case
status: draft
summary: United States v. Tunick, No. 1:25-cr-00499 (N.D. Ga.), is a pending federal prosecution charging Samuel Tunick under 18 U.S.C. § 2232(a) for allegedly deleting digital contents of a Google Pixel phone during a January 24, 2025 CBP secondary inspection at Atlanta’s airport; public reporting links the wipe to GrapheneOS duress credentials.
tags:
  - case
  - privacy
  - border-search
  - open-source-software
  - fourth-amendment
  - digital-rights
  - case-studies
sources:
  - SRC-TUNICK-INDICTMENT-2025
  - SRC-TUNICK-MOTION-SUPPRESS-2026
  - SRC-COURTLISTENER-TUNICK-DOCKET
  - SRC-USC-18-2232-LII
  - SRC-TECHCRUNCH-TUNICK-DURESS-2026
  - SRC-TECHSPOT-TUNICK-GRAPHENEOS-2026
  - SRC-GRAPHENEOS-FEATURES
relationships:
  - subject: CASE-US-V-TUNICK
    predicate: cites
    object: SRC-TUNICK-INDICTMENT-2025
    sources:
      - SRC-TUNICK-INDICTMENT-2025
  - subject: CASE-US-V-TUNICK
    predicate: cites
    object: SRC-TUNICK-MOTION-SUPPRESS-2026
    sources:
      - SRC-TUNICK-MOTION-SUPPRESS-2026
  - subject: CASE-US-V-TUNICK
    predicate: related_to
    object: STAT-18-USC-2232
    sources:
      - SRC-TUNICK-INDICTMENT-2025
  - subject: CASE-US-V-TUNICK
    predicate: related_to
    object: TECH-GRAPHENEOS
    sources:
      - SRC-TECHCRUNCH-TUNICK-DURESS-2026
  - subject: CASE-US-V-TUNICK
    predicate: related_to
    object: TOPIC-FOURTH-AMENDMENT
    sources:
      - SRC-TUNICK-MOTION-SUPPRESS-2026
last_verified: "2026-07-27"
indictment_date: "2025-11-13"
offense_date: "2025-01-24"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/legal/CASE-US-V-TUNICK.md`
- Source ID: `CASE-US-V-TUNICK`
- [**Edit this page**](https://github.com/itsmeront/open-internet-reference/edit/main/knowledge/legal/CASE-US-V-TUNICK.md) | [**Suggest a change**](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml&title=Edit+suggestion:+CASE-US-V-TUNICK)

!!! info "📝 Page Status: Draft — sourced but not yet reviewed"

    - **Status**: `draft`
    - **Sources**: 7
    - **Relationships**: 5
    - **Research debt items**: 6

---

# United States v. Tunick

## Summary

United States v. Tunick, No. 1:25-cr-00499-ELR-CCB (N.D. Ga.), is a pending one-count federal prosecution charging Samuel Tunick with destroying property to prevent seizure under 18 U.S.C. § 2232(a), based on alleged deletion of digital contents of a Google Pixel phone during a Customs and Border Protection secondary inspection at Hartsfield-Jackson Atlanta International Airport on or about January 24, 2025.[^1][^2] Public secondary reporting links the alleged wipe to [GrapheneOS](../technical/TECH-GRAPHENEOS.md) duress passcode features; the indictment itself does not name GrapheneOS.[^3][^4]

## Verified Facts

### Charging instrument

- A grand jury indictment filed November 13, 2025, in the U.S. District Court for the Northern District of Georgia (Atlanta Division) charges Samuel Tunick in Case No. 1:25-cr-00499-ELR-CCB.[^1][^5]
- The indictment alleges that on or about January 24, 2025, before and during a search for and seizure of property by a Customs and Border Patrol Tactical Terrorism Response Team supervisory officer, Tunick knowingly destroyed, damaged, wasted, disposed of, and otherwise took action to delete the digital contents of a Google Pixel cellular phone for the purpose of preventing and impairing the government’s lawful authority to take that property into custody and control, in violation of 18 U.S.C. § 2232(a).[^1]
- 18 U.S.C. § 2232(a) authorizes a fine or imprisonment of not more than five years, or both.[^2]

### Docket status (CourtListener)

- CourtListener’s docket for the case lists Judge Eleanor L. Ross (district) and Magistrate Judge Christopher C. Bly (referral).[^5]
- A December 3, 2025 minute entry records initial appearance and arraignment with a plea of not guilty to Count 1 and bond set at $10,000 non-surety.[^5]
- A March 17, 2026 docket entry records a defense motion to suppress evidence and statements (Doc. 21).[^5][^6]
- A July 20, 2026 minute entry records an evidentiary hearing on the suppression motion and sets post-hearing briefing deadlines into October 2026.[^5]

### Defense motion allegations (not adjudicated)

- The defense motion states Tunick is a U.S. citizen who was placed in secondary inspection at Hartsfield-Jackson Atlanta International Airport on January 24, 2025, while returning from the Dominican Republic.[^6]
- The motion alleges FBI personnel coordinated with CBP to question and search Tunick in connection with investigation of association with the Defend the Atlanta Forest movement opposing the Atlanta Public Safety Training Center (“Cop City”).[^6]
- The motion alleges CBP officers demanded a phone passcode, did not administer Miranda warnings, and repeatedly ignored Tunick’s requests for a lawyer.[^6]
- The motion states that Tunick eventually provided a password for his phone and e-reader, and that according to the government, when officers entered the password the phone’s “screen went blank, flashed several times and the phone appeared to restart.”[^6]
- The motion seeks suppression on Fifth/Sixth Amendment interrogation theories and Fourth Amendment border-search theories, including challenges to using border authority to investigate domestic activity.[^6]

### GrapheneOS / duress reporting (secondary)

- TechCrunch reported that Tunick’s attorneys confirmed GrapheneOS was running on the phone and described the case as involving a duress password that wipes device contents.[^3]
- TechSpot likewise reported the prosecution in connection with GrapheneOS wipe/passcode features.[^4]
- GrapheneOS official documentation describes an optional duress PIN/password that irreversibly wipes the device and installed eSIMs when entered.[^7]
- The indictment and the suppression motion text reviewed for this OIR page do not name GrapheneOS.[^1][^6]

## Historical Context

The case sits at the intersection of expanded digital device searches at ports of entry, open-source mobile security features designed for coercion scenarios, and federal use of a property-destruction-to-prevent-seizure statute against alleged deletion of phone data. As of the July 20, 2026 evidentiary hearing, the suppression motion remained pending with further briefing scheduled.[^5]


[^1]: [`SRC-TUNICK-INDICTMENT-2025`](../../../bibliography.md#SRC-TUNICK-INDICTMENT-2025) — United States v. Tunick Indictment (N.D. Ga. Nov. 13, 2025) (RECAP). Charging instrument.
[^2]: [`SRC-USC-18-2232-LII`](../../../bibliography.md#SRC-USC-18-2232-LII) — 18 U.S.C. § 2232 (Cornell LII). Primary statutory text (LII-hosted).
[^3]: [`SRC-TECHCRUNCH-TUNICK-DURESS-2026`](../../../bibliography.md#SRC-TECHCRUNCH-TUNICK-DURESS-2026) — TechCrunch (July 24, 2026). Secondary journalism.
[^4]: [`SRC-TECHSPOT-TUNICK-GRAPHENEOS-2026`](../../../bibliography.md#SRC-TECHSPOT-TUNICK-GRAPHENEOS-2026) — TechSpot Tunick / GrapheneOS report. Secondary journalism; intake article.
[^5]: [`SRC-COURTLISTENER-TUNICK-DOCKET`](../../../bibliography.md#SRC-COURTLISTENER-TUNICK-DOCKET) — CourtListener docket United States v. Tunick (1:25-cr-00499). PACER/RECAP-derived docket.
[^6]: [`SRC-TUNICK-MOTION-SUPPRESS-2026`](../../../bibliography.md#SRC-TUNICK-MOTION-SUPPRESS-2026) — Motion to Suppress (Mar. 17, 2026) (RECAP). Defense filing; allegations not adjudicated.
[^7]: [`SRC-GRAPHENEOS-FEATURES`](../../../bibliography.md#SRC-GRAPHENEOS-FEATURES) — GrapheneOS Features Overview (Duress PIN/Password). Official project documentation.

## Legal Analysis

Jurisdiction: U.S. District Court, Northern District of Georgia (criminal). Authority level: pending district-court prosecution; no conviction or published merits ruling is recorded on this page. The government’s theory treats alleged deletion of phone data during a CBP search/seizure as § 2232(a) property destruction. Defense theories challenge the interrogation and border search under the Fourth, Fifth, and Sixth Amendments and argue that resulting evidence of a wipe should be suppressed. This page does not state whether Tunick is guilty or whether GrapheneOS duress credentials were used.

## Relationships

- `CASE-US-V-TUNICK` cites [`SRC-TUNICK-INDICTMENT-2025`](../../../bibliography.md#SRC-TUNICK-INDICTMENT-2025).
- `CASE-US-V-TUNICK` cites [`SRC-TUNICK-MOTION-SUPPRESS-2026`](../../../bibliography.md#SRC-TUNICK-MOTION-SUPPRESS-2026).
- `CASE-US-V-TUNICK` related_to `STAT-18-USC-2232`.
- `CASE-US-V-TUNICK` related_to `TECH-GRAPHENEOS`.
- `CASE-US-V-TUNICK` related_to `TOPIC-FOURTH-AMENDMENT`.

## Sources

1. [`SRC-TUNICK-INDICTMENT-2025`](../../../bibliography.md#SRC-TUNICK-INDICTMENT-2025): United States v. Tunick — Indictment (N.D. Ga. Nov. 13, 2025).
2. [`SRC-USC-18-2232-LII`](../../../bibliography.md#SRC-USC-18-2232-LII): 18 U.S.C. § 2232 (Cornell LII).
3. [`SRC-TECHCRUNCH-TUNICK-DURESS-2026`](../../../bibliography.md#SRC-TECHCRUNCH-TUNICK-DURESS-2026): TechCrunch — Duress Password Border Search Report (July 24, 2026).
4. [`SRC-TECHSPOT-TUNICK-GRAPHENEOS-2026`](../../../bibliography.md#SRC-TECHSPOT-TUNICK-GRAPHENEOS-2026): TechSpot — GrapheneOS Phone Wipe Prosecution Report.
5. [`SRC-COURTLISTENER-TUNICK-DOCKET`](../../../bibliography.md#SRC-COURTLISTENER-TUNICK-DOCKET): CourtListener Docket — United States v. Tunick.
6. [`SRC-TUNICK-MOTION-SUPPRESS-2026`](../../../bibliography.md#SRC-TUNICK-MOTION-SUPPRESS-2026): United States v. Tunick — Motion to Suppress (Mar. 17, 2026).
7. [`SRC-GRAPHENEOS-FEATURES`](../../../bibliography.md#SRC-GRAPHENEOS-FEATURES): GrapheneOS Features Overview — Duress PIN/Password.

## Research Debt

- Locate a primary filing that expressly names GrapheneOS or “duress” credentials (if filed); until then keep OS attribution under secondary reporting.
- Add RECAP PDF for Doc. 8.1 not-guilty plea form as a dedicated source if needed beyond the docket minute entry.
- Track the suppression ruling and any trial or plea outcome; update status when adjudicated.
- Note: `offense_date` is the indictment’s “on or about January 24, 2025” alleged conduct date, not an adjudicated finding.
- Consider a focused topic page on border device searches / digital wipe features once additional cases are intake-reviewed.
- Domain expert (criminal procedure / border search) review before any status above `draft`.

## Document metadata

- Offense date: `2025-01-24`
- Indictment date: `2025-11-13`
- Last verified: `2026-07-27`
