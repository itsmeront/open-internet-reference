---
id: CASE-GETTY-V-STABILITY
title: Getty Images (US), Inc. v. Stability AI Ltd.
type: case
status: draft
summary: English High Court trial judgment dismissing Getty’s secondary-copyright claim that Stable Diffusion was an infringing copy, after Getty abandoned UK training and output copyright claims, with limited historic trade-mark findings; a later Northern District of California action over the same models remains at the pleading stage.
tags:
  - case
  - copyright
  - artificial-intelligence
  - digital-rights
sources:
  - SRC-GETTY-V-STABILITY-EWHC-2025
  - SRC-GETTY-V-STABILITY-US-COMPLAINT
  - SRC-GETTY-V-STABILITY-US-MTD-2026
relationships:
  - subject: CASE-GETTY-V-STABILITY
    predicate: cites
    object: SRC-GETTY-V-STABILITY-EWHC-2025
    sources:
      - SRC-GETTY-V-STABILITY-EWHC-2025
  - subject: CASE-GETTY-V-STABILITY
    predicate: cites
    object: SRC-GETTY-V-STABILITY-US-MTD-2026
    sources:
      - SRC-GETTY-V-STABILITY-US-MTD-2026
  - subject: CASE-GETTY-V-STABILITY
    predicate: related_to
    object: TOPIC-AI-COPYRIGHT
    sources:
      - SRC-GETTY-V-STABILITY-EWHC-2025
  - subject: CASE-GETTY-V-STABILITY
    predicate: related_to
    object: CASE-ANDERSEN-V-STABILITY
    sources:
      - SRC-GETTY-V-STABILITY-EWHC-2025
  - subject: CASE-GETTY-V-STABILITY
    predicate: related_to
    object: CASE-KNESCHKE-V-LAION
    sources:
      - SRC-GETTY-V-STABILITY-US-MTD-2026
last_verified: "2026-09-02"
decision_date: "2025-11-04"
---

# Getty Images (US), Inc. v. Stability AI Ltd.

## Summary

Getty Images (US), Inc. v. Stability AI Ltd., [2025] EWHC 2863 (Ch) (4 Nov. 2025), is a first-instance English trial judgment about Stability AI Limited’s Stable Diffusion image-generation models. Getty abandoned its primary UK training, output, and database-right copyright claims before closing. The remaining copyright theory—that the model weights were an “infringing copy” imported or dealt in under the Copyright, Designs and Patents Act 1988—failed. Limited historic trade-mark infringement was found from some generated watermarks. The judgment is English law and is not a U.S. fair-use holding.

A separate U.S. action, Getty Images (US), Inc. v. Stability AI, Ltd., No. 25-cv-06891 (N.D. Cal.), was filed August 14, 2025, after Getty dismissed a Delaware predecessor without prejudice. On April 23, 2026, the Northern District of California dismissed Getty’s DMCA false-CMI claim without prejudice and allowed trademark, federal unfair-competition, dilution, and California UCL claims to proceed. Copyright infringement was not before the court on that motion.

## Verified Facts

- The English claim, No. IL-2023-000007 in the Intellectual Property List (Chancery Division), was tried before Mrs Justice Joanna Smith in June 2025 and decided on 4 November 2025.[^1]
- Getty alleged primary and secondary copyright infringement, database-right infringement, trade-mark infringement, and passing off against Stability AI Limited concerning Stable Diffusion.[^1]
- Shortly before closing submissions, Getty abandoned its training-and-development copyright claim, substantially abandoned its output copyright claim, and could no longer advance the database-right claim. The court recorded that Getty acknowledged there was no evidence the training had occurred in the United Kingdom.[^1]
- Getty continued a secondary-copyright theory under CDPA sections 22 and 23: that Stability imported, possessed, sold, or distributed an “article,” namely Stable Diffusion, which was an infringing copy because making the model weights in the UK would have infringed. Getty did not allege that the model itself stored copies of the copyright works.[^1]
- The court dismissed the secondary-copyright claim. It held that an “article” may be intangible, but an AI model such as Stable Diffusion that does not store or reproduce any copyright works, and has never done so, is not an “infringing copy,” so there is no infringement under sections 22 and 23.[^1]
- The court found Stability not directly liable for tortious acts arising from release of Stable Diffusion v1.x via CompVis GitHub and Hugging Face pages.[^1]
- Getty succeeded in part on trade-mark claims: limited historic infringement of iStock marks under Trade Marks Act 1994 sections 10(1) and 10(2) for some v1.x watermarks accessed via DreamStudio or the developer platform, and of Getty Images marks under section 10(2) for a v2.x example. Claims as to later models (SD XL and v1.6), section 10(3), and additional copyright damages were dismissed. The court declined to decide passing off.[^1]
- Getty first sued Stability AI in the District of Delaware, No. 23-cv-135-JLH. On August 14, 2025, Getty dismissed that action without prejudice and filed a complaint in the Northern District of California, No. 25-cv-06891, against Stability AI Ltd., Stability AI, Inc., and Stability AI US Services Corporation.[^2][^3]
- The U.S. complaint alleges seven counts: (I) copyright infringement; (II) false copyright management information under 17 U.S.C. § 1202(a); (III) trademark infringement under 15 U.S.C. § 1114(1); (IV) unfair competition under 15 U.S.C. § 1125(a); (V) trademark dilution under 15 U.S.C. § 1125(c); (VI) California unfair competition; and (VII) California trademark dilution.[^3]
- Getty alleges that it has identified over 12 million links to images and associated text from Getty websites in a LAION dataset used to train Stable Diffusion, and that it selected 25,647 registered examples for the copyright claims in that complaint.[^2]
- On April 23, 2026, Judge Trina L. Thompson granted in part and denied in part Stability’s motion to dismiss Counts II through VII. Count II (§ 1202(a)) was dismissed without prejudice, with leave to amend by May 7, 2026. The court held that Getty had not pleaded the specific intent required by § 1202(a) to induce, enable, facilitate, or conceal infringement through false CMI, treating generated watermarks as alleged incidental byproducts of training. Trademark, federal unfair-competition, dilution, and California UCL claims survived.[^3]


