---
id: CASE-CONCORD-V-ANTHROPIC
title: Concord Music Group, Inc. v. Anthropic PBC
type: case
status: draft
summary: Pending Northern District of California publisher action alleging that Anthropic copied song lyrics to train Claude and that outputs reproduce those lyrics; the court denied Anthropic’s second motion to dismiss secondary-infringement and DMCA claims.
tags:
  - case
  - copyright
  - artificial-intelligence
  - digital-rights
sources:
  - SRC-CONCORD-V-ANTHROPIC-MTD-2025
  - SRC-CONCORD-V-ANTHROPIC-DOCKET
  - SRC-USC-17-107-LII
relationships:
  - subject: CASE-CONCORD-V-ANTHROPIC
    predicate: cites
    object: SRC-CONCORD-V-ANTHROPIC-MTD-2025
    sources:
      - SRC-CONCORD-V-ANTHROPIC-MTD-2025
  - subject: CASE-CONCORD-V-ANTHROPIC
    predicate: related_to
    object: TOPIC-AI-MUSIC-COPYRIGHT
    sources:
      - SRC-CONCORD-V-ANTHROPIC-MTD-2025
  - subject: CASE-CONCORD-V-ANTHROPIC
    predicate: related_to
    object: TOPIC-AI-COPYRIGHT
    sources:
      - SRC-CONCORD-V-ANTHROPIC-MTD-2025
  - subject: CASE-CONCORD-V-ANTHROPIC
    predicate: related_to
    object: CASE-GEMA-V-OPENAI
    sources:
      - SRC-CONCORD-V-ANTHROPIC-MTD-2025
