---
id: CASE-KNESCHKE-V-LAION
title: Kneschke v. LAION e.V.
type: case
status: draft
summary: German photographer’s claim against LAION over downloading an image to build an open AI training dataset was dismissed; the Hamburg Regional Court applied the scientific-research text-and-data-mining exception, and the Higher Regional Court affirmed, also applying the general TDM exception.
tags:
  - case
  - copyright
  - artificial-intelligence
  - digital-rights
sources:
  - SRC-KNESCHKE-LG-HAMBURG-2024
  - SRC-KNESCHKE-OLG-HAMBURG-2025
relationships:
  - subject: CASE-KNESCHKE-V-LAION
    predicate: cites
    object: SRC-KNESCHKE-LG-HAMBURG-2024
    sources:
      - SRC-KNESCHKE-LG-HAMBURG-2024
  - subject: CASE-KNESCHKE-V-LAION
    predicate: related_to
    object: CASE-GETTY-V-STABILITY
    sources:
      - SRC-KNESCHKE-LG-HAMBURG-2024
  - subject: CASE-KNESCHKE-V-LAION
    predicate: related_to
    object: CASE-GEMA-V-OPENAI
    sources:
      - SRC-KNESCHKE-OLG-HAMBURG-2025
  - subject: CASE-KNESCHKE-V-LAION
    predicate: related_to
    object: TOPIC-AI-COPYRIGHT
    sources:
      - SRC-KNESCHKE-LG-HAMBURG-2024
last_verified: "2026-09-02"
decision_date: "2024-09-27"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/legal/CASE-KNESCHKE-V-LAION.md`
- Source ID: `CASE-KNESCHKE-V-LAION`
- [**Edit this page**](https://github.com/itsmeront/open-internet-reference/edit/main/knowledge/legal/CASE-KNESCHKE-V-LAION.md) | [**Suggest a change**](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml&title=Edit+suggestion:+CASE-KNESCHKE-V-LAION)

!!! info "📝 Page Status: Draft — sourced but not yet reviewed"

    - **Status**: `draft`
    - **Sources**: 2
    - **Relationships**: 4
    - **Research debt items**: 3

---

# Kneschke v. LAION e.V.

## Summary

Kneschke v. LAION e.V., Az. 310 O 227/23 (LG Hamburg, Sept. 27, 2024), aff’d 5 U 104/24 (OLG Hamburg, Dec. 10, 2025), is a German copyright action by photographer Robert Kneschke against the nonprofit LAION over downloading his photograph from a stock-photo site to compile an image-text dataset used for AI training. The Regional Court dismissed the claim, holding the reproduction was covered by the scientific-research text-and-data-mining exception. The Higher Regional Court dismissed the appeal and, as reported, also applied the general TDM exception. The decisions are German law implementing the DSM Directive’s TDM exceptions; they are not U.S. fair-use holdings and do not decide commercial model training by for-profit labs.

## Verified Facts

- On September 27, 2024, Landgericht Hamburg, 10. Zivilkammer, entered judgment in 310 O 227/23 dismissing the photographer’s complaint (Tenor: “Die Klage wird abgewiesen.”).[^1]
- The court found that LAION reproduced the photograph by downloading it, thereby interfering with the photographer’s exploitation rights, but that the reproduction was covered by the statutory TDM exception for scientific research. It treated the general commercial TDM exception as doubtful on the facts and unnecessary to decide because the research exception applied.[^1]
- LAION’s dataset is described as a publicly available table of hyperlinks to images plus text descriptions (image-text pairs) that can be used to train generative models; the disputed act was a download to compare image content with an existing description.[^1]
- On December 10, 2025, the Hanseatic Higher Regional Court, 5 U 104/24, dismissed the photographer’s appeal from the September 27, 2024 judgment. The court’s reported holding is that LAION’s use was covered by both § 44b UrhG (general TDM) and § 60d UrhG (research TDM), including that the stock-site reservation of use did not meet the machine-readability requirement for an effective opt-out under § 44b(3).[^2]


[^1]: [`SRC-KNESCHKE-LG-HAMBURG-2024`](../../../bibliography.md#SRC-KNESCHKE-LG-HAMBURG-2024) — LG Hamburg, 310 O 227/23 (Sept. 27, 2024). Primary for tenor and first-instance holdings.

[^2]: [`SRC-KNESCHKE-OLG-HAMBURG-2025`](../../../bibliography.md#SRC-KNESCHKE-OLG-HAMBURG-2025) — OLG Hamburg decision report, 5 U 104/24 (Dec. 10, 2025). Primary for appellate caption and reported holdings.

## Historical Context

Kneschke is the leading German dataset-compilation case. It is distinct from [GEMA v. OpenAI](CASE-GEMA-V-OPENAI.md), which treated memorized lyrics in a commercial LLM as reproductions outside TDM, and from [Getty Images v. Stability AI](CASE-GETTY-V-STABILITY.md), an English trial about model weights as infringing copies. LAION is a nonprofit dataset publisher, not a commercial image-generator operator.

## Legal Analysis

Jurisdiction: Landgericht Hamburg, affirmed by OLG Hamburg. Authority level: German first- and second-instance copyright judgments applying §§ 44b and 60d UrhG / Arts. 3–4 of the DSM Directive. They do not bind U.S. courts and are not Court of Justice of the European Union rulings.[^1][^2]

The first-instance court decided only the download used to build the dataset, not whether later commercial training of a generative model is TDM.[^1] The appellate report adds that both TDM exceptions applied and that a natural-language website reservation was not an effective machine-readable opt-out on those facts.[^2] BGH review, if sought, is outside the sources cited here.

## Relationships

- `CASE-KNESCHKE-V-LAION` cites [`SRC-KNESCHKE-LG-HAMBURG-2024`](../../../bibliography.md#SRC-KNESCHKE-LG-HAMBURG-2024).
- `CASE-KNESCHKE-V-LAION` related_to `CASE-GETTY-V-STABILITY`.
- `CASE-KNESCHKE-V-LAION` related_to `CASE-GEMA-V-OPENAI`.
- `CASE-KNESCHKE-V-LAION` related_to `TOPIC-AI-COPYRIGHT`.

## Sources

1. [`SRC-KNESCHKE-LG-HAMBURG-2024`](../../../bibliography.md#SRC-KNESCHKE-LG-HAMBURG-2024): LG Hamburg, 310 O 227/23 (Sept. 27, 2024).
2. [`SRC-KNESCHKE-OLG-HAMBURG-2025`](../../../bibliography.md#SRC-KNESCHKE-OLG-HAMBURG-2025): OLG Hamburg, 5 U 104/24 (Dec. 10, 2025).

## Research Debt

- Replace the rewis reprint with an official LG PDF or openJur citation when available.
- Add the official OLG Hamburg judgment PDF and any BGH caption (reported elsewhere as I ZR 281/25) from those texts.
- Do not treat this as a holding that commercial generative-model training is lawful TDM.

## Document metadata

- Decision date: `2024-09-27`
- Last verified: `2026-09-02`
