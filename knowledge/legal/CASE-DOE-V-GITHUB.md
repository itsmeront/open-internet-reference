---
id: CASE-DOE-V-GITHUB
title: Doe 1 v. GitHub, Inc.
type: case
status: draft
summary: Open-source developers’ action alleging that GitHub Copilot training and outputs stripped copyright-management information and breached open-source licenses; the district court dismissed DMCA claims with prejudice, allowed contract claims, and a Ninth Circuit interlocutory appeal was argued in February 2026.
tags:
  - case
  - copyright
  - artificial-intelligence
  - digital-rights
  - open-source-software
sources:
  - SRC-DOE-V-GITHUB-MTD-2024
  - SRC-DOE-V-GITHUB-9THCIR-DOCKET
relationships:
  - subject: CASE-DOE-V-GITHUB
    predicate: cites
    object: SRC-DOE-V-GITHUB-MTD-2024
    sources:
      - SRC-DOE-V-GITHUB-MTD-2024
  - subject: CASE-DOE-V-GITHUB
    predicate: related_to
    object: TOPIC-AI-COPYRIGHT
    sources:
      - SRC-DOE-V-GITHUB-MTD-2024
  - subject: CASE-DOE-V-GITHUB
    predicate: related_to
    object: CASE-ANDERSEN-V-STABILITY
    sources:
      - SRC-DOE-V-GITHUB-MTD-2024
  - subject: CASE-DOE-V-GITHUB
    predicate: related_to
    object: CASE-GOOGLE-V-ORACLE
    sources:
      - SRC-DOE-V-GITHUB-MTD-2024
last_verified: "2026-09-02"
decision_date: "2024-06-24"
---

# Doe 1 v. GitHub, Inc.

## Summary

Doe 1 v. GitHub, Inc., No. 4:22-cv-06823 (N.D. Cal.), is a class action by anonymous open-source developers against GitHub, Microsoft, and OpenAI entities over GitHub Copilot. On June 24, 2024, Judge Jon S. Tigar dismissed the developers’ DMCA § 1202(b) copyright-management-information claims with prejudice, declined to dismiss breach-of-open-source-license claims, and dismissed unjust-enrichment and punitive-damages requests. Plaintiffs took an interlocutory appeal, Ninth Circuit No. 24-7700, which was argued February 11, 2026. No appellate opinion is recorded in the sources reviewed here.

## Verified Facts

- Defendants addressed in the June 24, 2024 order include GitHub, Inc., Microsoft, and OpenAI entities, including OpenAI Startup Fund I, L.P. and OpenAI Startup Fund Management, LLC.[^1]
- The court dismissed plaintiffs’ § 1202(b) claim with prejudice. It declined to dismiss the claim for breach of contract based on alleged open-source license violations against all defendants. It dismissed requests for monetary relief in the form of unjust enrichment and for punitive damages.[^1]
- Plaintiffs opened a Ninth Circuit appeal, No. 24-7700, from the Northern District of California case No. 4:22-cv-06823-JST. The appellate docket records case opening on December 23, 2024, and oral argument on February 11, 2026, in San Francisco.[^2]


[^1]: `SRC-DOE-V-GITHUB-MTD-2024` — Order (June 24, 2024). Primary for surviving and dismissed claims.

[^2]: `SRC-DOE-V-GITHUB-9THCIR-DOCKET` — Ninth Circuit docket No. 24-7700. Primary for appeal number, opening date, and argument date.

## Historical Context

Doe is the leading U.S. case about generative coding tools trained on public repositories. It is not a conventional training-is-fair-use book or news case. The live district-court theory after the 2024 order is contract: whether Copilot’s use of licensed code breached the terms under which the code was published. The dismissed DMCA theory is about stripped attribution and license headers, a CMI issue that also appears in image and lyric cases such as [Andersen](CASE-ANDERSEN-V-STABILITY.md) and [Concord](CASE-CONCORD-V-ANTHROPIC.md).[^1]

## Legal Analysis

Jurisdiction: Northern District of California, with an interlocutory appeal in the Ninth Circuit. Authority level: district-court pleading order plus an appellate docket showing argument but not a decision.[^1][^2]

The software-freedom stakes are the license-compliance claim and the CMI identicality question on appeal. A ruling that § 1202(b) requires an identical copy would limit DMCA metadata claims against generative outputs that are similar rather than verbatim. The surviving contract claim, if later tried, would test whether public open-source licenses can constrain model training and output independently of copyright fair use. This page does not treat either theory as resolved.

## Relationships

- `CASE-DOE-V-GITHUB` cites `SRC-DOE-V-GITHUB-MTD-2024`.
- `CASE-DOE-V-GITHUB` related_to `TOPIC-AI-COPYRIGHT`.
- `CASE-DOE-V-GITHUB` related_to `CASE-ANDERSEN-V-STABILITY`.
- `CASE-DOE-V-GITHUB` related_to `CASE-GOOGLE-V-ORACLE`.

## Sources

1. `SRC-DOE-V-GITHUB-MTD-2024`: Order on motions to dismiss (June 24, 2024).
2. `SRC-DOE-V-GITHUB-9THCIR-DOCKET`: Ninth Circuit docket No. 24-7700.

## Research Debt

- Add the original and operative complaints and the January 3, 2024 MTD order as pleading sources.
- Add the September 27, 2024 order certifying interlocutory appeal and staying the district case from that PDF.
- Add any Ninth Circuit opinion in No. 24-7700 when it issues.
- Add Authors Alliance / Samuelson Clinic amicus briefs only if OIR needs the appellate-advocacy record.
