---
id: TOPIC-CODE-AS-SPEECH
title: Code as Speech
type: topic
status: draft
summary: The code-as-speech doctrine concerns whether software source code receives First Amendment protection, tracing Bernstein, Junger, and Corley, and examining whether that protection could extend to open-source development practices.
tags:
  - first-amendment
  - speech-and-code
  - digital-rights
  - constitutional-law
  - open-source-software
  - cryptography
  - copyright
sources:
  - SRC-US-CONST-AMEND-I-LII
  - SRC-RENO-V-ACLU-GOVINFO
  - SRC-RENO-V-ACLU-LOC
  - SRC-BERNSTEIN-JUSTIA
  - SRC-JUNGER-CMU
  - SRC-CORLEY-LII
relationships:
  - subject: TOPIC-CODE-AS-SPEECH
    predicate: cites
    object: SRC-US-CONST-AMEND-I-LII
    sources:
      - SRC-US-CONST-AMEND-I-LII
  - subject: TOPIC-CODE-AS-SPEECH
    predicate: cites
    object: SRC-RENO-V-ACLU-LOC
    sources:
      - SRC-RENO-V-ACLU-LOC
  - subject: TOPIC-CODE-AS-SPEECH
    predicate: cites
    object: SRC-BERNSTEIN-JUSTIA
    sources:
      - SRC-BERNSTEIN-JUSTIA
  - subject: TOPIC-CODE-AS-SPEECH
    predicate: cites
    object: SRC-JUNGER-CMU
    sources:
      - SRC-JUNGER-CMU
  - subject: TOPIC-CODE-AS-SPEECH
    predicate: cites
    object: SRC-CORLEY-LII
    sources:
      - SRC-CORLEY-LII
  - subject: TOPIC-CODE-AS-SPEECH
    predicate: related_to
    object: TOPIC-FIRST-AMENDMENT
    sources:
      - SRC-US-CONST-AMEND-I-LII
  - subject: TOPIC-CODE-AS-SPEECH
    predicate: related_to
    object: CASE-RENO-V-ACLU
    sources:
      - SRC-RENO-V-ACLU-LOC
  - subject: TOPIC-CODE-AS-SPEECH
    predicate: related_to
    object: CASE-BERNSTEIN-V-DOJ
    sources:
      - SRC-BERNSTEIN-JUSTIA
  - subject: TOPIC-CODE-AS-SPEECH
    predicate: related_to
    object: CASE-JUNGER-V-DALEY
    sources:
      - SRC-JUNGER-CMU
  - subject: TOPIC-CODE-AS-SPEECH
    predicate: related_to
    object: CASE-UNIVERSAL-V-CORLEY
    sources:
      - SRC-CORLEY-LII
  - subject: TOPIC-CODE-AS-SPEECH
    predicate: related_to
    object: TOPIC-DEVELOPER-SOFTWARE-LIABILITY
    sources:
      - SRC-BERNSTEIN-JUSTIA
last_verified: "2026-07-25"
---

# Code as Speech

## Summary

The code-as-speech doctrine concerns whether software, encryption, or other expressive code receives First Amendment protection. OIR traces the core U.S. appellate arc from [Bernstein v. DOJ](CASE-BERNSTEIN-V-DOJ.md) through [Junger v. Daley](CASE-JUNGER-V-DALEY.md) and [Universal City Studios v. Corley](CASE-UNIVERSAL-V-CORLEY.md), then separates what those holdings establish from the open research question of whether First Amendment protection of code can support an “open software is free expression” argument covering open-source development practices such as forking, modifying, publishing, reverse engineering, and sharing code.

## Verified Facts

- `TOPIC-FIRST-AMENDMENT` is the OIR seed topic record for First Amendment rights.[^1]
- [Reno v. ACLU](CASE-RENO-V-ACLU.md) addresses First Amendment limits on Internet content regulation rather than software publication directly.[^2]
- In [Bernstein v. United States Department of Justice](CASE-BERNSTEIN-V-DOJ.md), 176 F.3d 1132 (9th Cir. 1999), the Ninth Circuit held that software source code is protected speech under the First Amendment and that challenged encryption export regulations constituted an unconstitutional prior restraint.[^3]
- Bernstein rejected the argument that source code’s functional application removes it from First Amendment protection.[^3]
- In [Junger v. Daley](CASE-JUNGER-V-DALEY.md), 209 F.3d 481 (6th Cir. 2000), the Sixth Circuit held that computer source code is protected by the First Amendment because of its expressiveness in conveying ideas, reversing a district-court finding that encryption source code was not sufficiently expressive.[^4]
- In [Universal City Studios v. Corley](CASE-UNIVERSAL-V-CORLEY.md), 273 F.3d 429 (2d Cir. 2001), the Second Circuit acknowledged that computer code conveys information and is therefore speech entitled to First Amendment scrutiny, while upholding a DMCA anti-circumvention injunction against distribution of DeCSS.[^5]
- Corley applied intermediate scrutiny rather than strict scrutiny, treating the DMCA anti-circumvention provision as a content-neutral regulation targeting the functional aspects of code.[^5]

