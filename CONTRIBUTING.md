# Contributing to Open Internet Reference

Thank you for helping build a comprehensive, independently verifiable knowledge base for digital rights and software freedom.

**How OIR works:** human-directed, AI-processed, source-bound. See `PROJECT_CHARTER.md` and `EDITORIAL_WORKFLOW.md`. Most merged pages remain `draft` (accepted into the draft corpus). `verified` is scarce and requires a human deep source audit. Public suggestions are **leads for processing**, not a volunteer editing obligation.

## Ways to Contribute

### 1. Send an intake lead (preferred for most people)

Point at a URL, organization, case, or error — you do not need to rewrite pages:

- Web editor: [openinternetresearch.com/admin/](https://openinternetresearch.com/admin/) (log into GitHub in the same browser first)
- [Intake proposal issue](https://github.com/itsmeront/open-internet-reference/issues/new?template=intake-document.yml)
- [Suggest an edit issue](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml)

AI usually processes the lead into draft records; a human merges accepted work into the draft corpus.

### 2. Submit a Direct Edit (Git workflow)

For contributors comfortable with Git:

1. Fork the repository
2. Create a branch: `git checkout -b your-change-description`
3. Make your changes following the standards below
4. Run validation: `python tools/validate_metadata.py`
5. Submit a pull request

### 3. AI-Assisted Contributions (primary labor path)

AI agents do most drafting and mechanical QA:

- AI-generated content must be submitted as pull requests
- AI commits must use a distinguishable Git author (e.g., `OIR-AI <ai@oir.example>`)
- AI-generated content starts as `draft` status — never directly `verified`
- AI content must include source references (not training-data claims as facts)
- Prefer facts + citations; keep interpretation in labeled analysis/commentary sections
- Human review is required before merge (**draft-corpus acceptance**, not automatic verification)
- Labels: `ai-generated` when applicable

## Content Standards

### Required for Knowledge Pages

Every knowledge page must have:

- YAML front matter with all required fields (see `DATA_MODEL.md`)
- A valid ID with the correct prefix (e.g., `CASE-`, `ORG-`, `PERSON-`)
- At least one source reference
- Status set to `draft` for new content
- A `## Research Debt` section listing anything you couldn't verify

### Evidence Rules

- Every significant factual claim must cite a source
- Prefer primary sources (court opinions, official pages, RFCs)
- Do not present AI-generated claims as verified facts
- Do not rely on unsourced AI output as evidence
- Mark uncertain information as research debt
- See `RESEARCH_STANDARDS.md` for full guidelines

### Validation

Before submitting, run:

```bash
python tools/validate_metadata.py    # Check metadata
python tools/validate_links.py       # Check local links
python tools/generate_indexes.py     # Regenerate indexes
mkdocs build --strict                # Build site
```

CI will run these checks automatically on your pull request. CI is mechanical QA, not truth certification.

## Review Process

1. **Automated checks** — CI validates metadata, links, and site build
2. **Human merge review** — accept into the **draft corpus** when sourcing and genre rules look sound
3. **Optional domain deep review** — when available for legal, technical, or organization domains
4. **Verified-core audit** — separate, periodic human check before `status: verified`
5. **Site publish** — merged `main` regenerates the public site

## What NOT to Submit

- Confidential or non-public contact information
- Unverified claims presented as facts
- Content copied verbatim from copyrighted sources without fair use justification
- Personal opinions not clearly labeled as commentary
- Content that bypasses the review process

## Labels

| Label | Meaning |
|---|---|
| `ai-generated` | Content was created by an AI agent |
| `needs-review` | Awaiting domain expert or director review |
| `needs-sources` | Content needs better source references |
| `research-debt` | Tracking unresolved verification work |

## Questions?

See `EDITORIAL_WORKFLOW.md` for the full editorial process, or open a discussion issue.
