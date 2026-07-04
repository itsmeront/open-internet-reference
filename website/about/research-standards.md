# Research Standards

OIR does not present a claim as fact unless it can be independently verified.

## Evidence Labels

- `verified_fact`: directly supported by a cited source.
- `historical_context`: contextual explanation based on cited sources.
- `technical_analysis`: technical interpretation with stated assumptions.
- `legal_analysis`: legal interpretation with jurisdiction and authority level.
- `commentary`: editorial or interpretive material.
- `recommendation`: proposed action or strategy.
- `unverified`: material that requires verification before use.

## Source Preference

Primary sources are preferred whenever available. Legal authorities, official standards, court filings, official publications, archival records, and original technical materials should be used before summaries or commentary.

## Source Reliability

| Tier | Examples | Use |
| --- | --- | --- |
| Primary authority | Court opinions, statutes, RFCs, dockets | Best support for legal and technical claims |
| Official record | Contact pages, annual reports, faculty pages | Good for role, mission, and contact data |
| Self-reported profile | Staff bios, about pages, firm bios | First source only; corroborate before `verified` |
| Secondary reporting | Journalism, scholarship, case summaries | Corroborate biography and impact claims |
| Tertiary summary | Wikipedia, snippets, uncited AI | Not sufficient alone |

Staff biographies and “about us” pages are useful for orientation but are **self-reported**. Pages that rely on them should stay in `draft` until independent sources confirm major claims, and should list what is still needed under **Research Debt**.

## Per-Claim Footnotes

Every bullet in **Verified Facts** must cite a source with a Markdown footnote:

```markdown
- Example fact supported by a source.[^1]

[^1]: `SRC-EXAMPLE` — Source title. Reliability note.
```

See `CITATION_GUIDE.md` and `RESEARCH_STANDARDS.md` in the repository root for complete rules.

## Review Status

- `draft` — not ready for use as reference material.
- `needs_sources` — missing adequate evidence.
- `in_review` — editorial or technical review underway.
- `verified` — claims checked against cited sources; biography-only gaps resolved or flagged.
- `deprecated` — retained for history only.
