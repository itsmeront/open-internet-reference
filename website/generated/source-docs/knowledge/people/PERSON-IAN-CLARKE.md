---
id: PERSON-IAN-CLARKE
title: Ian Clarke
type: person
status: draft
summary: Ian Clarke is a computer scientist who designed Freenet, founded Freenet Project Inc., and later led the 2023 Freenet relaunch while the original network continued as Hyphanet.
tags:
  - person
  - researcher
  - privacy
  - censorship-resistance
  - peer-to-peer-networking
  - open-source-software
  - content-moderation
  - case-studies
sources:
  - SRC-CLARKE-FREENET-BIO
  - SRC-CLARKE-DDISRS-1999
  - SRC-CLARKE-FREENET-PAPER-2001
  - SRC-FREENET-HISTORY
  - SRC-HYPHANET-RENAME
  - SRC-GUARDIAN-FREENET-DARK-SIDE-2009
  - SRC-TR-IAN-CLARKE
relationships:
  - subject: PERSON-IAN-CLARKE
    predicate: authored
    object: SRC-CLARKE-DDISRS-1999
    sources:
      - SRC-CLARKE-DDISRS-1999
      - SRC-CLARKE-FREENET-BIO
  - subject: PERSON-IAN-CLARKE
    predicate: authored
    object: SRC-CLARKE-FREENET-PAPER-2001
    sources:
      - SRC-CLARKE-FREENET-PAPER-2001
      - SRC-CLARKE-FREENET-BIO
  - subject: PERSON-IAN-CLARKE
    predicate: related_to
    object: TECH-HYPHANET
    sources:
      - SRC-CLARKE-FREENET-BIO
      - SRC-HYPHANET-RENAME
      - SRC-FREENET-HISTORY
  - subject: PERSON-IAN-CLARKE
    predicate: related_to
    object: TOPIC-DECENTRALIZED-MODERATION
    sources:
      - SRC-GUARDIAN-FREENET-DARK-SIDE-2009
