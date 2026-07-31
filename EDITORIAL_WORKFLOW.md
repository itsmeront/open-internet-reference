# Editorial Workflow

OIR is a **Git-first** reference project. Public collaboration should improve accuracy and traceability without bypassing review or turning intake into unverified publication.

The Git repository remains the single source of truth. Generated website output is derived from repository content and must not be edited directly.

## Production Model

**Human-directed, AI-processed, source-bound** (see `PROJECT_CHARTER.md`).

| Stage | Who | Meaning |
| --- | --- | --- |
| Prioritize / highlight intake | Human director | Choose what enters the pipeline |
| Draft pages, sources, links, debt lists | AI (typical) or human | Always `draft`; cite sources; no unsourced model claims |
| Mechanical QA | AI + CI | Metadata, links, IDs, build; **not** truth certification |
| Merge to `main` | Human | **Accept into the draft corpus** — not full verification |
| Research-debt sweeps | Human directs; AI executes | Periodic gap-closing on chosen pages |
| Promote to `verified` | Human deep audit | Scarce; claims checked against cited sources |

Most of the public site is expected to remain `draft`. That is intentional under this model.

## Roles

| Role | Responsibility |
| --- | --- |
| Public reader | Read, search, send intake leads or corrections |
| Contributor | Propose changes on branches; CI must pass |
| AI assistant | Process intake, draft records, mechanical QA, directed debt work |
| Domain expert | Optional deep review in an assigned domain (legal, technical, organizations) |
| Research editor | Prioritize work, merge into draft corpus, set `verified` only after deep source audit |
| Knowledge engineer | Maintain taxonomy, identifiers, relationships, and data model |
| Build engineer | Maintain validation, publishing, and release tooling |
| Architect | Approve structural or schema changes |

## Permission Model

Permissions are enforced through Git hosting (branch protection / rulesets, reviewers, `CODEOWNERS`) and editorial policy. Decap CMS / `/admin/` is an optional intake path that still produces pull requests.

Recommended mapping:

- **Suggest a lead** → web editor, GitHub Issues, or URL handoff for AI processing
- **Propose edits** → pull requests from forks or branches (often AI-authored with human merge)
- **Draft-corpus merge** → human acceptance that sourcing and genre rules are good enough to publish as `draft`
- **Verification** → research editors may set `status: verified` only after a periodic deep source audit
- **Taxonomy changes** → knowledge engineers; require taxonomy audit before merge

**Solo-director ruleset:** require PRs + green `docs`; **required approving reviews = 0** until a second human (or bot-opened PR) can approve. See `.github/BRANCH_PROTECTION.md`. Do not rely on admin bypass for routine merges. Raise approvals to 1 when collaborators join; keep `CODEOWNERS` current for that day.

## Collaboration Plan

### Current practice

- Humans highlight intake and review/merge PRs into the draft corpus.
- AI does most drafting and processing.
- Occasional research-debt campaigns deepen sourcing on pages the director cares about.
- A small verified core grows only when someone deep-checks claims against sources.

### Tooling phases (historical / ongoing)

- **Phase A:** Git-native issues, PR templates, `CODEOWNERS`
- **Phase B:** Taxonomy audits, intake helpers, review dashboards
- **Phase C:** Authenticated admin UI that still produces auditable Git changes (Decap CMS live for intake)

Rules that do not change:

- Suggestions do not change canonical content until merged
- Intake creates candidate or draft work, not a verified-core claim
- No silent path from intake to `verified` without human deep audit
- Taxonomy changes must note affected pages and deprecation plan

## Topics vs Tags

OIR uses two related concepts:

| Concept | Location | Purpose |
| --- | --- | --- |
| **Topic pages** | `knowledge/**/TOPIC-*.md` | Durable entities with IDs, sources, and relationships |
| **Tags** | `TAXONOMY.md` and page `tags:` | Reusable classification labels |

Administrative actions should distinguish:

- **Add topic page** → new `TOPIC-*` record with sources
- **Merge topics** → deprecate one ID, redirect relationships, document in PR
- **Add or merge tag** → update `TAXONOMY.md` and affected page front matter
- **Link document to topic** → add bibliography `SRC-*` and evidence-backed `relationships`

## Intake Rules

Documents proposed for intake are **candidates** until sourced into draft pages and merged.

1. Proposer submits URL, document type, jurisdiction, and relevance (issue, CMS, or direct handoff).
2. AI or editor creates or updates `bibliography/**/SRC-*.md` and related draft knowledge pages.
3. Knowledge pages cite source records; relationships require supporting sources.
4. Human merge accepts the draft into the public corpus.
5. Promotion to `verified` requires a separate deep audit: reverification date and primary or high-confidence source review.

Do not upload confidential, private, or non-public contact information through intake.

## Review Status

Valid `status` values are defined in `DATA_MODEL.md`:

- `draft` — accepted or proposed record; typical public state; **not** a claim of full human verification
- `needs_sources` — missing required sources
- `in_review` — under editorial or deep-audit review
- `verified` — human deep-checked claims against cited sources (scarce verified core)
- `deprecated` — retained for history; do not use for new citations

Research editors should not mark pages `verified` without checking sources, neutrality, and metadata validity. Merge ≠ verified.

## Validation Before Merge

Contributors and reviewers should run local checks before merge:

```powershell
.\.venv\Scripts\python tools\validate_metadata.py
.\.venv\Scripts\python tools\render_brand_assets.py
.\.venv\Scripts\python tools\generate_indexes.py
.\.venv\Scripts\python tools\validate_links.py
.\.venv\Scripts\mkdocs build --strict
```

CI runs the same checks on pull requests. These checks are mechanical QA, not certification that every claim is true.

## Related Documents

- `PROJECT_CHARTER.md`
- `CONTRIBUTING.md`
- `RESEARCH_STANDARDS.md`
- `DATA_MODEL.md`
- `TAXONOMY.md`
- `SOURCE_INTAKE.md`
- `intake/verification-queue.md`
