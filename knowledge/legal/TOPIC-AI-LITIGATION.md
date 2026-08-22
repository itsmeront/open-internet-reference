---
id: TOPIC-AI-LITIGATION
title: AI Litigation Landscape
type: topic
status: draft
summary: Inventory of major civil actions involving generative AI, spanning copyright of training data and outputs (including music), chatbot product-liability claims, and adjacent First Amendment issues.
tags:
  - artificial-intelligence
  - copyright
  - first-amendment
  - digital-rights
  - case-studies
  - intermediary-liability
sources:
  - SRC-THALER-V-PERLMUTTER-CADC
  - SRC-BARTZ-V-ANTHROPIC-FAIR-USE
  - SRC-BARTZ-V-ANTHROPIC-FINAL-APPROVAL
  - SRC-KADREY-V-META-FAIR-USE
  - SRC-THOMSON-REUTERS-V-ROSS-2025
  - SRC-NYT-V-OPENAI-MTD-2025
  - SRC-NYT-V-OPENAI-12C-2026
  - SRC-SPYDER-V-MEMENTUM-COMPLAINT
  - SRC-GARCIA-V-CHARACTER-MTD-2025
  - SRC-USCO-AI-COPYRIGHTABILITY-REPORT-2025
  - SRC-UMG-V-SUNO-COMPLAINT
  - SRC-UMG-V-UDIO-COMPLAINT
  - SRC-CONCORD-V-ANTHROPIC-MTD-2025
  - SRC-GEMA-V-OPENAI-LG-MUENCHEN-2025
relationships:
  - subject: TOPIC-AI-LITIGATION
    predicate: related_to
    object: TOPIC-AI-COPYRIGHT
    sources:
      - SRC-USCO-AI-COPYRIGHTABILITY-REPORT-2025
  - subject: TOPIC-AI-LITIGATION
    predicate: related_to
    object: TOPIC-BRAIN-ROT
    sources:
      - SRC-SPYDER-V-MEMENTUM-COMPLAINT
  - subject: TOPIC-AI-LITIGATION
    predicate: related_to
    object: CASE-THALER-V-PERLMUTTER
    sources:
      - SRC-THALER-V-PERLMUTTER-CADC
  - subject: TOPIC-AI-LITIGATION
    predicate: related_to
    object: CASE-BARTZ-V-ANTHROPIC
    sources:
      - SRC-BARTZ-V-ANTHROPIC-FINAL-APPROVAL
  - subject: TOPIC-AI-LITIGATION
    predicate: related_to
    object: CASE-KADREY-V-META
    sources:
      - SRC-KADREY-V-META-FAIR-USE
  - subject: TOPIC-AI-LITIGATION
    predicate: related_to
    object: CASE-THOMSON-REUTERS-V-ROSS
    sources:
      - SRC-THOMSON-REUTERS-V-ROSS-2025
  - subject: TOPIC-AI-LITIGATION
    predicate: related_to
    object: CASE-NYT-V-OPENAI
    sources:
      - SRC-NYT-V-OPENAI-MTD-2025
  - subject: TOPIC-AI-LITIGATION
    predicate: related_to
    object: CASE-SPYDER-V-MEMENTUM
    sources:
      - SRC-SPYDER-V-MEMENTUM-COMPLAINT
  - subject: TOPIC-AI-LITIGATION
    predicate: related_to
    object: CASE-GARCIA-V-CHARACTER-TECHNOLOGIES
    sources:
      - SRC-GARCIA-V-CHARACTER-MTD-2025
  - subject: TOPIC-AI-LITIGATION
    predicate: related_to
    object: TOPIC-AI-MUSIC-COPYRIGHT
    sources:
      - SRC-UMG-V-SUNO-COMPLAINT
  - subject: TOPIC-AI-LITIGATION
    predicate: related_to
    object: CASE-UMG-V-SUNO
    sources:
      - SRC-UMG-V-SUNO-COMPLAINT
  - subject: TOPIC-AI-LITIGATION
    predicate: related_to
    object: CASE-UMG-V-UDIO
    sources:
      - SRC-UMG-V-UDIO-COMPLAINT
  - subject: TOPIC-AI-LITIGATION
    predicate: related_to
    object: CASE-CONCORD-V-ANTHROPIC
    sources:
      - SRC-CONCORD-V-ANTHROPIC-MTD-2025
  - subject: TOPIC-AI-LITIGATION
    predicate: related_to
    object: CASE-GEMA-V-OPENAI
    sources:
      - SRC-GEMA-V-OPENAI-LG-MUENCHEN-2025
  - subject: TOPIC-AI-LITIGATION
    predicate: related_to
    object: TOPIC-FIRST-AMENDMENT
    sources:
      - SRC-GARCIA-V-CHARACTER-MTD-2025
  - subject: TOPIC-AI-LITIGATION
    predicate: related_to
    object: TOPIC-DEVELOPER-SOFTWARE-LIABILITY
    sources:
      - SRC-GARCIA-V-CHARACTER-MTD-2025
    notes: Adjacent inventory of proceedings against software authors; Garcia is civil product liability, not a criminal developer prosecution.
