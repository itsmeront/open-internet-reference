---
id: CASE-ANDERSEN-V-STABILITY
title: Andersen v. Stability AI Ltd.
type: case
status: draft
summary: Pending Northern District of California putative class action by visual artists alleging that Stability AI, Midjourney, DeviantArt, and Runway copied registered works to train image generators; the court allowed Copyright Act claims to proceed and dismissed DMCA claims with prejudice.
tags:
  - case
  - copyright
  - artificial-intelligence
  - digital-rights
sources:
  - SRC-ANDERSEN-V-STABILITY-MTD-2024
  - SRC-ANDERSEN-V-STABILITY-DOCKET
  - SRC-GOOGLE-GEN-AI-MTD-2025
relationships:
  - subject: CASE-ANDERSEN-V-STABILITY
    predicate: cites
    object: SRC-ANDERSEN-V-STABILITY-MTD-2024
    sources:
      - SRC-ANDERSEN-V-STABILITY-MTD-2024
  - subject: CASE-ANDERSEN-V-STABILITY
    predicate: related_to
    object: TOPIC-AI-COPYRIGHT
    sources:
      - SRC-ANDERSEN-V-STABILITY-MTD-2024
  - subject: CASE-ANDERSEN-V-STABILITY
    predicate: related_to
    object: CASE-GETTY-V-STABILITY
    sources:
      - SRC-ANDERSEN-V-STABILITY-MTD-2024
  - subject: CASE-ANDERSEN-V-STABILITY
    predicate: related_to
    object: CASE-DISNEY-V-MIDJOURNEY
    sources:
      - SRC-ANDERSEN-V-STABILITY-MTD-2024
  - subject: CASE-ANDERSEN-V-STABILITY
    predicate: related_to
    object: CASE-DOE-V-GITHUB
    sources:
      - SRC-ANDERSEN-V-STABILITY-MTD-2024
  - subject: CASE-ANDERSEN-V-STABILITY
    predicate: related_to
    object: CASE-IN-RE-GOOGLE-GEN-AI
    sources:
      - SRC-GOOGLE-GEN-AI-MTD-2025
last_verified: "2026-09-02"
decision_date: "2024-08-12"
---

# Andersen v. Stability AI Ltd.

## Summary

Andersen v. Stability AI Ltd., No. 3:23-cv-00201 (N.D. Cal.), is a putative class action by visual artists against Stability AI, Midjourney, DeviantArt, and Runway AI over alleged copying of training images into Stable Diffusion and related products. On August 12, 2024, Judge William H. Orrick denied motions to dismiss the Copyright Act claims, denied Midjourney’s motion to dismiss Lanham Act claims, dismissed DMCA claims with prejudice, and dismissed unjust-enrichment and DeviantArt contract claims (the latter with prejudice). The order is a pleading decision, not a fair-use holding.

## Verified Facts

- The action was filed January 13, 2023, in the Northern District of California as No. 3:23-cv-00201.[^2]
- The first amended complaint names artists including Sarah Andersen, Kelly McKernan, Karla Ortiz, Hawke Southworth, Grzegorz Rutkowski, Gregory Manchess, Gerald Brom, Jingna Zhang, Julia Kaye, and Adam Ellis, and alleges that Stable Diffusion used their artistic works as training images and can produce outputs “in the style” of those images.[^1]
- Defendants addressed in the August 12, 2024 order are Stability AI Ltd. and Stability AI, Inc., Midjourney, Inc., DeviantArt, Inc., and Runway AI, Inc.[^1]
- Plaintiffs allege that LAION training sets were used to train versions of Stable Diffusion, that the LAION-5B dataset contains URLs rather than image files, and that anyone using that dataset must first acquire copies of the images from those URLs.[^1]
- On August 12, 2024, the court denied defendants’ motions to dismiss the Copyright Act claims, denied Midjourney’s motion to dismiss the Lanham Act claims, dismissed the DMCA claims with prejudice, dismissed unjust-enrichment claims with leave to amend, and dismissed DeviantArt’s breach-of-contract and implied-covenant claims with prejudice.[^1]


[^1]: `SRC-ANDERSEN-V-STABILITY-MTD-2024` — Order (Aug. 12, 2024). Primary for FAC parties, alleged theories, and holdings.

[^2]: `SRC-ANDERSEN-V-STABILITY-DOCKET` — CourtListener docket for No. 3:23-cv-00201. Primary for filing date.

[^3]: `SRC-GOOGLE-GEN-AI-MTD-2025` — Order (Sept. 11, 2025). Primary for named-plaintiff overlap with the Google class action.

## Historical Context

Andersen is the leading U.S. visual-artist class action in the generative-image wave. It is distinct from [Getty Images v. Stability AI](CASE-GETTY-V-STABILITY.md), an English trial about secondary copyright and watermarks, and from [Disney v. Midjourney](CASE-DISNEY-V-MIDJOURNEY.md), a studio character-output case. Named plaintiff Sarah Andersen also appears in [In re Google Generative AI Copyright Litigation](CASE-IN-RE-GOOGLE-GEN-AI.md), a different docket.[^3] The August 2024 order cited the identicality approach from [Doe v. GitHub](CASE-DOE-V-GITHUB.md) when dismissing DMCA claims.[^1]

## Legal Analysis

Jurisdiction: Northern District of California. Authority level: Rule 12(b)(6) order. The court did not decide [§ 107](STAT-USC-107.md) fair use.[^1]

What survived is a training-copy and induced-infringement theory plus some Lanham Act “in the style of” claims against Midjourney. What did not survive is DMCA copyright-management-information removal, on an identical-copy requirement the court treated as fatal where outputs were not identical to training images.[^1] Later amended complaints and any class-certification or summary-judgment orders are outside the sources cited here.

## Relationships

- `CASE-ANDERSEN-V-STABILITY` cites `SRC-ANDERSEN-V-STABILITY-MTD-2024`.
- `CASE-ANDERSEN-V-STABILITY` related_to `TOPIC-AI-COPYRIGHT`.
- `CASE-ANDERSEN-V-STABILITY` related_to `CASE-GETTY-V-STABILITY`.
- `CASE-ANDERSEN-V-STABILITY` related_to `CASE-DISNEY-V-MIDJOURNEY`.
- `CASE-ANDERSEN-V-STABILITY` related_to `CASE-DOE-V-GITHUB`.
- `CASE-ANDERSEN-V-STABILITY` related_to `CASE-IN-RE-GOOGLE-GEN-AI`.

## Sources

1. `SRC-ANDERSEN-V-STABILITY-MTD-2024`: Order on motions to dismiss FAC (Aug. 12, 2024).
2. `SRC-ANDERSEN-V-STABILITY-DOCKET`: CourtListener docket for No. 3:23-cv-00201.
3. `SRC-GOOGLE-GEN-AI-MTD-2025`: In re Google Generative AI MTD order (Sept. 11, 2025).

## Research Debt

- Add the original complaint, the FAC, and any later operative complaint as pleading sources.
- Add the October 30, 2023 first MTD order and later discovery or class-certification orders from those PDFs.
- Add trial-schedule facts only from a court scheduling order, not from secondary trackers.
