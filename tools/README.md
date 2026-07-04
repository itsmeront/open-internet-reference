# Tools

This directory contains repository maintenance, validation, publishing, and export tools.

Current tools:

- `validate_metadata.py`: checks Markdown front matter in OIR content directories.
- `validate_links.py`: checks local Markdown links in authored documentation.
- `add_fact_citations.py`: adds per-claim footnotes and corroboration research debt to knowledge pages.
- `audit_case_mentions.py`: flags unlinked case mentions and adds research debt for missing `CASE-*` pages.
- `generate_indexes.py`: generates JSON exports and MkDocs pages under `generated/` and `website/generated/`.
- `moderation_queue.py`: builds the moderation dashboard (open PRs, draft content, stale verifications).
- `taxonomy_audit.py`: audits tag usage against `TAXONOMY.md` (orphans, undeclared tags, duplicates).
- `render_brand_assets.py`: rasterizes favicon assets from `website/assets/images/oir-logo-mark.svg`.
- `serve.py`: renders brand assets, regenerates indexes, and starts MkDocs local preview.

## Editorial report tools

`moderation_queue.py` and `taxonomy_audit.py` write both human-readable MkDocs pages and JSON exports:

| Tool | Markdown page | JSON export |
|------|---------------|-------------|
| `moderation_queue.py` | `website/generated/moderation.md` | `generated/moderation-queue.json` |
| `taxonomy_audit.py` | `website/generated/taxonomy-audit.md` | `generated/taxonomy-audit.json` |

Local usage:

```powershell
python tools/moderation_queue.py
python tools/taxonomy_audit.py
```

`moderation_queue.py` uses the GitHub CLI (`gh`) when available to list open pull requests. Set `GH_TOKEN` (or run `gh auth login`) for private repos or richer PR metadata.

JSON-only output:

```powershell
python tools/moderation_queue.py --json
python tools/taxonomy_audit.py --json
```

### CI and automation

These reports are regenerated in two places:

1. **Every validate build** (`.github/workflows/validate.yml`) — runs before `mkdocs build --strict`, so CI and published site builds always use fresh report data even if committed copies on `main` are slightly stale.
2. **Daily schedule** (`.github/workflows/moderation-reports.yml`) — runs at 06:00 UTC (or on manual `workflow_dispatch`) and opens/updates a pull request on branch `automated/moderation-reports` when report files change.

Because `main` is branch-protected (PR-only merges), the scheduled workflow **does not push directly to `main`**. Merge the automation PR when convenient, or configure a ruleset bypass — see `.github/BRANCH_PROTECTION.md` → *Automated Workflows and Branch Protection*.

The Node.js version notice in Actions logs (`actions/checkout`, `actions/setup-python` targeting Node 20 on Node 24 runners) is a deprecation warning only; it does not fail the workflow.

Local preview:

```powershell
.\.venv\Scripts\python tools\serve.py
```

Skip regeneration when indexes are already current:

```powershell
.\.venv\Scripts\python tools\serve.py --skip-generate
```

Typical validation workflow before publishing:

```powershell
.\.venv\Scripts\python tools\validate_metadata.py
.\.venv\Scripts\python tools\render_brand_assets.py
.\.venv\Scripts\python tools\generate_indexes.py
.\.venv\Scripts\python tools\moderation_queue.py
.\.venv\Scripts\python tools\taxonomy_audit.py
.\.venv\Scripts\python tools\validate_links.py
.\.venv\Scripts\mkdocs build --strict
```
