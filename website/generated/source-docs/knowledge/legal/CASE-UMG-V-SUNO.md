---
id: CASE-UMG-V-SUNO
title: UMG Recordings, Inc. v. Suno, Inc.
type: case
status: draft
summary: Pending District of Massachusetts copyright action in which major record labels allege that Suno copied sound recordings to train a generative music service; Suno asserts fair use, and Warner-affiliated plaintiffs later dismissed their claims with prejudice.
tags:
  - case
  - copyright
  - artificial-intelligence
  - digital-rights
sources:
  - SRC-UMG-V-SUNO-COMPLAINT
  - SRC-UMG-V-SUNO-ANSWER
  - SRC-UMG-V-SUNO-WARNER-DISMISSAL
  - SRC-USC-17-107-LII
relationships:
  - subject: CASE-UMG-V-SUNO
    predicate: cites
    object: SRC-UMG-V-SUNO-COMPLAINT
    sources:
      - SRC-UMG-V-SUNO-COMPLAINT
  - subject: CASE-UMG-V-SUNO
    predicate: related_to
    object: CASE-UMG-V-UDIO
    sources:
      - SRC-UMG-V-SUNO-COMPLAINT
  - subject: CASE-UMG-V-SUNO
    predicate: related_to
    object: TOPIC-AI-MUSIC-COPYRIGHT
    sources:
      - SRC-UMG-V-SUNO-COMPLAINT
  - subject: CASE-UMG-V-SUNO
    predicate: related_to
    object: TOPIC-AI-COPYRIGHT
    sources:
      - SRC-UMG-V-SUNO-COMPLAINT
  - subject: CASE-UMG-V-SUNO
    predicate: related_to
    object: STAT-USC-107
    sources:
      - SRC-UMG-V-SUNO-ANSWER
