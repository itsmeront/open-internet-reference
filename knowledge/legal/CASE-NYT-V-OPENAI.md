---
id: CASE-NYT-V-OPENAI
title: The New York Times Company v. Microsoft Corp. (OpenAI)
type: case
status: draft
summary: Pending Southern District of New York copyright litigation in which The New York Times and other publishers allege that OpenAI and Microsoft copied news works to train large language models and that outputs substitute for licensed journalism.
tags:
  - case
  - copyright
  - artificial-intelligence
  - digital-rights
sources:
  - SRC-NYT-V-OPENAI-COMPLAINT
  - SRC-NYT-V-OPENAI-MTD-2025
  - SRC-NYT-V-OPENAI-12C-2026
  - SRC-JPML-OPENAI-MDL-3143
  - SRC-NYT-V-PERPLEXITY-DOCKET
relationships:
  - subject: CASE-NYT-V-OPENAI
    predicate: cites
    object: SRC-NYT-V-OPENAI-MTD-2025
    sources:
      - SRC-NYT-V-OPENAI-MTD-2025
  - subject: CASE-NYT-V-OPENAI
    predicate: related_to
    object: TOPIC-AI-COPYRIGHT
    sources:
      - SRC-NYT-V-OPENAI-MTD-2025
  - subject: CASE-NYT-V-OPENAI
    predicate: related_to
    object: STAT-USC-107
    sources:
      - SRC-NYT-V-OPENAI-MTD-2025
  - subject: CASE-NYT-V-OPENAI
    predicate: related_to
    object: CASE-IN-RE-OPENAI
    sources:
      - SRC-JPML-OPENAI-MDL-3143
  - subject: CASE-NYT-V-OPENAI
    predicate: related_to
    object: CASE-DOW-JONES-V-PERPLEXITY
    sources:
      - SRC-NYT-V-PERPLEXITY-DOCKET
last_verified: "2026-09-02"
decision_date: "2025-04-04"
---

# The New York Times Company v. Microsoft Corp. (OpenAI)

## Summary

The New York Times Company v. Microsoft Corporation, No. 23-cv-11195 (S.D.N.Y.), is lead publisher copyright litigation against OpenAI and Microsoft over alleged copying of news works to train GPT-based products and alleged output-stage substitution. On April 4, 2025, Judge Sidney H. Stein largely denied motions to dismiss copyright claims in the Times, Daily News, and Center for Investigative Reporting actions. On August 6, 2026, the court dismissed with prejudice the news plaintiffs’ material-contribution contributory claims premised on alleged end-user infringement.

## Verified Facts

- The Times filed its complaint on December 27, 2023, against Microsoft Corporation and multiple OpenAI entities, alleging claims including direct, vicarious, and contributory copyright infringement, DMCA § 1202 violations, and unfair competition by misappropriation.[^1][^2]
- The complaint alleges that defendants used Times journalism to train GPT-based products including ChatGPT, ChatGPT Enterprise, Bing Chat, Azure OpenAI Service, and Microsoft 365 Copilot, and that outputs can reproduce Times content.[^1]
- Related publisher actions captioned in the April 4, 2025 opinion include Daily News LP v. Microsoft Corp., No. 24-cv-3285, and Center for Investigative Reporting, Inc. v. OpenAI, No. 24-cv-4872.[^2]
- On April 4, 2025, the court held that claims of direct infringement occurring more than three years before filing were not time-barred on the pleadings, because OpenAI had not shown plaintiffs discovered or should have discovered the alleged infringement by the relevant 2020/2021 dates.[^2]
- The court held that the publisher plaintiffs had plausibly alleged contributory copyright infringement at the pleading stage.[^2]
- The court dismissed without prejudice specified DMCA § 1202 claims, including Microsoft’s § 1202(b)(1) claims in all three actions, OpenAI’s § 1202(b)(1) claim in the Times action, and defendants’ § 1202(b)(3) claims in all three actions, while allowing Daily News and CIR § 1202(b)(1) claims against OpenAI to proceed.[^2]
- The court held that plaintiffs failed to plausibly allege “hot news” misappropriation as to news content and the Times’s Wirecutter recommendations.[^2]
- The court granted OpenAI’s motion to dismiss CIR’s direct-infringement claim insofar as it rested on ChatGPT/Copilot “abridgments” in Exhibit 11, holding those summaries were not substantially similar to CIR’s articles as a matter of law.[^2]
- On August 6, 2026, the court dismissed with prejudice the news plaintiffs’ “material contribution” contributory copyright claims against OpenAI and Microsoft premised on alleged direct infringement by end users, after the Supreme Court’s decision in Cox, 146 S. Ct. 959 (2026). OpenAI’s Rule 12(c) motion was denied as moot as to those plaintiffs because they agreed to that dismissal.[^3]
- The August 6, 2026 order also dismissed with prejudice trademark-dilution claims by the Times and Daily News, and denied the Times’s and Daily News’s motions for leave to amend to add new contributory theories against Microsoft.[^3]


