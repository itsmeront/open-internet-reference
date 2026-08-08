---
id: TECH-SAMOURAI-WALLET
title: Samourai Wallet
type: technology
status: draft
summary: Samourai Wallet was a Bitcoin privacy wallet whose co-founders pled guilty in 2025 in S.D.N.Y. to conspiracy to operate a money transmitting business knowing it transmitted crime proceeds; government announcements describe mixer features including Whirlpool.
tags:
  - technology
  - privacy
  - privacy-preserving-systems
  - open-source-risk
  - developer-rights
  - case-studies
  - computer-crime
  - digital-rights
sources:
  - SRC-IRS-SAMOURAI-PLEA-2025
  - SRC-IRS-SAMOURAI-SENTENCE-2025
relationships:
  - subject: TECH-SAMOURAI-WALLET
    predicate: cites
    object: SRC-IRS-SAMOURAI-PLEA-2025
    sources:
      - SRC-IRS-SAMOURAI-PLEA-2025
  - subject: TECH-SAMOURAI-WALLET
    predicate: related_to
    object: CASE-US-V-RODRIGUEZ
    sources:
      - SRC-IRS-SAMOURAI-PLEA-2025
  - subject: TECH-SAMOURAI-WALLET
    predicate: related_to
    object: TOPIC-DEVELOPER-SOFTWARE-LIABILITY
    sources:
      - SRC-IRS-SAMOURAI-PLEA-2025
  - subject: TECH-SAMOURAI-WALLET
    predicate: related_to
    object: TECH-TORNADO-CASH
    sources:
      - SRC-IRS-SAMOURAI-PLEA-2025
last_verified: "2026-08-08"
---

# Samourai Wallet

## Summary

Samourai Wallet is documented in OIR from U.S. government announcements about the criminal prosecution of its co-founders. Prosecutors described Samourai as a cryptocurrency mixer that facilitated large volumes of illegal transactions; the co-founders pled guilty in 2025 and received prison sentences. This page records the system as a privacy-tech pressure point and does not treat prosecutorial feature descriptions as independent technical specifications.

## Verified Facts

- IRS-CI announced that Samourai Wallet co-founders Keonne Rodriguez (CEO) and William Lonergan Hill (CTO) pled guilty on July 30, 2025, in S.D.N.Y. to conspiracy to operate a money transmitting business knowing the business transmitted crime proceeds.[^1]
- The plea announcement describes Samourai as a cryptocurrency mixer that facilitated more than $200 million in illegal transactions.[^1]
- The sentencing announcement states Rodriguez and Hill actively promoted Samourai to criminal users, including Hill marketing on a darknet forum and Rodriguez encouraging hackers on Twitter to send proceeds into Samourai’s Whirlpool.[^2]
- Rodriguez was sentenced to five years and Hill to four years in November 2025.[^2]
- See [United States v. Rodriguez (Samourai Wallet)](../legal/CASE-US-V-RODRIGUEZ.md).[^1]

## Historical Context

Samourai sits in the same OIR cluster as Tornado Cash and other financial-privacy tools facing money-transmission, sanctions, or laundering theories aimed at developers and operators. Government announcements are the current primary sources for OIR’s system description; independent technical documentation remains research debt.


[^1]: `SRC-IRS-SAMOURAI-PLEA-2025` — IRS-CI Samourai Wallet Founders Plead Guilty (July 30, 2025). Official government announcement.
[^2]: `SRC-IRS-SAMOURAI-SENTENCE-2025` — IRS-CI Samourai Wallet Founders Sentenced (Nov. 2025). Official government announcement.

## Technical Analysis

Assumptions: Feature names such as Whirlpool appear in government charging narratives. OIR does not yet cite Samourai’s own technical docs for architecture claims. Treat mixer/privacy-tool characterizations as prosecutorial descriptions unless corroborated by primary software documentation.

## Relationships

- `TECH-SAMOURAI-WALLET` cites `SRC-IRS-SAMOURAI-PLEA-2025`.
- `TECH-SAMOURAI-WALLET` related_to `CASE-US-V-RODRIGUEZ`.
- `TECH-SAMOURAI-WALLET` related_to `TOPIC-DEVELOPER-SOFTWARE-LIABILITY`.
- `TECH-SAMOURAI-WALLET` related_to `TECH-TORNADO-CASH`.

## Sources

1. `SRC-IRS-SAMOURAI-PLEA-2025`: IRS-CI — Samourai Wallet Founders Plead Guilty (July 30, 2025).
2. `SRC-IRS-SAMOURAI-SENTENCE-2025`: IRS-CI — Samourai Wallet Founders Sentenced (Nov. 2025).

## Research Debt

- Add Samourai technical documentation or archived project pages describing Whirlpool/Ricochet.
- Add indictment PDF and plea agreement text via the related case page’s research debt.
- Distinguish custodial vs non-custodial mixer theories with primary legal filings.
