---
id: TOPIC-DEVICE-SEARCH
title: Device Search, Seizure, and Anti-Forensics
type: topic
status: draft
summary: Topic on government search and seizure of digital devices—especially at the border—and privacy technologies such as duress wipes that can collide with obstruction or destruction-of-evidence statutes.
tags:
  - fourth-amendment
  - border-search
  - privacy
  - digital-rights
  - case-studies
  - open-source-software
sources:
  - SRC-TUNICK-INDICTMENT-2025
  - SRC-USC-18-2232-LII
  - SRC-GRAPHENEOS-FEATURES
  - SRC-TECHCRUNCH-TUNICK-DURESS-2026
  - SRC-TUNICK-MOTION-SUPPRESS-2026
relationships:
  - subject: TOPIC-DEVICE-SEARCH
    predicate: related_to
    object: CASE-US-V-TUNICK
    sources:
      - SRC-TUNICK-INDICTMENT-2025
  - subject: TOPIC-DEVICE-SEARCH
    predicate: related_to
    object: TECH-GRAPHENEOS
    sources:
      - SRC-GRAPHENEOS-FEATURES
      - SRC-TECHCRUNCH-TUNICK-DURESS-2026
  - subject: TOPIC-DEVICE-SEARCH
    predicate: related_to
    object: TOPIC-FOURTH-AMENDMENT
    sources:
      - SRC-TUNICK-MOTION-SUPPRESS-2026
  - subject: TOPIC-DEVICE-SEARCH
    predicate: related_to
    object: STAT-18-USC-2232
    sources:
      - SRC-USC-18-2232-LII
last_verified: "2026-08-08"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/legal/TOPIC-DEVICE-SEARCH.md`
- Source ID: `TOPIC-DEVICE-SEARCH`
- [**Edit this page**](https://github.com/itsmeront/open-internet-reference/edit/main/knowledge/legal/TOPIC-DEVICE-SEARCH.md) | [**Suggest a change**](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml&title=Edit+suggestion:+TOPIC-DEVICE-SEARCH)

!!! info "📝 Page Status: Draft — sourced but not yet reviewed"

    - **Status**: `draft`
    - **Sources**: 5
    - **Relationships**: 4
    - **Research debt items**: 4

---

# Device Search, Seizure, and Anti-Forensics

## Summary

This topic covers OIR materials on searching and seizing phones and other devices, with emphasis on border inspections and privacy features that can destroy data when credentials are entered. The lead case study is [United States v. Tunick](CASE-US-V-TUNICK.md), charging destruction of property to prevent seizure under 18 U.S.C. § 2232(a) after an alleged phone wipe during a CBP secondary inspection; public reporting links the wipe to GrapheneOS duress credentials.

## Verified Facts

- A November 13, 2025 indictment in *United States v. Tunick* (N.D. Ga.) charges Samuel Tunick under 18 U.S.C. § 2232(a) for allegedly deleting digital contents of a Google Pixel phone during a January 24, 2025 CBP secondary inspection at Atlanta’s airport.[^1]
- 18 U.S.C. § 2232(a) authorizes a fine or imprisonment of not more than five years, or both, for knowingly destroying or damaging property to prevent or impair the government’s lawful authority to take that property into custody.[^2]
- GrapheneOS features documentation states users can set a duress PIN/password that irreversibly wipes the device (and installed eSIMs) when entered anywhere device credentials are requested.[^3]
- TechCrunch reported that counsel for Tunick confirmed GrapheneOS was running on the phone at issue; the indictment itself does not name GrapheneOS.[^4]
- Tunick’s defense motion to suppress alleges CBP secondary inspection, demands for a phone passcode, and that according to the government the phone’s screen went blank and appeared to restart after a password was entered.[^5]

## Historical Context

Device searches sit at the intersection of Fourth Amendment doctrine, border-search authority, and modern phone encryption. OIR’s Tunick/GrapheneOS materials show how anti-forensic or duress features designed for user privacy can become the factual core of destruction-to-prevent-seizure charges. Broader digital-search holdings (for example Carpenter on location data) remain related through [TOPIC-FOURTH-AMENDMENT](TOPIC-FOURTH-AMENDMENT.md).


[^1]: [`SRC-TUNICK-INDICTMENT-2025`](../../../bibliography.md#SRC-TUNICK-INDICTMENT-2025) — United States v. Tunick Indictment (Nov. 13, 2025). Charging instrument.
[^2]: [`SRC-USC-18-2232-LII`](../../../bibliography.md#SRC-USC-18-2232-LII) — 18 U.S.C. § 2232 (Cornell LII). Primary statutory text.
[^3]: [`SRC-GRAPHENEOS-FEATURES`](../../../bibliography.md#SRC-GRAPHENEOS-FEATURES) — GrapheneOS Features Overview (Duress PIN/Password). Official project documentation.
[^4]: [`SRC-TECHCRUNCH-TUNICK-DURESS-2026`](../../../bibliography.md#SRC-TECHCRUNCH-TUNICK-DURESS-2026) — TechCrunch Tunick/duress reporting. Secondary journalism.
[^5]: [`SRC-TUNICK-MOTION-SUPPRESS-2026`](../../../bibliography.md#SRC-TUNICK-MOTION-SUPPRESS-2026) — Tunick motion to suppress. Defense filing; allegations not adjudicated.

## Legal Analysis

Jurisdiction for the lead example is U.S. federal criminal law (N.D. Ga.), pending as of OIR’s Tunick page. Section 2232(a) focuses on preventing seizure of property, not on whether a search was reasonable under the Fourth Amendment; suppression litigation may raise separate constitutional claims. Do not treat press attribution of GrapheneOS as a charging fact unless a primary filing names the OS.

## Relationships

- `TOPIC-DEVICE-SEARCH` related_to `CASE-US-V-TUNICK`.
- `TOPIC-DEVICE-SEARCH` related_to `TECH-GRAPHENEOS`.
- `TOPIC-DEVICE-SEARCH` related_to `TOPIC-FOURTH-AMENDMENT`.
- `TOPIC-DEVICE-SEARCH` related_to `STAT-18-USC-2232`.

## Sources

1. [`SRC-TUNICK-INDICTMENT-2025`](../../../bibliography.md#SRC-TUNICK-INDICTMENT-2025): United States v. Tunick — Indictment.
2. [`SRC-USC-18-2232-LII`](../../../bibliography.md#SRC-USC-18-2232-LII): 18 U.S.C. § 2232 (Cornell LII).
3. [`SRC-GRAPHENEOS-FEATURES`](../../../bibliography.md#SRC-GRAPHENEOS-FEATURES): GrapheneOS Features Overview — Duress PIN/Password.
4. [`SRC-TECHCRUNCH-TUNICK-DURESS-2026`](../../../bibliography.md#SRC-TECHCRUNCH-TUNICK-DURESS-2026): TechCrunch Tunick / duress report.
5. [`SRC-TUNICK-MOTION-SUPPRESS-2026`](../../../bibliography.md#SRC-TUNICK-MOTION-SUPPRESS-2026): Tunick motion to suppress.

## Research Debt

- Add border-search Supreme Court / circuit authorities beyond Tunick when intake’d.
- Add comparative materials on other OS duress/panic wipe features.
- Track Tunick suppression outcome and any opinion discussing GrapheneOS or § 2232(a).
- Link Carpenter and Chatrie more tightly once device-vs-cloud search distinctions are drafted.

## Document metadata

- Last verified: `2026-08-08`