[^1]: `SRC-NYT-V-OPENAI-COMPLAINT` — Original Times complaint (Dec. 27, 2023). Plaintiff allegations.

[^2]: `SRC-NYT-V-OPENAI-MTD-2025` — Opinion (Apr. 4, 2025). Primary district-court pleading-stage authority.

[^3]: `SRC-NYT-V-OPENAI-12C-2026` — Order (Aug. 6, 2026). Primary district-court authority on later contributory-claim dismissal.

[^4]: `SRC-JPML-OPENAI-MDL-3143` — JPML Transfer Order, MDL No. 3143. Primary for centralization of the Times action.

[^5]: `SRC-NYT-V-PERPLEXITY-DOCKET` — CourtListener docket for No. 1:25-cv-10106. Primary for the later Times filing against Perplexity.

## Historical Context

The Times action is the highest-profile news-publisher suit in the generative-AI copyright wave. Unlike [Bartz v. Anthropic PBC](CASE-BARTZ-V-ANTHROPIC.md) and [Kadrey v. Meta Platforms, Inc.](CASE-KADREY-V-META.md), which reached summary judgment on book-training fair use, this docket remained at pleadings and discovery as of the August 2026 order, with output substitution and training still live issues for remaining claims.[^2][^3] The Judicial Panel on Multidistrict Litigation transferred this action, among others, into [In re OpenAI, Inc., Copyright Infringement Litigation](CASE-IN-RE-OPENAI.md).[^4] A later Times complaint against Perplexity AI is recorded on [Dow Jones & Co. v. Perplexity AI, Inc.](CASE-DOW-JONES-V-PERPLEXITY.md).[^5]

## Legal Analysis

Jurisdiction: Southern District of New York. Authority level: district-court pleading orders; no fair-use merits holding is recorded here.

The April 2025 opinion is important for what it did not do: it refused to end the case on statute-of-limitations or contributory-infringement pleadings, while trimming DMCA CMI, hot-news, and some abridgment theories.[^2] Fair use remains a fact-intensive defense for later stages. The August 2026 order shows Supreme Court secondary-liability law (Cox) already reshaping AI cases: material-contribution theories tied to end-user outputs can fail even when direct-infringement claims against the model developer continue.[^3]

This page does not treat the complaint’s exhibits of allegedly memorized articles as proven copying.

## Relationships

- `CASE-NYT-V-OPENAI` cites `SRC-NYT-V-OPENAI-MTD-2025`.
- `CASE-NYT-V-OPENAI` related_to `TOPIC-AI-COPYRIGHT`.
- `CASE-NYT-V-OPENAI` related_to `STAT-USC-107`.
- `CASE-NYT-V-OPENAI` related_to `CASE-IN-RE-OPENAI`.
- `CASE-NYT-V-OPENAI` related_to `CASE-DOW-JONES-V-PERPLEXITY`.

## Sources

1. `SRC-NYT-V-OPENAI-COMPLAINT`: Times complaint (Dec. 27, 2023).
2. `SRC-NYT-V-OPENAI-MTD-2025`: Opinion on motions to dismiss (Apr. 4, 2025).
3. `SRC-NYT-V-OPENAI-12C-2026`: Order on Rule 12(c) contributory claims (Aug. 6, 2026).
4. `SRC-JPML-OPENAI-MDL-3143`: JPML Transfer Order, MDL No. 3143.
5. `SRC-NYT-V-PERPLEXITY-DOCKET`: CourtListener docket for Times v. Perplexity, No. 1:25-cv-10106.

## Research Debt

- Add the first amended Times complaint (ECF 170) as the operative pleading source.
- Document consolidation/MDL captioning (RECAP numbers differ across related dockets). The MDL transfer and author-class output claims are now [CASE-IN-RE-OPENAI](CASE-IN-RE-OPENAI.md).
- Add any summary-judgment or discovery orders on output logs after August 2026.
- Create a dedicated CASE page for Cox v. Sony (146 S. Ct. 959 (2026)) if OIR takes on secondary copyright liability more broadly.
- The Times action against Perplexity is recorded on [CASE-DOW-JONES-V-PERPLEXITY](CASE-DOW-JONES-V-PERPLEXITY.md); add that complaint and any later order from those PDFs.
