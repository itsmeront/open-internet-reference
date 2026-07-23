---
id: CASE-US-V-STORM
title: United States v. Storm
type: case
status: draft
summary: United States v. Storm, No. 1:23-cr-00430 (S.D.N.Y.), is the federal criminal prosecution of Tornado Cash co-founder Roman Storm; in August 2025 he was convicted of conspiring to operate an unlicensed money transmitting business.
tags:
  - case
  - computer-crime
  - sanctions
  - tornado-cash
  - case-studies
  - developer-rights
  - open-source-risk
sources:
  - SRC-DOJ-STORM-INDICTMENT
  - SRC-DOJ-STORM-CONVICTION-2025
  - SRC-TREASURY-SEMENOV-2023
  - SRC-FBI-SEMENOV
relationships:
  - subject: CASE-US-V-STORM
    predicate: cites
    object: SRC-DOJ-STORM-INDICTMENT
    sources:
      - SRC-DOJ-STORM-INDICTMENT
  - subject: CASE-US-V-STORM
    predicate: related_to
    object: TOPIC-TORNADO-CASH
    sources:
      - SRC-DOJ-STORM-INDICTMENT
  - subject: CASE-US-V-STORM
    predicate: related_to
    object: CASE-NL-V-PERTSEV
    sources:
      - SRC-TREASURY-SEMENOV-2023
last_verified: "2026-07-23"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/legal/CASE-US-V-STORM.md`
- Source ID: `CASE-US-V-STORM`
- [**Edit this page**](https://github.com/itsmeront/open-internet-reference/edit/main/knowledge/legal/CASE-US-V-STORM.md) | [**Suggest a change**](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml&title=Edit+suggestion:+CASE-US-V-STORM)

!!! info "📝 Page Status: Draft — sourced but not yet reviewed"

    - **Status**: `draft`
    - **Sources**: 4
    - **Relationships**: 3
    - **Research debt items**: 5
    - **Last verified**: 2026-07-23

---

# United States v. Storm

## Summary

United States v. Storm, No. 1:23-cr-00430 (S.D.N.Y.), is the federal criminal prosecution of Tornado Cash co-founder Roman Storm. In August 2025, the U.S. Attorney’s Office for the Southern District of New York reported that Storm was convicted of conspiring to operate an unlicensed money transmitting business.

## Verified Facts

- On August 23, 2023, Treasury stated that DOJ unsealed an indictment charging Roman Semenov and Roman Storm with conspiracy to commit money laundering, conspiracy to operate an unlicensed money transmitting business, and conspiracy to commit sanctions violations, and that Storm was arrested that day.[^1]
- The government-hosted indictment alleges that Storm and Semenov developed, marketed, and operated Tornado Cash as a cryptocurrency mixing service from which they sought and obtained profits, and that they knew the service was used for large-scale money laundering and sanctions evasion, including services involving the Lazarus Group.[^2]
- The indictment alleges Storm described himself as a cofounder of the Tornado Cash protocol and that Storm, Semenov, and another person (“CC-1”) were principal cofounders from the 2019 public launch through at least about August 8, 2022, when OFAC announced sanctions on Tornado Cash.[^2]
- The FBI Wanted notice for Roman Semenov lists charges of conspiracy to commit money laundering; conspiracy to operate an unlicensed money transmitting business; and conspiracy to violate the International Emergency Economic Powers Act, and states Semenov remains wanted.[^3]
- The U.S. Attorney’s Office for the Southern District of New York states that in August 2025 Roman Storm was convicted of conspiring to operate an unlicensed money transmitting business, and that trial proof showed Tornado Cash transmitted more than $1 billion in criminal proceeds, including hundreds of millions of dollars in proceeds from the Ronin hack publicly attributed by the FBI to the Lazarus Group.[^4]

## Historical Context

OFAC designated Tornado Cash in 2022. In August 2023, DOJ charged Storm and Semenov in the Southern District of New York while OFAC designated Semenov. Storm proceeded to trial in that district. Semenov remained a fugitive according to the FBI Wanted notice.


[^1]: [`SRC-TREASURY-SEMENOV-2023`](../../../bibliography.md#SRC-TREASURY-SEMENOV-2023) — Treasury Designates Roman Semenov, Co-Founder of Tornado Cash (Aug. 23, 2023). Official government press release.
[^2]: [`SRC-DOJ-STORM-INDICTMENT`](../../../bibliography.md#SRC-DOJ-STORM-INDICTMENT) — United States v. Storm / Semenov Indictment (S.D.N.Y. Aug. 2023). Charging instrument; allegations are not adjudicated findings unless proved or admitted.
[^3]: [`SRC-FBI-SEMENOV`](../../../bibliography.md#SRC-FBI-SEMENOV) — FBI Wanted — Roman Semenov. Official FBI Wanted notice.
[^4]: [`SRC-DOJ-STORM-CONVICTION-2025`](../../../bibliography.md#SRC-DOJ-STORM-CONVICTION-2025) — SDNY National Security Page — Roman Storm Conviction Note (Aug. 2025). Official USAO summary.

## Legal Analysis

Jurisdiction: U.S. District Court, Southern District of New York (criminal). Charged theories in the indictment include conspiracies under money-laundering, unlicensed money-transmitting, and IEEPA statutes. An indictment’s allegations are accusations. The USAO summary reports conviction on the unlicensed money-transmitting conspiracy count; disposition of other counts requires docket verification.

## Relationships

- `CASE-US-V-STORM` cites [`SRC-DOJ-STORM-INDICTMENT`](../../../bibliography.md#SRC-DOJ-STORM-INDICTMENT).
- `CASE-US-V-STORM` related_to `TOPIC-TORNADO-CASH`.
- `CASE-US-V-STORM` related_to `CASE-NL-V-PERTSEV`.

## Sources

1. [`SRC-TREASURY-SEMENOV-2023`](../../../bibliography.md#SRC-TREASURY-SEMENOV-2023): Treasury Designates Roman Semenov, Co-Founder of Tornado Cash (Aug. 23, 2023).
2. [`SRC-DOJ-STORM-INDICTMENT`](../../../bibliography.md#SRC-DOJ-STORM-INDICTMENT): United States v. Storm / Semenov Indictment (S.D.N.Y. Aug. 2023).
3. [`SRC-FBI-SEMENOV`](../../../bibliography.md#SRC-FBI-SEMENOV): FBI Wanted — Roman Semenov.
4. [`SRC-DOJ-STORM-CONVICTION-2025`](../../../bibliography.md#SRC-DOJ-STORM-CONVICTION-2025): SDNY National Security Page — Roman Storm Conviction Note (Aug. 2025).

## Research Debt

- Add docket entries / verdict form for hung or mistried counts (money-laundering conspiracy; IEEPA conspiracy) reported in secondary coverage.
- Add defense counsel appearances from PACER/RECAP (Waymaker LLP; Hecker Fink LLP) and assigned judge confirmation.
- Add superseding indictment if filed and used at trial.
- Clarify Semenov’s status on any superseding indictment versus original indictment.
- Link FinCEN/MSB regulatory materials cited at trial once identified.