last_verified: "2026-08-22"
---

# AI Litigation Landscape

## Summary

Generative AI is now a regular subject of civil litigation. The cases documented here fall into four clusters: (1) copyright in training data and model outputs, including news, books, and music, (2) copyright and trademark claims over AI-generated viral characters, (3) product-liability and speech defenses when chatbot products are alleged to have harmed users, and (4) one comparative German first-instance lyric judgment. This page is an inventory, not a prediction of outcomes.

## Verified Facts

- [Thaler v. Perlmutter](CASE-THALER-V-PERLMUTTER.md) (D.C. Cir. Mar. 18, 2025) held that the Copyright Act requires human authorship and affirmed refusal to register a work attributed solely to a generative-AI system.[^1]
- The Copyright Office’s January 2025 copyrightability report concluded that purely AI-generated material is not copyrightable and that prompts alone do not provide sufficient human control on current generally available technology.[^2]
- [Thomson Reuters v. Ross Intelligence](CASE-THOMSON-REUTERS-V-ROSS.md) (D. Del. Feb. 11, 2025) rejected fair use for a non-generative legal-research AI trained on Westlaw headnotes to compete with Westlaw.[^3]
- [Bartz v. Anthropic PBC](CASE-BARTZ-V-ANTHROPIC.md) (N.D. Cal. June 23, 2025) held that training Claude on books was transformative fair use but that a pirated permanent library was not; a $1.5 billion class settlement of piracy claims was finally approved July 20, 2026.[^4][^5]
- [Kadrey v. Meta Platforms, Inc.](CASE-KADREY-V-META.md) (N.D. Cal. June 25, 2025) granted Meta fair-use summary judgment on Llama training as to thirteen authors on that record, while leaving torrenting-distribution claims for later proceedings.[^6]
- [The New York Times Company v. Microsoft Corp.](CASE-NYT-V-OPENAI.md) (S.D.N.Y.) survived most of an April 4, 2025 motion to dismiss; an August 6, 2026 order dismissed material-contribution contributory claims premised on alleged end-user infringement.[^7][^8]
- [Spyder Games LLC v. Mementum Lab](CASE-SPYDER-V-MEMENTUM.md) (N.D. Cal., filed Nov. 26, 2025) seeks a declaration that AI-generated “brainrot” characters used in Steal a Brainrot are not copyrightable. See [Brain Rot and AI-Generated Meme Characters](TOPIC-BRAIN-ROT.md).[^9]
- [Garcia v. Character Technologies, Inc.](CASE-GARCIA-V-CHARACTER-TECHNOLOGIES.md) (M.D. Fla. May 20, 2025) allowed most wrongful-death and product-liability claims against a chatbot company and Google to proceed and declined, at the pleading stage, to treat LLM output as protected speech.[^10]
- Music copyright dockets are inventoried in [Music Copyright and Generative AI](TOPIC-AI-MUSIC-COPYRIGHT.md): [UMG v. Suno](CASE-UMG-V-SUNO.md) and [UMG v. Udio](CASE-UMG-V-UDIO.md) (sound recordings; partial dismissals; no U.S. fair-use holding), [Concord v. Anthropic](CASE-CONCORD-V-ANTHROPIC.md) (lyrics; secondary and DMCA claims survive dismissal), and [GEMA v. OpenAI](CASE-GEMA-V-OPENAI.md) (non-final German first-instance lyric judgment).[^11][^12][^13][^14]


