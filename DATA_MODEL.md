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
- `CONTACT-` outreach contact record

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

## Optional Front Matter

### Timeline date fields

These optional fields feed the public timeline. Format: `YYYY`, `YYYY-MM`, or `YYYY-MM-DD`.

| Field | Typical use | Timeline label |
| --- | --- | --- |
| `event_date` | Historical events and other one-off milestones | Historical event |
| `decision_date` | Court decisions, judgments, convictions, pleas, or other dispositive case outcomes | Decision |
| `enactment_date` | When legislation became law (signed / effective as documented) | Enactment |
| `legislative_override_date` | When legislation changed the law so a prior judicial outcome lost practical force (legislative / statutory override) | Legislative override |
| `charge_date` | Formal criminal charges (complaint, information, or other charging instrument when not using `indictment_date`) | Charge |
| `arrest_date` | Arrest or detention in connection with the matter | Arrest |
| `indictment_date` | Grand-jury indictment (or equivalent charging by indictment) | Indictment |

`historical_event` pages must include **at least one** of these timeline date fields.

```yaml
type: case
decision_date: "2017-06-19"
```

```yaml
type: statute
enactment_date: "1996"
```

```yaml
type: historical_event
legislative_override_date: "2008-07-10"
```

A page may set more than one timeline date when multiple milestones are documented (for example, a criminal case with `arrest_date`, `indictment_date`, and `decision_date`, or a statute with both an original `enactment_date` and a later `legislative_override_date`).

Prefer `indictment_date` when the charging instrument is an indictment; use `charge_date` for other formal charging events (or when sources say “charged” without specifying indictment).

Document publication dates, access dates, and `last_verified` appear on individual page footers instead of the timeline.

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
