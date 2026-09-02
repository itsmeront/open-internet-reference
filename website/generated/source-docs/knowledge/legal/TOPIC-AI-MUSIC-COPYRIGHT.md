---
id: TOPIC-AI-MUSIC-COPYRIGHT
title: Music Copyright and Generative AI
type: topic
status: draft
summary: Music-industry copyright claims against generative AI, covering U.S. sound-recording suits against Suno and Udio, U.S. publisher lyric suits against Anthropic (including Concord II, BMG, and the August 2026 Sony/Warner complaint), and the German first-instance GEMA v. OpenAI judgment.
tags:
  - copyright
  - artificial-intelligence
  - digital-rights
  - case-studies
sources:
  - SRC-UMG-V-SUNO-COMPLAINT
  - SRC-UMG-V-SUNO-ANSWER
  - SRC-UMG-V-SUNO-WARNER-DISMISSAL
  - SRC-UMG-V-UDIO-COMPLAINT
  - SRC-UMG-V-UDIO-DOCKET
  - SRC-SONY-V-UDIO-2026-COMPLAINT
  - SRC-CONCORD-V-ANTHROPIC-MTD-2025
  - SRC-GEMA-V-OPENAI-LG-MUENCHEN-2025
  - SRC-GEMA-V-OPENAI-PRESS-2025
  - SRC-SONY-V-ANTHROPIC-COMPLAINT-2026
  - SRC-CONCORD-II-COMPLAINT
  - SRC-CONCORD-II-RELATED-2026
  - SRC-BMG-V-ANTHROPIC-COMPLAINT
  - SRC-USC-17-107-LII
relationships:
  - subject: TOPIC-AI-MUSIC-COPYRIGHT
    predicate: related_to
    object: CASE-UMG-V-SUNO
    sources:
      - SRC-UMG-V-SUNO-COMPLAINT
  - subject: TOPIC-AI-MUSIC-COPYRIGHT
    predicate: related_to
    object: CASE-UMG-V-UDIO
    sources:
      - SRC-UMG-V-UDIO-COMPLAINT
  - subject: TOPIC-AI-MUSIC-COPYRIGHT
    predicate: related_to
    object: CASE-CONCORD-V-ANTHROPIC
    sources:
      - SRC-CONCORD-V-ANTHROPIC-MTD-2025
  - subject: TOPIC-AI-MUSIC-COPYRIGHT
    predicate: related_to
    object: CASE-GEMA-V-OPENAI
    sources:
      - SRC-GEMA-V-OPENAI-LG-MUENCHEN-2025
  - subject: TOPIC-AI-MUSIC-COPYRIGHT
    predicate: related_to
    object: TOPIC-AI-COPYRIGHT
    sources:
      - SRC-UMG-V-SUNO-COMPLAINT
  - subject: TOPIC-AI-MUSIC-COPYRIGHT
    predicate: related_to
    object: TOPIC-AI-LITIGATION
    sources:
      - SRC-UMG-V-SUNO-COMPLAINT
  - subject: TOPIC-AI-MUSIC-COPYRIGHT
    predicate: related_to
    object: STAT-USC-107
    sources:
      - SRC-UMG-V-SUNO-ANSWER
  - subject: TOPIC-AI-MUSIC-COPYRIGHT
    predicate: related_to
    object: CASE-SONY-V-ANTHROPIC
    sources:
      - SRC-SONY-V-ANTHROPIC-COMPLAINT-2026
  - subject: TOPIC-AI-MUSIC-COPYRIGHT
    predicate: related_to
    object: CASE-BMG-V-ANTHROPIC
    sources:
      - SRC-BMG-V-ANTHROPIC-COMPLAINT
