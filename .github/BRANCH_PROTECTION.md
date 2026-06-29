# Branch Protection Configuration

This document describes the recommended branch protection rules for the
`main` branch of `itsmeront/open-internet-reference`.

## Settings to Configure

Navigate to **Settings → Branches → Branch protection rules → Add rule** on GitHub.

### Branch name pattern

```
main
```

### Required settings

| Setting | Value | Rationale |
|---------|-------|-----------|
| Require a pull request before merging | ✅ | All changes go through PR review |
| Required approvals | 1 | At least one CODEOWNER must approve |
| Dismiss stale reviews on new pushes | ✅ | Force re-review after changes |
| Require review from code owners | ✅ | CODEOWNERS file controls who reviews what |
| Require status checks to pass | ✅ | CI validation must succeed |
| Required status checks | `validate` | The "docs" job in validate.yml |
| Require branches be up to date | ✅ | Prevent merge conflicts on main |
| Require conversation resolution | ✅ | All review comments must be addressed |
| Require linear history | ❌ | Merge commits are fine for audit trail |
| Include administrators | ❌ | Owner can bypass in emergencies |
| Restrict who can push | ✅ | Only via PR merge |
| Allow force pushes | ❌ | Never on main |
| Allow deletions | ❌ | Never delete main |

### Additional recommendations

| Setting | Value | Rationale |
|---------|-------|-----------|
| Require signed commits | ❌ (for now) | Enable once all contributors have GPG keys |
| Lock branch | ❌ | Branch should accept merges |
| Allow specified actors to bypass | Owner only | Emergency fixes |

## Label-based Auto-assignment

The moderation workflow uses labels to route PRs:

- `ai-generated` — auto-applied when commit author matches AI patterns
- `needs-review` — applied to all new PRs via the labeling workflow
- `moderation/pending` — PR is in the moderation queue
- `moderation/approved` — PR has been reviewed and approved
- `moderation/changes-requested` — reviewer requested changes

## How to Apply

These settings must be configured manually in the GitHub UI:

1. Go to https://github.com/itsmeront/open-internet-reference/settings/branches
2. Click "Add branch protection rule"
3. Enter `main` as the branch name pattern
4. Configure as described above
5. Click "Create" / "Save changes"

> **Note:** Branch protection rules require a GitHub Pro, Team, or Enterprise
> plan for private repositories. On free plans, some features may be limited.
