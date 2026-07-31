# Branch Protection Configuration

This document describes branch protection for the `main` branch of
`itsmeront/open-internet-reference`.

GitHub options:

- **Branch Rulesets** (recommended) — newer, more flexible
- **Classic Branch Protection Rules** — legacy

Active ruleset name in this repo: **Project Main**.

---

## Solo-director policy (current)

OIR is [human-directed, AI-processed](../EDITORIAL_WORKFLOW.md). One human director
prioritizes work and merges into the draft corpus. GitHub **does not allow you to
approve your own pull request**, so requiring 1 approving review forces constant
admin bypass.

**While solo, do not require approving reviews.** Keep the audit trail via PRs + CI.

| Gate | Solo director | When collaborators join |
|------|---------------|-------------------------|
| Require pull request before merging | ✅ | ✅ |
| Required approving reviews | **0** | **1** (and optionally require code owners) |
| Status check `docs` must pass | ✅ | ✅ |
| Require conversation resolution | ✅ (optional but useful) | ✅ |
| Admin bypass | Emergencies / automation only | Emergencies only |

Director review still happens: open the PR, read the diff, merge when satisfied.
That merge is **draft-corpus acceptance**, not a second-person Approve click.

### Optional later: AI opens the PR

If a GitHub App / bot opens the PR under a different identity, the human director
*can* click Approve. Restore `Required approvals = 1` when that path is reliable
or when a second human reviewer exists.

---

## Option A: Branch Rulesets (Recommended)

### Live ruleset: update Project Main

1. Open https://github.com/itsmeront/open-internet-reference/settings/rules
2. Click the ruleset **Project Main** (or create one named `Protect main` if missing)
3. Enforcement: **Active**
4. Target: **Include default branch**
5. Bypass list: **Repository admin** — keep for emergencies and automation edge cases; do **not** rely on it for every merge

### Rules to enable (solo director)

| Rule | Configuration | Rationale |
|------|---------------|-----------|
| **Restrict deletions** | ✅ | Never delete main |
| **Require a pull request before merging** | ✅ | All changes go through a PR |
| → Required approvals | **0** | Solo director cannot self-approve; avoid ritual bypass |
| → Dismiss stale pull request approvals when new commits are pushed | ✅ (harmless at 0; ready when raising to 1) | |
| → Require conversation resolution before merging | ✅ | Resolve threads before merge |
| → Require review from code owners | ❌ while solo | Enable with approvals = 1 when collaborators exist |
| → Require approval of the most recent reviewable push | ❌ while solo | Enable when adding collaborators |
| **Require status checks to pass** | ✅ | CI validation must succeed |
| → Status checks (add) | `docs` | Job name from `.github/workflows/validate.yml` |
| → Require branches be up to date | ✅ | Prevent merge conflicts |
| **Block force pushes** | ✅ | Never force-push to main |

### Step-by-step (create from scratch)

1. Go to https://github.com/itsmeront/open-internet-reference/settings/rules
2. Click **"New branch ruleset"** (or edit **Project Main**)
3. Name: `Protect main` or keep `Project Main`
4. Enforcement: **Active**
5. Target branches → **Include default branch**
6. Bypass list → Repository admin (emergencies)
7. Enable the rules in the table above — set **Required approvals** to **0**
8. Save / Update

### When you add collaborators

1. Edit the ruleset
2. Set **Required approvals** to **1**
3. Optionally enable **Require review from code owners**
4. Stop using admin bypass for routine merges

---

## Option B: Classic Branch Protection Rules (Legacy)

**Settings → Branches → Add classic branch protection rule**

Branch name pattern: `main`

| Setting | Solo director | With collaborators |
|---------|---------------|--------------------|
| Require a pull request before merging | ✅ | ✅ |
| Required approvals | **0** | **1** |
| Dismiss stale reviews on new pushes | ✅ | ✅ |
| Require review from code owners | ❌ | ✅ |
| Require status checks to pass | ✅ (`docs`) | ✅ |
| Require branches to be up to date | ✅ | ✅ |
| Require conversation resolution | ✅ | ✅ |
| Require linear history | ❌ | optional |
| Include administrators | ❌ | ❌ (bypass only in emergencies) |
| Allow force pushes | ❌ | ❌ |
| Allow deletions | ❌ | ❌ |

---

## Label-based Moderation Workflow

The moderation system uses labels to route PRs:

- `moderation/pending` — PR is in the moderation queue (auto-applied)
- `moderation/approved` — PR has been reviewed and approved
- `moderation/changes-requested` — reviewer requested changes
- `ai-generated` — auto-applied when commit author matches AI patterns
- `needs-review` — applied to all new PRs via the labeling workflow
- `area/*` — content area labels (auto-applied based on changed files)

`moderation/approved` is an editorial signal. Under the solo-director ruleset it is
**not** a GitHub merge requirement.

## Required Status Checks

When configuring status checks, add:

| Check name | Source |
|------------|--------|
| `docs` | `.github/workflows/validate.yml` — validates metadata, links, site build |
| `label-and-triage` | `.github/workflows/moderation.yml` — applies labels |

The `stale-check` job is informational only and should **not** be required
(it only runs on PR open events and reports warnings).

## Automated Workflows and Branch Protection

The **Generate Moderation Reports** workflow (`.github/workflows/moderation-reports.yml`)
updates report files on a daily schedule. Because `main` requires pull requests,
that workflow **cannot push directly to `main`**. It pushes to branch
`automated/moderation-reports` and then tries to open or update an automation PR.

### If Actions cannot create pull requests

GitHub may return:

> GitHub Actions is not permitted to create or approve pull requests.

That means the repository (or organization) has not allowed `GITHUB_TOKEN` to open PRs.
The scheduled workflow still **pushes the report branch** and succeeds; only the
automatic PR step is skipped. Open a PR manually:

https://github.com/itsmeront/open-internet-reference/compare/main...automated/moderation-reports?expand=1

To allow fully automated PRs:

1. Repo **Settings → Actions → General → Workflow permissions**
2. Enable **Allow GitHub Actions to create and approve pull requests**
3. On organization-owned repos, an org owner may need to allow this under **Organization settings → Actions → General** first

Merge automation PRs when convenient, or add one of these bypass options:

| Option | When to use |
|--------|-------------|
| **Merge automation PRs** | Default — keeps human review on all `main` changes |
| **Ruleset bypass for the workflow** | Hands-off daily updates; add *Generate Moderation Reports* to the ruleset bypass list |
| **Ruleset bypass for `github-actions[bot]`** | Broadest — allows any Actions bot push (use with care) |

Fresh copies of the reports are also regenerated during the `docs` CI job before
each MkDocs build, so published site builds stay current even before automation
PRs are merged.

## Verifying It Works

After the solo-director configuration:

1. Create a test branch and PR authored by the director
2. Confirm the PR **can** merge when `docs` is green **without** a second approval and **without** admin bypass
3. Confirm force pushes to `main` are blocked
4. Confirm the branch cannot be deleted

When collaborators are online and approvals are raised to 1:

1. Confirm a self-authored PR cannot merge without another person's approval
2. Confirm admin bypass is unused for routine work

> **Note:** Some features (required reviews, code owner enforcement) require
> GitHub Pro, Team, or Enterprise for private repositories. Making the repo
> public unlocks all ruleset features on any plan.