last_verified: "2026-08-22"
filing_date: "2024-06-24"
decision_date: "2025-12-09"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/legal/CASE-UMG-V-SUNO.md`
- Source ID: `CASE-UMG-V-SUNO`
- [**Edit this page**](https://github.com/itsmeront/open-internet-reference/edit/main/knowledge/legal/CASE-UMG-V-SUNO.md) | [**Suggest a change**](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml&title=Edit+suggestion:+CASE-UMG-V-SUNO)

!!! info "📝 Page Status: Draft — sourced but not yet reviewed"

    - **Status**: `draft`
    - **Sources**: 4
    - **Relationships**: 5
    - **Research debt items**: 3

---

# UMG Recordings, Inc. v. Suno, Inc.

## Summary

UMG Recordings, Inc. v. Suno, Inc., No. 1:24-cv-11611 (D. Mass.), is the major-label copyright action against the generative music service Suno. Universal, Sony, and Warner affiliates alleged that Suno copied their sound recordings to train a commercial music generator. Suno answered that any copying is fair use. Warner-affiliated plaintiffs later stipulated to dismissal of their claims with prejudice. As of the sources reviewed here, UMG and Sony claims remain, and no court has issued a fair-use merits ruling.

## Verified Facts

- On June 24, 2024, UMG Recordings, Inc., Capitol Records, LLC, Sony Music Entertainment, and Warner-affiliated companies filed a copyright complaint against Suno, Inc. in the District of Massachusetts.[^1]
- The complaint alleges that building Suno required copying and ingesting “decades worth of the world’s most popular sound recordings” so the model could generate outputs that imitate human recordings, and that Suno did so without authorization.[^1]
- Plaintiffs assert two counts: direct infringement of post-1972 copyrighted sound recordings under 17 U.S.C. § 106, and direct infringement of pre-1972 recordings under the Music Modernization Act, 17 U.S.C. § 1401. They seek a willfulness declaration, an injunction, and statutory damages under § 504(c).[^1]
- Exhibit A to the complaint is described as an illustrative, non-exhaustive list of works; plaintiffs state they intend to amend later to add additional recordings.[^1]
- In its August 1, 2024 answer, Suno admits that constructing its model required showing the program “tens of millions of instances of different kinds of recordings” to derive statistical insights, and asserts that any copying of copyrightable expression is fair use in service of creating a new, non-infringing product.[^2]
- Suno also pleads copyright misuse and unclean hands, de minimis copying, innocent infringement, and other affirmative defenses.[^2]
- On December 9, 2025, Atlantic Recording Corporation, Atlantic Records Group LLC, Rhino Entertainment LLC, The All Blacks U.S.A., Inc., Warner Music International Services Limited, and Warner Records Inc. stipulated under Rule 41(a)(1)(A)(ii) that their claims against Suno are dismissed with prejudice, and that claims of all other plaintiffs are unaffected.[^3]


[^1]: [`SRC-UMG-V-SUNO-COMPLAINT`](../../../bibliography.md#SRC-UMG-V-SUNO-COMPLAINT) — Original complaint (June 24, 2024). Plaintiff allegations except as to filing date, parties, and claims pleaded.

[^2]: [`SRC-UMG-V-SUNO-ANSWER`](../../../bibliography.md#SRC-UMG-V-SUNO-ANSWER) — Suno answer (Aug. 1, 2024). Defendant admissions and defenses.

[^3]: [`SRC-UMG-V-SUNO-WARNER-DISMISSAL`](../../../bibliography.md#SRC-UMG-V-SUNO-WARNER-DISMISSAL) — Warner stipulation of dismissal (Dec. 9, 2025).

## Historical Context

The Suno and [Udio](CASE-UMG-V-UDIO.md) complaints were filed the same day and use parallel theories: unauthorized copying of master sound recordings to train a competing generative-music product.[^1] They sit beside publisher lyric suits such as [Concord v. Anthropic](CASE-CONCORD-V-ANTHROPIC.md) and the German first-instance lyric judgment in [GEMA v. OpenAI](CASE-GEMA-V-OPENAI.md). Unlike [Bartz v. Anthropic PBC](CASE-BARTZ-V-ANTHROPIC.md) and [Kadrey v. Meta Platforms, Inc.](CASE-KADREY-V-META.md), this docket had not reached a fair-use summary-judgment ruling in the sources reviewed here.

## Legal Analysis

Jurisdiction: District of Massachusetts. Authority level: complaint, answer, and a partial Rule 41 dismissal. No merits holding on [§ 107](STAT-USC-107.md) is recorded here.[^1][^2][^3]

The live dispute is whether ingesting copyrighted sound recordings to train a commercial music generator is fair use. Suno’s answer frames the copies as unseen intermediate analysis of genre and style, which copyright does not protect, and cites Google v. Oracle and Authors Guild v. Google.[^2] The labels plead the opposite: wholesale commercial copying whose outputs occupy the same market as the recordings copied.[^1] That is a fact-intensive § 107 question. This page does not treat prompt-engineered “soundalike” exhibits as proven copying.

The Warner stipulation ends those plaintiffs’ claims with prejudice. It does not disclose terms and does not resolve UMG or Sony claims.[^3]

## Relationships

- `CASE-UMG-V-SUNO` cites [`SRC-UMG-V-SUNO-COMPLAINT`](../../../bibliography.md#SRC-UMG-V-SUNO-COMPLAINT).
- `CASE-UMG-V-SUNO` related_to `CASE-UMG-V-UDIO`.
- `CASE-UMG-V-SUNO` related_to `TOPIC-AI-MUSIC-COPYRIGHT`.
- `CASE-UMG-V-SUNO` related_to `TOPIC-AI-COPYRIGHT`.
- `CASE-UMG-V-SUNO` related_to `STAT-USC-107`.

## Sources

1. [`SRC-UMG-V-SUNO-COMPLAINT`](../../../bibliography.md#SRC-UMG-V-SUNO-COMPLAINT): Original complaint (June 24, 2024).
2. [`SRC-UMG-V-SUNO-ANSWER`](../../../bibliography.md#SRC-UMG-V-SUNO-ANSWER): Suno answer (Aug. 1, 2024).
3. [`SRC-UMG-V-SUNO-WARNER-DISMISSAL`](../../../bibliography.md#SRC-UMG-V-SUNO-WARNER-DISMISSAL): Warner stipulation of dismissal (Dec. 9, 2025).
4. [`SRC-USC-17-107-LII`](../../../bibliography.md#SRC-USC-17-107-LII): 17 U.S.C. § 107.

## Research Debt

- Add any later amended complaint, DMCA § 1201 stream-ripping claim if leave to amend is granted, and the January 28, 2026 order entering the Warner stipulation.
- Add a fair-use or other merits order when one issues.
- Do not treat press reports of licensing-partnership terms as facts unless a party filing or official release states them.

## Document metadata

- Decision date: `2025-12-09`
- Filing date: `2024-06-24`
- Last verified: `2026-08-22`
