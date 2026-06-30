# Branch Protection Configuration

This document describes the recommended branch protection for the `main` branch
of `itsmeront/open-internet-reference`.

GitHub now offers two options:

- **Branch Rulesets** (recommended) — newer, more flexible, supports org-level rules
- **Classic Branch Protection Rules** — legacy system, still functional

We recommend **Branch Rulesets** as they are GitHub's actively-developed path
forward and offer better composability.

---

## Option A: Branch Rulesets (Recommended)

Navigate to **Settings → Rules → Rulesets → "Add branch ruleset"**

### Basic Settings

| Field | Value |
|-------|-------|
| Ruleset name | `Protect main` |
| Enforcement status | Active |
| Target branches | Include: `main` |
| Bypass list | Repository admin (for emergencies only) |

### Rules to Enable

| Rule | Configuration | Rationale |
|------|---------------|-----------|
| **Restrict deletions** | ✅ | Never delete main |
| **Require a pull request before merging** | ✅ | All changes go through PR review |
| → Required approvals | 1 | At least one CODEOWNER must approve |
| → Dismiss stale reviews | ✅ | Force re-review after new pushes |
| → Require review from code owners | ✅ | CODEOWNERS file routes reviews |
| → Require approval of most recent push | ✅ | Last pusher can't self-approve |
| **Require status checks to pass** | ✅ | CI validation must succeed |
| → Status checks (add) | `docs` | The job name from validate.yml |
| → Require branches be up to date | ✅ | Prevent merge conflicts |
| **Block force pushes** | ✅ | Never force-push to main |
| **Require conversation resolution** | ✅ | All review comments addressed |

### Rules to Leave Disabled (for now)

| Rule | Rationale |
|------|-----------|
| Require signed commits | Enable once all contributors have GPG/SSH signing keys |
| Require linear history | Merge commits are fine for audit trail |
| Require deployments to succeed | No deployment environments configured yet |
| Restrict creations | Not needed for main |

### Step-by-Step

1. Go to https://github.com/itsmeront/open-internet-reference/settings/rules
2. Click **"Add branch ruleset"**
3. Name it `Protect main`
4. Set enforcement to **Active**
5. Under "Target branches" → Add target → Include → type `main`
6. Under "Bypass list" → Add bypass → Repository admin
7. Check each rule listed above and configure the sub-settings
8. Click **"Create"**

---

## Option B: Classic Branch Protection Rules (Legacy)

If you prefer the classic system, navigate to **Settings → Branches → "Add classic branch protection rule"**

### Branch name pattern

```
main
```

### Settings

| Setting | Value | Rationale |
|---------|-------|-----------|
| Require a pull request before merging | ✅ | All changes go through PR review |
| Required approvals | 1 | At least one CODEOWNER must approve |
| Dismiss stale reviews on new pushes | ✅ | Force re-review after changes |
| Require review from code owners | ✅ | CODEOWNERS file controls who reviews what |
| Require status checks to pass | ✅ | CI validation must succeed |
| Required status checks | `docs` | The job name from validate.yml |
| Require branches be up to date | ✅ | Prevent merge conflicts on main |
| Require conversation resolution | ✅ | All review comments must be addressed |
| Require linear history | ❌ | Merge commits are fine for audit trail |
| Include administrators | ❌ | Owner can bypass in emergencies |
| Restrict who can push | ✅ | Only via PR merge |
| Allow force pushes | ❌ | Never on main |
| Allow deletions | ❌ | Never delete main |

---

## Label-based Moderation Workflow

The moderation system uses labels to route PRs:

- `moderation/pending` — PR is in the moderation queue (auto-applied)
- `moderation/approved` — PR has been reviewed and approved
- `moderation/changes-requested` — reviewer requested changes
- `ai-generated` — auto-applied when commit author matches AI patterns
- `needs-review` — applied to all new PRs via the labeling workflow
- `area/*` — content area labels (auto-applied based on changed files)

## Required Status Checks

When configuring status checks, add:

| Check name | Source |
|------------|--------|
| `docs` | `.github/workflows/validate.yml` — validates metadata, links, site build |
| `label-and-triage` | `.github/workflows/moderation.yml` — applies labels |

The `stale-check` job is informational only and should **not** be required
(it only runs on PR open events and reports warnings).

## Verifying It Works

After configuration:

1. Create a test branch and PR
2. Confirm the PR cannot be merged without:
   - Passing CI (`docs` job green)
   - At least one approval from a code owner
3. Confirm force pushes to `main` are blocked
4. Confirm the branch cannot be deleted

> **Note:** Some features (required reviews, code owner enforcement) require
> GitHub Pro, Team, or Enterprise for private repositories.
