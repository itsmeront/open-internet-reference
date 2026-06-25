---
id: TOPIC-ONION-ROUTING
title: Onion Routing
type: topic
status: draft
summary: Onion routing is a technique for anonymous communication over a network in which messages pass through multiple relays in layered encryption.
tags:
  - privacy
  - censorship-resistance
  - open-source-software
  - technical
sources:
  - SRC-TOR-PROJECT-HISTORY
  - SRC-TOR-DESIGN-PAPER
relationships:
  - subject: TOPIC-ONION-ROUTING
    predicate: cites
    object: SRC-TOR-PROJECT-HISTORY
    sources:
      - SRC-TOR-PROJECT-HISTORY
  - subject: TOPIC-ONION-ROUTING
    predicate: cites
    object: SRC-TOR-DESIGN-PAPER
    sources:
      - SRC-TOR-DESIGN-PAPER
  - subject: TOPIC-ONION-ROUTING
    predicate: related_to
    object: ORG-TOR-PROJECT
    sources:
      - SRC-TOR-PROJECT-HISTORY
last_verified: "2026-06-19"
---

# Onion Routing

## Summary

Onion routing is a technique for anonymous communication over a network in which messages pass through multiple relays in layered encryption.

## Verified Facts

- The Tor Project history page states that onion routing research began in the mid-1990s.
- The Tor Project history page states that "Tor" stood for The Onion Routing.
- The Tor design paper describes Tor as a circuit-based low-latency anonymous communication service and second-generation onion routing system.
- `ORG-TOR-PROJECT` is the OIR seed organization record for the Tor Project.

## Historical Context

Historical context has not yet been drafted beyond the summary on the official Tor Project history page and the Tor design paper abstract.

## Technical Analysis

Technical analysis has not yet been drafted. Future work should add earlier onion routing research papers and current Tor specification sources.

## Relationships

- `TOPIC-ONION-ROUTING` cites `SRC-TOR-PROJECT-HISTORY`.
- `TOPIC-ONION-ROUTING` cites `SRC-TOR-DESIGN-PAPER`.
- `TOPIC-ONION-ROUTING` related_to `ORG-TOR-PROJECT`.

## Sources

- `SRC-TOR-PROJECT-HISTORY`: Tor Project History Page.
- `SRC-TOR-DESIGN-PAPER`: Tor: The Second-Generation Onion Router.

## Research Debt

- Add primary research papers on early onion routing from the U.S. Naval Research Laboratory.
- Add current Tor specification sources for implementation details.
- Distinguish onion routing as a general technique from Tor-specific implementation details.
