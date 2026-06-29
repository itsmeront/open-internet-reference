# Moderation Queue

Last updated: (not yet generated)

This page surfaces pending contributions, draft content, and items needing editorial attention.

## Summary

| Metric | Count |
|--------|-------|
| Open PRs awaiting review | — |
| AI-generated PRs | — |
| Stale PRs (>7 days no activity) | — |
| Draft content items | — |
| Items needing sources | — |
| Stale verifications (>6 months) | — |

## Pull Requests Pending Review

*Run `python tools/moderation_queue.py` to populate this page, or wait for the scheduled GitHub Action.*

## Draft Content Needing Attention

*Data will appear after the moderation queue tool runs against the repository.*

## Stale Verifications

*Content with verification dates older than 6 months will be listed here.*

## Moderator Actions

### Reviewing a PR

1. Click the PR link to view changes on GitHub
2. Check that content follows `RESEARCH_STANDARDS.md`
3. Verify source references are valid and accessible
4. Ensure AI-generated content is properly labeled
5. Approve or request changes via GitHub review

### Promoting Draft Content

1. Verify all required metadata fields are present
2. Check that sources meet citation standards
3. Update `status` from `draft` → `in_review` → `verified`
4. Set `last_verified` to today's date

### Handling Stale Content

1. Re-check source URLs for availability
2. Verify factual claims are still accurate
3. Update `last_verified` date or flag as `needs_sources`
