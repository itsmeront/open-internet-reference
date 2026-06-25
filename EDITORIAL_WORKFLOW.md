# Editorial Workflow

OIR is a **Git-first** reference project. Public collaboration should improve accuracy and traceability without bypassing review or turning intake into unverified publication.

The Git repository remains the single source of truth. Generated website output is derived from repository content and must not be edited directly.

## Roles

| Role | Responsibility |
| --- | --- |
| Public reader | Read, search, suggest corrections |
| Contributor | Propose changes on branches; CI must pass |
| Domain expert | Review and merge changes in an assigned domain (legal, technical, organizations) |
| Research editor | Verify sources, set review status, resolve research debt |
| Knowledge engineer | Maintain taxonomy, identifiers, relationships, and data model |
| Build engineer | Maintain validation, publishing, and release tooling |
| Architect | Approve structural or schema changes |

## Permission Model

OIR does not yet provide an authenticated web CMS. Permissions are enforced through Git hosting (branch protection, reviewers, `CODEOWNERS`) and editorial policy.

Recommended mapping:

- **Suggest only** → GitHub Issues using the templates in `.github/ISSUE_TEMPLATE/`
- **Propose edits** → pull requests from forks or branches
- **Domain merge rights** → code owners or named reviewers for `knowledge/legal/`, `knowledge/technical/`, etc.
- **Verification** → research editors may set `status: verified` only when source requirements are met
- **Taxonomy changes** → knowledge engineers; require taxonomy audit before merge

Configure real reviewers in `.github/CODEOWNERS` before enforcing required reviews on protected branches.

## Phased Collaboration Plan

### Phase A: Git-native collaboration (Sprint 9)

Goal: enable suggestions and structured proposals without a custom admin application.

Deliverables:

- Issue templates for edit suggestions, intake proposals, and taxonomy/topic requests
- Pull request template aligned with validation requirements
- `CODEOWNERS` scaffold for domain review paths
- This workflow document and `CONTRIBUTING.md` cross-links

Rules:

- Suggestions do not change canonical content until merged
- Intake proposals create candidate work, not verified knowledge
- Taxonomy changes must note affected pages and deprecation plan

### Phase B: Editorial tooling on Git (post–v0.1.0)

Goal: make topic maintenance and review assignment easier while keeping Git as canonical storage.

Planned capabilities:

- Taxonomy and topic audit reports (tag usage, orphan topics, duplicate candidates)
- Intake proposal helper that opens a PR or draft file from structured input
- Optional metadata fields for reviewer assignment and review queues
- Generated dashboards that surface assignment and stale verification work

### Phase C: Authenticated admin UI (medium-term)

Goal: administrators and domain experts manage topics, relationships, and intake through a UI that **still produces auditable Git changes**.

Planned capabilities:

- Authenticated admin for taxonomy merge, topic lifecycle, and relationship editing
- Topic browser: related sources, knowledge pages, open research debt
- Intake upload and URL submission with mandatory provenance fields
- All actions create commits or pull requests; CI validation runs before merge
- No silent publish path from intake to `verified` without editor approval

OIR should **not** adopt a database-only CMS that bypasses Git history unless Git remains an export target for audit.

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

Documents proposed for intake are **candidates** until verified.

1. Proposer submits URL, document type, jurisdiction, and relevance via the intake issue template or PR.
2. Editor creates or updates `bibliography/**/SRC-*.md` with appropriate `status`.
3. Knowledge pages cite source records; relationships require supporting sources.
4. Promotion to `verified` requires reverification date and primary or high-confidence source review.

Do not upload confidential, private, or non-public contact information through intake.

## Review Status

Valid `status` values are defined in `DATA_MODEL.md`:

- `draft` — seed or incomplete record
- `needs_sources` — missing required sources
- `in_review` — under editorial review
- `verified` — meets current research standards
- `deprecated` — retained for history; do not use for new citations

Research editors should not mark pages `verified` without checking sources, neutrality, and metadata validity.

## Validation Before Merge

Contributors and reviewers should run local checks before merge:

```powershell
.\.venv\Scripts\python tools\validate_metadata.py
.\.venv\Scripts\python tools\render_brand_assets.py
.\.venv\Scripts\python tools\generate_indexes.py
.\.venv\Scripts\python tools\validate_links.py
.\.venv\Scripts\mkdocs build --strict
```

CI runs the same checks on pull requests.

## Related Documents

- `CONTRIBUTING.md`
- `RESEARCH_STANDARDS.md`
- `DATA_MODEL.md`
- `TAXONOMY.md`
- `SOURCE_INTAKE.md`
- `intake/verification-queue.md`
