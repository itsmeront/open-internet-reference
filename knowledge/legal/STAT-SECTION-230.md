---
id: STAT-SECTION-230
title: Section 230 (47 U.S.C. § 230)
type: statute
status: draft
summary: Section 230 of the Communications Decency Act (47 U.S.C. § 230), enacted in 1996, provides that internet platforms shall not be treated as publishers of user-generated content and protects good-faith content moderation, forming the legal foundation for the modern internet.
tags:
  - internet-governance
  - intermediary-liability
  - digital-rights
  - first-amendment
sources:
  - SRC-SECTION-230-LII
  - SRC-SECTION-230-EFF
relationships:
  - subject: STAT-SECTION-230
    predicate: cites
    object: SRC-SECTION-230-LII
    sources:
      - SRC-SECTION-230-LII
  - subject: STAT-SECTION-230
    predicate: cites
    object: SRC-SECTION-230-EFF
    sources:
      - SRC-SECTION-230-EFF
  - subject: STAT-SECTION-230
    predicate: related_to
    object: CASE-RENO-V-ACLU
    sources:
      - SRC-SECTION-230-EFF
last_verified: "2026-06-25"
---

# Section 230 (47 U.S.C. § 230)

## Summary

Section 230 of the Communications Decency Act (47 U.S.C. § 230), enacted in 1996, provides that internet platforms shall not be treated as publishers of user-generated content and protects good-faith content moderation, forming the legal foundation for the modern internet.

## Official Sources

- **Current text (Cornell LII)**: https://www.law.cornell.edu/uscode/text/47/230
- **EFF Section 230 page**: https://www.eff.org/issues/cda230
- **EFF Legislative History**: https://www.eff.org/issues/cda230/legislative-history

## Key Provisions

### § 230(c)(1) — Publisher Immunity

"No provider or user of an interactive computer service shall be treated as the publisher or speaker of any information provided by another information content provider."

This means platforms cannot be sued for content their users post.

### § 230(c)(2) — Good Samaritan Protection

Protects platforms that voluntarily restrict access to material they consider objectionable, even if constitutionally protected. This enables content moderation without creating publisher liability.

## Legislative History

| Year | Action | Significance |
|---|---|---|
| 1996 | Enacted as part of Communications Decency Act (Title V of Telecommunications Act) | Response to conflicting court rulings on platform liability (Cubby v. CompuServe, Stratton Oakmont v. Prodigy) |
| 1996 | CDA content restrictions struck down (Reno v. ACLU) | Section 230 survived as the one standing provision of the CDA |
| 2018 | FOSTA-SESTA amendment | Created exception for sex trafficking content (narrowing 230 immunity) |

## Co-Authors

- **Sen. Ron Wyden** (D-OR) — original co-author, continues to defend against weakening
- **Rep. Chris Cox** (R-CA) — original co-author

As Wyden stated: Section 230 "ensures the person who creates content is the one legally responsible for it."

## Threats and Proposed Changes

The statute faces ongoing pressure from multiple directions:
- **EARN IT Act** (opposed by Wyden, EFF): would condition 230 immunity on compliance with government standards, potentially undermining encryption
- **Conservative proposals**: would restrict platforms' ability to moderate content
- **Progressive proposals**: would impose liability for algorithmic amplification

## Interpreting Cases

- **Reno v. ACLU** (1997): Supreme Court struck down CDA content restrictions; Section 230 survived as remaining provision.
- **Gonzalez v. Google** (2023): Supreme Court narrowly avoided ruling on Section 230's scope regarding algorithmic recommendations.

## Relevance to Open Source and Software Companies

Section 230 is foundational for:
- Any platform hosting user-generated content
- Open source projects with community forums, issue trackers, or package repositories
- Companies providing cloud hosting, social features, or communication tools
- The ability to moderate harmful content without taking on publisher liability for all content

Without Section 230, most interactive internet services could not exist in their current form.

## Relationships

- `STAT-SECTION-230` cites `SRC-SECTION-230-LII`.
- `STAT-SECTION-230` cites `SRC-SECTION-230-EFF`.
- `STAT-SECTION-230` related_to `CASE-RENO-V-ACLU`.

## Sources

- `SRC-SECTION-230-LII`: 47 U.S.C. § 230 (Cornell LII).
- `SRC-SECTION-230-EFF`: EFF Section 230 Page.

## Research Debt

- Add Gonzalez v. Google case page.
- Document FOSTA-SESTA amendment and its impact.
- Add Stratton Oakmont v. Prodigy and Cubby v. CompuServe background.
- Document current legislative threats in detail.
- Review per-fact footnote-to-source mapping; multiple sources are cited on this page.