[^1]: `SRC-GETTY-V-STABILITY-EWHC-2025` — [2025] EWHC 2863 (Ch) (4 Nov. 2025). Primary for parties, abandoned claims, and English holdings.

[^2]: `SRC-GETTY-V-STABILITY-US-COMPLAINT` — U.S. complaint (Aug. 14, 2025). Primary for N.D. Cal. filing, defendants, alleged dataset copying, and the 25,647 registered examples.

[^3]: `SRC-GETTY-V-STABILITY-US-MTD-2026` — Order (Apr. 23, 2026). Primary for Delaware dismissal history, the seven counts, and the § 1202(a) / trademark / UCL rulings.

## Historical Context

Getty is the leading comparative image-training dispute with both a completed English trial and a live U.S. pleading-stage action. Unlike [Andersen v. Stability AI Ltd.](CASE-ANDERSEN-V-STABILITY.md), which remains a U.S. artists’ class action about training copies, the English trial never reached a merits holding that training Stable Diffusion on Getty photographs in the UK was copyright infringement, because that claim was abandoned for lack of UK training evidence.[^1] The U.S. complaint’s training theory is still pending; the April 2026 order did not decide it.[^3]

LAION datasets also appear in [Kneschke v. LAION](CASE-KNESCHKE-V-LAION.md) (German TDM exceptions for dataset compilation) and [In re Google Generative AI Copyright Litigation](CASE-IN-RE-GOOGLE-GEN-AI.md). Those cases have different defendants and different legal systems.[^3]

## Legal Analysis

Jurisdiction: High Court of England and Wales, plus a pending Northern District of California action. Authority level: English first-instance copyright and trade-mark judgment; U.S. Rule 12(b)(6) order on non-copyright counts. Neither source binds the other forum. The English judgment is not a Court of Justice of the European Union ruling, and the U.S. order is not a [§ 107](STAT-USC-107.md) holding.[^1][^3]

The English copyright holding is narrow. The court did not decide that training on copyrighted photographs is lawful. It decided that, on Getty’s remaining theory, model weights that do not store or reproduce the works are not infringing copies for secondary-infringement purposes under the CDPA.[^1] The English trade-mark findings concern generated Getty/iStock watermarks as signs, a different legal interest from copyright in the underlying photographs.[^1]

The U.S. false-CMI dismissal is also narrow. Stability moved only on Counts II through VII; Count I (copyright infringement) was not dismissed. The court required double scienter under § 1202(a) and treated incidental watermark generation as insufficient intent at that pleading.[^3] Trademark and UCL survival is a likelihood-of-confusion and borrowing-statute pleading result, not a finding that outputs infringe.

## Relationships

- `CASE-GETTY-V-STABILITY` cites `SRC-GETTY-V-STABILITY-EWHC-2025`.
- `CASE-GETTY-V-STABILITY` cites `SRC-GETTY-V-STABILITY-US-MTD-2026`.
- `CASE-GETTY-V-STABILITY` related_to `TOPIC-AI-COPYRIGHT`.
- `CASE-GETTY-V-STABILITY` related_to `CASE-ANDERSEN-V-STABILITY`.
- `CASE-GETTY-V-STABILITY` related_to `CASE-KNESCHKE-V-LAION`.

## Sources

1. `SRC-GETTY-V-STABILITY-EWHC-2025`: Getty Images v. Stability AI [2025] EWHC 2863 (Ch).
2. `SRC-GETTY-V-STABILITY-US-COMPLAINT`: U.S. complaint (Aug. 14, 2025).
3. `SRC-GETTY-V-STABILITY-US-MTD-2026`: Order on motion to dismiss (Apr. 23, 2026).

## Research Debt

- Add [2025] EWHC 3343 (Ch) (permission to appeal) and any Court of Appeal decision from those PDFs.
- Add any first amended U.S. complaint after the May 7, 2026 deadline, and any later order on Count I.
- Do not treat abandoned UK training claims as a holding that training is lawful.
