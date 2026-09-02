---
id: CASE-IN-RE-OPENAI
title: In re OpenAI, Inc., Copyright Infringement Litigation
type: case
status: draft
summary: Multidistrict copyright litigation in the Southern District of New York consolidating author and publisher actions against OpenAI and Microsoft; the court denied OpenAI’s motion to dismiss author class claims based on alleged ChatGPT outputs without deciding fair use.
tags:
  - case
  - copyright
  - artificial-intelligence
  - digital-rights
sources:
  - SRC-JPML-OPENAI-MDL-3143
  - SRC-IN-RE-OPENAI-OUTPUT-MTD-2025
relationships:
  - subject: CASE-IN-RE-OPENAI
    predicate: cites
    object: SRC-JPML-OPENAI-MDL-3143
    sources:
      - SRC-JPML-OPENAI-MDL-3143
  - subject: CASE-IN-RE-OPENAI
    predicate: cites
    object: SRC-IN-RE-OPENAI-OUTPUT-MTD-2025
    sources:
      - SRC-IN-RE-OPENAI-OUTPUT-MTD-2025
  - subject: CASE-IN-RE-OPENAI
    predicate: related_to
    object: CASE-NYT-V-OPENAI
    sources:
      - SRC-JPML-OPENAI-MDL-3143
  - subject: CASE-IN-RE-OPENAI
    predicate: related_to
    object: TOPIC-AI-COPYRIGHT
    sources:
      - SRC-IN-RE-OPENAI-OUTPUT-MTD-2025
last_verified: "2026-09-02"
decision_date: "2025-10-27"
---

# In re OpenAI, Inc., Copyright Infringement Litigation

## Summary

In re OpenAI, Inc., Copyright Infringement Litigation, MDL No. 3143 (S.D.N.Y.), is the centralized pretrial docket for copyright actions alleging that OpenAI and Microsoft used copyrighted works to train large language models. The Judicial Panel on Multidistrict Litigation transferred out-of-district cases to Judge Sidney H. Stein. On October 27, 2025, the court denied OpenAI’s motion to dismiss author class plaintiffs’ direct-infringement claim based on ChatGPT outputs. The news-publisher track remains documented on [The New York Times Company v. Microsoft Corp.](CASE-NYT-V-OPENAI.md).

## Verified Facts

- In MDL No. 3143, the Judicial Panel on Multidistrict Litigation found that twelve actions in the Northern District of California and the Southern District of New York shared factual questions about OpenAI and Microsoft training large language models such as GPT-4 and generating outputs through products including ChatGPT and Bing Chat/Copilot, and it transferred the out-of-district actions to the Southern District of New York for coordinated or consolidated pretrial proceedings before Judge Sidney H. Stein.[^1]
- Schedule A to the transfer order listed, among others, Tremblay, Silverman, Chabon, and Millette (N.D. Cal.); Authors Guild, Alter, Basbanes, Raw Story, The Intercept, Daily News, and Center for Investigative Reporting (S.D.N.Y.); and The New York Times Company v. Microsoft Corporation, No. 1:23-cv-11195.[^1]
- The Panel described differences among author class claims (books used as training input), news claims (training plus alleged verbatim or detailed output summaries), DMCA copyright-management-information claims that do not allege copyright infringement, and a YouTube-transcript class (Millette), but held those differences did not prevent centralization.[^1]
- On October 27, 2025, in 25-md-3143, Judge Stein denied OpenAI’s motion to dismiss the Consolidated Class Action Complaint’s output-based direct-infringement claim in putative class actions including Authors Guild, No. 23-cv-8292. The court held that the complaint adequately stated a prima facie claim because some alleged ChatGPT outputs, including a detailed summary of George R.R. Martin’s *A Game of Thrones* and an alternate-sequel outline using protected setting, plot, and characters, could be found substantially similar by a reasonable jury applying the more discerning observer test.[^2]
- The October 27, 2025 opinion states that it makes no conclusions regarding fair use.[^2]


[^1]: `SRC-JPML-OPENAI-MDL-3143` — JPML Transfer Order (MDL No. 3143). Primary for centralization and Schedule A.

[^2]: `SRC-IN-RE-OPENAI-OUTPUT-MTD-2025` — Opinion & Order (Oct. 27, 2025). Primary for output-claim pleading holding.

## Historical Context

The MDL gathers the book-author class actions that began as Authors Guild, Tremblay, Silverman, and related suits, together with news and DMCA cases already before Judge Stein. It is a pretrial coordination device, not a single merits judgment that training is or is not fair use.[^1][^2]

## Legal Analysis

Jurisdiction: JPML centralization into the Southern District of New York. Authority level: transfer order plus a Rule 12(b)(6) opinion on output similarity. The October 2025 order is important for what it did not do: it refused to end output claims as a matter of law at the pleading stage, while expressly reserving [§ 107](STAT-USC-107.md).[^2] Training-input claims were not the subject of that motion.

News-publisher pleading orders remain on the Times page. This page does not treat alleged ChatGPT summaries as proven copying.

## Relationships

- `CASE-IN-RE-OPENAI` cites `SRC-JPML-OPENAI-MDL-3143`.
- `CASE-IN-RE-OPENAI` cites `SRC-IN-RE-OPENAI-OUTPUT-MTD-2025`.
- `CASE-IN-RE-OPENAI` related_to `CASE-NYT-V-OPENAI`.
- `CASE-IN-RE-OPENAI` related_to `TOPIC-AI-COPYRIGHT`.

## Sources

1. `SRC-JPML-OPENAI-MDL-3143`: JPML Transfer Order, MDL No. 3143.
2. `SRC-IN-RE-OPENAI-OUTPUT-MTD-2025`: Opinion denying motion to dismiss output claims (Oct. 27, 2025).

## Research Debt

- Replace the law-firm hosted October 27, 2025 opinion with a RECAP/PACER original when available.
- Add the consolidated class action complaint (Baldacci et al.) as the operative author pleading.
- Add later summary-judgment or discovery orders on output logs from those PDFs.
- Document tag-along actions filed after Schedule A only from later JPML or docket entries.
