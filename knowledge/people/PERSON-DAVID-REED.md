---
id: PERSON-DAVID-REED
title: David P. Reed
type: person
status: draft
summary: David P. Reed is a computer scientist and co-inventor of the end-to-end principle, a foundational Internet design argument, who participated in early TCP/IP work and designed UDP.
tags:
  - person
  - internet-architecture
  - distributed-systems
  - network-protocols
sources:
  - SRC-REED-BIO
relationships:
  - subject: PERSON-DAVID-REED
    predicate: cites
    object: SRC-REED-BIO
    sources:
      - SRC-REED-BIO
last_verified: "2026-07-04"
---

# David P. Reed

## Summary

David P. Reed is a computer scientist and co-inventor of the end-to-end principle, a foundational Internet design argument, who participated in early TCP/IP work and designed UDP.

## Verified Facts

- Co-inventor of the end-to-end argument with Jerome Saltzer and David D. Clark; co-author of the 1984 paper *End-to-End Arguments in System Design*.[^1]
- Participated in early TCP/IP development and designed the User Datagram Protocol (UDP).[^1]
- PhD in computer science and engineering from MIT; former MIT Laboratory for Computer Science faculty member (1978–1983).[^1]
- Adjunct Professor at the MIT Media Lab; co-led the Viral Communications research group.[^1]
- Former HP Fellow; held research and chief scientist roles at Lotus Development, Software Arts, and Interval Research.[^1]
- Formulated Reed's Law on the scaling utility of group-forming networks.[^1]


[^1]: `SRC-REED-BIO` — David P. Reed Official Biography. Self-reported profile; corroboration pending.

## Expert Testimony and Public Advocacy

Reed is frequently cited when courts and regulators need to understand why Internet architecture places intelligence at the edges rather than in intermediary networks. The end-to-end principle is a standard reference in debates about net neutrality, intermediary filtering, and whether network operators can safely implement application-level functions in the core.

## Relevance to Lawsuits Involving Software and Internet Infrastructure

Reed is particularly useful when a case turns on:

- Whether a network intermediary can implement filtering, inspection, or application logic without breaking the system
- Architectural tradeoffs between edge-based and core-based security or policy enforcement
- UDP, connectionless protocols, and real-time application design
- Scalability and group dynamics in networked systems (Reed's Law)

His work helps explain *why* the Internet was designed the way it was — not merely how current products implement it.

## Relationships

- `PERSON-DAVID-REED` cites `SRC-REED-BIO`.

## Sources

1. `SRC-REED-BIO`: David P. Reed Official Biography.

## Research Debt

- Add primary citation for the 1984 end-to-end arguments paper as bibliography source.
- Document specific expert declarations or testimony with court records.
- Cross-link to `PERSON-LAUREN-WEINSTEIN` and net neutrality topic pages.
- Corroborate self-reported biography or about-page claims with independent sources (institutional profile, court docket, case page, or reputable journalism).
