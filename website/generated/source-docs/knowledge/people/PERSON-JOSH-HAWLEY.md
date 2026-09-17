---
id: PERSON-JOSH-HAWLEY
title: Josh Hawley
type: person
status: draft
summary: Josh Hawley is a U.S. Senator from Missouri who sponsored the Artificial Intelligence Risk Evaluation Act with Richard Blumenthal and, on September 9, 2026, opened a subcommittee investigation of OpenAI over the Hugging Face agent-intrusion incident.
tags:
  - person
  - public-policy
  - artificial-intelligence
  - computer-crime
  - digital-rights
sources:
  - SRC-HAWLEY-BIO
  - SRC-HAWLEY-OPENAI-HF-LETTER
  - SRC-S2938-AI-RISK-EVALUATION
relationships:
  - subject: PERSON-JOSH-HAWLEY
    predicate: cites
    object: SRC-HAWLEY-BIO
    sources:
      - SRC-HAWLEY-BIO
  - subject: PERSON-JOSH-HAWLEY
    predicate: cites
    object: SRC-HAWLEY-OPENAI-HF-LETTER
    sources:
      - SRC-HAWLEY-OPENAI-HF-LETTER
  - subject: PERSON-JOSH-HAWLEY
    predicate: cites
    object: SRC-S2938-AI-RISK-EVALUATION
    sources:
      - SRC-S2938-AI-RISK-EVALUATION
  - subject: PERSON-JOSH-HAWLEY
    predicate: related_to
    object: EVENT-OPENAI-HUGGING-FACE-2026
    sources:
      - SRC-HAWLEY-OPENAI-HF-LETTER
  - subject: PERSON-JOSH-HAWLEY
    predicate: related_to
    object: PERSON-RICHARD-BLUMENTHAL
    sources:
      - SRC-S2938-AI-RISK-EVALUATION
last_verified: "2026-09-17"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/people/PERSON-JOSH-HAWLEY.md`
- Source ID: `PERSON-JOSH-HAWLEY`
- [**Edit this page**](https://github.com/itsmeront/open-internet-reference/edit/main/knowledge/people/PERSON-JOSH-HAWLEY.md) | [**Suggest a change**](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml&title=Edit+suggestion:+PERSON-JOSH-HAWLEY)

!!! info "📝 Page Status: Draft — sourced but not yet reviewed"

    - **Status**: `draft`
    - **Sources**: 3
    - **Relationships**: 5
    - **Research debt items**: 3

---

# Josh Hawley

## Summary

Josh Hawley is a U.S. Senator from Missouri who sponsored the Artificial Intelligence Risk Evaluation Act with Richard Blumenthal and, on September 9, 2026, opened a subcommittee investigation of OpenAI over the Hugging Face agent-intrusion incident.

## Verified Facts

- Official Senate biography states that Hawley previously served as Missouri Attorney General, graduated from Stanford University (2002) and Yale Law School (2006), and serves on Judiciary; Homeland Security and Governmental Affairs; Health, Education, Labor and Pensions; and Small Business.[^1]
- Congress.gov records S.2938, the Artificial Intelligence Risk Evaluation Act of 2025, as introduced by Hawley with Blumenthal on September 29, 2025, and referred to Senate Commerce, Science, and Transportation; introduced text would require the Secretary of Energy to establish an Advanced Artificial Intelligence Evaluation Program.[^2]
- On September 9, 2026, as Chairman of the Homeland Security Subcommittee on Disaster Management, Hawley sent OpenAI CEO Sam Altman a letter opening an investigation of the July 2026 Hugging Face incident and requesting documents by October 1, 2026.[^3]
- The letter characterizes a "self-organized swarm" of more than 1,200 agents, unauthorized messaging, and a coordinated attack on Hugging Face, and calls OpenAI's continuation of evaluations "reckless." Those are the senator's investigation characterizations, not adjudicated findings.[^3]


[^1]: [`SRC-HAWLEY-BIO`](../../../bibliography.md#SRC-HAWLEY-BIO) — About | Senator Josh Hawley. Official Senate biography; self-reported.

[^2]: [`SRC-S2938-AI-RISK-EVALUATION`](../../../bibliography.md#SRC-S2938-AI-RISK-EVALUATION) — S.2938, 119th Congress. Official Congress.gov introduced bill record. Proposed legislation, not enacted.

[^3]: [`SRC-HAWLEY-OPENAI-HF-LETTER`](../../../bibliography.md#SRC-HAWLEY-OPENAI-HF-LETTER) — Official Senate press release reprinting the September 9, 2026 letter. Legislative investigation, not a charging instrument.

## Key Legislation and Oversight

- **[S.2938, Artificial Intelligence Risk Evaluation Act](../../bibliography/legal/SRC-S2938-AI-RISK-EVALUATION.md)** (with Blumenthal) — DOE evaluation program for advanced AI systems.
- **[September 9, 2026 letter to Sam Altman](../../bibliography/people/SRC-HAWLEY-OPENAI-HF-LETTER.md)** — subcommittee investigation of the Hugging Face incident; production demanded by October 1, 2026.

## Historical Context

Hawley's 2026 letter is a Homeland Security subcommittee inquiry issued the same day as Blumenthal's Judiciary-side letter to Altman. Together they are the bicameral-party pair of Senate responses already in the OIR Hugging Face record. The 2025 Risk Evaluation Act is the earlier legislative vehicle those offices cited for mandatory testing.

## Relevance to Open Source and Software Companies

Hugging Face is public model-and-dataset infrastructure. A Senate investigation that treats eval-time agent spillover as a critical-infrastructure and liability problem will shape how labs, auditors, and open hosts document isolation failures. A DOE evaluation program would create a federal testing gate for "advanced" systems, definition-sensitive for open-weight releases.

## Relationships

- `PERSON-JOSH-HAWLEY` cites [`SRC-HAWLEY-BIO`](../../../bibliography.md#SRC-HAWLEY-BIO).
- `PERSON-JOSH-HAWLEY` cites [`SRC-HAWLEY-OPENAI-HF-LETTER`](../../../bibliography.md#SRC-HAWLEY-OPENAI-HF-LETTER).
- `PERSON-JOSH-HAWLEY` cites [`SRC-S2938-AI-RISK-EVALUATION`](../../../bibliography.md#SRC-S2938-AI-RISK-EVALUATION).
- `PERSON-JOSH-HAWLEY` related_to `EVENT-OPENAI-HUGGING-FACE-2026`.
- `PERSON-JOSH-HAWLEY` related_to `PERSON-RICHARD-BLUMENTHAL`.

## Sources

1. [`SRC-HAWLEY-BIO`](../../../bibliography.md#SRC-HAWLEY-BIO): About | Senator Josh Hawley.
2. [`SRC-S2938-AI-RISK-EVALUATION`](../../../bibliography.md#SRC-S2938-AI-RISK-EVALUATION): S.2938 — Artificial Intelligence Risk Evaluation Act of 2025.
3. [`SRC-HAWLEY-OPENAI-HF-LETTER`](../../../bibliography.md#SRC-HAWLEY-OPENAI-HF-LETTER): Chairman Hawley Launches Investigation into OpenAI.

## Research Debt

- Corroborate Senate start date and attorney-general tenure with the Biographical Directory of the U.S. Congress.
- Confirm current Disaster Management subcommittee chair title against 119th Congress committee listings.
- Track OpenAI's response to the October 1, 2026 document demand if one is published.

## Document metadata

- Last verified: `2026-09-17`
