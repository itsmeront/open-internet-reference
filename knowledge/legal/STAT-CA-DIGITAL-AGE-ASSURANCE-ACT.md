---
id: STAT-CA-DIGITAL-AGE-ASSURANCE-ACT
title: California Digital Age Assurance Act (Civ. Code §§ 1798.500–1798.505)
type: statute
status: draft
summary: California’s Digital Age Assurance Act (AB 1043; Civ. Code Title 1.81.9) requires operating system providers to collect age at account setup and send age-bracket signals to apps, and requires developers to request those signals; effective January 1, 2026 and operative January 1, 2027.
tags:
  - age-verification
  - privacy
  - digital-rights
  - public-policy
  - internet-governance
sources:
  - SRC-CA-CIV-1798-500-DIGITAL-AGE-ASSURANCE
  - SRC-CA-AB-1043-STATUS
relationships:
  - subject: STAT-CA-DIGITAL-AGE-ASSURANCE-ACT
    predicate: cites
    object: SRC-CA-CIV-1798-500-DIGITAL-AGE-ASSURANCE
    sources:
      - SRC-CA-CIV-1798-500-DIGITAL-AGE-ASSURANCE
  - subject: STAT-CA-DIGITAL-AGE-ASSURANCE-ACT
    predicate: cites
    object: SRC-CA-AB-1043-STATUS
    sources:
      - SRC-CA-AB-1043-STATUS
  - subject: STAT-CA-DIGITAL-AGE-ASSURANCE-ACT
    predicate: related_to
    object: TOPIC-APP-STORE-AGE-VERIFICATION
    sources:
      - SRC-CA-CIV-1798-500-DIGITAL-AGE-ASSURANCE
last_verified: "2026-08-08"
enactment_date: "2025-10-13"
---

# California Digital Age Assurance Act (Civ. Code §§ 1798.500–1798.505)

## Summary

California’s Digital Age Assurance Act, added by AB 1043 (Stats. 2025, Ch. 675), creates Civil Code Title 1.81.9. It obligates operating system providers to obtain age information at account setup and to expose age-bracket “signals” to developers via API, and obligates developers to request those signals when apps are downloaded and launched. The title is effective January 1, 2026 and operative January 1, 2027.

## Official Sources

- **Codified text (leginfo)**: https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=CIV&division=3.&title=1.81.9.&part=4.&chapter=&article=
- **AB 1043 bill status**: https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB1043

## Verified Facts

- Title 1.81.9 (Civil Code §§ 1798.500–1798.505) was added by Stats. 2025, Ch. 675, Sec. 1 (AB 1043).[^1]
- AB 1043 was chaptered by the Secretary of State on October 13, 2025, as Chapter 675, Statutes of 2025.[^2]
- The title is effective January 1, 2026 and operative January 1, 2027 pursuant to § 1798.505.[^1]
- “Age bracket data” must indicate, at minimum, whether a user is under 13; 13–15; 16–17; or 18 or older.[^1]
- An operating system provider must provide an accessible interface at account setup for an account holder to indicate the user’s birth date, age, or both, and must provide requesting developers a real-time API signal identifying the user’s age bracket.[^1]
- A developer must request a signal when the application is downloaded and launched, and generally must treat the signal as the primary age-range indicator (subject to clear and convincing contrary internal information).[^1]
- For devices with account setup completed before January 1, 2027, OS providers must provide a legacy age interface before July 1, 2027; certain pre-2027 downloads require developers to request a signal before July 1, 2027.[^1]
- Enforcement is by California Attorney General civil action: up to $2,500 per affected child for each negligent violation and up to $7,500 per affected child for each intentional violation, plus injunctive relief.[^1]
- Good-faith OS providers and covered application stores are not liable for erroneous signals or for developer conduct after receiving a signal.[^1]

## Key Provisions

| Section | Subject |
|---|---|
| § 1798.500 | Definitions (account holder, age bracket data, signal, OS provider, developer, covered application store) |
| § 1798.501 | OS duties (age interface + API signal); developer duties (request signal; use as primary indicator) |
| § 1798.502 | Legacy devices/apps compliance by July 1, 2027 |
| § 1798.503 | AG civil penalties and good-faith safe harbor for erroneous signals |
| § 1798.504 | Antitrust/nondiscrimination, interaction with AADC, exemptions, severability |
| § 1798.505 | Operative date January 1, 2027 |

## Distinction from App Store Accountability Acts

Unlike Texas SB 2420 and similar “App Store Accountability Act” statutes, California’s law is framed as an **operating-system age-bracket signaling** regime rather than a full app-store age-verification and per-download parental-consent gate. Pair with [TOPIC-APP-STORE-AGE-VERIFICATION](TOPIC-APP-STORE-AGE-VERIFICATION.md) and [STAT-TX-APP-STORE-ACCOUNTABILITY](STAT-TX-APP-STORE-ACCOUNTABILITY.md).


[^1]: `SRC-CA-CIV-1798-500-DIGITAL-AGE-ASSURANCE` — California Civil Code Title 1.81.9 (leginfo). Primary statute text.
[^2]: `SRC-CA-AB-1043-STATUS` — California AB 1043 bill status (chaptered Oct. 13, 2025). Official legislative status.

## Relationships

- `STAT-CA-DIGITAL-AGE-ASSURANCE-ACT` cites `SRC-CA-CIV-1798-500-DIGITAL-AGE-ASSURANCE`.
- `STAT-CA-DIGITAL-AGE-ASSURANCE-ACT` cites `SRC-CA-AB-1043-STATUS`.
- `STAT-CA-DIGITAL-AGE-ASSURANCE-ACT` related_to `TOPIC-APP-STORE-AGE-VERIFICATION`.

## Sources

1. `SRC-CA-CIV-1798-500-DIGITAL-AGE-ASSURANCE`: California Civil Code Title 1.81.9 — Digital Age Assurance Act (leginfo).
2. `SRC-CA-AB-1043-STATUS`: California AB 1043 Bill Status — Chaptered October 13, 2025.

## Research Debt

- Add Attorney General guidance or implementing materials if issued before January 1, 2027.
- Document any constitutional challenges to AB 1043 / Title 1.81.9 when filed.
- Cross-link California Age-Appropriate Design Code (Civ. Code § 1798.99.28 et seq.) with primary sources.
- Clarify covered-application-store duties relative to OS-provider duties with industry implementation notes once available.
