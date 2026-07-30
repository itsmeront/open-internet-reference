---
id: PERSON-PAVEL-DUROV
title: Pavel Durov
type: person
status: draft
summary: Pavel Durov is the founder, owner, and CEO of Telegram; OIR documents Russian and French criminal proceedings alleging platform-related facilitation or moderation failures, including a July 2026 FSB charge and international wanted listing.
tags:
  - person
  - secure-messaging
  - privacy
  - encryption-law
  - intermediary-liability
  - digital-rights
sources:
  - SRC-TELEGRAM-PRESS
  - SRC-AP-DUROV-FSB-2026
  - SRC-BBC-DUROV-FSB-2026
  - SRC-MEDUZA-DUROV-FSB-2026
  - SRC-FRANCE24-DUROV-KAMINSKI-2024
  - SRC-RFERL-TELEGRAM-BLOCK-2018
relationships:
  - subject: PERSON-PAVEL-DUROV
    predicate: affiliated_with
    object: ORG-TELEGRAM
    sources:
      - SRC-TELEGRAM-PRESS
  - subject: PERSON-PAVEL-DUROV
    predicate: related_to
    object: EVENT-FSB-DUROV-TELEGRAM-2026
    sources:
      - SRC-AP-DUROV-FSB-2026
  - subject: PERSON-PAVEL-DUROV
    predicate: represented_by
    object: PERSON-DAVID-OLIVIER-KAMINSKI
    sources:
      - SRC-FRANCE24-DUROV-KAMINSKI-2024
    notes: France 24/AFP identified Kaminski as Durov's lawyer in the August 2024 French charging episode.
  - subject: PERSON-PAVEL-DUROV
    predicate: related_to
    object: TOPIC-DEVELOPER-SOFTWARE-LIABILITY
    sources:
      - SRC-AP-DUROV-FSB-2026
  - subject: PERSON-PAVEL-DUROV
    predicate: related_to
    object: TOPIC-INTERMEDIARY-LIABILITY
    sources:
      - SRC-AP-DUROV-FSB-2026
last_verified: "2026-07-29"
arrest_date: "2024-08-24"
charge_date: "2024-08-28"
---

# Pavel Durov

## Summary

Pavel Durov is the founder, owner, and CEO of Telegram. OIR documents government criminal and regulatory pressure against him and the platform, including Russia's July 2026 FSB charges alleging facilitation of terrorist activity and France's 2024 platform-moderation investigation.

## Verified Facts

- Telegram's official press page states that Pavel Durov is the founder, owner, and CEO of Telegram, lives in Dubai, and holds dual citizenship of the United Arab Emirates and France.[^1]
- The same press page states that Durov left Russia in 2014 after losing control of his previous company for refusing to hand over data of Ukrainian protesters to security agencies.[^1]
- Associated Press reported on July 29, 2026, that Russian authorities charged Durov with aiding terrorism and that the FSB said it was adding him to international wanted lists.[^2]
- BBC News reported the same day that an international arrest warrant had been issued and that the FSB alleged Telegram failed to remove channels, chats, and bots used by Ukraine.[^3]
- Meduza, citing Interfax, reported that the FSB charged Durov with facilitating terrorist activity under Part 1.1 of Article 205.1 of Russia's Criminal Code and stated he was being placed on an international wanted list.[^4]
- Associated Press reported that if convicted in Russia, Durov could face up to life in prison, and that Durov had earlier accused Russian authorities of fabricating pretexts to restrict Telegram and suppress privacy and free speech.[^2]
- France 24 / AFP reported that in August 2024 French authorities charged Durov over alleged failures to curb illegal content and related platform offenses, and identified David-Olivier Kaminski as his lawyer.[^5]
- Associated Press reported that as of July 29, 2026, the Paris prosecutor's office said Durov remained under formal investigation in France.[^2]
- RFE/RL reported that Durov refused 2017–2018 FSB demands for Telegram encryption keys and that a Moscow court ordered Telegram blocked in April 2018.[^6]

## Historical Context

