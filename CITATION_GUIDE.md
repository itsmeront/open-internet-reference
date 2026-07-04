# Citation Guide

## Purpose

Citations make OIR independently verifiable. Every significant factual claim, quotation, legal proposition, relationship, and timeline entry should be traceable to a source.

## Minimum Source Record

Each source record should capture:

- Permanent identifier
- Title
- Author or issuing body
- Publication date, decision date, or effective date
- Source type
- URL, reporter citation, docket number, ISBN, DOI, RFC number, or archival identifier
- Access date for web sources
- Notes about reliability, provenance, or limitations

## Source Identifiers

Use stable identifiers with type prefixes:

- `SRC-` for general source records
- `CASE-` for court cases
- `STAT-` for statutes
- `REG-` for regulations
- `RFC-` for RFCs
- `STD-` for technical standards
- `PAPER-` for academic papers
- `BOOK-` for books

Examples:

- `CASE-BERNSTEIN`
- `STAT-DMCA`
- `RFC-8446`
- `PAPER-KADEMLIA`

## Web Sources

For web sources:

- Prefer official URLs.
- Record the access date.
- Add an archive URL when available.
- Avoid relying on snippets, summaries, or search results.

## Quotations

Only quote text that has been directly checked. Preserve exact wording, spelling, capitalization, and punctuation unless using clearly marked brackets or ellipses.

## Legal Citations

Legal citations should prefer official reporters, docket records, statutory citations, regulatory citations, or official court PDFs where available. Summaries may be useful for context, but they should not replace primary authority.

## Per-Claim Footnotes

Knowledge pages must tie each **Verified Facts** bullet to at least one source using [MkDocs footnotes](https://squidfunk.github.io/mkdocs-material/reference/footnotes/).

### Footnote format

```markdown
- The Ninth Circuit held that source code is expressive speech protected by the First Amendment.[^1]

[^1]: `SRC-BERNSTEIN-JUSTIA` — Bernstein v. DOJ Court Opinion (Justia). Primary legal authority.
```

```markdown
- The official ACLU biography describes Granick as surveillance and cybersecurity counsel.[^1]

[^1]: `SRC-GRANICK-ACLU-BIO` — Jennifer Granick ACLU Staff Biography. Self-reported staff biography; corroboration pending.
```

### Reliability notes in footnotes

Append a brief reliability note after the source title when relevant:

- **Primary legal authority** — court opinion, statute, RFC, or official record.
- **Official organizational record** — contact page, annual report, institutional page.
- **Self-reported staff biography** — add “corroboration pending”.
- **Self-reported about page** — add “corroboration pending”.
- **Secondary reporting** — name the outlet or publication type when helpful.

### When a second source is required

Add research debt (and keep page status at `draft` or `needs_sources`) when claims like these appear with only a biography or about page:

- Lead counsel or argued-before-the-Supreme-Court roles
- Landmark case involvement
- Forced a policy or program change
- Awards, rankings, or “first” / “only” claims
- Quantitative impact statements

### Case and statute mentions

When Verified Facts or Historical Context name a case (for example, *EMA v. Brown* or *Carpenter v. United States*):

- Link to the corresponding `CASE-*` page when it exists.
- Footnote a primary case source (`SRC-*` opinion, docket, or official case page), not only the biography that mentions the case.
- If no case page exists, add research debt: `Create CASE-* page and primary source for [case name].`

Run `python tools/audit_case_mentions.py` to audit knowledge pages for unlinked case mentions.

### Source list vs footnotes

- **Footnotes** — per-claim support inside Verified Facts and Historical Context.
- **Sources section** — full bibliography for the page.
- **Front matter `sources:`** — machine-readable list used by indexes and the relationship graph.
