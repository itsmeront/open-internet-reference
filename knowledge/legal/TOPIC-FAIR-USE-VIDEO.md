---
id: TOPIC-FAIR-USE-VIDEO
title: Fair Use and Video
type: topic
status: draft
summary: U.S. fair use law as it applies to video that incorporates copyrighted music, footage, clips, or other third-party material, documented from statute and cited sources.
tags:
  - copyright
  - digital-rights
sources:
  - SRC-USC-17-107-LII
  - SRC-USC-17-107-GOVINFO
  - SRC-EFF-BLOGGERS-IP
  - SRC-LENZ-V-UNIVERSAL-CA9
relationships:
  - subject: TOPIC-FAIR-USE-VIDEO
    predicate: cites
    object: SRC-USC-17-107-LII
    sources:
      - SRC-USC-17-107-LII
  - subject: TOPIC-FAIR-USE-VIDEO
    predicate: cites
    object: SRC-EFF-BLOGGERS-IP
    sources:
      - SRC-EFF-BLOGGERS-IP
  - subject: TOPIC-FAIR-USE-VIDEO
    predicate: related_to
    object: STAT-USC-107
    sources:
      - SRC-USC-17-107-LII
  - subject: TOPIC-FAIR-USE-VIDEO
    predicate: related_to
    object: CASE-LENZ-V-UNIVERSAL
    sources:
      - SRC-LENZ-V-UNIVERSAL-CA9
  - subject: TOPIC-FAIR-USE-VIDEO
    predicate: related_to
    object: TOPIC-DMCA-TAKEDOWN-RESPONSE
    sources:
      - SRC-EFF-BLOGGERS-IP
  - subject: TOPIC-FAIR-USE-VIDEO
    predicate: related_to
    object: ORG-EFF
    sources:
      - SRC-EFF-BLOGGERS-IP
last_verified: "2026-07-19"
---

# Fair Use and Video

## Summary

This page documents U.S. fair use law as it applies to video that incorporates copyrighted music, footage, clips, or other third-party material. Fair use is determined case by case under 17 U.S.C. § 107.

## Verified Facts

- Fair use of a copyrighted work for purposes such as criticism, comment, news reporting, teaching, scholarship, or research is not an infringement of copyright under 17 U.S.C. § 107.[^1]
- Section 107 directs courts to consider four factors: (1) purpose and character of the use, including commercial vs. nonprofit educational character; (2) nature of the copyrighted work; (3) amount and substantiality of the portion used in relation to the work as a whole; and (4) effect on the potential market for or value of the copyrighted work.[^1]
- The EFF legal guide states that there are no hard-and-fast rules for fair use and that guidelines about word counts or percentages are not the law.[^2]
- The EFF legal guide states that transformative uses are favored over mere copying, that non-commercial uses are more likely to be fair use, and that commercial use does not by itself preclude fair use.[^2]
- The EFF legal guide states that using factual or published material is more likely to be fair use than using highly creative or unpublished works.[^2]
- The EFF legal guide states that copying nearly all of a work, or copying its "heart," is less likely to be fair use.[^2]
- The EFF legal guide states that uses substituting for the original in the market weigh against fair use, and that criticism or parody reducing market demand may still be fair use when transformative.[^2]
- The EFF legal guide states that copyright protects expression rather than bare facts or ideas, and that reporters may state facts and ideas from another work without copying its expression.[^2]
- The EFF legal guide states that parody copies from the work it mocks, while satire uses recognizable elements from an original work to comment on something else, and that courts have given parody broader fair use leeway than satire.[^2]
- In [Lenz v. Universal Music Corp.](CASE-LENZ-V-UNIVERSAL.md), the Ninth Circuit held that copyright holders must consider fair use in good faith before sending a DMCA takedown notification.[^3]
- The Lenz case involved a 29-second home video in which Prince's "Let's Go Crazy" played in the background.[^3]


[^1]: `SRC-USC-17-107-LII` — 17 U.S.C. § 107. Primary authority.

[^2]: `SRC-EFF-BLOGGERS-IP` — EFF Legal Guide for Bloggers — Intellectual Property. Official educational guide; secondary source.

[^3]: `SRC-LENZ-V-UNIVERSAL-CA9` — Lenz v. Universal Music Corp., 801 F.3d 1126 (9th Cir. 2015). Primary authority.

## Historical Context

Lenz v. Universal arose after Universal Music sent a DMCA takedown notification to YouTube over a home video containing a Prince song; Lenz sent a counter-notification and later sued under 17 U.S.C. § 512(f).[^3] The case is commonly referred to as the "dancing baby" case in secondary reporting.

## Legal Analysis

Fair use under § 107 is an equitable, case-by-case doctrine without fixed quantitative thresholds.[^1][^2] For DMCA notice purposes, the Ninth Circuit treated fair use as a use "authorized by the law" under § 107, meaning a copyright holder's § 512(c)(3)(A)(v) good-faith statement requires consideration of whether the targeted use is fair use.[^3] The Lenz court did not require copyright holders to reach the correct fair use conclusion, but held that failure to consider fair use raises a triable issue about subjective good faith belief.[^3]

Analysis of platform copyright enforcement systems (for example automated matching on video hosts) is not yet documented here with primary sources. See [DMCA Takedown and Counter-Notification](TOPIC-DMCA-TAKEDOWN-RESPONSE.md) for statutory notice-and-takedown procedure.

## Relationships

- `TOPIC-FAIR-USE-VIDEO` cites `SRC-USC-17-107-LII`.
- `TOPIC-FAIR-USE-VIDEO` cites `SRC-EFF-BLOGGERS-IP`.
- `TOPIC-FAIR-USE-VIDEO` related_to `STAT-USC-107`.
- `TOPIC-FAIR-USE-VIDEO` related_to `CASE-LENZ-V-UNIVERSAL`.
- `TOPIC-FAIR-USE-VIDEO` related_to `TOPIC-DMCA-TAKEDOWN-RESPONSE`.
- `TOPIC-FAIR-USE-VIDEO` related_to `ORG-EFF`.

## Sources

1. `SRC-USC-17-107-LII`: 17 U.S.C. § 107.
2. `SRC-EFF-BLOGGERS-IP`: EFF Legal Guide for Bloggers — Intellectual Property.
3. `SRC-LENZ-V-UNIVERSAL-CA9`: Lenz v. Universal Music Corp., 801 F.3d 1126 (9th Cir. 2015).

Additional sources (not yet cited in footnotes):

- `SRC-USC-17-107-GOVINFO`: 17 U.S.C. § 107 (GovInfo).

## Research Debt

- Add primary sources for leading music and film fair use cases cited in the EFF guide (Campbell v. Acuff-Rose, Dr. Seuss Enterprises v. Penguin Books).
- Document video-platform copyright enforcement with official platform policy sources.
- Corroborate EFF fair use factor summaries with primary case law beyond the guide.
- Add jurisdiction notes for non-U.S. creators uploading to U.S.-based platforms.
