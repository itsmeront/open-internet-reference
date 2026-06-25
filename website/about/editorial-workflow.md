# Editorial Workflow

OIR is a **Git-first** reference project. The repository is the source of truth; the public site is generated from it.

## How to Contribute

| Action | Path |
| --- | --- |
| Suggest a correction | GitHub Issue → *Suggest an edit* (after repo is on GitHub) |
| Propose a document for intake | GitHub Issue → *Propose intake document* |
| Request topic or tag changes | GitHub Issue → *Topic or taxonomy change* |
| Submit a direct fix | Pull request with validation checks |

See `CONTRIBUTING.md` and `EDITORIAL_WORKFLOW.md` in the repository root for full policy.

## Roles

- **Contributors** propose changes on branches.
- **Domain experts** review merges in legal, technical, or organization domains.
- **Research editors** verify sources and review status.
- **Knowledge engineers** maintain taxonomy, IDs, and relationships.

Authenticated web editing is **planned** (Sprint 9). Near-term collaboration uses GitHub Issues and pull requests. Medium-term admin tooling will produce **commits or PRs**, not silent database edits.

## Topics vs Tags

- **Topic pages** (`TOPIC-*`) are durable knowledge records with sources and relationships.
- **Tags** in `TAXONOMY.md` classify pages for search and indexes.

Maintainers merge topics, deprecate IDs, and link documents through evidence-backed metadata—not through hand-edited generated pages.

## Sprint 9 Phases

1. **Phase A (Git-native)** — issue templates, PR template, code owners scaffold
2. **Phase B (tooling)** — taxonomy audits, intake helpers, review assignment dashboards
3. **Phase C (admin UI)** — authenticated topic administration that still flows through Git

Details: `ROADMAP.md` Sprint 9 and `EDITORIAL_WORKFLOW.md`.
