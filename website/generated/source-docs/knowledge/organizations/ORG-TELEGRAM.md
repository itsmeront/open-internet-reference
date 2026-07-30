---
id: ORG-TELEGRAM
title: Telegram
type: organization
status: draft
summary: Telegram is a Dubai-based messaging platform founded by Pavel Durov; OIR documents it as a secure-messaging company facing repeated government pressure over moderation, encryption access, and alleged facilitation of unlawful activity.
tags:
  - organization
  - privacy
  - secure-messaging
  - encryption-law
  - intermediary-liability
  - digital-rights
sources:
  - SRC-TELEGRAM-PRESS
  - SRC-TELEGRAM-FAQ
  - SRC-AP-DUROV-FSB-2026
  - SRC-RFERL-TELEGRAM-BLOCK-2018
relationships:
  - subject: ORG-TELEGRAM
    predicate: cites
    object: SRC-TELEGRAM-PRESS
    sources:
      - SRC-TELEGRAM-PRESS
  - subject: ORG-TELEGRAM
    predicate: cites
    object: SRC-TELEGRAM-FAQ
    sources:
      - SRC-TELEGRAM-FAQ
  - subject: ORG-TELEGRAM
    predicate: affiliated_with
    object: PERSON-PAVEL-DUROV
    sources:
      - SRC-TELEGRAM-PRESS
  - subject: ORG-TELEGRAM
    predicate: related_to
    object: EVENT-FSB-DUROV-TELEGRAM-2026
    sources:
      - SRC-AP-DUROV-FSB-2026
  - subject: ORG-TELEGRAM
    predicate: related_to
    object: TOPIC-INTERMEDIARY-LIABILITY
    sources:
      - SRC-AP-DUROV-FSB-2026
  - subject: ORG-TELEGRAM
    predicate: represented_by
    object: PERSON-PAVEL-CHIKOV
    sources:
      - SRC-RFERL-TELEGRAM-BLOCK-2018
    notes: RFE/RL identified Chikov as representing Telegram in the 2018 Russian blocking litigation; scope and duration beyond that episode need corroboration.
last_verified: "2026-07-29"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/organizations/ORG-TELEGRAM.md`
- Source ID: `ORG-TELEGRAM`
- [**Edit this page**](https://github.com/itsmeront/open-internet-reference/edit/main/knowledge/organizations/ORG-TELEGRAM.md) | [**Suggest a change**](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml&title=Edit+suggestion:+ORG-TELEGRAM)

!!! info "📝 Page Status: Draft — sourced but not yet reviewed"

    - **Status**: `draft`
    - **Sources**: 4
    - **Relationships**: 6
    - **Research debt items**: 6

---

# Telegram

## Summary

Telegram is a Dubai-based messaging platform founded by Pavel Durov. OIR documents it from official Telegram pages and reputable reporting on government demands for access, blocking, and criminal pressure tied to alleged use of the platform for unlawful activity.

## Verified Facts

- Telegram's official press page describes Telegram as a cloud-based mobile and desktop messaging app focused on security and speed.[^1]
- The official press page states the company is based in Dubai and that in 2025 Telegram passed 1 billion monthly active users.[^1]
- The official FAQ states that the Telegram development team is based in Dubai.[^2]
- The official press page states that Pavel Durov is the founder, owner, and CEO of Telegram.[^1]
- Associated Press reported on July 29, 2026, that Russia's Federal Security Service (FSB) accused Telegram's administration of failing to remove channels, chats, and bots allegedly used to prepare and coordinate sabotage, terrorism, and related crimes in Russia.[^3]
- RFE/RL reported that in April 2018 a Moscow court ordered Telegram blocked in Russia after the company refused FSB demands for encryption keys, and that Pavel Chikov represented Telegram in that dispute.[^4]

## Historical Context

Telegram has repeatedly been a site of conflict between platform operators and governments over encryption access, content moderation, and criminal facilitation theories. OIR treats Russian and French criminal allegations as reported proceedings, not as adjudicated findings that Telegram "supports terrorism."


[^1]: [`SRC-TELEGRAM-PRESS`](https://www.telegram.org/press) — Telegram Press Info. Official organizational record; self-reported.
[^2]: [`SRC-TELEGRAM-FAQ`](https://telegram.org/faq) — Telegram FAQ. Official organizational record; self-reported.
[^3]: [`SRC-AP-DUROV-FSB-2026`](https://apnews.com/article/russia-telegram-pavel-durov-ukraine-a6efe4692f3415c2046f0893d114174b) — AP News — Russia Accuses Telegram CEO Pavel Durov of Aiding Terrorism. Secondary reporting of FSB allegations.
[^4]: [`SRC-RFERL-TELEGRAM-BLOCK-2018`](https://www.rferl.org/a/russia-court-orders-telegram-to-be-blocked-in-russia/29164292.html) — RFE/RL — Russian Court Orders Telegram App Blocked (2018). Secondary reporting.

## Analysis

The July 2026 Russian charges against Durov sit at the intersection of intermediary liability, secure messaging, and state efforts to compel platform cooperation during wartime information control. Comparative context includes earlier Russian encryption-key demands (2018) and French platform-moderation charges (2024). See [EVENT-FSB-DUROV-TELEGRAM-2026](../legal/EVENT-FSB-DUROV-TELEGRAM-2026.md).

## Relationships

- `ORG-TELEGRAM` cites [`SRC-TELEGRAM-PRESS`](https://www.telegram.org/press).
- `ORG-TELEGRAM` cites [`SRC-TELEGRAM-FAQ`](https://telegram.org/faq).
- `ORG-TELEGRAM` affiliated_with `PERSON-PAVEL-DUROV`.
- `ORG-TELEGRAM` related_to `EVENT-FSB-DUROV-TELEGRAM-2026`.
- `ORG-TELEGRAM` related_to `TOPIC-INTERMEDIARY-LIABILITY`.
- `ORG-TELEGRAM` represented_by `PERSON-PAVEL-CHIKOV` (2018 Russian blocking dispute, per RFE/RL).

## Sources

1. [`SRC-TELEGRAM-PRESS`](https://www.telegram.org/press): Telegram Press Info.
2. [`SRC-TELEGRAM-FAQ`](https://telegram.org/faq): Telegram FAQ.
3. [`SRC-AP-DUROV-FSB-2026`](https://apnews.com/article/russia-telegram-pavel-durov-ukraine-a6efe4692f3415c2046f0893d114174b): AP News — Russia Accuses Telegram CEO Pavel Durov of Aiding Terrorism.
4. [`SRC-RFERL-TELEGRAM-BLOCK-2018`](https://www.rferl.org/a/russia-court-orders-telegram-to-be-blocked-in-russia/29164292.html): RFE/RL — Russian Court Orders Telegram App Blocked (2018).

## Research Debt

- Locate FSB primary press statement and Interfax wire copy for the July 29, 2026 charges.
- Add corporate-entity source records for Telegram Group Inc. / Telegram FZ-LLC from privacy policy or registry filings.
- Document independent technical sources on Telegram's encryption model (MTProto vs. default cloud chats vs. Secret Chats).
- Create a dedicated event or case page for the 2018 Russian blocking order with primary court/Roskomnadzor sources.
- Identify current commercial outside counsel or law firms retained by Telegram beyond historically reported individual lawyers.
- Corroborate self-reported press/FAQ claims with independent sources.

## Document metadata

- Last verified: `2026-07-29`
