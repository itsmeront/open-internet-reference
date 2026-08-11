---
id: TOPIC-APP-STORE-AGE-VERIFICATION
title: App Store and Operating System Age-Verification Laws
type: topic
status: draft
summary: Overview of U.S. state laws that pressure app stores and operating systems to verify or signal user age and to gate minors’ app access—covering California’s OS age-bracket signaling act, Texas/Utah/Louisiana/Alabama App Store Accountability Acts, key implementation dates, and major litigation status.
tags:
  - age-verification
  - first-amendment
  - privacy
  - digital-rights
  - public-policy
  - internet-governance
sources:
  - SRC-CA-CIV-1798-500-DIGITAL-AGE-ASSURANCE
  - SRC-CA-AB-1043-STATUS
  - SRC-TX-SB-2420-ENROLLED
  - SRC-CCIA-V-PAXTON-PI-ORDER
  - SRC-CA5-SB2420-STAY-ORDER
  - SRC-CCIA-SB2420-LITIGATION-PAGE
  - SRC-TX-TRIBUNE-SB2420-SCOTUS-2026
  - SRC-LA-ACT-185-ASAA
  - SRC-AL-HB161-ENROLLED
  - SRC-ALSTON-UTAH-ASAA-DISMISSAL-2026
relationships:
  - subject: TOPIC-APP-STORE-AGE-VERIFICATION
    predicate: related_to
    object: STAT-CA-DIGITAL-AGE-ASSURANCE-ACT
    sources:
      - SRC-CA-CIV-1798-500-DIGITAL-AGE-ASSURANCE
  - subject: TOPIC-APP-STORE-AGE-VERIFICATION
    predicate: related_to
    object: STAT-TX-APP-STORE-ACCOUNTABILITY
    sources:
      - SRC-TX-SB-2420-ENROLLED
  - subject: TOPIC-APP-STORE-AGE-VERIFICATION
    predicate: related_to
    object: CASE-CCIA-V-PAXTON-SB2420
    sources:
      - SRC-CCIA-V-PAXTON-PI-ORDER
  - subject: TOPIC-APP-STORE-AGE-VERIFICATION
    predicate: related_to
    object: TOPIC-FIRST-AMENDMENT
    sources:
      - SRC-CCIA-V-PAXTON-PI-ORDER
last_verified: "2026-08-08"
---

# App Store and Operating System Age-Verification Laws

## Summary

Since 2024–2026, multiple U.S. states have enacted laws that push age validation into the software distribution stack—either by requiring **app stores** to verify age and obtain parental consent for minors (the “App Store Accountability Act” / ASAA model), or by requiring **operating systems** to collect age and emit age-bracket signals to apps (California’s Digital Age Assurance Act). These statutes are a distinct cluster from website pornography age-verification laws, though they share a child-protection rationale and First Amendment pressure. This topic maps the major enacted state regimes, operative dates, and litigation status as of last verification.

## Two regulatory models

### Operating-system age signals (California)

California AB 1043 created Civil Code Title 1.81.9 (Digital Age Assurance Act). OS providers must gather age at account setup and provide developers a real-time age-bracket signal; developers must request the signal on download/launch. Effective January 1, 2026; **operative January 1, 2027**; legacy compliance by July 1, 2027.[^1][^2] Detail: [STAT-CA-DIGITAL-AGE-ASSURANCE-ACT](STAT-CA-DIGITAL-AGE-ASSURANCE-ACT.md).

### App-store age verification + parental consent (ASAA model)

Texas SB 2420 and related state acts require commercially reasonable age verification at app-store account creation, parent-account affiliation for minors, parental consent before downloads/purchases, developer age ratings, and DTPA-style or AG enforcement. Texas detail: [STAT-TX-APP-STORE-ACCOUNTABILITY](STAT-TX-APP-STORE-ACCOUNTABILITY.md).

## Landscape table (enacted / re-enacted regimes)

