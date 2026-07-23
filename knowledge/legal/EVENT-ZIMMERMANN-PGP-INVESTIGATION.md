---
id: EVENT-ZIMMERMANN-PGP-INVESTIGATION
title: U.S. Criminal Investigation of Phil Zimmermann / PGP (Closed 1996)
type: historical_event
status: draft
summary: U.S. authorities investigated Phil Zimmermann for years over distribution of Pretty Good Privacy (PGP) encryption software; the Northern District of California U.S. Attorney declined prosecution and closed the investigation in January 1996.
tags:
  - historical-event
  - cryptography
  - export-control
  - open-source-risk
  - developer-rights
  - speech-and-code
  - case-studies
sources:
  - SRC-ZIMMERMANN-DECLINATION-1996
  - SRC-ZIMMERMANN-INVESTIGATION-CLOSED
  - SRC-ZIMMERMANN-BIO
relationships:
  - subject: EVENT-ZIMMERMANN-PGP-INVESTIGATION
    predicate: cites
    object: SRC-ZIMMERMANN-DECLINATION-1996
    sources:
      - SRC-ZIMMERMANN-DECLINATION-1996
  - subject: EVENT-ZIMMERMANN-PGP-INVESTIGATION
    predicate: related_to
    object: PERSON-PHIL-ZIMMERMANN
    sources:
      - SRC-ZIMMERMANN-DECLINATION-1996
  - subject: EVENT-ZIMMERMANN-PGP-INVESTIGATION
    predicate: related_to
    object: TOPIC-DEVELOPER-SOFTWARE-LIABILITY
    sources:
      - SRC-ZIMMERMANN-DECLINATION-1996
  - subject: EVENT-ZIMMERMANN-PGP-INVESTIGATION
    predicate: related_to
    object: CASE-BERNSTEIN-V-DOJ
    sources:
      - SRC-ZIMMERMANN-INVESTIGATION-CLOSED
last_verified: "2026-07-23"
---

# U.S. Criminal Investigation of Phil Zimmermann / PGP (Closed 1996)

## Summary

U.S. authorities investigated Phil Zimmermann in connection with distribution of Pretty Good Privacy (PGP) encryption software. In January 1996, the U.S. Attorney for the Northern District of California declined prosecution and closed the investigation.

## Verified Facts

- Counsel for Zimmermann published the text of a letter from Assistant U.S. Attorney William Keane stating that the U.S. Attorney’s Office for the Northern District of California decided Zimmermann would not be prosecuted in connection with the posting to USENET in June 1991 of Pretty Good Privacy, and that the investigation was closed.[^1]
- The same publication includes a U.S. Attorney press statement that the office declined prosecution of any individuals in connection with the June 1991 USENET posting of PGP and that the investigation was closed.[^1]
- EPIC Alert reported on January 11, 1996, that federal prosecutors closed the criminal investigation into Zimmermann without filing charges over PGP distribution.[^2]
- Zimmermann’s official biography states he created PGP, published in 1991, and was subject to a multi-year U.S. criminal investigation related to cryptographic software export that closed without indictment in 1996.[^3]

## Historical Context

PGP was widely distributed encryption software. Export-control rules treated certain cryptography as munitions during the 1990s. The Zimmermann matter ended by declination of prosecution rather than by trial verdict.


[^1]: `SRC-ZIMMERMANN-DECLINATION-1996` — Phil Zimmermann — PGP Investigation Closed (Jan. 1996 Declination Letter). Republished government declination text.
[^2]: `SRC-ZIMMERMANN-INVESTIGATION-CLOSED` — EPIC Alert — Charges Dropped Against Phil Zimmermann. Secondary contemporaneous report.
[^3]: `SRC-ZIMMERMANN-BIO` — Phil Zimmermann Official Biography. Self-reported profile; corroboration pending for biographical details beyond the declination.

## Legal Analysis

No indictment or conviction issued. Documented outcome is prosecutorial declination in N.D. Cal. Related First Amendment / export litigation involving other parties appears in [Bernstein v. DOJ](CASE-BERNSTEIN-V-DOJ.md) and [Junger v. Daley](CASE-JUNGER-V-DALEY.md).

## Relationships

- `EVENT-ZIMMERMANN-PGP-INVESTIGATION` cites `SRC-ZIMMERMANN-DECLINATION-1996`.
- `EVENT-ZIMMERMANN-PGP-INVESTIGATION` related_to `PERSON-PHIL-ZIMMERMANN`.
- `EVENT-ZIMMERMANN-PGP-INVESTIGATION` related_to `TOPIC-DEVELOPER-SOFTWARE-LIABILITY`.
- `EVENT-ZIMMERMANN-PGP-INVESTIGATION` related_to `CASE-BERNSTEIN-V-DOJ`.

## Sources

1. `SRC-ZIMMERMANN-DECLINATION-1996`: Phil Zimmermann — PGP Investigation Closed (Jan. 1996 Declination Letter).
2. `SRC-ZIMMERMANN-INVESTIGATION-CLOSED`: EPIC Alert — Charges Dropped Against Phil Zimmermann.
3. `SRC-ZIMMERMANN-BIO`: Phil Zimmermann Official Biography.

## Research Debt

- Locate original U.S. Attorney PDF/letter on a government archive if available.
- Add Arms Export Control Act / ITAR regulatory citations contemporaneous to the investigation.
- Link published PGP source-code book (MIT Press) as a dedicated source record.
