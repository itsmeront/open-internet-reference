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
  - SRC-BERNSTEIN-EFF-25
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
    predicate: cites
    object: SRC-BERNSTEIN-EFF-25
    sources:
      - SRC-BERNSTEIN-EFF-25
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

# Bernstein v. United States Department of Justice

## Summary

Bernstein v. United States Department of Justice, 176 F.3d 1132 (9th Cir. 1999), held that software source code is protected speech under the First Amendment and that government regulations preventing its publication constituted an unconstitutional prior restraint.

## Verified Facts

- The case citation is 176 F.3d 1132 (9th Cir. 1999).[^1]
- Daniel J. Bernstein, a mathematician and cryptographer, developed an encryption algorithm called "Snuffle" and wanted to publish the source code and an explanatory academic paper.[^1]
- The Export Administration Regulations (EAR) prevented Bernstein from freely publishing the encryption source code.[^1]
- The Ninth Circuit held that the challenged regulations constituted a prior restraint on speech that offends the First Amendment.[^1]
- The court affirmed the district court's judgment that source code is expressive speech protected by the First Amendment.[^1]
- The government argued that because source code has a functional application in addition to its expressive application, it falls outside First Amendment protections; the court rejected this argument.[^1]
- EFF served as counsel for Bernstein. Cindy Cohn was the outside lead attorney for EFF in this case, beginning her involvement in 1993.[^1]
- After four years and one regulatory change, the Ninth Circuit issued its ruling.[^1]
- The EFF case page describes this as a landmark legal victory that greatly reduced the burdens and barriers to exporting open source encryption software.[^1]

## Historical Context

The case arose during the 1990s "crypto wars" when the U.S. government classified encryption software as a munition and restricted its export. Bernstein's challenge was one of several cases testing whether source code qualified as protected speech. The regulations initially fell under the International Traffic in Arms Regulations (ITAR) administered by the State Department, then shifted to the Export Administration Regulations (EAR) under the Department of Commerce during the litigation.

The government petitioned for rehearing en banc on June 21, 1999. The en banc court granted rehearing and vacated the three-judge panel opinion. However, before the en banc court could hear the case, the government substantially revised the export regulations, rendering much of the dispute moot. The case was remanded to the district court in light of the new regulations. While the panel opinion was technically vacated, its reasoning — that source code is speech and export controls constitute a prior restraint — profoundly influenced both Junger v. Daley and subsequent regulatory reform.


[^1]: `SRC-BERNSTEIN-JUSTIA` — Bernstein v. United States Department of Justice, 176 F.3d 1132 (9th Cir. 1999) (Justia). Primary authority.

## Legal Analysis

The Ninth Circuit treated encryption source code as expressive speech subject to First Amendment protection, rejecting the government's argument that the functional nature of code removes it from First Amendment coverage. The court characterized the EAR licensing requirements as a prior restraint on speech — one of the most disfavored forms of government restriction under First Amendment doctrine. This holding established that source code publication cannot be subjected to prior review and licensing by the government without meeting strict constitutional standards.

## Practical Impact

EFF describes this as "one of EFF's first major legal victories" that "established code as speech and changed United States export regulations on encryption software, paving the way for international e-commerce." The ruling led to regulatory changes that made it easier to publish encryption software online without U.S. government approval. This directly enabled the global availability of open source encryption tools (OpenSSL, GnuPG, etc.) and secure internet protocols (TLS/SSL) that underpin modern online commerce and communications.

## Significance for Software Companies

This case is foundational for the principle that source code is speech. It directly protects the right of software companies and developers to publish, distribute, and share source code — including encryption implementations — without government pre-approval. Any attempt to restrict code distribution must now be evaluated under First Amendment standards.

## Relationships

- `CASE-BERNSTEIN-V-DOJ` cites `SRC-BERNSTEIN-JUSTIA`.
- `CASE-BERNSTEIN-V-DOJ` cites `SRC-BERNSTEIN-EFF`.
- `CASE-BERNSTEIN-V-DOJ` cites `SRC-BERNSTEIN-EFF-25`.
- `CASE-BERNSTEIN-V-DOJ` related_to `TOPIC-FIRST-AMENDMENT`.
- `CASE-BERNSTEIN-V-DOJ` related_to `TOPIC-CODE-AS-SPEECH`.

## Sources

- `SRC-BERNSTEIN-JUSTIA`: Bernstein v. United States Department of Justice, 176 F.3d 1132 (9th Cir. 1999) (Justia).
- `SRC-BERNSTEIN-EFF`: Bernstein v. US Dept. of Justice EFF Case Page.
- `SRC-BERNSTEIN-EFF-25`: EFF at 25 — Remembering the Case that Established Code as Speech.

## Research Debt

- Add the earlier district court opinions (Bernstein I through IV).
- Review per-fact footnote-to-source mapping; multiple sources are cited on this page.