| Jurisdiction | Law | Model | Key dates | Litigation / status (as of 2026-08-08) |
|---|---|---|---|---|
| [**California**](STAT-CA-DIGITAL-AGE-ASSURANCE-ACT.md) | [AB 1043 / Civ. Code §§ 1798.500–1798.505](STAT-CA-DIGITAL-AGE-ASSURANCE-ACT.md) | OS age-bracket signals to apps | Chaptered 2025-10-13; effective 2026-01-01; **operative 2027-01-01**; legacy by 2027-07-01 | Enacted; no OIR-documented constitutional challenge yet[^1][^2] |
| [**Texas**](STAT-TX-APP-STORE-ACCOUNTABILITY.md) | [SB 2420 / Bus. & Com. Code ch. 121](STAT-TX-APP-STORE-ACCOUNTABILITY.md) | App-store AV + parental consent + developer ratings | **Effective 2026-01-01** | [PI granted 2025-12-23; 5th Cir. stay 2026-06-04; SCOTUS denied emergency vacatur (July 2026 per CCIA) → **enforceable pending appeal**](CASE-CCIA-V-PAXTON-SB2420.md)[^3][^4][^5][^6][^7] |
| **Utah** | [ASAA; amended by HB 498 (per secondary)](../../bibliography/legal/SRC-ALSTON-UTAH-ASAA-DISMISSAL-2026.md) | App-store AV model (amended) | Obligations delayed to **2027-05-06** (per secondary) | [CCIA challenge filed Feb 2026; **voluntarily dismissed 2026-04-21** after amendments removing AG enforcement / delaying ops](../../bibliography/legal/SRC-ALSTON-UTAH-ASAA-DISMISSAL-2026.md)[^10] |
| [**Louisiana**](../../bibliography/legal/SRC-LA-ACT-185-ASAA.md) | [Act No. 185 (2026)](../../bibliography/legal/SRC-LA-ACT-185-ASAA.md) | App-store AV model (re-enacted/delayed) | Substantive provisions **effective 2027-07-01** | Enacted delay/replacement text; monitor new challenges[^8] |
| [**Alabama**](../../bibliography/legal/SRC-AL-HB161-ENROLLED.md) | [HB 161 (enrolled 2026)](../../bibliography/legal/SRC-AL-HB161-ENROLLED.md) | App-store AV model | **Effective 2027-01-01** | Enacted; AG rulemaking contemplated; monitor challenges[^9] |

## Texas litigation (lead case)

[CASE-CCIA-V-PAXTON-SB2420](CASE-CCIA-V-PAXTON-SB2420.md) is the lead federal test of the ASAA model:

1. **Dec 23, 2025** — W.D. Tex. (Pitman) preliminary injunction: Act likely unconstitutional.[^4]
2. **June 4, 2026** — Fifth Circuit stays injunctions pending appeal → Texas may enforce.[^5]
3. **July 2026** — Supreme Court denies emergency application to vacate stay (CCIA timeline).[^6]
4. **Merits appeal ongoing** — no final appellate holding on constitutionality yet.[^6][^7]

## Why this matters for open internet systems

These laws shift age gating into infrastructure layers (stores and OS APIs). Effects include identity/age-data collection at account creation, parental-consent friction for minors’ access to lawful apps, developer rating and consent-integration duties, and potential nationwide product design changes driven by a few large state markets. California’s signal model may create “actual knowledge” of age brackets for developers even without store-level ID checks. Pair with [TOPIC-FIRST-AMENDMENT](TOPIC-FIRST-AMENDMENT.md).

## Verified Facts

- California Title 1.81.9 requires OS age interfaces and age-bracket signals; operative January 1, 2027.[^1]
- Texas SB 2420 takes effect January 1, 2026 and imposes app-store age verification and parental consent.[^3]
- Texas enforcement was enjoined in December 2025, then a Fifth Circuit stay (June 4, 2026) and SCOTUS non-vacatur left the law enforceable pending appeal.[^4][^5][^6]
- Louisiana Act 185 states that sections 2 through 4 become effective July 1, 2027.[^8]
- Alabama HB 161 enrolled text states an effective date of January 1, 2027.[^9]
- Secondary reporting states Utah’s ASAA obligations were delayed to May 6, 2027 and that CCIA’s Utah challenge was voluntarily dismissed April 21, 2026.[^10]


