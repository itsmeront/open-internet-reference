# Editorial Workflow

OIR is a **Git-first** reference project. The repository is the source of truth; the public site is generated from it.

Production model: **[human-directed, AI-processed, source-bound](how-we-work.md)**.

## Pipeline

1. **Human** highlights intake or research-debt work.
2. **AI** (typical) drafts source and knowledge records with citations — status `draft`.
3. **CI / mechanical QA** checks metadata, links, and build (not truth).
4. **Human** merges → accepted into the **draft corpus**.
5. **Occasional human deep audit** may promote a page into the scarce **verified core**.

Merge ≠ verified.

## How to Contribute

| Action | Path |
| --- | --- |
| Send an intake lead | [Suggest Content](suggest.md) / web editor, or GitHub *Propose intake document* |
| Suggest a correction | GitHub Issue → *Suggest an edit* |
| Request topic or tag changes | GitHub Issue → *Topic or taxonomy change* |
| Submit a direct fix | Pull request with validation checks (often AI-authored) |

See `CONTRIBUTING.md` and `EDITORIAL_WORKFLOW.md` in the repository root for full policy.

## Roles

- **Human research editor** — prioritizes work, merges into the draft corpus, deep-audits the verified core, directs debt sweeps.
- **AI assistants** — process intake, draft content, mechanical QA.
- **Contributors** — propose changes on branches (human or AI).
- **Domain experts** — optional deep review in legal, technical, or organization domains.
- **Knowledge engineers** — taxonomy, IDs, and relationships.

Authenticated web editing via Decap CMS (`/admin/`) is an optional intake path that still produces pull requests — not silent database edits.

## Topics vs Tags

- **Topic pages** (`TOPIC-*`) are durable knowledge records with sources and relationships.
- **Tags** in `TAXONOMY.md` classify pages for search and indexes.

Maintainers merge topics, deprecate IDs, and link documents through evidence-backed metadata—not through hand-edited generated pages.

## Status meanings (short)

- `draft` — normal public state after merge
- `verified` — human deep-checked against sources (rare)
- `needs_sources` / `in_review` / `deprecated` — as in research standards

Details: root `EDITORIAL_WORKFLOW.md` and `ROADMAP.md`.
