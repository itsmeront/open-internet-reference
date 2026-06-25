# Contributing

OIR is an evidence-first reference project. Contributions should improve accuracy, traceability, clarity, or maintainability.

## Contribution Rules

- Do not add unsourced factual claims.
- Prefer primary sources.
- Mark uncertainty explicitly.
- Keep legal analysis separate from legal advice.
- Keep commentary separate from verified facts.
- Do not manually edit generated artifacts in `generated/`.
- Run validation before submitting substantial changes.

## New Knowledge Pages

When adding a knowledge page:

1. Start from `knowledge/_templates/knowledge-page.md`.
2. Assign a durable identifier using `DATA_MODEL.md`.
3. Add front matter.
4. Add sources for significant claims.
5. Add relationships only when evidence-backed.
6. Record research debt for unresolved questions.

## Development Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .[docs]
python tools/validate_metadata.py
mkdocs serve
```

## Review Expectations

Review should check:

- Source quality
- Citation accuracy
- Neutrality
- Metadata validity
- Cross-link integrity
- Clear separation of fact, analysis, commentary, and recommendations

## Collaboration Without Direct Edit Access

You do not need write access to help improve OIR.

- **Suggest an edit** → open a GitHub Issue using the *Suggest an edit* template (after the repository is published on GitHub).
- **Propose intake** → use the *Propose intake document* issue template.
- **Topic or taxonomy change** → use the *Topic or taxonomy change* issue template.
- **Submit a fix** → open a pull request; the PR template lists validation checks.

Roles, permissions, intake rules, and the phased plan for authenticated admin tooling are documented in `EDITORIAL_WORKFLOW.md`.

Domain experts may receive merge rights on paths such as `knowledge/legal/` or `knowledge/technical/` via `.github/CODEOWNERS` once maintainers configure them.