[^1]: `SRC-CA-CIV-1798-500-DIGITAL-AGE-ASSURANCE` — California Civil Code Title 1.81.9 (leginfo). Primary statute.
[^2]: `SRC-CA-AB-1043-STATUS` — AB 1043 chaptered Oct. 13, 2025. Official status.
[^3]: `SRC-TX-SB-2420-ENROLLED` — Texas SB 2420 enrolled. Primary statute.
[^4]: `SRC-CCIA-V-PAXTON-PI-ORDER` — W.D. Tex. PI order (Dec. 23, 2025).
[^5]: `SRC-CA5-SB2420-STAY-ORDER` — Fifth Circuit stay (June 4, 2026).
[^6]: `SRC-CCIA-SB2420-LITIGATION-PAGE` — CCIA litigation timeline (party secondary).
[^7]: `SRC-TX-TRIBUNE-SB2420-SCOTUS-2026` — Texas Tribune on SCOTUS non-intervention (journalism; date tension with CCIA).
[^8]: `SRC-LA-ACT-185-ASAA` — Louisiana Act No. 185 enrolled text.
[^9]: `SRC-AL-HB161-ENROLLED` — Alabama HB 161 enrolled PDF.
[^10]: `SRC-ALSTON-UTAH-ASAA-DISMISSAL-2026` — Alston & Bird alert on Utah amendments and dismissal (secondary).

## Relationships

- `TOPIC-APP-STORE-AGE-VERIFICATION` related_to `STAT-CA-DIGITAL-AGE-ASSURANCE-ACT`.
- `TOPIC-APP-STORE-AGE-VERIFICATION` related_to `STAT-TX-APP-STORE-ACCOUNTABILITY`.
- `TOPIC-APP-STORE-AGE-VERIFICATION` related_to `CASE-CCIA-V-PAXTON-SB2420`.
- `TOPIC-APP-STORE-AGE-VERIFICATION` related_to `TOPIC-FIRST-AMENDMENT`.

## Sources

1. `SRC-CA-CIV-1798-500-DIGITAL-AGE-ASSURANCE`: California Civil Code Title 1.81.9.
2. `SRC-CA-AB-1043-STATUS`: California AB 1043 Bill Status.
3. `SRC-TX-SB-2420-ENROLLED`: Texas SB 2420 Enrolled Text.
4. `SRC-CCIA-V-PAXTON-PI-ORDER`: CCIA v. Paxton PI Order.
5. `SRC-CA5-SB2420-STAY-ORDER`: Fifth Circuit Stay Order.
6. `SRC-CCIA-SB2420-LITIGATION-PAGE`: CCIA Litigation Page.
7. `SRC-TX-TRIBUNE-SB2420-SCOTUS-2026`: Texas Tribune SCOTUS coverage.
8. `SRC-LA-ACT-185-ASAA`: Louisiana Act No. 185.
9. `SRC-AL-HB161-ENROLLED`: Alabama HB 161 Enrolled.
10. `SRC-ALSTON-UTAH-ASAA-DISMISSAL-2026`: Alston & Bird Utah ASAA dismissal alert.

## Research Debt

- Add official Utah Code / HB 498 primary text to replace secondary-only Utah dates and enforcement changes.
- Create dedicated STAT pages for Utah, Louisiana, and Alabama when OIR expands beyond the overview.
- Track additional 2026–2027 state ASAA bills (and failures) with primary bill status pages.
- Separate topic or pages for **website** age-verification laws (e.g., Free Speech Coalition / *Moody*-adjacent line) and cross-link.
- Resolve SCOTUS denial exact date via Supreme Court docket.
- Document Apple/Google implementation notices and any multi-state compliance architecture once public.
- Note interaction with California Age-Appropriate Design Code and COPPA.
