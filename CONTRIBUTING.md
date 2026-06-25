# Contributing to Open Internet Reference

Thank you for helping build a comprehensive, independently verifiable knowledge base for digital rights and software freedom.

## Ways to Contribute

### 1. Suggest a Correction (no Git required)

If you notice an error, outdated information, or broken link:

- [Open a "Suggest an edit" issue](../../issues/new?template=suggest-edit.yml) on GitHub
- Describe what's wrong and what the correct information should be
- Include sources for your correction if possible

### 2. Propose New Content (no Git required)

To propose a new organization, lawyer, case, or topic:

- [Open an "Intake proposal" issue](../../issues/new?template=intake-document.yml) on GitHub
- Provide the document URL, type, relevance, and any provenance information
- A research editor will review and create appropriate records

### 3. Submit a Direct Edit (Git workflow)

For contributors comfortable with Git:

1. Fork the repository
2. Create a branch: `git checkout -b your-change-description`
3. Make your changes following the standards below
4. Run validation: `python tools/validate_metadata.py`
5. Submit a pull request

### 4. AI-Assisted Contributions

AI agents can contribute through the same workflows:

- AI-generated content must be submitted as pull requests
- AI commits must use a distinguishable Git author (e.g., `OIR-AI <ai@oir.example>`)
- AI-generated content starts as `draft` status — never directly `verified`
- AI content must include source references (not just training data claims)
- Human review is required before any AI contribution is merged

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

CI will run these checks automatically on your pull request.

## Review Process

1. **Automated checks** — CI validates metadata, links, and site build
2. **Domain review** — domain experts review content in their area (legal, technical, organizations)
3. **Research verification** — research editors check sources before status changes
4. **Merge** — approved PRs are merged to main; site regenerates automatically

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
| `needs-review` | Awaiting domain expert review |
| `needs-sources` | Content needs better source references |
| `research-debt` | Tracking unresolved verification work |

## Questions?

See `EDITORIAL_WORKFLOW.md` for the full editorial process, or open a discussion issue.
