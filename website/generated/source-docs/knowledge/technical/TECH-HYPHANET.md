---
id: TECH-HYPHANET
title: Hyphanet (formerly Freenet)
type: technology
status: draft
summary: Hyphanet is the continuation of the original Freenet peer-to-peer network for anonymous, censorship-resistant publishing; it later added Web of Trust spam-resistance after unmoderated forums were disrupted by spam.
tags:
  - technology
  - privacy
  - censorship-resistance
  - peer-to-peer-networking
  - open-source-software
  - content-moderation
  - case-studies
sources:
  - SRC-HYPHANET-HOME
  - SRC-HYPHANET-RENAME
  - SRC-CLARKE-DDISRS-1999
  - SRC-HYPHANET-WOT-README
  - SRC-DRAKETO-WOT-FRIENDLY-2018
  - SRC-GUARDIAN-FREENET-DARK-SIDE-2009
  - SRC-LWN-GNUNET-INTRO-2005
  - SRC-CLARKE-FREENET-PAPER-2001
  - SRC-FREENET-HISTORY
relationships:
  - subject: TECH-HYPHANET
    predicate: cites
    object: SRC-HYPHANET-HOME
    sources:
      - SRC-HYPHANET-HOME
  - subject: TECH-HYPHANET
    predicate: cites
    object: SRC-CLARKE-DDISRS-1999
    sources:
      - SRC-CLARKE-DDISRS-1999
  - subject: TECH-HYPHANET
    predicate: related_to
    object: PERSON-IAN-CLARKE
    sources:
      - SRC-CLARKE-DDISRS-1999
      - SRC-CLARKE-FREENET-PAPER-2001
      - SRC-HYPHANET-RENAME
  - subject: TECH-HYPHANET
    predicate: related_to
    object: TOPIC-DECENTRALIZED-MODERATION
    sources:
      - SRC-HYPHANET-WOT-README
      - SRC-DRAKETO-WOT-FRIENDLY-2018
  - subject: TECH-HYPHANET
    predicate: related_to
    object: TECH-GNUNET
    sources:
      - SRC-LWN-GNUNET-INTRO-2005
