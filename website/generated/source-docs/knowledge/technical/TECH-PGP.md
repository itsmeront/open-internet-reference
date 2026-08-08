---
id: TECH-PGP
title: Pretty Good Privacy (PGP)
type: technology
status: draft
summary: Pretty Good Privacy (PGP) is public-key encryption software created by Phil Zimmermann and published in 1991; its distribution triggered a multi-year U.S. criminal export investigation that closed without prosecution in 1996.
tags:
  - technology
  - cryptography
  - privacy
  - open-source-software
  - export-control
  - speech-and-code
  - case-studies
  - digital-rights
sources:
  - SRC-ZIMMERMANN-BIO
  - SRC-ZIMMERMANN-DECLINATION-1996
  - SRC-ZIMMERMANN-INVESTIGATION-CLOSED
relationships:
  - subject: TECH-PGP
    predicate: cites
    object: SRC-ZIMMERMANN-BIO
    sources:
      - SRC-ZIMMERMANN-BIO
  - subject: TECH-PGP
    predicate: related_to
    object: PERSON-PHIL-ZIMMERMANN
    sources:
      - SRC-ZIMMERMANN-BIO
  - subject: TECH-PGP
    predicate: related_to
    object: EVENT-ZIMMERMANN-PGP-INVESTIGATION
    sources:
      - SRC-ZIMMERMANN-DECLINATION-1996
  - subject: TECH-PGP
    predicate: related_to
    object: TOPIC-END-TO-END-ENCRYPTION
    sources:
      - SRC-ZIMMERMANN-BIO
  - subject: TECH-PGP
    predicate: related_to
    object: TOPIC-CODE-AS-SPEECH
    sources:
      - SRC-ZIMMERMANN-INVESTIGATION-CLOSED
last_verified: "2026-08-08"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/technical/TECH-PGP.md`
- Source ID: `TECH-PGP`
- [**Edit this page**](https://github.com/itsmeront/open-internet-reference/edit/main/knowledge/technical/TECH-PGP.md) | [**Suggest a change**](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml&title=Edit+suggestion:+TECH-PGP)

!!! info "📝 Page Status: Draft — sourced but not yet reviewed"

    - **Status**: `draft`
    - **Sources**: 3
    - **Relationships**: 5
    - **Research debt items**: 3

---

# Pretty Good Privacy (PGP)

## Summary

Pretty Good Privacy (PGP) is encryption software created by Phil Zimmermann and published in 1991. OIR documents PGP as a foundational civilian cryptography system whose USENET distribution led to a closed U.S. criminal export investigation and sits upstream of later code-as-speech litigation about publishing encryption software.

## Verified Facts

- Zimmermann’s official biography states he created Pretty Good Privacy (PGP), published in 1991 as a human-rights-oriented encryption tool.[^1]
- Counsel for Zimmermann published the text of a January 1996 letter from Assistant U.S. Attorney William Keane stating that the U.S. Attorney’s Office for the Northern District of California would not prosecute Zimmermann in connection with the June 1991 USENET posting of Pretty Good Privacy and that the investigation was closed.[^2]
- The same publication includes a U.S. Attorney press statement that the office declined prosecution of any individuals in connection with that June 1991 PGP posting and closed the investigation.[^2]
- EPIC Alert reported on January 11, 1996, that federal prosecutors closed the criminal investigation into Zimmermann without filing charges over PGP distribution.[^3]
- See [EVENT-ZIMMERMANN-PGP-INVESTIGATION](../legal/EVENT-ZIMMERMANN-PGP-INVESTIGATION.md) and [PERSON-PHIL-ZIMMERMANN](../people/PERSON-PHIL-ZIMMERMANN.md).[^1][^2]

## Historical Context

During the 1990s “crypto wars,” U.S. export rules treated strong cryptography as munitions. PGP’s wide distribution made Zimmermann a central figure in debates over civilian encryption. Related First Amendment challenges to encryption-export restraints appear in [Bernstein v. DOJ](../legal/CASE-BERNSTEIN-V-DOJ.md) and [Junger v. Daley](../legal/CASE-JUNGER-V-DALEY.md).


[^1]: [`SRC-ZIMMERMANN-BIO`](../../../bibliography.md#SRC-ZIMMERMANN-BIO) — Phil Zimmermann Official Biography. Self-reported profile; corroboration pending for design details beyond investigation outcome.
[^2]: [`SRC-ZIMMERMANN-DECLINATION-1996`](../../../bibliography.md#SRC-ZIMMERMANN-DECLINATION-1996) — Zimmermann PGP Investigation Closed (Jan. 1996 Declination Letter). Republished government declination text.
[^3]: [`SRC-ZIMMERMANN-INVESTIGATION-CLOSED`](../../../bibliography.md#SRC-ZIMMERMANN-INVESTIGATION-CLOSED) — EPIC Alert — Charges Dropped Against Phil Zimmermann. Secondary contemporaneous report.

## Technical Analysis

Assumptions: This draft treats PGP as the historical software system named in investigation and biography sources. It does not yet distinguish OpenPGP/GnuPG lineage, protocol versions, or current implementations; those require additional primary technical sources.

## Relationships

- `TECH-PGP` cites [`SRC-ZIMMERMANN-BIO`](../../../bibliography.md#SRC-ZIMMERMANN-BIO).
- `TECH-PGP` related_to `PERSON-PHIL-ZIMMERMANN`.
- `TECH-PGP` related_to `EVENT-ZIMMERMANN-PGP-INVESTIGATION`.
- `TECH-PGP` related_to `TOPIC-END-TO-END-ENCRYPTION`.
- `TECH-PGP` related_to `TOPIC-CODE-AS-SPEECH`.

## Sources

1. [`SRC-ZIMMERMANN-BIO`](../../../bibliography.md#SRC-ZIMMERMANN-BIO): Phil Zimmermann Official Biography.
2. [`SRC-ZIMMERMANN-DECLINATION-1996`](../../../bibliography.md#SRC-ZIMMERMANN-DECLINATION-1996): Zimmermann PGP Investigation Closed (Jan. 1996 Declination Letter).
3. [`SRC-ZIMMERMANN-INVESTIGATION-CLOSED`](../../../bibliography.md#SRC-ZIMMERMANN-INVESTIGATION-CLOSED): EPIC Alert — Charges Dropped Against Phil Zimmermann.

## Research Debt

- Add OpenPGP / RFC and GnuPG primary technical sources.
- Add contemporaneous PGP user documentation or source-release announcements from 1991.
- Cross-link export-control statutes and ITAR/EAR history pages when drafted.

## Document metadata

- Last verified: `2026-08-08`
