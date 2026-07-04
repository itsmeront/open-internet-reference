# Research Standards

## Core Rule

Do not present a claim as fact unless it can be independently verified.

## Evidence Classes

Use the following labels when drafting and reviewing knowledge pages:

- `verified_fact`: directly supported by a cited source.
- `historical_context`: contextual explanation based on cited sources.
- `technical_analysis`: technical interpretation that should identify assumptions and source material.
- `legal_analysis`: legal interpretation that should identify jurisdiction, authority level, and limits.
- `commentary`: editorial or interpretive material, clearly separated from factual claims.
- `recommendation`: proposed action or strategy, clearly separated from analysis.
- `unverified`: material that requires verification before being used as support.

## Source Preference

Prefer sources in this order:

1. Primary legal authorities, official standards, official publications, court filings, and archival records.
2. Peer-reviewed scholarship, books from reputable publishers, and official organizational publications.
3. Reputable journalism and expert commentary.
4. Secondary summaries and tertiary references.

Do not rely on unsourced AI output as evidence.

## Source Reliability

Not all cited sources carry the same weight. Classify sources when drafting and reviewing:

| Tier | Examples | How to use |
| --- | --- | --- |
| **Primary authority** | Court opinions, statutes, regulations, RFCs, docket filings, official government records | Preferred support for legal, technical, and historical claims. |
| **Official record** | Organization contact pages, annual reports, press releases, institutional faculty pages | Good for current role, address, and stated mission; still check date and scope. |
| **Self-reported profile** | Staff biographies, “about us” pages, firm attorney bios, LinkedIn summaries | Useful for intake and orientation, but treat career and impact claims as **uncorroborated** until supported elsewhere. |
| **Secondary reporting** | Reputable journalism, books, peer-reviewed scholarship, amicus briefs, case pages | Use to corroborate biography claims and major litigation involvement. |
| **Tertiary summary** | Wikipedia, search snippets, uncited AI output | Do not use as sole support for factual claims. |

### Rules for self-reported sources

Staff biographies and organization “about” pages are **self-reported**. They are acceptable as a first source, but:

- Do **not** mark a page `verified` when significant claims rely only on a biography or about page.
- Add **research debt** naming the independent sources still needed (institutional profile, court docket, case page, reputable journalism).
- Prefer a second source for litigation roles, landmark cases, awards, and quantitative claims.

## Per-Claim Citations

Every bullet in **Verified Facts** (and every significant bullet in **Historical Context**) must cite at least one source with a Markdown footnote.

Format:

```markdown
## Verified Facts

- Jameel Jaffer is the inaugural executive director of the Knight First Amendment Institute.[^1]
- At the ACLU, he co-led litigation that compelled disclosure of the Bush administration torture memos.[^1]

[^1]: `SRC-JAFFER-KNIGHT` — Jameel Jaffer Knight Institute Biography. Self-reported staff biography; corroboration pending.
```

Rules:

- One footnote label may support multiple facts when the same source supports each claim.
- Use different footnote labels when facts come from different sources.
- Place footnote definitions immediately after the section they support, before the next `##` heading.
- The footnote definition must include the source ID in backticks and the source title.
- Add a short reliability note when the source is self-reported or otherwise limited.
- The page-level **Sources** section lists every source on the page; number footnoted sources to match footnote labels (`1.` = `[^1]`, `2.` = `[^2]`).

A page may move to `verified` only when significant claims are checked against cited sources and biography-only claims either have corroboration or remain explicitly flagged in research debt.

## Case and Statute Mentions

When a knowledge page mentions a court case or formal legal proceeding by name in **Verified Facts** or **Historical Context**:

1. **If a `CASE-*` page exists**, link to it and cite a primary source (court opinion, docket, or case page) in a footnote — not only a biography.
2. **If no `CASE-*` page exists yet**, add a **Research Debt** item to create the case page and source record, or to link an existing primary source.
3. Do not leave case names as unsupported prose, especially when the claim involves attorney participation, holdings, or outcomes.

Example:

```markdown
- Fallow represented video game makers in challenges culminating in [Brown v. Entertainment Merchants Assn.](knowledge/legal/CASE-BROWN-V-ENTERTAINMENT-MERCHANTS.md) (*EMA v. Brown*).[^2]

[^2]: `SRC-BROWN-V-EMA-LII` — Brown v. Entertainment Merchants Assn., 564 U.S. 786 (2011) (Cornell LII). Primary authority.
```

Use `python tools/audit_case_mentions.py` to find unlinked case mentions across knowledge pages.

## Verification Rules

- Record the source for every significant factual claim with a footnote.
- Record the access date for web sources.
- Quote only from sources that have been directly reviewed.
- Preserve uncertainty instead of forcing confidence.
- Mark unclear provenance as research debt.
- Do not invent people, organizations, cases, citations, quotations, relationships, contact information, or dates.

## Review Status

Each knowledge page should use one of these statuses:

- `draft`: created but not ready for use as reference material.
- `needs_sources`: useful outline, but missing adequate evidence.
- `in_review`: undergoing editorial or technical review.
- `verified`: claims have been checked against cited sources.
- `deprecated`: retained for history but no longer recommended.

## Research Debt

Research debt should be tracked explicitly when:

- A claim has insufficient source support.
- A claim relies only on a self-reported biography or about page and needs independent corroboration.
- Major litigation, policy, or technical impact claims need dockets, case pages, or secondary reporting.
- A better primary source likely exists.
- A citation needs a stable URL, archive URL, or official reporter reference.
- Per-fact footnotes need manual review to confirm the correct source mapping.
- A relationship is plausible but not yet evidence-backed.
- A page needs domain expert review.