Durov's public profile combines secure-messaging entrepreneurship with repeated confrontations over compelled access and content moderation. OIR records Russian terrorism-facilitation allegations and French platform charges as contested legal claims reported by reputable outlets, not as proven findings.


[^1]: `SRC-TELEGRAM-PRESS` — Telegram Press Info. Official/self-reported.
[^2]: `SRC-AP-DUROV-FSB-2026` — AP News — Russia Accuses Telegram CEO Pavel Durov of Aiding Terrorism. Secondary reporting.
[^3]: `SRC-BBC-DUROV-FSB-2026` — BBC News — Russia Charges Telegram Founder Pavel Durov with Facilitating Terrorism. Secondary reporting.
[^4]: `SRC-MEDUZA-DUROV-FSB-2026` — Meduza — FSB Accuses Durov of Aiding Terrorism and Issues International Arrest Warrant. Secondary reporting citing Interfax.
[^5]: `SRC-FRANCE24-DUROV-KAMINSKI-2024` — France 24 / AFP — Telegram Boss Durov Charged in France. Secondary reporting.
[^6]: `SRC-RFERL-TELEGRAM-BLOCK-2018` — RFE/RL — Russian Court Orders Telegram App Blocked (2018). Secondary reporting.

## Relevance to Lawsuits Involving Software and Internet Infrastructure

Durov is relevant when analyzing:

- Criminal theories that treat messaging-platform operators as facilitators of user crimes
- Government demands for encryption keys or compelled moderation of wartime communications
- Cross-border arrest warrants and platform-liability pressure against expatriate founders
- Comparative intermediary-liability approaches in Russia, France, and other jurisdictions

See [EVENT-FSB-DUROV-TELEGRAM-2026](../legal/EVENT-FSB-DUROV-TELEGRAM-2026.md) and [ORG-TELEGRAM](../organizations/ORG-TELEGRAM.md).

## Relationships

- `PERSON-PAVEL-DUROV` affiliated_with `ORG-TELEGRAM`.
- `PERSON-PAVEL-DUROV` related_to `EVENT-FSB-DUROV-TELEGRAM-2026`.
- `PERSON-PAVEL-DUROV` represented_by `PERSON-DAVID-OLIVIER-KAMINSKI` (French 2024 proceedings, per AFP/France 24).
- `PERSON-PAVEL-DUROV` related_to `TOPIC-DEVELOPER-SOFTWARE-LIABILITY`.
- `PERSON-PAVEL-DUROV` related_to `TOPIC-INTERMEDIARY-LIABILITY`.

## Sources

1. `SRC-TELEGRAM-PRESS`: Telegram Press Info.
2. `SRC-AP-DUROV-FSB-2026`: AP News — Russia Accuses Telegram CEO Pavel Durov of Aiding Terrorism.
3. `SRC-BBC-DUROV-FSB-2026`: BBC News — Russia Charges Telegram Founder Pavel Durov with Facilitating Terrorism.
4. `SRC-MEDUZA-DUROV-FSB-2026`: Meduza — FSB Accuses Durov of Aiding Terrorism and Issues International Arrest Warrant.
5. `SRC-FRANCE24-DUROV-KAMINSKI-2024`: France 24 / AFP — Telegram Boss Durov Charged in France.
6. `SRC-RFERL-TELEGRAM-BLOCK-2018`: RFE/RL — Russian Court Orders Telegram App Blocked (2018).

## Research Debt

- Locate FSB primary statement and Russian Criminal Code text for Article 205.1 Part 1.1 as applied.
- Create a dedicated French-proceedings event/case page with prosecutor statements and docket identifiers.
- Confirm French arrest calendar date (page uses 2024-08-24 from “late Saturday” before the Wednesday 2024-08-28 charging reported by AFP/France 24).
- Corroborate dual-citizenship and Dubai-residence claims with independent sources beyond Telegram's press page.
- Document Nikolai Durov's role with primary sources if OIR adds a separate person page.
- Identify counsel for the 2026 Russian warrant (if any public representation exists) and any commercial law firms retained by Telegram.
- Evaluate Law.com/other reports naming Dmitry Agranovsky before creating a person page.
