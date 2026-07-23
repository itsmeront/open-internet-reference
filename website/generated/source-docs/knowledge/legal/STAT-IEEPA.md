---
id: STAT-IEEPA
title: International Emergency Economic Powers Act (50 U.S.C. §§ 1701–1708)
type: statute
status: draft
summary: The International Emergency Economic Powers Act (IEEPA), 50 U.S.C. §§ 1701–1708, authorizes the President to regulate transactions and block property in which foreign countries or nationals have interests during declared national emergencies; OFAC administers related sanctions programs.
tags:
  - statute
  - sanctions
  - digital-rights
sources:
  - SRC-IEEPA-50-USC-1702-LII
  - SRC-VAN-LOON-5TH-CIR-JUSTIA
relationships:
  - subject: STAT-IEEPA
    predicate: cites
    object: SRC-IEEPA-50-USC-1702-LII
    sources:
      - SRC-IEEPA-50-USC-1702-LII
  - subject: STAT-IEEPA
    predicate: related_to
    object: CASE-VAN-LOON-V-TREASURY
    sources:
      - SRC-VAN-LOON-5TH-CIR-JUSTIA
  - subject: STAT-IEEPA
    predicate: related_to
    object: TOPIC-TORNADO-CASH
    sources:
      - SRC-VAN-LOON-5TH-CIR-JUSTIA
last_verified: "2026-07-23"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/legal/STAT-IEEPA.md`
- Source ID: `STAT-IEEPA`
- [**Edit this page**](https://github.com/itsmeront/open-internet-reference/edit/main/knowledge/legal/STAT-IEEPA.md) | [**Suggest a change**](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml&title=Edit+suggestion:+STAT-IEEPA)

!!! info "📝 Page Status: Draft — sourced but not yet reviewed"

    - **Status**: `draft`
    - **Sources**: 2
    - **Relationships**: 3
    - **Research debt items**: 3
    - **Last verified**: 2026-07-23

---

# International Emergency Economic Powers Act (50 U.S.C. §§ 1701–1708)

## Summary

The International Emergency Economic Powers Act (IEEPA), 50 U.S.C. §§ 1701–1708, authorizes the President to regulate certain transactions and to deal with property in which foreign countries or nationals have interests during declared national emergencies. Treasury’s Office of Foreign Assets Control (OFAC) administers related economic sanctions programs.

## Verified Facts

- 50 U.S.C. § 1702 sets out presidential authorities under IEEPA, including authority, under declared national emergency conditions, to investigate, regulate, or prohibit transactions involving any property in which any foreign country or a national thereof has any interest by any person, or with respect to any property, subject to the jurisdiction of the United States.[^1]
- In Van Loon v. Department of the Treasury, the Fifth Circuit held that Tornado Cash immutable smart contracts are not “property” of a foreign national or entity under IEEPA and therefore cannot be blocked under IEEPA on that theory.[^2]

## Official Sources

- **50 U.S.C. § 1702 (Cornell LII)**: https://www.law.cornell.edu/uscode/text/50/1702


[^1]: [`SRC-IEEPA-50-USC-1702-LII`](../../../bibliography.md#SRC-IEEPA-50-USC-1702-LII) — 50 U.S.C. § 1702 (Cornell LII). Statute text.
[^2]: [`SRC-VAN-LOON-5TH-CIR-JUSTIA`](../../../bibliography.md#SRC-VAN-LOON-5TH-CIR-JUSTIA) — Van Loon v. Department of the Treasury, No. 23-50669 (5th Cir. Nov. 26, 2024) (Justia). Primary authority.

## Legal Analysis

IEEPA is the principal statute under which many OFAC blocking programs operate through executive orders. Van Loon construes the “property” element of that blocking authority as applied to immutable smart contracts. Separate criminal provisions enforce certain IEEPA violations; those criminal cases are tracked on related case pages.

## Relationships

- `STAT-IEEPA` cites [`SRC-IEEPA-50-USC-1702-LII`](../../../bibliography.md#SRC-IEEPA-50-USC-1702-LII).
- `STAT-IEEPA` related_to `CASE-VAN-LOON-V-TREASURY`.
- `STAT-IEEPA` related_to `TOPIC-TORNADO-CASH`.

## Sources

1. [`SRC-IEEPA-50-USC-1702-LII`](../../../bibliography.md#SRC-IEEPA-50-USC-1702-LII): 50 U.S.C. § 1702 (Cornell LII).
2. [`SRC-VAN-LOON-5TH-CIR-JUSTIA`](../../../bibliography.md#SRC-VAN-LOON-5TH-CIR-JUSTIA): Van Loon v. Department of the Treasury, No. 23-50669 (5th Cir. Nov. 26, 2024) (Justia).

## Research Debt

- Add GovInfo / OLRC official U.S. Code text sources for §§ 1701–1708.
- Add Executive Orders 13694 and 13722 as `REG-*` or dedicated source records.
- Summarize IEEPA’s informational-materials limitation (50 U.S.C. § 1702(b)) and any Tornado Cash litigation treatment of that clause.