last_verified: "2026-08-08"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/technical/TECH-HYPHANET.md`
- Source ID: `TECH-HYPHANET`
- [**Edit this page**](https://github.com/itsmeront/open-internet-reference/edit/main/knowledge/technical/TECH-HYPHANET.md) | [**Suggest a change**](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml&title=Edit+suggestion:+TECH-HYPHANET)

!!! info "📝 Page Status: Draft — sourced but not yet reviewed"

    - **Status**: `draft`
    - **Sources**: 9
    - **Relationships**: 5
    - **Research debt items**: 5

---

# Hyphanet (formerly Freenet)

## Summary

Hyphanet is free software for anonymous file sharing, freesite publishing, and forums on a decentralized store designed to resist censorship. The project began as Freenet from Ian Clarke's late-1990s design work and renamed to Hyphanet in 2023 after Freenet Project, Inc. reused the Freenet name for a different system.

## Verified Facts

- The official Hyphanet home page describes Hyphanet as free software for anonymously sharing files, browsing and publishing freesites, and using plugins for microblogging, forums, media sharing, and spam resistance without a central authority.[^1]
- An official Hyphanet announcement states that in early 2023 the board of Freenet Project, Inc. renamed its Locutus project to "Freenet," requiring the original Freenet project (begun in 1999) to rename; the community chose the name Hyphanet.[^2]
- [Ian Clarke](../people/PERSON-IAN-CLARKE.md)'s 1999 University of Edinburgh report "A Distributed Decentralised Information Storage and Retrieval System" describes a robust key-indexed storage and retrieval system with no central control or administration, including anonymous publication and retrieval.[^3]
- Clarke co-authored the 2001 Freenet design paper describing anonymous publication, replication, and retrieval without broadcast search or a centralized location index.[^4]
- The Web of Trust plugin README states that in an anonymous, censorship-resistant Freenet-like network, attackers who cannot remove content may instead drown it in spam, and that conventional IP-based or content-download spam filters do not work in that setting.[^5]
- Arne Babenhauserheide's 2018 essay states that Frost, an older Hyphanet forum system, broke down when anonymous users automated spam for months until constructive communication mostly died, and that Web of Trust mechanisms were developed in response.[^6]
- A 2009 Guardian feature quotes Ian Clarke saying Freenet could technically destroy child pornography on Freenet but that modifying Freenet to filter would make Freenet a target for further takedown demands and "would be the end of Freenet."[^7]

## Historical Context

Freenet emerged from student research into decentralized anonymous storage and was publicly associated with both political speech under censorship and with unlawful content. Project maintainers later invested in collaborative reputation systems (Web of Trust, FMS, Sone) for communication layers where central bans were unavailable. The 2023 rename separates the original network's identity from a newer project that took the Freenet name.


[^1]: [`SRC-HYPHANET-HOME`](https://www.hyphanet.org/) — Hyphanet Home Page. Official project page.
[^2]: [`SRC-HYPHANET-RENAME`](https://www.hyphanet.org/freenet-renamed-to-hyphanet.html) — Freenet Renamed to Hyphanet. Official project announcement.
[^3]: [`SRC-CLARKE-DDISRS-1999`](https://cs.baylor.edu/~donahoo/classes/5321/papers/C99.pdf) — A Distributed Decentralised Information Storage and Retrieval System. Primary undergraduate research report.
[^4]: [`SRC-CLARKE-FREENET-PAPER-2001`](https://www.cs.princeton.edu/courses/archive/fall09/cos518/papers/freenet.pdf) — Freenet workshop paper (2001). Primary academic design paper.
[^5]: [`SRC-HYPHANET-WOT-README`](https://github.com/hyphanet/plugin-WebOfTrust/blob/next/README.md) — Hyphanet Web of Trust Plugin README. Official developer documentation.
[^6]: [`SRC-DRAKETO-WOT-FRIENDLY-2018`](https://www.draketo.de/english/freenet/friendly-communication-with-anonymity) — Arne Babenhauserheide essay. Contributor historical account.
[^7]: [`SRC-GUARDIAN-FREENET-DARK-SIDE-2009`](https://www.theguardian.com/technology/2009/nov/26/dark-side-internet-freenet) — The Guardian (2009). Reputable journalism with attributed Clarke quotation.

## Technical Analysis

Assumptions: This page treats Hyphanet's datastore censorship resistance and application-layer Web of Trust filtering as distinct layers. Datastore design aims to make global content removal hard; communication plugins later added subjective trust/spam filtering so users need not download disruptors' traffic. Claims about whether WoT "keeps communication friendly" are contributor evaluations ([`SRC-DRAKETO-WOT-FRIENDLY-2018`](https://www.draketo.de/english/freenet/friendly-communication-with-anonymity)), not independently measured outcomes in this draft.

## Relationships

- `TECH-HYPHANET` cites [`SRC-HYPHANET-HOME`](https://www.hyphanet.org/).
- `TECH-HYPHANET` cites [`SRC-CLARKE-DDISRS-1999`](https://cs.baylor.edu/~donahoo/classes/5321/papers/C99.pdf).
- `TECH-HYPHANET` related_to `PERSON-IAN-CLARKE`.
- `TECH-HYPHANET` related_to `TOPIC-DECENTRALIZED-MODERATION`.
- `TECH-HYPHANET` related_to `TECH-GNUNET`.

## Sources

1. [`SRC-HYPHANET-HOME`](https://www.hyphanet.org/): Hyphanet Home Page.
2. [`SRC-HYPHANET-RENAME`](https://www.hyphanet.org/freenet-renamed-to-hyphanet.html): Freenet Renamed to Hyphanet.
3. [`SRC-CLARKE-DDISRS-1999`](https://cs.baylor.edu/~donahoo/classes/5321/papers/C99.pdf): A Distributed Decentralised Information Storage and Retrieval System.
4. [`SRC-CLARKE-FREENET-PAPER-2001`](https://www.cs.princeton.edu/courses/archive/fall09/cos518/papers/freenet.pdf): Freenet: A Distributed Anonymous Information Storage and Retrieval System (2001).
5. [`SRC-HYPHANET-WOT-README`](https://github.com/hyphanet/plugin-WebOfTrust/blob/next/README.md): Hyphanet Web of Trust Plugin README.
6. [`SRC-DRAKETO-WOT-FRIENDLY-2018`](https://www.draketo.de/english/freenet/friendly-communication-with-anonymity): Arne Babenhauserheide — Hyphanet Web of Trust Keeps Communication Friendly.
7. [`SRC-GUARDIAN-FREENET-DARK-SIDE-2009`](https://www.theguardian.com/technology/2009/nov/26/dark-side-internet-freenet): The Guardian — The Dark Side of the Internet (2009).

### Additional sources

- [`SRC-LWN-GNUNET-INTRO-2005`](https://lwn.net/Articles/162190/): used for the related_to link to `TECH-GNUNET`.
- [`SRC-FREENET-HISTORY`](https://freenet.org/about/history/): Freenet History Page (2023 rename/spin-off from Freenet Project perspective).

## Research Debt

- Add Freenet Project, Inc. / Hyphanet nonprofit organization records.
- Add peer-reviewed follow-ons (including IEEE Internet Computing 2002).
- Locate contemporaneous Frost spam reports beyond later contributor retrospectives.
- Clarify legal cases involving Freenet use (e.g. U.S. prosecutions) with primary dockets.
- Keep naming clear between Hyphanet and the post-2023 Locutus/"Freenet" project ([`SRC-FREENET-HISTORY`](https://freenet.org/about/history/) vs [`SRC-HYPHANET-RENAME`](https://www.hyphanet.org/freenet-renamed-to-hyphanet.html)).

## Document metadata

- Last verified: `2026-08-08`