[^1]: `SRC-THALER-V-PERLMUTTER-CADC` — 130 F.4th 1039 (D.C. Cir. 2025).

[^2]: `SRC-USCO-AI-COPYRIGHTABILITY-REPORT-2025` — Copyright Office Part 2 report (Jan. 2025).

[^3]: `SRC-THOMSON-REUTERS-V-ROSS-2025` — D. Del. Feb. 11, 2025.

[^4]: `SRC-BARTZ-V-ANTHROPIC-FAIR-USE` — N.D. Cal. June 23, 2025.

[^5]: `SRC-BARTZ-V-ANTHROPIC-FINAL-APPROVAL` — N.D. Cal. July 20, 2026.

[^6]: `SRC-KADREY-V-META-FAIR-USE` — 788 F. Supp. 3d 1026 (N.D. Cal. 2025).

[^7]: `SRC-NYT-V-OPENAI-MTD-2025` — S.D.N.Y. Apr. 4, 2025.

[^8]: `SRC-NYT-V-OPENAI-12C-2026` — S.D.N.Y. Aug. 6, 2026.

[^9]: `SRC-SPYDER-V-MEMENTUM-COMPLAINT` — N.D. Cal. Nov. 26, 2025. Pending; allegations.

[^10]: `SRC-GARCIA-V-CHARACTER-MTD-2025` — M.D. Fla. May 20, 2025. Pleading-stage order.

[^11]: `SRC-UMG-V-SUNO-COMPLAINT` — D. Mass. June 24, 2024. Pending.

[^12]: `SRC-UMG-V-UDIO-COMPLAINT` — S.D.N.Y. June 2024. Pending.

[^13]: `SRC-CONCORD-V-ANTHROPIC-MTD-2025` — N.D. Cal. Oct. 6, 2025.

[^14]: `SRC-GEMA-V-OPENAI-LG-MUENCHEN-2025` — LG München I Nov. 11, 2025. Not final.

## Case map

| Cluster | Leading OIR page | What is actually decided (as of sources cited) |
| --- | --- | --- |
| Output authorship | [Thaler](CASE-THALER-V-PERLMUTTER.md) | Machine listed as sole author cannot register. |
| Training vs piracy | [Bartz](CASE-BARTZ-V-ANTHROPIC.md) | Training fair use; pirated library not; piracy claims settled. |
| Training market harm | [Kadrey](CASE-KADREY-V-META.md) | Fair use on this record; dilution theory undeveloped. |
| Competing research AI | [Ross](CASE-THOMSON-REUTERS-V-ROSS.md) | Not fair use; tool was not generative. |
| News outputs | [Times v. OpenAI](CASE-NYT-V-OPENAI.md) | Claims largely survive dismissal; some secondary theories dismissed. |
| Meme-character ownership | [Spyder](CASE-SPYDER-V-MEMENTUM.md) | Pending declaration action. |
| Music masters | [Suno](CASE-UMG-V-SUNO.md) / [Udio](CASE-UMG-V-UDIO.md) | Pending; partial dismissals; no U.S. fair-use holding. |
| Music lyrics (U.S.) | [Concord](CASE-CONCORD-V-ANTHROPIC.md) | Secondary and CMI claims survive 12(b)(6). |
| Music lyrics (DE) | [GEMA](CASE-GEMA-V-OPENAI.md) | First-instance liability; not final. |
| Chatbot harm | [Garcia](CASE-GARCIA-V-CHARACTER-TECHNOLOGIES.md) | Design-defect claims proceed; speech defense not established at 12(b)(6). |

## Legal Analysis

These dockets are not one “AI law.” Copyright training cases apply [§ 107](STAT-USC-107.md) to copying that happens before a user sees an answer. Authorship cases ask who, if anyone, owns the answer or the image. Product-liability cases ask whether the software is a product whose design can be defective, which collides with [First Amendment](TOPIC-FIRST-AMENDMENT.md) arguments that outputs are speech.[^10]

For open-internet and software-freedom work, two tensions matter. First, a broad training-is-always-infringement rule would raise the cost of building models, including open-weight models; Bartz and Kadrey show district judges already disagree about how to weigh that against market harm.[^4][^6] Second, treating chatbot text as unprotected non-speech at the pleading stage, as in Garcia, could expand design-defect litigation against conversational software without a merits record on causation.[^10]

