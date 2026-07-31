---
id: ORG-FIRE
title: Foundation for Individual Rights and Expression
type: organization
status: draft
summary: FIRE is a U.S. 501(c)(3) nonprofit that defends free speech and free thought through campus advocacy, litigation, policy reform, and public education; founded in 1999 and renamed in 2022 when it expanded beyond higher education.
tags:
  - organization
  - first-amendment
  - civil-society
  - outreach
sources:
  - SRC-FIRE-MISSION
  - SRC-FIRE-SUBMIT-CASE
  - SRC-FIRE-PRABHAKAR-CASE
relationships:
  - subject: ORG-FIRE
    predicate: cites
    object: SRC-FIRE-MISSION
    sources:
      - SRC-FIRE-MISSION
  - subject: ORG-FIRE
    predicate: cites
    object: SRC-FIRE-SUBMIT-CASE
    sources:
      - SRC-FIRE-SUBMIT-CASE
  - subject: ORG-FIRE
    predicate: cites
    object: SRC-FIRE-PRABHAKAR-CASE
    sources:
      - SRC-FIRE-PRABHAKAR-CASE
  - subject: ORG-FIRE
    predicate: related_to
    object: TOPIC-FIRST-AMENDMENT
    sources:
      - SRC-FIRE-MISSION
last_verified: "2026-07-31"
---

# Foundation for Individual Rights and Expression

## Summary

The Foundation for Individual Rights and Expression (FIRE) is a U.S. nonprofit that, according to its official mission page, defends and sustains individual rights to free speech and free thought through education, advocacy, and litigation, with a special emphasis on students and faculty.

## Verified Facts

- FIRE’s official mission page states that it defends and sustains the individual rights of all Americans to free speech and free thought, and that it educates the public, promotes a culture of respect for those rights, and provides means to preserve them.[^1]
- The mission page places special emphasis on defending individual rights of students and faculty on U.S. campuses, including freedom of speech, freedom of association, due process, legal equality, religious liberty, and sanctity of conscience.[^1]
- FIRE was founded in 1999 as the Foundation for Individual Rights in Education; in 2022 it changed its name to the Foundation for Individual Rights and Expression to reflect a broader off-campus free-expression mission.[^1]
- FIRE describes itself as a tax-exempt nonprofit organization under Section 501(c)(3) of the Internal Revenue Code.[^1]
- FIRE maintains a public “Submit a Case” page for confidential online case submissions and states that submitting a case does not create an attorney-client relationship unless FIRE expressly agrees through a signed agreement.[^2]
- The Submit a Case page lists a Faculty Legal Defense Fund hotline for faculty at public colleges and universities (254-500-3533) and a Student Press Freedom Initiative hotline for student journalists, student media, and advisors (717-734-7734).[^2]

## Historical Context

Intake of this organization page was prompted by a Decap CMS proposal noting FIRE’s support for a Florida professor in a dispute over assigned course material. FIRE’s case page describes representing Vinita Prabhakar in a federal lawsuit filed July 29, 2026, against South Florida State College officials after termination following an English-literature assignment.[^3] Treat that narrative as advocacy-attributed until primary court records are intake’d.


[^1]: `SRC-FIRE-MISSION` — FIRE Mission Page. Official organizational record; self-reported.
[^2]: `SRC-FIRE-SUBMIT-CASE` — FIRE Submit a Case Page. Official public intake path.
[^3]: `SRC-FIRE-PRABHAKAR-CASE` — FIRE Case Page — Prabhakar v. Hawkins et al. Advocacy case page.

## Public Contact Information

- Website: https://www.thefire.org/
- Mission: https://www.thefire.org/about-us/mission
- Submit a case: https://www.thefire.org/submit-a-case
- Faculty Legal Defense Fund hotline (public universities faculty): 254-500-3533
- Student Press Freedom Initiative hotline: 717-734-7734

## Relevance to Open Source and Software Companies

FIRE’s core docket is campus and public free-expression / academic-freedom litigation rather than software-specific tech policy. It may still be relevant when developers, student journalists, faculty, or software-adjacent speakers face government or public-institution speech sanctions. Prefer EFF, ACLU, Knight, CDT, or specialized tech counsel for encryption, intermediary liability, and computer-crime matters.

## Relationships

- `ORG-FIRE` cites `SRC-FIRE-MISSION`.
- `ORG-FIRE` cites `SRC-FIRE-SUBMIT-CASE`.
- `ORG-FIRE` cites `SRC-FIRE-PRABHAKAR-CASE`.
- `ORG-FIRE` related_to `TOPIC-FIRST-AMENDMENT`.

## Sources

1. `SRC-FIRE-MISSION`: FIRE Mission Page.
2. `SRC-FIRE-SUBMIT-CASE`: FIRE Submit a Case Page.
3. `SRC-FIRE-PRABHAKAR-CASE`: FIRE Case Page — Prabhakar v. Hawkins et al.

## Research Debt

- Corroborate founding story (Kors/Silverglate) and 2022 expansion plan with independent journalism or IRS filings; do not promote self-reported victory/policy-change tallies from the mission page without independent sources.
- Add PACER complaint/docket for *Prabhakar v. Hawkins* before creating a CASE-* page; optional secondary NYT / local press bibliography if URL confirmed.
- Create a dedicated `contacts/` record only after outreach CRM requirements are defined; hotlines/process should be rechecked before use.
- Document technology-adjacent FIRE litigation or amicus work if primary sources exist.
- Domain expert review before status above `draft`.
- Renamed from Decap CMS stub ID `ORG-FOUNDATION-FOR-IND-RIGHTS-EXPRESSION` to `ORG-FIRE` to match acronym-style org IDs (`ORG-EFF`, `ORG-ACLU`).
