---
id: STAT-CFAA-1030
title: Computer Fraud and Abuse Act (18 U.S.C. § 1030)
type: statute
status: draft
summary: The Computer Fraud and Abuse Act (CFAA), 18 U.S.C. § 1030, is the primary U.S. federal anti-hacking statute, originally enacted in 1984 and substantially amended in 1986, 1994, 1996, 2001, 2002, and 2008, which criminalizes unauthorized access to computers and has been widely criticized for vagueness and prosecutorial overreach.
tags:
  - computer-crime
  - digital-rights
  - internet-governance
sources:
  - SRC-USC-18-1030-LII
  - SRC-USC-18-1030-GOVINFO
  - SRC-VAN-BUREN-LII
relationships:
  - subject: STAT-CFAA-1030
    predicate: cites
    object: SRC-USC-18-1030-LII
    sources:
      - SRC-USC-18-1030-LII
  - subject: STAT-CFAA-1030
    predicate: cites
    object: SRC-USC-18-1030-GOVINFO
    sources:
      - SRC-USC-18-1030-GOVINFO
  - subject: STAT-CFAA-1030
    predicate: related_to
    object: TOPIC-COMPUTER-FRAUD
    sources:
      - SRC-USC-18-1030-GOVINFO
  - subject: STAT-CFAA-1030
    predicate: related_to
    object: CASE-VAN-BUREN-V-US
    sources:
      - SRC-VAN-BUREN-LII
last_verified: "2026-06-25"
---

# Computer Fraud and Abuse Act (18 U.S.C. § 1030)

## Summary

The Computer Fraud and Abuse Act (CFAA) is the primary U.S. federal criminal statute addressing unauthorized computer access. Originally enacted in 1984 and substantially expanded in 1986, it has been amended multiple times and remains controversial for its broad language and potential for prosecutorial overreach.

## Official Sources

- **Current text (Cornell LII)**: https://www.law.cornell.edu/uscode/text/18/1030
- **Current text (GovInfo)**: https://www.govinfo.gov/content/pkg/USCODE-2023-title18/html/USCODE-2023-title18-partI-chap47-sec1030.htm

## Legislative History

| Year | Action | Significance |
|---|---|---|
| 1984 | Original enactment (Comprehensive Crime Control Act) | Created 18 U.S.C. § 1030 targeting unauthorized access to government and financial computers |
| 1986 | Computer Fraud and Abuse Act | Major expansion: added computer vandalism, unauthorized access offenses, broadened scope beyond federal computers |
| 1989 | Amendment | Technical corrections |
| 1994 | Amendment | Added civil cause of action, expanded to cover interstate computer crime |
| 1996 | National Information Infrastructure Protection Act | Expanded "protected computer" definition, increased penalties |
| 2001 | USA PATRIOT Act | Expanded scope for terrorism-related offenses, increased penalties, broadened definitions |
| 2002 | Cyber Security Enhancement Act | Increased maximum penalties |
| 2008 | Identity Theft Enforcement and Restitution Act | Further expanded scope and penalties |

## Key Provisions

- **§ 1030(a)(1)**: Unauthorized access to classified information via computer
- **§ 1030(a)(2)**: Obtaining information from protected computers without authorization or exceeding authorized access
- **§ 1030(a)(3)**: Unauthorized access to government computers
- **§ 1030(a)(4)**: Computer fraud (accessing to defraud and obtain value)
- **§ 1030(a)(5)**: Causing damage to protected computers (malware, DoS)
- **§ 1030(a)(6)**: Trafficking in passwords
- **§ 1030(a)(7)**: Extortion involving computers

## Proposed Reforms

### Aaron's Law (not enacted)

Introduced by Rep. Zoe Lofgren and Sen. Ron Wyden (with Sen. Rand Paul), Aaron's Law would:
- Delete the vague phrase "exceeds authorized access"
- Clarify the definition of "access without authorization"
- Prevent stacking of charges for the same underlying conduct
- Distinguish common internet activity from harmful cyberattacks

Named after Aaron Swartz, who faced up to 35 years under the CFAA for downloading academic articles.

## Interpreting Cases

- **Van Buren v. United States** (2021): Supreme Court narrowed "exceeds authorized access" to a gates-up-or-down inquiry — does not cover policy-violating use of systems one is authorized to access.
- **United States v. Nosal** (9th Cir.): Addressed employee access violations.
- **hiQ Labs v. LinkedIn** (9th Cir.): Addressed whether scraping public data violates the CFAA.

## Criticism

The CFAA has been widely criticized for:
- Vague definitions that criminalize common internet behavior
- Enabling prosecutorial overreach (stacking charges for exponentially higher penalties)
- Chilling security research by making vulnerability testing legally risky
- Being used to threaten terms-of-service violations as federal crimes
- The case of Aaron Swartz highlighted these concerns and inspired reform efforts

## Relevance to Open Source and Software Companies

The CFAA directly affects:
- Security researchers conducting vulnerability testing
- Developers building web scrapers or API clients
- Companies with terms of service that users might technically "exceed"
- Open source contributors accessing codebases
- The Van Buren decision (2021) significantly narrowed the statute's scope, providing more certainty for developers

## Relationships

- `STAT-CFAA-1030` cites `SRC-USC-18-1030-LII`.
- `STAT-CFAA-1030` cites `SRC-USC-18-1030-GOVINFO`.
- `STAT-CFAA-1030` related_to `TOPIC-COMPUTER-FRAUD`.
- `STAT-CFAA-1030` related_to `CASE-VAN-BUREN-V-US`.

## Sources

- `SRC-USC-18-1030-LII`: 18 U.S.C. § 1030 (Cornell LII).
- `SRC-USC-18-1030-GOVINFO`: 18 U.S.C. § 1030 (GovInfo).

## Research Debt

- Add hiQ Labs v. LinkedIn and United States v. Nosal case pages.
- Document the Aaron Swartz case in detail.
- Add CRS Report on CFAA as a source.
- Review per-fact footnote-to-source mapping; multiple sources are cited on this page.