## Historical Context

Late-1990s encryption export controls produced the first major appellate tests of whether publishing source code is constitutionally protected expression. [Bernstein](CASE-BERNSTEIN-V-DOJ.md) framed encryption source-code licensing under the Export Administration Regulations as a prior restraint and treated source code as expressive speech.[^3] [Junger](CASE-JUNGER-V-DALEY.md), decided the following year in a different circuit, likewise held that source code is protected because it conveys programming ideas, reinforcing multi-circuit recognition that code can be speech even where regulations were later amended on remand.[^4]

[Corley](CASE-UNIVERSAL-V-CORLEY.md) shifted the factual setting from export licensing of encryption teaching materials to civil DMCA enforcement against distribution of circumvention code (DeCSS). The Second Circuit accepted that code is speech, but upheld an injunction by treating regulation of code’s functional capacity to circumvent access controls as content-neutral and subject to intermediate scrutiny.[^5] Together, the three decisions establish both coverage (code can be speech) and limits (speech coverage does not automatically invalidate every restriction on distribution of functional code).

OIR also treats [Reno v. ACLU](CASE-RENO-V-ACLU.md) as related Internet-speech precedent: it constrains content-based regulation of online expression, but it is not itself a holding that software source code is protected speech.[^2]


[^1]: `SRC-US-CONST-AMEND-I-LII` — U.S. Constitution First Amendment (Cornell LII). Primary authority.
[^2]: `SRC-RENO-V-ACLU-GOVINFO` — Reno v. American Civil Liberties Union, 521 U.S. 844 (1997) (GovInfo). Primary authority.
[^3]: `SRC-BERNSTEIN-JUSTIA` — Bernstein v. United States Department of Justice, 176 F.3d 1132 (9th Cir. 1999) (Justia). Primary authority.
[^4]: `SRC-JUNGER-CMU` — Junger v. Daley Opinion Text (CMU). Primary authority.
[^5]: `SRC-CORLEY-LII` — Universal City Studios v. Corley Opinion Text (Open Casebook). Primary authority.

## Legal Analysis

Jurisdiction for the core trilogy is U.S. federal appellate (Ninth, Sixth, and Second Circuits). Authority level is circuit precedent within each circuit; none of these three decisions is a Supreme Court holding that source code is categorically protected speech in all regulatory contexts.

**What the trilogy supports (sourced holdings).** Bernstein and Junger support the proposition that publishing and teaching encryption source code can be expressive activity protected by the First Amendment, and that prior-licensing regimes for such publication face serious constitutional scrutiny.[^3][^4] Corley supports the narrower but important proposition that computer code is speech for First Amendment purposes even when a court upholds a distribution injunction under intermediate scrutiny aimed at functional effects.[^5]

**What the trilogy does not decide.** None of Bernstein, Junger, or Corley holds that “open source development” as a practice — forking, collaborative modification, continuous republication, reverse engineering, or peer sharing of code — is itself a categorically protected form of First Amendment expression. Those cases address particular government restraints on publication or distribution of specific code (export licensing; DMCA anti-circumvention trafficking). Extending coverage from *code as expressive medium* to *open development as expressive practice* is an analytical step beyond the cited holdings and must be labeled as such.

**Open research question: open software as free expression.** A coherent research program for OIR is to ask whether First Amendment doctrine that already treats source code as speech can extend, in principle, to the communicative practices that define open-source software:

| Practice | How it relates to the trilogy | Open question (not a holding) |
| --- | --- | --- |
| Publishing / sharing source | Closest to Bernstein/Junger publication claims | When does regulation of distribution become a prior restraint vs. an intermediate-scrutiny functional limit (Corley)? |
| Forking / modifying | Builds on expressive authorship of derivative source | Does collaborative authorship and republication of modified trees receive the same coverage as an original author’s publication? |
| Reverse engineering | Factually adjacent to DeCSS/Corley reverse-engineering origins | First Amendment coverage of RE code may still lose under intermediate scrutiny or collide with copyright/DMCA doctrines distinct from speech coverage |
| Open collaboration / continuous sharing | Not litigated as such in the trilogy | Would courts treat community development workflows as protected expressive association/publication, or as regulable functional conduct? |

