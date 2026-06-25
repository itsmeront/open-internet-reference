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

# Signal

## Summary

Signal is documented in OIR from its official website as a nonprofit-associated private messaging service.

## Verified Facts

- Signal maintains an official website at `https://signal.org/`.
- The official website describes Signal as using end-to-end encryption powered by the open source Signal Protocol.
- The official website describes Signal as an independent nonprofit not tied to major tech companies.
- Signal maintains official protocol documentation at `https://signal.org/docs/`.
- Official Signal specifications include X3DH and the Double Ratchet algorithm.

## Historical Context

Historical context has not yet been drafted.

## Analysis

Analysis has not yet been drafted. Future work should use official Signal sources and independent sources to document governance, technical architecture, and history.

## Relationships

- `ORG-SIGNAL` cites `SRC-SIGNAL-HOME`.
- `ORG-SIGNAL` cites `SRC-SIGNAL-DOCS`.
- `ORG-SIGNAL` cites `SRC-SIGNAL-X3DH`.
- `ORG-SIGNAL` cites `SRC-SIGNAL-DOUBLE-RATCHET`.

## Sources

- `SRC-SIGNAL-HOME`: Signal Official Website.
- `SRC-SIGNAL-DOCS`: Signal Protocol Documentation.
- `SRC-SIGNAL-X3DH`: The X3DH Key Agreement Protocol.
- `SRC-SIGNAL-DOUBLE-RATCHET`: The Double Ratchet Algorithm.

## Research Debt

- Add official organization, foundation, or governance source if distinct from the homepage.
- Add independent sources for history and organizational structure.
