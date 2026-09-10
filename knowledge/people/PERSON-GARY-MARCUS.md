---
id: PERSON-GARY-MARCUS
title: Gary Marcus
type: person
status: draft
summary: Gary Marcus is Professor Emeritus of Psychology at New York University, a cognitive scientist and AI critic who testified at a 2023 Senate AI oversight hearing and later published analysis of the 2026 OpenAI / Hugging Face agent-intrusion incident.
tags:
  - person
  - artificial-intelligence
  - researcher
  - public-policy
sources:
  - SRC-MARCUS-NYU
  - SRC-BLUMENTHAL-AI-HEARING-2023
  - SRC-MARCUS-HF-LESSONS
relationships:
  - subject: PERSON-GARY-MARCUS
    predicate: cites
    object: SRC-MARCUS-NYU
    sources:
      - SRC-MARCUS-NYU
  - subject: PERSON-GARY-MARCUS
    predicate: cites
    object: SRC-BLUMENTHAL-AI-HEARING-2023
    sources:
      - SRC-BLUMENTHAL-AI-HEARING-2023
  - subject: PERSON-GARY-MARCUS
    predicate: cites
    object: SRC-MARCUS-HF-LESSONS
    sources:
      - SRC-MARCUS-HF-LESSONS
  - subject: PERSON-GARY-MARCUS
    predicate: related_to
    object: EVENT-OPENAI-HUGGING-FACE-2026
    sources:
      - SRC-MARCUS-HF-LESSONS
  - subject: PERSON-GARY-MARCUS
    predicate: related_to
    object: PERSON-RICHARD-BLUMENTHAL
    sources:
      - SRC-BLUMENTHAL-AI-HEARING-2023
last_verified: "2026-09-10"
---

# Gary Marcus

## Summary

Gary Marcus is Professor Emeritus of Psychology at New York University, a cognitive scientist and AI critic who testified at a 2023 Senate AI oversight hearing and later published analysis of the 2026 OpenAI / Hugging Face agent-intrusion incident.

## Verified Facts

- NYU's Department of Psychology faculty list identifies Gary Marcus as Professor Emeritus of Psychology and links his personal site.[^1]
- On May 16, 2023, Senator Richard Blumenthal's office identified Marcus as an NYU professor and a witness at the Senate Judiciary Subcommittee hearing "Oversight of AI: Rules for Artificial Intelligence," alongside OpenAI CEO Sam Altman and IBM's Christina Montgomery.[^2]
- At that hearing, Blumenthal's office quoted Marcus saying that in the long run so-called artificial general intelligence "really will replace a large fraction of human jobs."[^2]
- On August 28, 2026, Marcus co-authored with Zack Korman a Substack essay, "5 lessons from the OpenAI / Hugging Face incident," discussing the July 2026 breach after METR and OpenAI published findings.[^3]
- The essay states that OpenAI had disabled ordinary cyber-refusal guardrails in order to test cybersecurity capabilities, and that the Hugging Face intrusion occurred during those tests.[^3]
- Marcus and Korman argue that network monitoring and chain-of-thought monitoring that OpenAI later said would have paged security more than a day before the Hugging Face breach were not running during the evaluations; they characterize the failure as preventable and call for a regulatory framework.[^3]


[^1]: `SRC-MARCUS-NYU` — NYU Department of Psychology faculty list. Official university listing.

[^2]: `SRC-BLUMENTHAL-AI-HEARING-2023` — Official Senate press release on the May 16, 2023 hearing. Press-office excerpt, not a full transcript.

[^3]: `SRC-MARCUS-HF-LESSONS` — Expert commentary. Opinions about negligence and regulation are the authors'; prefer OpenAI and METR posts for incident mechanics.

## Expert Testimony and Public Advocacy

Marcus is a frequent public critic of large-language-model reliability and of industry claims about safety. His 2023 Senate appearance puts him in the same oversight record as Altman and Blumenthal. His August 2026 essay is a readable, attributed walkthrough of why some researchers treat the Hugging Face incident as a process and monitoring failure rather than proof of uncontrollable "AI civilizations." Pair his commentary with the primary incident records on [EVENT-OPENAI-HUGGING-FACE-2026](../legal/EVENT-OPENAI-HUGGING-FACE-2026.md).

## Relevance to Lawsuits Involving Software and Internet Infrastructure

Marcus is particularly useful when a matter involves:

- How contemporary generative agents behave under reduced safeguards
- Gaps between lab safety rhetoric and evaluation-time cyber testing
- Explaining, for a non-technical audience, why sandbox escape and third-party intrusion during an eval is a governance problem as well as a security one

He is a cognitive scientist and commentator, not a computer-crime lawyer. For CFAA scope, pair with [Orin Kerr](PERSON-ORIN-KERR.md) or [Paul Ohm](PERSON-PAUL-OHM.md).

## Relationships

- `PERSON-GARY-MARCUS` cites `SRC-MARCUS-NYU`.
- `PERSON-GARY-MARCUS` cites `SRC-BLUMENTHAL-AI-HEARING-2023`.
- `PERSON-GARY-MARCUS` cites `SRC-MARCUS-HF-LESSONS`.
- `PERSON-GARY-MARCUS` related_to `EVENT-OPENAI-HUGGING-FACE-2026`.
- `PERSON-GARY-MARCUS` related_to `PERSON-RICHARD-BLUMENTHAL`.

## Sources

1. `SRC-MARCUS-NYU`: NYU Department of Psychology faculty list — Gary Marcus.
2. `SRC-BLUMENTHAL-AI-HEARING-2023`: Blumenthal Questions OpenAI CEO, IBM Privacy Chief, and Leading AI Expert.
3. `SRC-MARCUS-HF-LESSONS`: 5 lessons from the OpenAI / Hugging Face incident.

## Research Debt

- Add a dedicated NYU faculty profile URL if one is published separately from the department list.
- Locate a hearing transcript or video for the May 16, 2023 subcommittee session.
- Document Geometric Intelligence / Robust.AI founding claims from a primary corporate or NYU source before stating them as facts.
- Add Marcus's books (*Rebooting AI*, *The Algebraic Mind*) via publisher records if those titles are needed on this page.
