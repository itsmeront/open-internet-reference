---
id: ORG-TOR-PROJECT
title: Tor Project
type: organization
status: draft
summary: Tor Project is a nonprofit organization documented in OIR from official Tor Project pages about privacy and onion routing technology.
tags:
  - organization
  - privacy
  - open-source-software
  - outreach
sources:
  - SRC-TOR-PROJECT-CONTACT
  - SRC-TOR-PROJECT-HISTORY
relationships:
  - subject: ORG-TOR-PROJECT
    predicate: cites
    object: SRC-TOR-PROJECT-CONTACT
    sources:
      - SRC-TOR-PROJECT-CONTACT
  - subject: ORG-TOR-PROJECT
    predicate: cites
    object: SRC-TOR-PROJECT-HISTORY
    sources:
      - SRC-TOR-PROJECT-HISTORY
  - subject: ORG-TOR-PROJECT
    predicate: related_to
    object: TOPIC-ONION-ROUTING
    sources:
      - SRC-TOR-PROJECT-HISTORY
last_verified: "2026-06-19"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/organizations/ORG-TOR-PROJECT.md`
- Source ID: `ORG-TOR-PROJECT`

---

# Tor Project

## Summary

Tor Project is a nonprofit organization documented in OIR from official Tor Project pages about privacy and onion routing technology.

## Verified Facts

- The Tor Project maintains an official contact page at <https://www.torproject.org/about/contact/>.
- The Tor Project maintains an official history page at <https://www.torproject.org/about/history/>.
- The official history page states that The Tor Project, Inc. became a 501(c)(3) nonprofit in 2006.
- The official history page states that onion routing research began in the mid-1990s and that "Tor" stood for The Onion Routing.

## Historical Context

Historical context has not yet been drafted beyond the summary on the official history page.

## Analysis

Analysis has not yet been drafted. Future work should add primary research sources for onion routing design and deployment.

## Relationships

- `ORG-TOR-PROJECT` cites [`SRC-TOR-PROJECT-CONTACT`](https://www.torproject.org/about/contact/).
- `ORG-TOR-PROJECT` cites [`SRC-TOR-PROJECT-HISTORY`](https://www.torproject.org/about/history/).
- `ORG-TOR-PROJECT` related_to `TOPIC-ONION-ROUTING`.

## Sources

- [`SRC-TOR-PROJECT-CONTACT`](https://www.torproject.org/about/contact/): Tor Project Contact Page.
- [`SRC-TOR-PROJECT-HISTORY`](https://www.torproject.org/about/history/): Tor Project History Page.

## Research Debt

- Add primary research papers on onion routing.
- Add independent sources for technical work and governance.
- Create a separate contact record only after outreach use requirements are defined.
