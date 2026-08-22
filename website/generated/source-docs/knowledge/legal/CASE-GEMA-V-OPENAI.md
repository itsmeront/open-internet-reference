---
id: CASE-GEMA-V-OPENAI
title: GEMA v. OpenAI (LG München I)
type: case
status: draft
summary: First-instance Munich judgment holding that memorization of nine German song lyrics in OpenAI models 4 and 4o, and output of those lyrics, infringed copyright and was not covered by the text-and-data-mining exception; the decision is not final.
tags:
  - case
  - copyright
  - artificial-intelligence
  - digital-rights
sources:
  - SRC-GEMA-V-OPENAI-LG-MUENCHEN-2025
  - SRC-GEMA-V-OPENAI-PRESS-2025
relationships:
  - subject: CASE-GEMA-V-OPENAI
    predicate: cites
    object: SRC-GEMA-V-OPENAI-LG-MUENCHEN-2025
    sources:
      - SRC-GEMA-V-OPENAI-LG-MUENCHEN-2025
  - subject: CASE-GEMA-V-OPENAI
    predicate: related_to
    object: TOPIC-AI-MUSIC-COPYRIGHT
    sources:
      - SRC-GEMA-V-OPENAI-LG-MUENCHEN-2025
  - subject: CASE-GEMA-V-OPENAI
    predicate: related_to
    object: TOPIC-AI-COPYRIGHT
    sources:
      - SRC-GEMA-V-OPENAI-LG-MUENCHEN-2025
  - subject: CASE-GEMA-V-OPENAI
    predicate: related_to
    object: CASE-CONCORD-V-ANTHROPIC
    sources:
      - SRC-GEMA-V-OPENAI-LG-MUENCHEN-2025
