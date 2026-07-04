---
id: ORG-SIGNAL
title: Signal
type: organization
status: draft
summary: Signal is documented in OIR from its official website as a nonprofit-associated private messaging service.
tags:
  - organization
  - privacy
  - secure-messaging
sources:
  - SRC-SIGNAL-HOME
  - SRC-SIGNAL-DOCS
  - SRC-SIGNAL-X3DH
  - SRC-SIGNAL-DOUBLE-RATCHET
relationships:
  - subject: ORG-SIGNAL
    predicate: cites
    object: SRC-SIGNAL-HOME
    sources:
      - SRC-SIGNAL-HOME
  - subject: ORG-SIGNAL
    predicate: cites
    object: SRC-SIGNAL-DOCS
    sources:
      - SRC-SIGNAL-DOCS
  - subject: ORG-SIGNAL
    predicate: cites
    object: SRC-SIGNAL-X3DH
    sources:
      - SRC-SIGNAL-X3DH
  - subject: ORG-SIGNAL
    predicate: cites
    object: SRC-SIGNAL-DOUBLE-RATCHET
    sources:
      - SRC-SIGNAL-DOUBLE-RATCHET
last_verified: "2026-06-19"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/organizations/ORG-SIGNAL.md`
- Source ID: `ORG-SIGNAL`
- [**Edit this page**](https://github.com/itsmeront/open-internet-reference/edit/main/knowledge/organizations/ORG-SIGNAL.md) | [**Suggest a change**](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml&title=Edit+suggestion:+ORG-SIGNAL)

!!! info "📝 Page Status: Draft — sourced but not yet reviewed"

    - **Status**: `draft`
    - **Sources**: 4
    - **Relationships**: 4
    - **Research debt items**: 3
    - **Last verified**: 2026-06-19

---

# Signal

## Summary

Signal is documented in OIR from its official website as a nonprofit-associated private messaging service.

## Verified Facts

- Signal maintains an official website at <https://signal.org/>.[^1]
- The official website describes Signal as using end-to-end encryption powered by the open source Signal Protocol.[^1]
- The official website describes Signal as an independent nonprofit not tied to major tech companies.[^1]
- Signal maintains official protocol documentation at <https://signal.org/docs/>.[^1]
- Official Signal specifications include X3DH and the Double Ratchet algorithm.[^1]

## Historical Context

Historical context has not yet been drafted.


[^1]: [`SRC-SIGNAL-HOME`](https://signal.org/) — Signal Official Website. Official source; review reliability tier.

## Analysis

Analysis has not yet been drafted. Future work should use official Signal sources and independent sources to document governance, technical architecture, and history.

## Relationships

- `ORG-SIGNAL` cites [`SRC-SIGNAL-HOME`](https://signal.org/).
- `ORG-SIGNAL` cites [`SRC-SIGNAL-DOCS`](https://signal.org/docs/).
- `ORG-SIGNAL` cites [`SRC-SIGNAL-X3DH`](https://signal.org/docs/specifications/x3dh/x3dh.pdf).
- `ORG-SIGNAL` cites [`SRC-SIGNAL-DOUBLE-RATCHET`](https://signal.org/docs/specifications/doubleratchet/doubleratchet.pdf).

## Sources

1. [`SRC-SIGNAL-HOME`](https://signal.org/): Signal Official Website.

Additional sources (not yet cited in footnotes):

- [`SRC-SIGNAL-DOCS`](https://signal.org/docs/): Signal Protocol Documentation.
- [`SRC-SIGNAL-X3DH`](https://signal.org/docs/specifications/x3dh/x3dh.pdf): The X3DH Key Agreement Protocol.
- [`SRC-SIGNAL-DOUBLE-RATCHET`](https://signal.org/docs/specifications/doubleratchet/doubleratchet.pdf): The Double Ratchet Algorithm.

## Research Debt

- Add official organization, foundation, or governance source if distinct from the homepage.
- Add independent sources for history and organizational structure.
- Review per-fact footnote-to-source mapping; multiple sources are cited on this page.