last_verified: "2026-08-08"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/people/PERSON-IAN-CLARKE.md`
- Source ID: `PERSON-IAN-CLARKE`
- [**Edit this page**](https://github.com/itsmeront/open-internet-reference/edit/main/knowledge/people/PERSON-IAN-CLARKE.md) | [**Suggest a change**](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml&title=Edit+suggestion:+PERSON-IAN-CLARKE)

!!! info "📝 Page Status: Draft — sourced but not yet reviewed"

    - **Status**: `draft`
    - **Sources**: 7
    - **Relationships**: 4
    - **Research debt items**: 6

---

# Ian Clarke

## Summary

Ian Clarke is a computer scientist and entrepreneur best known for designing Freenet, the censorship-resistant peer-to-peer system that later continued as Hyphanet. He is founder and president of Freenet Project Inc. and led the 2023 decision to apply the Freenet name to a new architecture while spinning off the original network.

## Verified Facts

- Freenet project materials identify Clarke as the creator of Freenet and as founder and president of Freenet Project Inc., described there as a 501(c)(3) nonprofit developing the project.[^1]
- Those materials state that Clarke studied Computer Science and Artificial Intelligence at the University of Edinburgh, graduating in 1999, and that his final-year project became the design that launched Freenet.[^1]
- Clarke's 1999 Edinburgh report, "A Distributed Decentralised Information Storage and Retrieval System," describes a key-indexed storage and retrieval system with no central control or administration and with anonymous publication and retrieval.[^2]
- Clarke is a co-author of the 2001 paper "Freenet: A Distributed Anonymous Information Storage and Retrieval System," which describes Freenet as a peer-to-peer system for anonymous publication, replication, and retrieval without broadcast search or a centralized location index.[^3]
- Freenet's official history page states Freenet was initially developed in 1999 at the University of Edinburgh by Ian Clarke, that Locutus was rebranded as Freenet in March 2023, and that the original Freenet codebase was spun off as Hyphanet.[^4]
- Hyphanet's rename announcement states that Freenet Project, Inc. renamed Locutus to "Freenet," requiring the original Freenet project (begun in 1999) to rename to Hyphanet.[^5]
- Freenet's history page states that, as architect of Freenet and president of the Freenet nonprofit, Clarke made the decision to rebrand Locutus as Freenet and spin off the original codebase as Hyphanet.[^4]
- A 2009 Guardian feature quotes Clarke acknowledging child pornography on Freenet and arguing that adding filters would invite further pressure and "would be the end of Freenet."[^6]
- An MIT Technology Review innovator profile describes Clarke as releasing Freenet in 2000 as anonymous peer-to-peer storage and quotes him: "You cannot have freedom of communication and enforce copyright law."[^7]

## Historical Context

Clarke's student design work seeded one of the earliest widely discussed censorship-resistant anonymous storage networks. Public debate around Freenet repeatedly focused on the absence of central content control. In 2023, project leadership split naming and architecture: the original network continued under Hyphanet maintainers, while Clarke's organization advanced a new Freenet architecture derived from Locutus.


[^1]: [`SRC-CLARKE-FREENET-BIO`](https://freenet.org/about/people/ian-clarke/) — Ian Clarke Freenet Project Biography. Self-reported project biography; corroboration pending for nonprofit status and download counts.
[^2]: [`SRC-CLARKE-DDISRS-1999`](https://cs.baylor.edu/~donahoo/classes/5321/papers/C99.pdf) — A Distributed Decentralised Information Storage and Retrieval System. Primary undergraduate research report.
[^3]: [`SRC-CLARKE-FREENET-PAPER-2001`](https://www.cs.princeton.edu/courses/archive/fall09/cos518/papers/freenet.pdf) — Freenet workshop paper (2001). Primary academic design paper.
[^4]: [`SRC-FREENET-HISTORY`](https://freenet.org/about/history/) — Freenet History Page. Official organization page for the post-2023 Freenet project.
[^5]: [`SRC-HYPHANET-RENAME`](https://www.hyphanet.org/freenet-renamed-to-hyphanet.html) — Freenet Renamed to Hyphanet. Official Hyphanet announcement.
[^6]: [`SRC-GUARDIAN-FREENET-DARK-SIDE-2009`](https://www.theguardian.com/technology/2009/nov/26/dark-side-internet-freenet) — The Guardian (2009). Reputable journalism with attributed quotation.
[^7]: [`SRC-TR-IAN-CLARKE`](https://www.technologyreview.com/innovator/ian-clarke/) — MIT Technology Review innovator profile. Secondary reporting.

## Expert Testimony and Public Advocacy

Clarke has been a long-running public advocate for architectures that make centralized censorship and tracing difficult. OIR's Freenet/Hyphanet moderation topic records his attributed refusal to add global content filters as a concrete statement of that tradeoff. His Technology Review profile likewise frames Freenet as colliding with copyright enforcement and free-communication goals.

## Relevance to Lawsuits Involving Software and Internet Infrastructure

Clarke is particularly useful when a matter involves:

- Anonymous or censorship-resistant peer-to-peer storage design
- Developer liability or public debate over unlawful content on uncensorable networks
- Distinguishing datastore immutability/uncensorability from application-layer spam or trust systems
- Historical precedent for "no central index" systems contrasted with Napster-like architectures

## Relationships

- `PERSON-IAN-CLARKE` authored [`SRC-CLARKE-DDISRS-1999`](https://cs.baylor.edu/~donahoo/classes/5321/papers/C99.pdf).
- `PERSON-IAN-CLARKE` authored [`SRC-CLARKE-FREENET-PAPER-2001`](https://www.cs.princeton.edu/courses/archive/fall09/cos518/papers/freenet.pdf).
- `PERSON-IAN-CLARKE` related_to `TECH-HYPHANET`.
- `PERSON-IAN-CLARKE` related_to `TOPIC-DECENTRALIZED-MODERATION`.

## Sources

1. [`SRC-CLARKE-FREENET-BIO`](https://freenet.org/about/people/ian-clarke/): Ian Clarke — Freenet Project Biography.
2. [`SRC-CLARKE-DDISRS-1999`](https://cs.baylor.edu/~donahoo/classes/5321/papers/C99.pdf): A Distributed Decentralised Information Storage and Retrieval System.
3. [`SRC-CLARKE-FREENET-PAPER-2001`](https://www.cs.princeton.edu/courses/archive/fall09/cos518/papers/freenet.pdf): Freenet: A Distributed Anonymous Information Storage and Retrieval System (2001).
4. [`SRC-FREENET-HISTORY`](https://freenet.org/about/history/): Freenet History Page.
5. [`SRC-HYPHANET-RENAME`](https://www.hyphanet.org/freenet-renamed-to-hyphanet.html): Freenet Renamed to Hyphanet.
6. [`SRC-GUARDIAN-FREENET-DARK-SIDE-2009`](https://www.theguardian.com/technology/2009/nov/26/dark-side-internet-freenet): The Guardian — The Dark Side of the Internet (2009).
7. [`SRC-TR-IAN-CLARKE`](https://www.technologyreview.com/innovator/ian-clarke/): MIT Technology Review — Ian Clarke Innovator Profile.

## Research Debt

- Add Freenet Project Inc. organization and contact records with independent nonprofit verification (IRS/Charity Navigator or equivalent), not only freenet.org self-description.
- Add IEEE Internet Computing 2002 Freenet paper source record.
- Corroborate TR35/TR100 award labeling with a Technology Review list page if the innovator profile alone is treated as insufficient.
- Add ORG page for the current Freenet project distinct from `TECH-HYPHANET`.
- Document Revver/Uprizer and other commercial roles with independent sources if those claims become material.
- Link Clarke quotations in `TOPIC-DECENTRALIZED-MODERATION` and `TECH-HYPHANET` to this person page in body text.

## Document metadata

- Last verified: `2026-08-08`
