---
id: TECH-TORNADO-CASH
title: Tornado Cash (Ethereum Mixer Protocol)
type: technology
status: draft
summary: Tornado Cash is an open-source Ethereum smart-contract protocol that pools and shuffles cryptocurrency deposits so withdrawals can be made to different addresses, reducing on-chain linkability between deposit and withdrawal.
tags:
  - technology
  - privacy-preserving-systems
  - censorship-resistance
  - open-source-software
  - tornado-cash
  - case-studies
sources:
  - SRC-VAN-LOON-5TH-CIR-JUSTIA
  - SRC-OFAC-FAQ-1076
  - SRC-TREASURY-TC-AUG-2022
relationships:
  - subject: TECH-TORNADO-CASH
    predicate: cites
    object: SRC-VAN-LOON-5TH-CIR-JUSTIA
    sources:
      - SRC-VAN-LOON-5TH-CIR-JUSTIA
  - subject: TECH-TORNADO-CASH
    predicate: related_to
    object: TOPIC-TORNADO-CASH
    sources:
      - SRC-VAN-LOON-5TH-CIR-JUSTIA
  - subject: TECH-TORNADO-CASH
    predicate: related_to
    object: CASE-VAN-LOON-V-TREASURY
    sources:
      - SRC-VAN-LOON-5TH-CIR-JUSTIA
last_verified: "2026-07-23"
---

# Generated Source Mirror

This page is generated from the source Markdown file so it can be viewed inside the MkDocs site.

- Source path: `knowledge/technical/TECH-TORNADO-CASH.md`
- Source ID: `TECH-TORNADO-CASH`
- [**Edit this page**](https://github.com/itsmeront/open-internet-reference/edit/main/knowledge/technical/TECH-TORNADO-CASH.md) | [**Suggest a change**](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml&title=Edit+suggestion:+TECH-TORNADO-CASH)

!!! info "📝 Page Status: Draft — sourced but not yet reviewed"

    - **Status**: `draft`
    - **Sources**: 3
    - **Relationships**: 3
    - **Research debt items**: 3
    - **Last verified**: 2026-07-23

---

# Tornado Cash (Ethereum Mixer Protocol)

## Summary

Tornado Cash is an open-source Ethereum smart-contract protocol that pools and shuffles cryptocurrency deposits so withdrawals can be made to different addresses, reducing on-chain linkability between deposit and withdrawal.

## Verified Facts

- The Fifth Circuit describes Tornado Cash as a decentralized, open-source software project whose contributors uploaded smart contracts to the Ethereum blockchain in 2019, including both mutable and immutable smart contracts that are open-source and stored on Ethereum.[^1]
- The Fifth Circuit describes Tornado Cash pool smart contracts as collecting, pooling, and shuffling cryptocurrencies deposited by many users; depositors receive credentials entitling withdrawal of the same amount, including to a different wallet, severing the public link between deposit and withdrawal addresses.[^1]
- The Fifth Circuit states that the mixing process occurs automatically with no human intervention, and that anonymity depends on a critical mass of concurrent users.[^1]
- The Fifth Circuit distinguishes mutable smart contracts (managed and changeable) from immutable smart contracts (cannot be altered or removed; conversion to immutable is irreversible).[^1]
- The Fifth Circuit states that immutable Tornado Cash crypto-mixing smart contracts are unownable, uncontrollable, and unchangeable—even by their creators.[^1]
- Treasury’s August 8, 2022 press release states Tornado Cash had been used to launder more than $7 billion worth of virtual currency since its creation in 2019, including over $455 million stolen by the Lazarus Group in what Treasury described as the largest known virtual currency heist to date at that time.[^2]
- OFAC FAQ 1076 states that SDN identifiers for Tornado Cash included certain virtual currency wallet addresses and the URL for Tornado Cash’s website, that the website had been deleted from the Internet but remained available through certain archives, and that interacting with open-source code itself in a way that does not involve a prohibited transaction with Tornado Cash is not prohibited (including copying code and making it available online, discussing it, teaching about it, or including it in academic materials, absent additional facts).[^3]

## Historical Context

Tornado Cash smart contracts were deployed on Ethereum beginning in 2019. In 2022, OFAC designated Tornado Cash and listed associated addresses and the project website URL. Intermediary access paths (such as the website identified by OFAC) were disrupted while, per the Fifth Circuit’s description, immutable contracts remained unalterable on-chain.


[^1]: [`SRC-VAN-LOON-5TH-CIR-JUSTIA`](../../../bibliography.md#SRC-VAN-LOON-5TH-CIR-JUSTIA) — Van Loon v. Department of the Treasury, No. 23-50669 (5th Cir. Nov. 26, 2024) (Justia). Primary authority for technical description used by the court.
[^2]: [`SRC-TREASURY-TC-AUG-2022`](../../../bibliography.md#SRC-TREASURY-TC-AUG-2022) — U.S. Treasury Sanctions Notorious Virtual Currency Mixer Tornado Cash (Aug. 8, 2022). Official government press release.
[^3]: [`SRC-OFAC-FAQ-1076`](../../../bibliography.md#SRC-OFAC-FAQ-1076) — OFAC FAQ 1076 — Prohibitions Resulting from Tornado Cash Designation. Official OFAC FAQ.

## Technical Analysis

Assumptions: This page relies on the Fifth Circuit’s technical primer and OFAC/Treasury descriptions rather than an independent code audit. Ethereum smart contracts execute according to deployed bytecode; immutability, as used in Van Loon, means no party can update or remove the contract after it is made immutable. Mixer anonymity is probabilistic and depends on pool size and user behavior. Distribution and user-interface layers (repositories, DNS, frontends, RPC providers, issuer-controlled tokens) are distinct from on-chain contract execution and may be controlled by intermediaries even when contracts remain callable.

## Relationships

- `TECH-TORNADO-CASH` cites [`SRC-VAN-LOON-5TH-CIR-JUSTIA`](../../../bibliography.md#SRC-VAN-LOON-5TH-CIR-JUSTIA).
- `TECH-TORNADO-CASH` related_to `TOPIC-TORNADO-CASH`.
- `TECH-TORNADO-CASH` related_to `CASE-VAN-LOON-V-TREASURY`.

## Sources

1. [`SRC-VAN-LOON-5TH-CIR-JUSTIA`](../../../bibliography.md#SRC-VAN-LOON-5TH-CIR-JUSTIA): Van Loon v. Department of the Treasury, No. 23-50669 (5th Cir. Nov. 26, 2024) (Justia).
2. [`SRC-TREASURY-TC-AUG-2022`](../../../bibliography.md#SRC-TREASURY-TC-AUG-2022): U.S. Treasury Sanctions Notorious Virtual Currency Mixer Tornado Cash (Aug. 8, 2022).
3. [`SRC-OFAC-FAQ-1076`](../../../bibliography.md#SRC-OFAC-FAQ-1076): OFAC FAQ 1076 — Prohibitions Resulting from Tornado Cash Designation.

## Research Debt

- Add primary source materials for GitHub account/repository suspensions and Circle USDC blacklisting (issuer/on-chain events or official statements).
- Add contract addresses and immutability proofs from Ethereum explorers or project releases with archival URLs.
- Relate to `PROTOCOL-TCP` and network-layer censorship literature only after evidence-backed comparison sources are added.
