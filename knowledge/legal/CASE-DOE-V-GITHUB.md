---
id: CASE-DOE-V-GITHUB
title: Doe 1 v. GitHub, Inc.
type: case
status: draft
monitor: true
summary: Open-source developers’ action alleging that GitHub Copilot training and outputs stripped copyright-management information and breached open-source licenses. The Ninth Circuit affirmed dismissal of the DMCA claims on September 16, 2026. Open-source-license contract claims were not part of that appeal.
tags:
  - case
  - copyright
  - artificial-intelligence
  - digital-rights
  - open-source-software
sources:
  - SRC-DOE-V-GITHUB-MTD-2024
  - SRC-DOE-V-GITHUB-9THCIR-DOCKET
  - SRC-DOE-V-GITHUB-9THCIR-OPINION
relationships:
  - subject: CASE-DOE-V-GITHUB
    predicate: cites
    object: SRC-DOE-V-GITHUB-MTD-2024
    sources:
      - SRC-DOE-V-GITHUB-MTD-2024
  - subject: CASE-DOE-V-GITHUB
    predicate: cites
    object: SRC-DOE-V-GITHUB-9THCIR-OPINION
    sources:
      - SRC-DOE-V-GITHUB-9THCIR-OPINION
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
last_verified: "2026-10-17"
decision_date: "2026-09-16"
---

# Doe 1 v. GitHub, Inc.

## Summary

Doe 1 v. GitHub, Inc., No. 4:22-cv-06823 (N.D. Cal.), is a class action by anonymous open-source developers against GitHub, Microsoft, and OpenAI entities over GitHub Copilot. On June 24, 2024, Judge Jon S. Tigar dismissed the developers’ DMCA § 1202(b) copyright-management-information claims with prejudice, declined to dismiss breach-of-open-source-license claims, and dismissed unjust-enrichment and punitive-damages requests. On September 16, 2026, the Ninth Circuit affirmed that dismissal in No. 24-7700. The appeal did not decide the contract claims.

## Verified Facts

- Defendants addressed in the June 24, 2024 order include GitHub, Inc., Microsoft, and OpenAI entities, including OpenAI Startup Fund I, L.P. and OpenAI Startup Fund Management, LLC.[^1]
- The court dismissed plaintiffs’ § 1202(b) claim with prejudice. It declined to dismiss the claim for breach of contract based on alleged open-source license violations against all defendants. It dismissed requests for monetary relief in the form of unjust enrichment and for punitive damages.[^1]
- Plaintiffs opened a Ninth Circuit appeal, No. 24-7700, from the Northern District of California case No. 4:22-cv-06823-JST. The appellate docket records case opening on December 23, 2024, and oral argument on February 11, 2026, in San Francisco.[^2]
- On September 16, 2026, the Ninth Circuit affirmed. The panel was Judges Sidney R. Thomas and Eric D. Miller and District Judge Stanley Blumenfeld, Jr., sitting by designation. Judge Miller wrote the opinion. The appeal was interlocutory under 28 U.S.C. § 1292(b). The court found Article III standing and held that plaintiffs do not state a § 1202(b)(1) claim on the output theory: Copilot and Codex create new works that never contained the plaintiffs’ copyright-management information, so the systems do not “remove or alter” that information from a copy of an existing work. The court treated the input theory as forfeited. The opinion ends “AFFIRMED.” It does not decide the open-source license contract claims that the district court left in the case.[^3]


[^1]: `SRC-DOE-V-GITHUB-MTD-2024` — Order (June 24, 2024). Primary for surviving and dismissed claims.

[^2]: `SRC-DOE-V-GITHUB-9THCIR-DOCKET` — Ninth Circuit docket No. 24-7700. Primary for appeal number, opening date, and argument date.

[^3]: `SRC-DOE-V-GITHUB-9THCIR-OPINION` — Doe v. GitHub, No. 24-7700 (9th Cir. Sept. 16, 2026). Primary opinion. The opinion cites 17 U.S.C. § 1202(b).

## Historical Context

Doe is the leading U.S. case about generative coding tools trained on public repositories. It is not a conventional training-is-fair-use book or news case. The live district-court theory after the Ninth Circuit’s affirmance is contract: whether Copilot’s use of licensed code breached the terms under which the code was published. The DMCA theory about stripped attribution and license headers is closed on the output theory the court decided, and it remains a CMI issue in image and lyric cases such as [Andersen](CASE-ANDERSEN-V-STABILITY.md) and [Concord](CASE-CONCORD-V-ANTHROPIC.md).[^1][^3]

## Legal Analysis

Jurisdiction: Northern District of California, with an interlocutory appeal decided by the Ninth Circuit. Authority level: published appellate opinion affirming dismissal of the DMCA claims, plus a district-court pleading order that left the contract claims in the case.[^1][^3]

On the record before the Ninth Circuit, Copilot and Codex outputs are new works that never contained the plaintiffs’ copyright-management information, so there was nothing on those copies for the systems to remove or alter.[^3] The surviving contract claim, if later tried, would test whether public open-source licenses can constrain model training and output independently of that DMCA theory. The § 1202(b) output claim is decided. The contract claim is open.

## Relationships

- `CASE-DOE-V-GITHUB` cites `SRC-DOE-V-GITHUB-MTD-2024`.
- `CASE-DOE-V-GITHUB` cites `SRC-DOE-V-GITHUB-9THCIR-OPINION`.
- `CASE-DOE-V-GITHUB` related_to `TOPIC-AI-COPYRIGHT`.
- `CASE-DOE-V-GITHUB` related_to `CASE-ANDERSEN-V-STABILITY`.
- `CASE-DOE-V-GITHUB` related_to `CASE-GOOGLE-V-ORACLE`.

## Sources

1. `SRC-DOE-V-GITHUB-MTD-2024`: Order on motions to dismiss (June 24, 2024).
2. `SRC-DOE-V-GITHUB-9THCIR-DOCKET`: Ninth Circuit docket No. 24-7700.
3. `SRC-DOE-V-GITHUB-9THCIR-OPINION`: Ninth Circuit opinion (Sept. 16, 2026).

## Research Debt

- Add the original and operative complaints and the January 3, 2024 MTD order as pleading sources.
- Add the September 27, 2024 order certifying interlocutory appeal and staying the district case from that PDF.
- Track the district-court contract claims that the September 16, 2026 opinion did not decide.
- Add Authors Alliance / Samuelson Clinic amicus briefs only if OIR needs the appellate-advocacy record.