last_verified: "2026-09-02"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/legal/TOPIC-AI-MUSIC-COPYRIGHT.md`
- Source ID: `TOPIC-AI-MUSIC-COPYRIGHT`
- [**Edit this page**](https://github.com/itsmeront/open-internet-reference/edit/main/knowledge/legal/TOPIC-AI-MUSIC-COPYRIGHT.md) | [**Suggest a change**](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml&title=Edit+suggestion:+TOPIC-AI-MUSIC-COPYRIGHT)

!!! info "📝 Page Status: Draft — sourced but not yet reviewed"

    - **Status**: `draft`
    - **Sources**: 14
    - **Relationships**: 9
    - **Research debt items**: 4

---

# Music Copyright and Generative AI

## Summary

Generative-AI music disputes split along the same two copyright interests the industry has always separated: sound recordings (the recorded performance) and musical compositions (the song, including lyrics). U.S. major labels sued Suno and Udio over alleged unlicensed copying of masters. U.S. publishers sued Anthropic over lyrics in Claude, including Concord/UMG publishers (Concord I and Concord II), BMG, and a later Sony/Warner complaint. A German first-instance court held OpenAI liable for memorizing and outputting nine German lyrics. As of the sources reviewed here, no U.S. court had issued a fair-use merits ruling on training a generative music model.

## Verified Facts

- In [UMG Recordings, Inc. v. Suno, Inc.](CASE-UMG-V-SUNO.md), Universal, Sony, and Warner affiliates alleged in June 2024 that Suno copied their sound recordings to train a commercial music generator. Suno admitted training on tens of millions of recordings and pleaded fair use. Warner-affiliated plaintiffs later dismissed their claims with prejudice; UMG and Sony claims remained.[^1][^2][^3]
- In [UMG Recordings, Inc. v. Uncharted Labs, Inc.](CASE-UMG-V-UDIO.md), the same majors filed a parallel June 2024 sound-recording action against Udio in the Southern District of New York. UMG/Capitol and Warner later dismissed their claims without prejudice. Sony remained and in July 2026 filed a second action asserting 30,117 additional recordings.[^4][^5][^6]
- Both original label complaints plead post-1972 infringement under the Copyright Act and pre-1972 infringement under 17 U.S.C. § 1401, and both treat Exhibit A as an illustrative work list.[^1][^4]
- In [Concord Music Group, Inc. v. Anthropic PBC](CASE-CONCORD-V-ANTHROPIC.md), eight publishers allege that Anthropic used copyrighted lyrics to train Claude and that outputs reproduce those lyrics. On October 6, 2025, the Northern District of California denied Anthropic’s motion to dismiss the amended secondary-infringement and DMCA CMI claims. A second action, Concord II, filed January 28, 2026, alleges torrenting of books containing compositions and was related to Concord I on February 18, 2026.[^7][^12][^13]
- In [BMG Rights Management (US) LLC v. Anthropic PBC](CASE-BMG-V-ANTHROPIC.md), BMG sued Anthropic on March 17, 2026, alleging training and output infringement, torrenting, and CMI removal, and identifying Concord I and Concord II as related.[^14]
- In [Sony Music Publishing (US) LLC v. Anthropic PBC](CASE-SONY-V-ANTHROPIC.md), Sony and Warner Chappell affiliates sued Anthropic, Dario Amodei, and Benjamin Mann on August 28, 2026, alleging torrenting, scraping, training, output reproduction, and CMI removal as to musical compositions.[^11]
- In [GEMA v. OpenAI](CASE-GEMA-V-OPENAI.md), Landgericht München I on November 11, 2025 largely granted GEMA’s claims over nine German lyrics, holding that memorization in models 4 and 4o and output of those lyrics were unauthorized reproductions not covered by the text-and-data-mining exception. The court stated the judgment is not final.[^8][^9]
- U.S. fair use is a four-factor, case-specific limitation in [17 U.S.C. § 107](STAT-USC-107.md). Suno’s answer invokes that defense; the label complaints argue it does not apply. No source cited on this page is a U.S. judicial determination of that question for a music generator.[^1][^2][^10]


[^1]: [`SRC-UMG-V-SUNO-COMPLAINT`](../../../bibliography.md#SRC-UMG-V-SUNO-COMPLAINT) — Suno complaint (June 24, 2024).

[^2]: [`SRC-UMG-V-SUNO-ANSWER`](../../../bibliography.md#SRC-UMG-V-SUNO-ANSWER) — Suno answer (Aug. 1, 2024).

[^3]: [`SRC-UMG-V-SUNO-WARNER-DISMISSAL`](../../../bibliography.md#SRC-UMG-V-SUNO-WARNER-DISMISSAL) — Warner stipulation (Dec. 9, 2025).

[^4]: [`SRC-UMG-V-UDIO-COMPLAINT`](../../../bibliography.md#SRC-UMG-V-UDIO-COMPLAINT) — Udio complaint (June 2024).

[^5]: [`SRC-UMG-V-UDIO-DOCKET`](../../../bibliography.md#SRC-UMG-V-UDIO-DOCKET) — Udio docket, including 2025 dismissals.

[^6]: [`SRC-SONY-V-UDIO-2026-COMPLAINT`](../../../bibliography.md#SRC-SONY-V-UDIO-2026-COMPLAINT) — Sony follow-on complaint (July 20, 2026).

[^7]: [`SRC-CONCORD-V-ANTHROPIC-MTD-2025`](../../../bibliography.md#SRC-CONCORD-V-ANTHROPIC-MTD-2025) — Concord order denying MTD (Oct. 6, 2025).

[^8]: [`SRC-GEMA-V-OPENAI-LG-MUENCHEN-2025`](../../../bibliography.md#SRC-GEMA-V-OPENAI-LG-MUENCHEN-2025) — LG München I judgment (Nov. 11, 2025).

[^9]: [`SRC-GEMA-V-OPENAI-PRESS-2025`](../../../bibliography.md#SRC-GEMA-V-OPENAI-PRESS-2025) — Official press release (Nov. 11, 2025).

[^10]: [`SRC-USC-17-107-LII`](../../../bibliography.md#SRC-USC-17-107-LII) — 17 U.S.C. § 107.

[^11]: [`SRC-SONY-V-ANTHROPIC-COMPLAINT-2026`](../../../bibliography.md#SRC-SONY-V-ANTHROPIC-COMPLAINT-2026) — Sony/Warner publisher complaint (Aug. 28, 2026). Pending; allegations.

[^12]: [`SRC-CONCORD-II-COMPLAINT`](../../../bibliography.md#SRC-CONCORD-II-COMPLAINT) — Concord II complaint (Jan. 28, 2026). Pending; allegations.

[^13]: [`SRC-CONCORD-II-RELATED-2026`](../../../bibliography.md#SRC-CONCORD-II-RELATED-2026) — Related-case order (Feb. 18, 2026).

[^14]: [`SRC-BMG-V-ANTHROPIC-COMPLAINT`](../../../bibliography.md#SRC-BMG-V-ANTHROPIC-COMPLAINT) — BMG complaint (Mar. 17, 2026). Pending; allegations.

## Historical Context

Recorded-music copyright already distinguished the composition from the fixed recording. Generative systems cut across that line. A text model that emits lyrics is a composition problem. An audio model that emits a new recording in the style of existing masters is a sound-recording problem, and sometimes also a composition problem if melody or lyrics are reproduced. The 2024 label complaints treat the second problem as mass infringement of § 106 and § 1401 rights.[^1][^4] The publisher and GEMA matters treat the first as unauthorized reproduction and making available of lyrics.[^7][^8]

Book-training decisions such as [Bartz](CASE-BARTZ-V-ANTHROPIC.md) and [Kadrey](CASE-KADREY-V-META.md) are adjacent but not controlling here: different works, different outputs, and no music-generator fair-use holding.

## Legal Analysis

Keep four questions separate.

**Which exclusive right?** Labels plead reproduction of sound recordings used as training audio.[^1][^4] Publishers and GEMA plead reproduction and dissemination of lyrics.[^7][^8] A holding on one right does not decide the other.

**Has a court decided training?** In the United States, as of these sources, no. Suno pleaded fair use; Concord survived a motion to dismiss on secondary and CMI theories without a § 107 ruling.[^2][^7] In Germany, LG München I did decide that extractable memorization of lyrics is a reproduction outside commercial TDM, but that judgment is not final and is not U.S. law.[^8][^9]

**What do partial dismissals mean?** Warner’s Suno exit was with prejudice.[^3] UMG’s and Warner’s Udio exits were without prejudice.[^5] Neither set of stipulations states that training is lawful, and Sony’s 2026 Udio action shows the remaining label expanding the work list rather than abandoning the theory.[^6]

**Outputs versus weights.** GEMA treats simple-prompt regurgitation as proof that the work is fixed in the model and as a separate communication to the public.[^8] U.S. label complaints also rely on generated “soundalikes,” but those exhibits remain allegations.[^1][^4]

Broader authorship and book/news training issues stay on [Copyright and Generative AI](TOPIC-AI-COPYRIGHT.md). The docket inventory is on [AI Litigation Landscape](TOPIC-AI-LITIGATION.md).

## Relationships

- `TOPIC-AI-MUSIC-COPYRIGHT` related_to `CASE-UMG-V-SUNO`.
- `TOPIC-AI-MUSIC-COPYRIGHT` related_to `CASE-UMG-V-UDIO`.
- `TOPIC-AI-MUSIC-COPYRIGHT` related_to `CASE-CONCORD-V-ANTHROPIC`.
- `TOPIC-AI-MUSIC-COPYRIGHT` related_to `CASE-GEMA-V-OPENAI`.
- `TOPIC-AI-MUSIC-COPYRIGHT` related_to `TOPIC-AI-COPYRIGHT`.
- `TOPIC-AI-MUSIC-COPYRIGHT` related_to `TOPIC-AI-LITIGATION`.
- `TOPIC-AI-MUSIC-COPYRIGHT` related_to `STAT-USC-107`.
- `TOPIC-AI-MUSIC-COPYRIGHT` related_to `CASE-SONY-V-ANTHROPIC`.
- `TOPIC-AI-MUSIC-COPYRIGHT` related_to `CASE-BMG-V-ANTHROPIC`.

## Sources

1. [`SRC-UMG-V-SUNO-COMPLAINT`](../../../bibliography.md#SRC-UMG-V-SUNO-COMPLAINT): Suno complaint (2024).
2. [`SRC-UMG-V-SUNO-ANSWER`](../../../bibliography.md#SRC-UMG-V-SUNO-ANSWER): Suno answer (2024).
3. [`SRC-UMG-V-SUNO-WARNER-DISMISSAL`](../../../bibliography.md#SRC-UMG-V-SUNO-WARNER-DISMISSAL): Warner Suno dismissal (2025).
4. [`SRC-UMG-V-UDIO-COMPLAINT`](../../../bibliography.md#SRC-UMG-V-UDIO-COMPLAINT): Udio complaint (2024).
5. [`SRC-UMG-V-UDIO-DOCKET`](../../../bibliography.md#SRC-UMG-V-UDIO-DOCKET): Udio docket and dismissals.
6. [`SRC-SONY-V-UDIO-2026-COMPLAINT`](../../../bibliography.md#SRC-SONY-V-UDIO-2026-COMPLAINT): Sony second Udio complaint (2026).
7. [`SRC-CONCORD-V-ANTHROPIC-MTD-2025`](../../../bibliography.md#SRC-CONCORD-V-ANTHROPIC-MTD-2025): Concord MTD denial (2025).
8. [`SRC-GEMA-V-OPENAI-LG-MUENCHEN-2025`](../../../bibliography.md#SRC-GEMA-V-OPENAI-LG-MUENCHEN-2025): Munich judgment (2025).
9. [`SRC-GEMA-V-OPENAI-PRESS-2025`](../../../bibliography.md#SRC-GEMA-V-OPENAI-PRESS-2025): Munich press release (2025).
10. [`SRC-USC-17-107-LII`](../../../bibliography.md#SRC-USC-17-107-LII): 17 U.S.C. § 107.
11. [`SRC-SONY-V-ANTHROPIC-COMPLAINT-2026`](../../../bibliography.md#SRC-SONY-V-ANTHROPIC-COMPLAINT-2026): Sony/Warner publisher complaint (2026).
12. [`SRC-CONCORD-II-COMPLAINT`](../../../bibliography.md#SRC-CONCORD-II-COMPLAINT): Concord II complaint (2026).
13. [`SRC-CONCORD-II-RELATED-2026`](../../../bibliography.md#SRC-CONCORD-II-RELATED-2026): Concord II related-case order (2026).
14. [`SRC-BMG-V-ANTHROPIC-COMPLAINT`](../../../bibliography.md#SRC-BMG-V-ANTHROPIC-COMPLAINT): BMG v. Anthropic complaint (2026).

## Research Debt

- Add GEMA v. Suno or other official German audio-model judgments when the court text is available.
- Add Anthropic’s response in Sony/Warner, BMG, and Concord II, and any motion to dismiss.
- Add U.S. fair-use or § 1201 orders in the Suno and Udio dockets when they issue.
- Do not use lawsuit-tracker royalty or equity figures as facts.

## Document metadata

- Last verified: `2026-09-02`