Criminal and sanctions cases involving software authors remain on [Documented Proceedings Involving Software Authors and Operators](TOPIC-DEVELOPER-SOFTWARE-LIABILITY.md); they are a different inventory.

## Relationships

- `TOPIC-AI-LITIGATION` related_to `TOPIC-AI-COPYRIGHT`.
- `TOPIC-AI-LITIGATION` related_to `TOPIC-BRAIN-ROT`.
- `TOPIC-AI-LITIGATION` related_to `CASE-THALER-V-PERLMUTTER`.
- `TOPIC-AI-LITIGATION` related_to `CASE-BARTZ-V-ANTHROPIC`.
- `TOPIC-AI-LITIGATION` related_to `CASE-KADREY-V-META`.
- `TOPIC-AI-LITIGATION` related_to `CASE-THOMSON-REUTERS-V-ROSS`.
- `TOPIC-AI-LITIGATION` related_to `CASE-NYT-V-OPENAI`.
- `TOPIC-AI-LITIGATION` related_to `CASE-SPYDER-V-MEMENTUM`.
- `TOPIC-AI-LITIGATION` related_to `CASE-GARCIA-V-CHARACTER-TECHNOLOGIES`.
- `TOPIC-AI-LITIGATION` related_to `TOPIC-AI-MUSIC-COPYRIGHT`.
- `TOPIC-AI-LITIGATION` related_to `CASE-UMG-V-SUNO`.
- `TOPIC-AI-LITIGATION` related_to `CASE-UMG-V-UDIO`.
- `TOPIC-AI-LITIGATION` related_to `CASE-CONCORD-V-ANTHROPIC`.
- `TOPIC-AI-LITIGATION` related_to `CASE-GEMA-V-OPENAI`.
- `TOPIC-AI-LITIGATION` related_to `TOPIC-FIRST-AMENDMENT`.
- `TOPIC-AI-LITIGATION` related_to `TOPIC-DEVELOPER-SOFTWARE-LIABILITY`.

## Sources

1. `SRC-THALER-V-PERLMUTTER-CADC`: Thaler v. Perlmutter, 130 F.4th 1039 (D.C. Cir. 2025).
2. `SRC-USCO-AI-COPYRIGHTABILITY-REPORT-2025`: Copyright Office AI copyrightability report, Part 2 (2025).
3. `SRC-THOMSON-REUTERS-V-ROSS-2025`: Thomson Reuters v. Ross Intelligence (D. Del. 2025).
4. `SRC-BARTZ-V-ANTHROPIC-FAIR-USE`: Bartz fair-use order (2025).
5. `SRC-BARTZ-V-ANTHROPIC-FINAL-APPROVAL`: Bartz settlement final approval (2026).
6. `SRC-KADREY-V-META-FAIR-USE`: Kadrey v. Meta (2025).
7. `SRC-NYT-V-OPENAI-MTD-2025`: Times MTD opinion (2025).
8. `SRC-NYT-V-OPENAI-12C-2026`: Times Rule 12(c) order (2026).
9. `SRC-SPYDER-V-MEMENTUM-COMPLAINT`: Spyder complaint (2025).
10. `SRC-GARCIA-V-CHARACTER-MTD-2025`: Garcia MTD order (2025).
11. `SRC-UMG-V-SUNO-COMPLAINT`: UMG v. Suno complaint (2024).
12. `SRC-UMG-V-UDIO-COMPLAINT`: UMG v. Udio complaint (2024).
13. `SRC-CONCORD-V-ANTHROPIC-MTD-2025`: Concord MTD denial (2025).
14. `SRC-GEMA-V-OPENAI-LG-MUENCHEN-2025`: GEMA v. OpenAI (2025).

## Research Debt

- Add Walters v. OpenAI (defamation / ChatGPT hallucinations) with a primary docket and any opinion.
- Add Getty Images v. Stability AI (UK and U.S.) from judgments.
- Add EU AI Act public-enforcement matters only with official documents.
- Verify Garcia docket for any 2026 settlement or judgment before stating the case is resolved.
- Defamation, biometric-privacy, and employment AI cases are not yet in this inventory.