**Analytical limits (commentary, not verified doctrine).** Corley’s expressive/functional split is the main doctrinal obstacle to a simple “open software is free expression” slogan: once a court characterizes a restriction as targeting functional effects rather than communicative content, intermediate scrutiny may sustain the restriction even while conceding that code is speech.[^5] Separate bodies of law — copyright fair use, DMCA § 1201, CFAA “authorization,” export controls, and sanctions — can constrain open-source activity without ever denying that code can be speech. Related OIR inventory of enforcement against software authors and operators appears in [TOPIC-DEVELOPER-SOFTWARE-LIABILITY](TOPIC-DEVELOPER-SOFTWARE-LIABILITY.md).

This page does not state whether any particular open-source project, fork, reverse-engineering effort, or publication is lawful or constitutionally protected.

## Relationships

- `TOPIC-CODE-AS-SPEECH` cites `SRC-US-CONST-AMEND-I-LII`.
- `TOPIC-CODE-AS-SPEECH` cites `SRC-RENO-V-ACLU-LOC`.
- `TOPIC-CODE-AS-SPEECH` cites `SRC-BERNSTEIN-JUSTIA`.
- `TOPIC-CODE-AS-SPEECH` cites `SRC-JUNGER-CMU`.
- `TOPIC-CODE-AS-SPEECH` cites `SRC-CORLEY-LII`.
- `TOPIC-CODE-AS-SPEECH` related_to `TOPIC-FIRST-AMENDMENT`.
- `TOPIC-CODE-AS-SPEECH` related_to `CASE-RENO-V-ACLU`.
- `TOPIC-CODE-AS-SPEECH` related_to `CASE-BERNSTEIN-V-DOJ`.
- `TOPIC-CODE-AS-SPEECH` related_to `CASE-JUNGER-V-DALEY`.
- `TOPIC-CODE-AS-SPEECH` related_to `CASE-UNIVERSAL-V-CORLEY`.
- `TOPIC-CODE-AS-SPEECH` related_to `TOPIC-DEVELOPER-SOFTWARE-LIABILITY`.

## Sources

1. `SRC-US-CONST-AMEND-I-LII`: U.S. Constitution First Amendment (Cornell LII).
2. `SRC-RENO-V-ACLU-GOVINFO`: Reno v. American Civil Liberties Union, 521 U.S. 844 (1997) (GovInfo).
3. `SRC-BERNSTEIN-JUSTIA`: Bernstein v. United States Department of Justice, 176 F.3d 1132 (9th Cir. 1999) (Justia).
4. `SRC-JUNGER-CMU`: Junger v. Daley Opinion Text (CMU).
5. `SRC-CORLEY-LII`: Universal City Studios v. Corley Opinion Text (Open Casebook).

Additional sources (not yet cited in footnotes):

- `SRC-RENO-V-ACLU-LOC`: Reno v. American Civil Liberties Union, 521 U.S. 844 (1997) (U.S. Reports PDF).

## Research Debt

- Review per-fact footnote-to-source mapping against the Bernstein, Junger, and Corley opinions (quote-level corroboration of each Verified Facts bullet).
- Add scholarly and advocacy secondary sources that explicitly argue from Bernstein/Junger/Corley to open-source development as expression; do not treat that extension as verified doctrine until sourced.
- Distinguish expressive-code claims from commercial-speech doctrine and from copyright fair-use reverse-engineering precedents (e.g., Google v. Oracle and earlier interoperability cases) with dedicated source records and CASE links where missing.
- Document DMCA § 1201 exemption rulemakings and security-research exceptions as related but non-constitutional constraints on reverse engineering and tool publication.
- Evaluate whether `TOPIC-TORNADO-CASH` / `CASE-VAN-LOON-V-TREASURY` should be linked after First Amendment claims in the Tornado Cash civil record are sourced; Van Loon’s published holding is an IEEPA “property” ruling, not a code-as-speech holding.
- Consider a focused follow-on draft page (or section expansion) titled around “open software as free expression” only after secondary literature and case citations for forking/modification/association claims are intake-reviewed.
- Domain expert (constitutional / copyright) review before any status change above `draft`.