last_verified: "2026-08-22"
decision_date: "2025-11-11"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/legal/CASE-GEMA-V-OPENAI.md`
- Source ID: `CASE-GEMA-V-OPENAI`
- [**Edit this page**](https://github.com/itsmeront/open-internet-reference/edit/main/knowledge/legal/CASE-GEMA-V-OPENAI.md) | [**Suggest a change**](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml&title=Edit+suggestion:+CASE-GEMA-V-OPENAI)

!!! info "📝 Page Status: Draft — sourced but not yet reviewed"

    - **Status**: `draft`
    - **Sources**: 2
    - **Relationships**: 4
    - **Research debt items**: 3

---

# GEMA v. OpenAI (LG München I)

## Summary

GEMA v. OpenAI, Az. 42 O 14139/24 (LG München I, Nov. 11, 2025), is a German first-instance copyright judgment for Germany’s musical collecting society against two OpenAI group companies. The 42nd Civil Chamber largely granted injunction, information, and damages claims over nine German song lyrics, holding that memorization in models 4 and 4o and output of those lyrics were unauthorized reproductions not covered by the text-and-data-mining exception. A personality-rights claim over misattributed altered lyrics was dismissed. The court’s press release states that the judgment is not final.

## Verified Facts

- On November 11, 2025, Landgericht München I entered judgment in 42 O 14139/24 on claims by GEMA against two OpenAI-group defendants concerning nine well-known German song lyrics, including “Atemlos” (Kristina Bach) and “Wie schön, dass du geboren bist” (Rolf Zuckowski).[^1][^2]
- The court enjoined the defendants, on pain of a fine of up to €250,000 or imprisonment, from reproducing the lyrics in large language models without consent, as occurred in models 4 and 4o, and from making the lyrics available or reproducing them in chatbot outputs without consent.[^1]
- The court also ordered the defendants to provide an organized accounting of the extent of those acts and resulting revenues (from specified start dates for each defendant) and addressed damages and pre-litigation costs in the tenor.[^1]
- The official headnotes state that memorization can be found by comparing the original work with output from a simple prompt; that memorization in a language model is a reproduction under § 16 UrhG because the work is physically fixed and can be made indirectly perceptible; that fixation does not require identifying a discrete dataset if the work is present in model parameters; and that § 44b UrhG covers reproductions when compiling training material, not training that goes beyond preparing text-and-data mining.[^1]
- The court held the model operators liable for infringing outputs because they exercise control (Tatherrschaft); users may assume control if they provoke outputs, but that is not so for simple prompts.[^1]
- The chamber rejected the TDM exception for in-model reproductions: preparatory copies for analysis do not affect authors’ exploitation interests, but storing works in specified model parameters does. It also rejected an analogical extension of § 44b and rejected § 57 UrhG (insignificant accessory) because the training corpus is not itself a protected main work.[^2]
- The chamber dismissed GEMA’s additional claim for violation of general personality rights based on incorrect attribution of altered lyrics.[^2]
- The official press release states that the judgment is not legally binding (nicht rechtskräftig). The official decision report lists an appellate caption OLG München 6 U 3662/25 e.[^1][^2]


[^1]: [`SRC-GEMA-V-OPENAI-LG-MUENCHEN-2025`](../../../bibliography.md#SRC-GEMA-V-OPENAI-LG-MUENCHEN-2025) — Official Endurteil report (Nov. 11, 2025). Primary for tenor, headnotes, and appeal caption.

[^2]: [`SRC-GEMA-V-OPENAI-PRESS-2025`](../../../bibliography.md#SRC-GEMA-V-OPENAI-PRESS-2025) — Official court press release (Nov. 11, 2025). Primary for summary holdings, dismissed personality-rights claim, and non-final status.

## Historical Context

GEMA is a collecting society asserting lyrics, not record-label master rights. The theory—that a model that can emit lyrics on a simple prompt has reproduced those lyrics in its parameters—parallels the U.S. publisher allegations in [Concord v. Anthropic](CASE-CONCORD-V-ANTHROPIC.md), but this is a first-instance merits judgment under the German Copyright Act and the InfoSoc and DSM Directives, not a U.S. fair-use case.

## Legal Analysis

Jurisdiction: Landgericht München I (first instance). Authority level: non-final German judgment. It does not bind U.S. courts and is not a Court of Justice of the European Union ruling.[^1][^2]

The doctrinal move is to treat extractable memorization as “reproduction in any manner or form” under Art. 2 InfoSoc Directive / § 16 UrhG, including fixation as probability parameters.[^1][^2] The court then narrows commercial TDM (§ 44b UrhG / Art. 4 DSM Directive) to corpus-preparation copies, not lasting embodiment of works in a trained model.[^1] Operator liability for simple-prompt outputs follows from the court’s view that the model, not the user, generates the content.[^1]

Comparative use: this is evidence of one EU member-state first-instance approach to lyrics and LLMs. It is not a statement of settled EU law, and it is not a holding about generative audio models such as [Suno](CASE-UMG-V-SUNO.md) or [Udio](CASE-UMG-V-UDIO.md).

## Relationships

- `CASE-GEMA-V-OPENAI` cites [`SRC-GEMA-V-OPENAI-LG-MUENCHEN-2025`](../../../bibliography.md#SRC-GEMA-V-OPENAI-LG-MUENCHEN-2025).
- `CASE-GEMA-V-OPENAI` related_to `TOPIC-AI-MUSIC-COPYRIGHT`.
- `CASE-GEMA-V-OPENAI` related_to `TOPIC-AI-COPYRIGHT`.
- `CASE-GEMA-V-OPENAI` related_to `CASE-CONCORD-V-ANTHROPIC`.

## Sources

1. [`SRC-GEMA-V-OPENAI-LG-MUENCHEN-2025`](../../../bibliography.md#SRC-GEMA-V-OPENAI-LG-MUENCHEN-2025): LG München I Endurteil, 42 O 14139/24 (Nov. 11, 2025).
2. [`SRC-GEMA-V-OPENAI-PRESS-2025`](../../../bibliography.md#SRC-GEMA-V-OPENAI-PRESS-2025): LG München I Pressemitteilung 11/2025.

## Research Debt

- Add any OLG München appellate judgment in 6 U 3662/25 e when issued.
- Add GEMA’s complaint or a certified English translation only if an official or party-issued text is available.
- Add GEMA v. Suno or other German music-AI judgments from official court texts, not trackers.

## Document metadata

- Decision date: `2025-11-11`
- Last verified: `2026-08-22`
