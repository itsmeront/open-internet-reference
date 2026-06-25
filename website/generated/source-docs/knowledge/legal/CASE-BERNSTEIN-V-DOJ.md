---
id: CASE-BERNSTEIN-V-DOJ
title: Bernstein v. United States Department of Justice
type: case
status: draft
summary: Bernstein v. United States Department of Justice, 176 F.3d 1132 (9th Cir. 1999), held that software source code is protected speech under the First Amendment and that government regulations preventing its publication constituted an unconstitutional prior restraint.
tags:
  - first-amendment
  - cryptography
  - speech-and-code
  - export-control
  - digital-rights
sources:
  - SRC-BERNSTEIN-JUSTIA
  - SRC-BERNSTEIN-EFF
relationships:
  - subject: CASE-BERNSTEIN-V-DOJ
    predicate: cites
    object: SRC-BERNSTEIN-JUSTIA
    sources:
      - SRC-BERNSTEIN-JUSTIA
  - subject: CASE-BERNSTEIN-V-DOJ
    predicate: cites
    object: SRC-BERNSTEIN-EFF
    sources:
      - SRC-BERNSTEIN-EFF
  - subject: CASE-BERNSTEIN-V-DOJ
    predicate: related_to
    object: TOPIC-FIRST-AMENDMENT
    sources:
      - SRC-BERNSTEIN-JUSTIA
  - subject: CASE-BERNSTEIN-V-DOJ
    predicate: related_to
    object: TOPIC-CODE-AS-SPEECH
    sources:
      - SRC-BERNSTEIN-JUSTIA
last_verified: "2026-06-25"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/legal/CASE-BERNSTEIN-V-DOJ.md`
- Source ID: `CASE-BERNSTEIN-V-DOJ`

!!! info "📝 Page Status: Draft — sourced but not yet reviewed"

    - **Status**: `draft`
    - **Sources**: 2
    - **Relationships**: 4
    - **Research debt items**: 4
    - **Last verified**: 2026-06-25

---

# Bernstein v. United States Department of Justice

## Summary

Bernstein v. United States Department of Justice, 176 F.3d 1132 (9th Cir. 1999), held that software source code is protected speech under the First Amendment and that government regulations preventing its publication constituted an unconstitutional prior restraint.

## Verified Facts

- The case citation is 176 F.3d 1132 (9th Cir. 1999).
- Daniel J. Bernstein, a mathematician and cryptographer, developed an encryption algorithm called "Snuffle" and wanted to publish the source code and an explanatory academic paper.
- The Export Administration Regulations (EAR) prevented Bernstein from freely publishing the encryption source code.
- The Ninth Circuit held that the challenged regulations constituted a prior restraint on speech that offends the First Amendment.
- The court affirmed the district court's judgment that source code is expressive speech protected by the First Amendment.
- The government argued that because source code has a functional application in addition to its expressive application, it falls outside First Amendment protections; the court rejected this argument.
- EFF served as counsel for Bernstein. Cindy Cohn was the outside lead attorney for EFF in this case, beginning her involvement in 1993.
- After four years and one regulatory change, the Ninth Circuit issued its ruling.
- The EFF case page describes this as a landmark legal victory that greatly reduced the burdens and barriers to exporting open source encryption software.

## Historical Context

The case arose during the 1990s "crypto wars" when the U.S. government classified encryption software as a munition and restricted its export. Bernstein's challenge was one of several cases testing whether source code qualified as protected speech. The regulations initially fell under the International Traffic in Arms Regulations (ITAR) administered by the State Department, then shifted to the Export Administration Regulations (EAR) under the Department of Commerce during the litigation.

## Legal Analysis

The Ninth Circuit treated encryption source code as expressive speech subject to First Amendment protection, rejecting the government's argument that the functional nature of code removes it from First Amendment coverage. The court characterized the EAR licensing requirements as a prior restraint on speech — one of the most disfavored forms of government restriction under First Amendment doctrine. This holding established that source code publication cannot be subjected to prior review and licensing by the government without meeting strict constitutional standards.

## Significance for Software Companies

This case is foundational for the principle that source code is speech. It directly protects the right of software companies and developers to publish, distribute, and share source code — including encryption implementations — without government pre-approval. Any attempt to restrict code distribution must now be evaluated under First Amendment standards.

## Relationships

- `CASE-BERNSTEIN-V-DOJ` cites [`SRC-BERNSTEIN-JUSTIA`](../../../bibliography.md#SRC-BERNSTEIN-JUSTIA).
- `CASE-BERNSTEIN-V-DOJ` cites [`SRC-BERNSTEIN-EFF`](../../../bibliography.md#SRC-BERNSTEIN-EFF).
- `CASE-BERNSTEIN-V-DOJ` related_to `TOPIC-FIRST-AMENDMENT`.
- `CASE-BERNSTEIN-V-DOJ` related_to `TOPIC-CODE-AS-SPEECH`.

## Sources

- [`SRC-BERNSTEIN-JUSTIA`](../../../bibliography.md#SRC-BERNSTEIN-JUSTIA): Bernstein v. United States Department of Justice, 176 F.3d 1132 (9th Cir. 1999) (Justia).
- [`SRC-BERNSTEIN-EFF`](../../../bibliography.md#SRC-BERNSTEIN-EFF): Bernstein v. US Dept. of Justice EFF Case Page.

## Research Debt

- Add the earlier district court opinions (Bernstein I through IV).
- Document the subsequent en banc vacatur and its procedural history.
- Document practical impact on encryption export regulations post-decision.
- Connect to Cindy Cohn's attorney page.
