---
id: CASE-US-V-RODRIGUEZ
title: United States v. Rodriguez (Samourai Wallet)
type: case
status: draft
summary: Keonne Rodriguez and William Lonergan Hill, co-founders of Samourai Wallet, pled guilty in S.D.N.Y. to conspiracy to operate a money transmitting business knowing it transmitted crime proceeds and were sentenced to five and four years in prison.
tags:
  - case
  - computer-crime
  - open-source-risk
  - developer-rights
  - privacy
  - case-studies
sources:
  - SRC-IRS-SAMOURAI-PLEA-2025
  - SRC-IRS-SAMOURAI-SENTENCE-2025
relationships:
  - subject: CASE-US-V-RODRIGUEZ
    predicate: cites
    object: SRC-IRS-SAMOURAI-PLEA-2025
    sources:
      - SRC-IRS-SAMOURAI-PLEA-2025
  - subject: CASE-US-V-RODRIGUEZ
    predicate: related_to
    object: TOPIC-DEVELOPER-SOFTWARE-LIABILITY
    sources:
      - SRC-IRS-SAMOURAI-PLEA-2025
  - subject: CASE-US-V-RODRIGUEZ
    predicate: related_to
    object: CASE-US-V-STORM
    sources:
      - SRC-IRS-SAMOURAI-PLEA-2025
last_verified: "2026-07-23"
---

# United States v. Rodriguez (Samourai Wallet)

## Summary

Keonne Rodriguez and William Lonergan Hill, co-founders of Samourai Wallet, pled guilty in the Southern District of New York to conspiracy to operate a money transmitting business knowing the business transmitted crime proceeds, and were sentenced to five years and four years in prison, respectively.

## Verified Facts

- IRS-CI and SDNY prosecutors announced that Rodriguez (CEO) and Hill (CTO), co-founders of Samourai Wallet, pled guilty on July 30, 2025, before U.S. District Judge Denise L. Cote to participating in a conspiracy to operate a money transmitting business that transmitted crime proceeds.[^1]
- The plea announcement states each pled guilty to one count of conspiracy to operate a money transmitting business knowing the business transmitted crime proceeds, carrying a maximum sentence of five years in prison, and that as part of plea agreements they agreed to forfeit $237,832,360.55.[^1]
- The plea announcement describes Samourai as a cryptocurrency mixer that facilitated more than $200 million in illegal transactions, and states Hill was a U.S. national arrested in Portugal.[^1]
- IRS-CI announced that Rodriguez was sentenced to five years in prison on November 6, 2025, and Hill to four years on November 19, 2025, before Judge Denise L. Cote.[^2]
- The sentencing announcement states the conspiracy involved knowingly transmitting criminal proceeds exceeding $237 million from sources including drug trafficking, darknet marketplaces, cyber-intrusions, frauds, sanctioned jurisdictions, murder-for-hire schemes, and a child pornography website, as alleged by the government.[^2]
- The sentencing announcement states Rodriguez and Hill actively promoted Samourai to criminal users, including Hill marketing on a darknet forum and Rodriguez encouraging hackers on Twitter to send proceeds into Samourai’s Whirlpool.[^2]

## Historical Context

Samourai Wallet provided Bitcoin privacy features including Whirlpool and Ricochet, as described in government announcements. Criminal proceedings in S.D.N.Y. produced guilty pleas in July 2025 and sentences in November 2025.


[^1]: `SRC-IRS-SAMOURAI-PLEA-2025` — IRS-CI Samourai Wallet Founders Plead Guilty (July 30, 2025). Official government announcement.
[^2]: `SRC-IRS-SAMOURAI-SENTENCE-2025` — IRS-CI Samourai Wallet Founders Sentenced (Nov. 2025). Official government announcement.

## Legal Analysis

Jurisdiction: U.S. District Court, Southern District of New York (criminal). Documented disposition is a guilty plea to a conspiracy count involving operation of a money transmitting business with knowledge that the business transmitted crime proceeds, followed by custodial sentences. Government descriptions of software features and user criminality are prosecutorial allegations accepted to the extent embodied in the plea; full indictment text and docket entries remain research debt.

## Relationships

- `CASE-US-V-RODRIGUEZ` cites `SRC-IRS-SAMOURAI-PLEA-2025`.
- `CASE-US-V-RODRIGUEZ` related_to `TOPIC-DEVELOPER-SOFTWARE-LIABILITY`.
- `CASE-US-V-RODRIGUEZ` related_to `CASE-US-V-STORM`.

## Sources

1. `SRC-IRS-SAMOURAI-PLEA-2025`: IRS-CI — Samourai Wallet Founders Plead Guilty (July 30, 2025).
2. `SRC-IRS-SAMOURAI-SENTENCE-2025`: IRS-CI — Samourai Wallet Founders Sentenced (Nov. 2025).

## Research Debt

- Add SDNY docket number, indictment PDF, and plea agreement text.
- Add DOJ USAO-SDNY parallel press releases as cross-sources.
- Document whether money-laundering counts were charged and dismissed or not pursued.
- Add technical primary sources describing Whirlpool/Ricochet architecture.