last_verified: "2026-08-22"
decision_date: "2025-10-06"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/legal/CASE-CONCORD-V-ANTHROPIC.md`
- Source ID: `CASE-CONCORD-V-ANTHROPIC`
- [**Edit this page**](https://github.com/itsmeront/open-internet-reference/edit/main/knowledge/legal/CASE-CONCORD-V-ANTHROPIC.md) | [**Suggest a change**](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml&title=Edit+suggestion:+CASE-CONCORD-V-ANTHROPIC)

!!! info "📝 Page Status: Draft — sourced but not yet reviewed"

    - **Status**: `draft`
    - **Sources**: 3
    - **Relationships**: 4
    - **Research debt items**: 4

---

# Concord Music Group, Inc. v. Anthropic PBC

## Summary

Concord Music Group, Inc. v. Anthropic PBC, No. 24-cv-03811 (N.D. Cal.), is music-publisher litigation over song lyrics and Anthropic’s Claude models. After an initial dismissal of secondary-infringement and DMCA claims with leave to amend, Judge Eumi K. Lee on October 6, 2025 denied Anthropic’s motion to dismiss the first amended complaint. Direct infringement, contributory and vicarious infringement, and DMCA copyright-management-information claims therefore proceeded past that pleading stage. The case is about musical compositions (lyrics), not sound-recording masters.

## Verified Facts

- The action pending in the Northern District of California as No. 5:24-cv-03811 reflects a complaint originally filed October 18, 2023 in the Middle District of Tennessee and later transferred; the N.D. Cal. docket date is June 26, 2024.[^2]
- Plaintiffs are eight music publishing companies: Concord Music Group, Inc., Capitol CMG, Inc., Universal Music Corp., Songs of Universal, Inc., Universal Music - MGB NA LLC, Polygram Publishing, Inc., Universal Music - Z Tunes LLC, and ABKCO Music, Inc.[^1]
- The first amended complaint alleges that the publishers own or control exclusive rights in millions of musical compositions, including 500 works listed in Exhibit A, and that Anthropic used those lyrics to train Claude and that Claude outputs the lyrics to users.[^1]
- Publishers allege that Anthropic curated training data from third-party datasets including Common Crawl and The Pile, and that it used the Newspaper algorithm in a way that removed copyright management information more effectively than available alternatives.[^1]
- Claims in the FAC are (I) direct copyright infringement, (II) contributory infringement, (III) vicarious infringement, and (IV) removal or alteration of CMI under the DMCA.[^1]
- On March 26, 2025, the court granted Anthropic’s first motion to dismiss the secondary-infringement and CMI claims, with leave to amend. Publishers filed the FAC on April 25, 2025. Anthropic moved again on May 9, 2025.[^1]
- On October 6, 2025, the court denied the second motion to dismiss in full, holding that the FAC plausibly alleged contributory infringement, vicarious infringement, and DMCA § 1202(b)(1) and (b)(3) claims, and ordered Anthropic to answer within 14 days after a ruling on plaintiffs’ motion for leave to file a second amended complaint.[^1]


[^1]: [`SRC-CONCORD-V-ANTHROPIC-MTD-2025`](../../../bibliography.md#SRC-CONCORD-V-ANTHROPIC-MTD-2025) — Order denying MTD (Oct. 6, 2025). Primary for parties, claims, procedural history, alleged FAC facts, and holdings.

[^2]: [`SRC-CONCORD-V-ANTHROPIC-DOCKET`](../../../bibliography.md#SRC-CONCORD-V-ANTHROPIC-DOCKET) — CourtListener docket for No. 5:24-cv-03811. Primary for original Tennessee filing date and transfer caption.

## Historical Context

Concord is the leading U.S. publisher suit about lyrics in large language models, distinct from the label suits against [Suno](CASE-UMG-V-SUNO.md) and [Udio](CASE-UMG-V-UDIO.md) (sound recordings) and from [Bartz v. Anthropic PBC](CASE-BARTZ-V-ANTHROPIC.md) (books and a pirated-library settlement). The October 2025 order is a pleading decision, not a fair-use holding.

## Legal Analysis

Jurisdiction: Northern District of California. Authority level: Rule 12(b)(6) order. The court accepted FAC allegations as true for that motion and did not decide [§ 107](STAT-USC-107.md).[^1]

Two points matter for the rest of the AI-copyright map. First, the works are short, highly memorable lyrics. Publishers allege regurgitation from simple prompts, which is closer to the output-substitution theory in [Times v. OpenAI](CASE-NYT-V-OPENAI.md) than to Bartz’s purchased-book training holding.[^1] Second, the court allowed DMCA CMI claims to proceed on allegations that Anthropic chose a stripping algorithm and distributed lyrics without CMI while concealing its own infringement, distinguishing Tremblay’s third-party-user framing.[^1]

A related later action, Concord Music Group, Inc. v. Anthropic PBC, No. 5:26-cv-00880 (N.D. Cal.), appears on CourtListener as filed January 28, 2026. This page does not treat that docket’s allegations as found facts.

## Relationships

- `CASE-CONCORD-V-ANTHROPIC` cites [`SRC-CONCORD-V-ANTHROPIC-MTD-2025`](../../../bibliography.md#SRC-CONCORD-V-ANTHROPIC-MTD-2025).
- `CASE-CONCORD-V-ANTHROPIC` related_to `TOPIC-AI-MUSIC-COPYRIGHT`.
- `CASE-CONCORD-V-ANTHROPIC` related_to `TOPIC-AI-COPYRIGHT`.
- `CASE-CONCORD-V-ANTHROPIC` related_to `CASE-GEMA-V-OPENAI`.

## Sources

1. [`SRC-CONCORD-V-ANTHROPIC-MTD-2025`](../../../bibliography.md#SRC-CONCORD-V-ANTHROPIC-MTD-2025): Order denying motion to dismiss FAC (Oct. 6, 2025).
2. [`SRC-CONCORD-V-ANTHROPIC-DOCKET`](../../../bibliography.md#SRC-CONCORD-V-ANTHROPIC-DOCKET): CourtListener docket for No. 5:24-cv-03811.
3. [`SRC-USC-17-107-LII`](../../../bibliography.md#SRC-USC-17-107-LII): 17 U.S.C. § 107.

## Research Debt

- Add the original Tennessee complaint, the FAC, and any second amended complaint as operative-pleading sources.
- Add the March 26, 2025 dismissal order and any preliminary-injunction ruling from primary PDFs.
- Add No. 5:26-cv-00880 (and any BMG publisher action) from those complaints, not trackers.
- Add Anthropic’s answer and any later merits order.

## Document metadata

- Decision date: `2025-10-06`
- Last verified: `2026-08-22`
