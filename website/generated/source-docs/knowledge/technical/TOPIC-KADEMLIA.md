---
id: TOPIC-KADEMLIA
title: Kademlia
type: topic
status: draft
summary: Kademlia is a peer-to-peer distributed hash table described in a 2002 paper by Petar Maymounkov and David Mazières.
tags:
  - peer-to-peer-networking
  - distributed-systems
  - distributed-hash-tables
sources:
  - SRC-KADEMLIA-PAPER
relationships:
  - subject: TOPIC-KADEMLIA
    predicate: cites
    object: SRC-KADEMLIA-PAPER
    sources:
      - SRC-KADEMLIA-PAPER
last_verified: "2026-06-17"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/technical/TOPIC-KADEMLIA.md`
- Source ID: `TOPIC-KADEMLIA`
- [:material-pencil: Edit this page](https://github.com/itsmeront/open-internet-reference/edit/main/knowledge/technical/TOPIC-KADEMLIA.md){ .md-button }  [:material-comment-alert-outline: Suggest a change](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml&title=Edit+suggestion:+TOPIC-KADEMLIA){ .md-button }

!!! info "📝 Page Status: Draft — sourced but not yet reviewed"

    - **Status**: `draft`
    - **Sources**: 1
    - **Relationships**: 1
    - **Research debt items**: 3
    - **Last verified**: 2026-06-17

---

# Kademlia

## Summary

Kademlia is a peer-to-peer distributed hash table described in a 2002 paper by Petar Maymounkov and David Mazières.

## Verified Facts

- The paper "Kademlia: A Peer-to-Peer Information System Based on the XOR Metric" was published in 2002.
- The paper is authored by Petar Maymounkov and David Mazières.

## Historical Context

This page is currently a seed record. Broader historical context should compare Kademlia with other distributed hash table systems only after those sources are added.

## Technical Analysis

Technical analysis has not yet been drafted. Future work should summarize the XOR metric, routing behavior, and fault-tolerance claims directly from the Kademlia paper.

## Relationships

- `TOPIC-KADEMLIA` cites [`SRC-KADEMLIA-PAPER`](https://pdos.csail.mit.edu/~petar/papers/maymounkov-kademlia.pdf).

## Sources

- [`SRC-KADEMLIA-PAPER`](https://pdos.csail.mit.edu/~petar/papers/maymounkov-kademlia.pdf): Kademlia: A Peer-to-Peer Information System Based on the XOR Metric.

## Research Debt

- Add pages for distributed hash tables and peer-to-peer networking.
- Verify and document later real-world uses of Kademlia.
- Add relationships to DHT, peer-to-peer, and content-addressing topics after those pages exist.
