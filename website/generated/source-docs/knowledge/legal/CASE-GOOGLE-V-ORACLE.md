---
id: CASE-GOOGLE-V-ORACLE
title: Google LLC v. Oracle America, Inc.
type: case
status: draft
summary: Google LLC v. Oracle America, Inc., 593 U.S. ___ (2021), held in a 6-2 decision that Google's copying of approximately 11,500 lines of Java API declaring code for use in Android constituted fair use under copyright law.
tags:
  - copyright
  - speech-and-code
  - digital-rights
  - open-source-software
sources:
  - SRC-GOOGLE-ORACLE-JUSTIA
relationships:
  - subject: CASE-GOOGLE-V-ORACLE
    predicate: cites
    object: SRC-GOOGLE-ORACLE-JUSTIA
    sources:
      - SRC-GOOGLE-ORACLE-JUSTIA
  - subject: CASE-GOOGLE-V-ORACLE
    predicate: related_to
    object: TOPIC-CODE-AS-SPEECH
    sources:
      - SRC-GOOGLE-ORACLE-JUSTIA
last_verified: "2026-06-25"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/legal/CASE-GOOGLE-V-ORACLE.md`
- Source ID: `CASE-GOOGLE-V-ORACLE`
- [**Edit this page**](https://github.com/itsmeront/open-internet-reference/edit/main/knowledge/legal/CASE-GOOGLE-V-ORACLE.md) | [**Suggest a change**](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml&title=Edit+suggestion:+CASE-GOOGLE-V-ORACLE)

!!! info "📝 Page Status: Draft — sourced but not yet reviewed"

    - **Status**: `draft`
    - **Sources**: 1
    - **Relationships**: 2
    - **Research debt items**: 3
    - **Last verified**: 2026-06-25

---

# Google LLC v. Oracle America, Inc.

## Summary

Google LLC v. Oracle America, Inc., 593 U.S. ___ (2021), held in a 6-2 decision that Google's copying of approximately 11,500 lines of Java API declaring code for use in Android constituted fair use under copyright law.

## Verified Facts

- Case citation 593 U.S. ___ (2021), No. 18-956.[^1]
- Decided April 5, 2021.[^1]
- 6-2 decision authored by Justice Breyer.[^1]
- Google copied roughly 11,500 lines of Java SE API declaring code.[^1]
- Court held Google's use was fair use as a matter of law.[^1]
- Court found Google reimplemented a user interface taking only what was needed to allow programmers to use accrued talents in new transformative program.[^1]
- Decision bypassed the question of whether APIs are copyrightable.[^1]
- Reversed Federal Circuit's 2018 ruling.[^1]
- Oracle had sought damages upward of $10 billion.[^1]
- Decade-long litigation.[^1]

## Historical Context

The dispute began in 2010 when Oracle (which had acquired Sun Microsystems and the Java platform) sued Google for using Java API declarations in Android. The case went through multiple rounds of litigation, including two jury trials and two Federal Circuit appeals, before reaching the Supreme Court. The Federal Circuit had ruled that APIs are copyrightable and that Google's use was not fair use. The Supreme Court reversed on the fair use question without reaching the copyrightability issue.


[^1]: [`SRC-GOOGLE-ORACLE-JUSTIA`](../../../bibliography.md#SRC-GOOGLE-ORACLE-JUSTIA) — Google LLC v. Oracle America, Inc., 593 U.S. ___ (2021) (Justia). Primary authority.

## Legal Analysis

The Court applied the four statutory fair use factors (17 U.S.C. § 107) and found all four favored Google or were neutral:

1. **Purpose and character**: Google's use was transformative — it reimplemented the API in a new platform (smartphones) to allow programmers to apply their existing skills.
2. **Nature of the copyrighted work**: The declaring code was primarily functional, bound up with uncopyrightable ideas.
3. **Amount used**: Google took only what was needed (the declarations, not the implementing code) to enable programmer familiarity.
4. **Market effect**: Android did not serve as a market substitute for Java SE; the relevant market was smartphones, which Sun/Oracle had failed to enter successfully.

The Court explicitly declined to resolve whether API declarations are copyrightable, assuming for argument's sake that they are while finding fair use regardless.

## Dissenting Opinion

Justice Thomas, joined by Justice Alito, dissented. The dissent argued that the majority misapplied every factor of the fair use analysis. Key points from the dissent:

- The majority's approach effectively decides copyrightability (against Oracle) while nominally declining to address it.
- Google's use was commercial and not transformative — it copied the declaring code to achieve the same purpose (enabling programmers to use familiar interfaces).
- The amount copied (11,500 lines) was substantial and went beyond what was necessary.
- The market harm was real — Oracle lost the opportunity to license Java for mobile platforms.
- The dissent warned the decision could reduce incentives to create original APIs.

Justice Barrett took no part in the case.

## Practical Impact

The decision protects the common software development practice of reimplementing APIs for interoperability and platform portability. It provides legal cover for developers and companies that build compatible implementations of existing interfaces, which is foundational to open source projects that implement standard APIs (e.g., Wine, ReactOS, Mono, OpenJDK).

## Significance for Software Companies

Protects software interoperability. Establishes that reimplementing an API for a transformative purpose can be fair use. Critical for open source projects that implement standard APIs. The ruling provides significant comfort for companies building compatible software that uses the same programming interfaces as existing platforms.

## Relationships

- `CASE-GOOGLE-V-ORACLE` cites [`SRC-GOOGLE-ORACLE-JUSTIA`](../../../bibliography.md#SRC-GOOGLE-ORACLE-JUSTIA).
- `CASE-GOOGLE-V-ORACLE` related_to `TOPIC-CODE-AS-SPEECH`.

## Sources

1. [`SRC-GOOGLE-ORACLE-JUSTIA`](../../../bibliography.md#SRC-GOOGLE-ORACLE-JUSTIA): Google LLC v. Oracle America, Inc., 593 U.S. ___ (2021) (Justia).

## Research Debt

- Document the lower court procedural history in detail.
- Add additional source records for amicus briefs from open source organizations.
- Document the impact on subsequent API reimplementation cases.
