# Data Model

## Design Goals

OIR uses Markdown as the human-editable source format and structured front matter as the machine-readable metadata layer.

The model should support:

- Durable page identifiers
- Evidence-backed relationships
- Review status
- Research debt
- Website publishing
- Knowledge graph export
- Bibliography, glossary, timeline, and retrieval dataset generation

## Identifier Prefixes

Use uppercase identifiers with stable prefixes:

- `TOPIC-` topic or concept
- `ORG-` organization
- `PERSON-` person
- `ATT-` attorney
- `JUDGE-` judge
- `CASE-` court case
- `COURT-` court
- `STAT-` statute
- `REG-` regulation
- `TECH-` technology
- `PROTOCOL-` protocol
- `PAPER-` academic paper
- `BOOK-` book
- `EVENT-` historical event
- `SRC-` source record

## Required Front Matter

Knowledge pages should include:

```yaml
---
id: TOPIC-EXAMPLE
title: Example Topic
type: topic
status: draft
summary: One-sentence neutral summary.
tags:
  - internet-architecture
sources: []
relationships: []
last_verified: null
---
```

## Entity Types

Initial entity types:

- `topic`
- `organization`
- `person`
- `attorney`
- `judge`
- `court`
- `case`
- `statute`
- `regulation`
- `technology`
- `protocol`
- `academic_paper`
- `book`
- `historical_event`
- `source`

## Relationship Model

Relationships are first-class data and must be evidence-backed.

Relationship records should capture:

```yaml
subject: ORG-EXAMPLE
predicate: represented_by
object: ATT-EXAMPLE
sources:
  - SRC-EXAMPLE
notes: Optional explanation of scope or uncertainty.
```

Initial predicates:

- `represented_by`
- `argued`
- `decided`
- `interprets`
- `cites`
- `authored`
- `published`
- `implements`
- `standardizes`
- `funded_by`
- `affiliated_with`
- `opposes`
- `supports`
- `related_to`

## Review Status

Valid status values:

- `draft`
- `needs_sources`
- `in_review`
- `verified`
- `deprecated`

## Generated Data

Generated artifacts should be written under `generated/`. Human-authored source files should not depend on generated files as the only source of truth.
