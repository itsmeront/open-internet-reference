---
id: CASE-KADREY-V-META
title: Kadrey v. Meta Platforms, Inc.
type: case
status: draft
summary: Kadrey v. Meta Platforms, Inc., 788 F. Supp. 3d 1026 (N.D. Cal. 2025), granted Meta summary judgment that copying thirteen authors’ books to train Llama was fair use on that record, while leaving torrenting-distribution claims for later proceedings.
tags:
  - case
  - copyright
  - artificial-intelligence
  - digital-rights
sources:
  - SRC-KADREY-V-META-FAIR-USE
  - SRC-USC-17-107-LII
relationships:
  - subject: CASE-KADREY-V-META
    predicate: cites
    object: SRC-KADREY-V-META-FAIR-USE
    sources:
      - SRC-KADREY-V-META-FAIR-USE
  - subject: CASE-KADREY-V-META
    predicate: related_to
    object: STAT-USC-107
    sources:
      - SRC-USC-17-107-LII
  - subject: CASE-KADREY-V-META
    predicate: related_to
    object: TOPIC-AI-COPYRIGHT
    sources:
      - SRC-KADREY-V-META-FAIR-USE
  - subject: CASE-KADREY-V-META
    predicate: related_to
    object: CASE-BARTZ-V-ANTHROPIC
    sources:
      - SRC-KADREY-V-META-FAIR-USE
last_verified: "2026-08-22"
decision_date: "2025-06-25"
---

# Kadrey v. Meta Platforms, Inc.

## Summary

Kadrey v. Meta Platforms, Inc., 788 F. Supp. 3d 1026 (N.D. Cal. 2025), is a Northern District of California action by thirteen authors alleging that Meta downloaded their books from shadow libraries and used them to train Llama models. On June 25, 2025, Judge Vince Chhabria granted Meta’s cross-motion for partial summary judgment on fair use as to that training copying, emphasizing the plaintiffs’ failure to present market-dilution evidence, while scheduling further proceedings on alleged unlawful distribution during torrenting.

## Verified Facts

- Case No. 3:23-cv-03417-VC, U.S. District Court for the Northern District of California. Order dated June 25, 2025 (Dkt. 598).[^1]
- Plaintiffs are thirteen authors, described by the court as mostly famous fiction writers, who sued Meta for downloading their books from online “shadow libraries” and using them to train Llama large language models.[^1]
- The court stated that, in most cases, unauthorized copying of protected works to train generative AI “will likely” be illegal because of market-dilution risk, but that courts must decide on the evidence presented.[^1]
- Plaintiffs’ two primary market theories on the fair-use motions were that Llama could reproduce small snippets and that training without permission diminished a market to license books as AI training data. The court called both “clear losers” on this record: Llama was not capable of generating enough text from the plaintiffs’ books to matter, and plaintiffs were not entitled to a licensing market for AI training data as such.[^1]
- The court identified market dilution (flooding the market with competing AI-generated works) as the potentially winning theory, but held that plaintiffs barely addressed it and presented no meaningful evidence of it.[^1]
- Because Meta’s use was highly transformative, the court held plaintiffs needed to win decisively on the fourth fair-use factor; absent dilution evidence, factor four favored Meta and Meta was entitled to summary judgment on fair use for using these plaintiffs’ books as LLM training data.[^1]
- The court distinguished [Bartz v. Anthropic PBC](CASE-BARTZ-V-ANTHROPIC.md), arguing that Judge Alsup underweighted market harm by analogizing AI training to teaching schoolchildren to write.[^1]
- The order states that a separate ruling would grant Meta summary judgment on the DMCA claim, and set a July 11, 2025 conference on the claim that Meta unlawfully distributed the works during torrenting.[^1]


[^1]: `SRC-KADREY-V-META-FAIR-USE` — Order on partial summary judgment (June 25, 2025). Primary district-court authority.

## Historical Context

Kadrey and Bartz were decided in the same district two days apart and immediately framed a split in how Northern District judges weigh transformativeness against market harm for LLM training.[^1] Kadrey is not a holding that shadow-library downloading is always lawful; the court left distribution/torrenting issues open and repeatedly warned that other plaintiffs with a developed dilution record might win.[^1]

## Legal Analysis

Jurisdiction: N.D. Cal. Authority level: district-court partial summary judgment. Not circuit precedent.

The opinion treats [17 U.S.C. § 107](STAT-USC-107.md) as fact-specific. Factor one favored Meta as highly transformative; factor four was treated as the most important and turned on the absence of dilution proof rather than on a categorical rule that training is fair use.[^1] The court rejected an argument that adverse copyright rulings would halt LLM development, stating that developers could license works or use public-domain materials.[^1]

Software companies should not read Kadrey as a safe harbor for training on pirated books. The fair-use win is limited to copying these thirteen authors’ books as training data on this evidentiary record, with distribution claims reserved.[^1]

## Relationships

- `CASE-KADREY-V-META` cites `SRC-KADREY-V-META-FAIR-USE`.
- `CASE-KADREY-V-META` related_to `STAT-USC-107`.
- `CASE-KADREY-V-META` related_to `TOPIC-AI-COPYRIGHT`.
- `CASE-KADREY-V-META` related_to `CASE-BARTZ-V-ANTHROPIC`.

## Sources

1. `SRC-KADREY-V-META-FAIR-USE`: Kadrey v. Meta Platforms, Inc., 788 F. Supp. 3d 1026 (N.D. Cal. 2025).

Additional sources (not yet cited in footnotes):

- `SRC-USC-17-107-LII`: 17 U.S.C. § 107.

## Research Debt

- Add a CourtListener/RECAP copy of Dkt. 598 in addition to the Justia PDF.
- Document the later torrenting/distribution rulings and any appeal.
- Identify the thirteen named plaintiffs from the complaint as a source-backed list.
- Add the Copyright Office fair-use summary (788 F. Supp. 3d) as a secondary finding aid only.
