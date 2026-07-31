---
id: TECH-GRAPHENEOS
title: GrapheneOS
type: technology
status: draft
summary: GrapheneOS is a privacy- and security-focused open-source mobile operating system for Google Pixel devices that documents an optional duress PIN/password which irreversibly wipes the device when entered.
tags:
  - technology
  - privacy
  - open-source-software
  - cryptography
  - digital-rights
  - border-search
sources:
  - SRC-GRAPHENEOS-FEATURES
  - SRC-TECHCRUNCH-TUNICK-DURESS-2026
  - SRC-TECHSPOT-TUNICK-GRAPHENEOS-2026
  - SRC-TUNICK-INDICTMENT-2025
relationships:
  - subject: TECH-GRAPHENEOS
    predicate: cites
    object: SRC-GRAPHENEOS-FEATURES
    sources:
      - SRC-GRAPHENEOS-FEATURES
  - subject: TECH-GRAPHENEOS
    predicate: related_to
    object: CASE-US-V-TUNICK
    sources:
      - SRC-TECHCRUNCH-TUNICK-DURESS-2026
last_verified: "2026-07-27"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/technical/TECH-GRAPHENEOS.md`
- Source ID: `TECH-GRAPHENEOS`
- [**Edit this page**](https://github.com/itsmeront/open-internet-reference/edit/main/knowledge/technical/TECH-GRAPHENEOS.md) | [**Suggest a change**](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml&title=Edit+suggestion:+TECH-GRAPHENEOS)

!!! info "📝 Page Status: Draft — sourced but not yet reviewed"

    - **Status**: `draft`
    - **Sources**: 4
    - **Relationships**: 2
    - **Research debt items**: 3

---

# GrapheneOS

## Summary

GrapheneOS is a privacy- and security-focused open-source mobile operating system that runs on supported Google Pixel phones. Official documentation describes an optional duress PIN/password that irreversibly wipes the device (and installed eSIMs) when entered in place of ordinary unlock credentials.[^1]

## Verified Facts

- GrapheneOS’s features documentation states that users can set a duress PIN/password that will irreversibly wipe the device, along with any installed eSIMs, once entered anywhere device credentials are requested (including the lock screen).[^1]
- The same documentation states the wipe does not require a reboot and cannot be interrupted, and that both a duress PIN and a duress password are mandatory to enable the feature.[^1]
- The documentation states that if the duress PIN/password is the same as the actual unlock method, the actual unlock method takes precedence and no wipe occurs.[^1]
- TechCrunch reported that counsel for Samuel Tunick confirmed GrapheneOS was running on the phone at issue in [United States v. Tunick](../legal/CASE-US-V-TUNICK.md).[^2]
- TechSpot’s coverage likewise centers the Tunick prosecution on GrapheneOS wipe/passcode features during an airport search.[^3]
- The Tunick indictment alleges deletion of digital contents of a Google Pixel phone but does not name GrapheneOS.[^4]

## Historical Context

Public reporting in 2026 connected GrapheneOS’s duress wipe capability to a Northern District of Georgia prosecution alleging that providing a passcode during a CBP secondary inspection caused deletion of phone data. OIR separates the project’s documented feature set from unresolved case-specific facts about which software and credential were used.


[^1]: [`SRC-GRAPHENEOS-FEATURES`](../../../bibliography.md#SRC-GRAPHENEOS-FEATURES) — GrapheneOS Features Overview (Duress PIN/Password). Official project documentation.
[^2]: [`SRC-TECHCRUNCH-TUNICK-DURESS-2026`](../../../bibliography.md#SRC-TECHCRUNCH-TUNICK-DURESS-2026) — TechCrunch (July 24, 2026). Secondary journalism; counsel confirmation attributed by TechCrunch.
[^3]: [`SRC-TECHSPOT-TUNICK-GRAPHENEOS-2026`](https://www.techspot.com/news/113236-us-prosecutors-charge-atlanta-man-after-grapheneos-phone.html) — TechSpot Tunick / GrapheneOS report. Secondary journalism.
[^4]: [`SRC-TUNICK-INDICTMENT-2025`](../../../bibliography.md#SRC-TUNICK-INDICTMENT-2025) — United States v. Tunick Indictment (Nov. 13, 2025). Charging instrument.

## Technical Analysis

Assumptions: This page relies on GrapheneOS’s public feature description rather than an independent code audit. A duress credential is an optional, user-configured unlock-path input that triggers an irreversible wipe rather than unlocking user data. Whether any particular wipe in a law-enforcement encounter was caused by GrapheneOS duress credentials is a fact question for the underlying case record and is not established solely by the existence of the feature.

## Relationships

- `TECH-GRAPHENEOS` cites [`SRC-GRAPHENEOS-FEATURES`](../../../bibliography.md#SRC-GRAPHENEOS-FEATURES).
- `TECH-GRAPHENEOS` related_to `CASE-US-V-TUNICK`.

## Sources

1. [`SRC-GRAPHENEOS-FEATURES`](../../../bibliography.md#SRC-GRAPHENEOS-FEATURES): GrapheneOS Features Overview — Duress PIN/Password.
2. [`SRC-TECHCRUNCH-TUNICK-DURESS-2026`](../../../bibliography.md#SRC-TECHCRUNCH-TUNICK-DURESS-2026): TechCrunch — DOJ Accuses American of Wiping Phone with Duress Password (July 24, 2026).
3. [`SRC-TECHSPOT-TUNICK-GRAPHENEOS-2026`](https://www.techspot.com/news/113236-us-prosecutors-charge-atlanta-man-after-grapheneos-phone.html): TechSpot — Prosecutors Charge Atlanta Man After GrapheneOS Phone Wipe.
4. [`SRC-TUNICK-INDICTMENT-2025`](../../../bibliography.md#SRC-TUNICK-INDICTMENT-2025): United States v. Tunick — Indictment (N.D. Ga. Nov. 13, 2025).

## Research Debt

- Locate a primary court filing that names GrapheneOS (if any) rather than relying on press-attributed counsel statements.
- Add GrapheneOS about/FAQ and supported-device documentation source records.
- Document other OS/vendor “duress wipe” or panic-credential features for comparative technical context.

## Document metadata

- Last verified: `2026-07-27`
