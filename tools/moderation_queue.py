"""Moderation queue — surface pending contributions for review.

Scans pull requests and draft content to build a moderation dashboard showing:
- Open PRs awaiting review (with labels, age, content areas)
- Draft content needing promotion
- Stale reviews (assigned but not acted on)
- AI-generated contributions pending human review

Usage:
    python tools/moderation_queue.py                     # Generate moderation page
    python tools/moderation_queue.py --json              # Output JSON for API
    python tools/moderation_queue.py --stale-days 14     # Custom stale threshold

Output:
    website/generated/moderation.md — generated moderation dashboard
    generated/moderation-queue.json — machine-readable queue for MCP/API
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
WEBSITE_GENERATED_DIR = ROOT / "website" / "generated"
MODERATION_PAGE = WEBSITE_GENERATED_DIR / "moderation.md"
MODERATION_JSON = ROOT / "generated" / "moderation-queue.json"

# GitHub API requires a token for private repos
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
REPO_OWNER = "itsmeront"
REPO_NAME = "open-internet-reference"


def get_open_prs() -> list[dict[str, Any]]:
    """Fetch open pull requests using the GitHub CLI (gh) if available."""
    prs: list[dict[str, Any]] = []

    try:
        result = subprocess.run(
            [
                "gh", "pr", "list",
                "--repo", f"{REPO_OWNER}/{REPO_NAME}",
                "--state", "open",
                "--json", "number,title,author,labels,createdAt,updatedAt,isDraft,reviewRequests,files",
                "--limit", "100",
            ],
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode == 0 and result.stdout.strip():
            prs = json.loads(result.stdout)
    except (FileNotFoundError, subprocess.TimeoutExpired, json.JSONDecodeError):
        # gh CLI not available or failed — fall back to local git data
        pass

    return prs


def classify_pr(pr: dict[str, Any]) -> dict[str, Any]:
    """Classify a PR for the moderation queue."""
    labels = [lbl.get("name", "") if isinstance(lbl, dict) else str(lbl) for lbl in pr.get("labels", [])]
    created = pr.get("createdAt", "")
    updated = pr.get("updatedAt", "")

    # Parse dates
    now = datetime.now(timezone.utc)
    age_days = 0
    stale_days = 0

    if created:
        try:
            created_dt = datetime.fromisoformat(created.replace("Z", "+00:00"))
            age_days = (now - created_dt).days
        except ValueError:
            pass

    if updated:
        try:
            updated_dt = datetime.fromisoformat(updated.replace("Z", "+00:00"))
            stale_days = (now - updated_dt).days
        except ValueError:
            pass

    # Determine content areas from file paths
    areas: set[str] = set()
    for f in pr.get("files", []):
        path = f.get("path", "") if isinstance(f, dict) else str(f)
        if path.startswith("knowledge/legal/"):
            areas.add("legal")
        elif path.startswith("knowledge/organizations/"):
            areas.add("organizations")
        elif path.startswith("knowledge/people/"):
            areas.add("people")
        elif path.startswith("bibliography/"):
            areas.add("bibliography")
        elif path.startswith("contacts/"):
            areas.add("contacts")
        elif path.startswith("intake/"):
            areas.add("intake")
        elif path.startswith("knowledge/"):
            areas.add("knowledge")
        elif path.startswith("tools/") or path.startswith(".github/"):
            areas.add("infrastructure")
        elif path.startswith("website/"):
            areas.add("website")

    # Flags
    is_ai = "ai-generated" in labels
    needs_review = "needs-review" in labels or "moderation/pending" in labels
    is_stale = stale_days >= 7
    is_draft = pr.get("isDraft", False)

    # Priority scoring (higher = needs attention sooner)
    priority = 0
    if needs_review:
        priority += 3
    if is_ai:
        priority += 2  # AI content needs human review
    if is_stale:
        priority += 2
    if age_days > 14:
        priority += 1

    author = pr.get("author", {})
    author_login = author.get("login", "unknown") if isinstance(author, dict) else str(author)

    return {
        "number": pr.get("number"),
        "title": pr.get("title", "Untitled"),
        "author": author_login,
        "labels": labels,
        "areas": sorted(areas),
        "age_days": age_days,
        "stale_days": stale_days,
        "is_ai": is_ai,
        "is_draft": is_draft,
        "needs_review": needs_review,
        "is_stale": is_stale,
        "priority": priority,
    }


def scan_draft_content() -> list[dict[str, Any]]:
    """Scan local content for items in draft or needs_sources status."""
    drafts: list[dict[str, Any]] = []

    try:
        import yaml
    except ImportError:
        # PyYAML not available, skip local scan
        return drafts

    content_dirs = [
        ROOT / "knowledge",
        ROOT / "bibliography",
        ROOT / "contacts",
    ]

    for content_dir in content_dirs:
        if not content_dir.exists():
            continue

        for md_file in content_dir.rglob("*.md"):
            try:
                text = md_file.read_text(encoding="utf-8")
                if not text.startswith("---"):
                    continue

                end_idx = text.index("---", 3)
                front = yaml.safe_load(text[3:end_idx])

                if not front or not isinstance(front, dict):
                    continue

                status = front.get("status", "")
                if status in ("draft", "needs_sources", "in_review"):
                    rel_path = md_file.relative_to(ROOT)
                    drafts.append({
                        "path": str(rel_path),
                        "id": front.get("id", ""),
                        "title": front.get("title", md_file.stem),
                        "status": status,
                        "last_verified": front.get("last_verified", ""),
                        "tags": front.get("tags", []),
                    })
            except (ValueError, yaml.YAMLError, OSError):
                continue

    return drafts


def scan_stale_verifications(days_threshold: int = 180) -> list[dict[str, Any]]:
    """Find content with verification dates older than threshold."""
    stale: list[dict[str, Any]] = []

    try:
        import yaml
    except ImportError:
        return stale

    threshold = datetime.now() - timedelta(days=days_threshold)

    for md_file in (ROOT / "knowledge").rglob("*.md"):
        try:
            text = md_file.read_text(encoding="utf-8")
            if not text.startswith("---"):
                continue

            end_idx = text.index("---", 3)
            front = yaml.safe_load(text[3:end_idx])

            if not front or not isinstance(front, dict):
                continue

            lv = front.get("last_verified", "")
            if not lv:
                continue

            if isinstance(lv, str):
                try:
                    dt = datetime.fromisoformat(lv)
                    if dt < threshold:
                        rel_path = md_file.relative_to(ROOT)
                        stale.append({
                            "path": str(rel_path),
                            "id": front.get("id", ""),
                            "title": front.get("title", md_file.stem),
                            "last_verified": lv,
                            "days_stale": (datetime.now() - dt).days,
                        })
                except ValueError:
                    pass
        except (ValueError, OSError):
            continue

    return sorted(stale, key=lambda x: x.get("days_stale", 0), reverse=True)


def generate_moderation_page(
    pr_queue: list[dict[str, Any]],
    draft_content: list[dict[str, Any]],
    stale_items: list[dict[str, Any]],
) -> str:
    """Generate the Markdown moderation dashboard."""
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# Moderation Queue",
        "",
        f"Last updated: {now}",
        "",
        "This page surfaces pending contributions, draft content, and items needing editorial attention.",
        "",
    ]

    # Summary counts
    ai_count = sum(1 for pr in pr_queue if pr["is_ai"])
    stale_pr_count = sum(1 for pr in pr_queue if pr["is_stale"])
    draft_count = len(draft_content)
    needs_sources_count = sum(1 for d in draft_content if d["status"] == "needs_sources")

    lines.extend([
        "## Summary",
        "",
        f"| Metric | Count |",
        f"|--------|-------|",
        f"| Open PRs awaiting review | {len(pr_queue)} |",
        f"| AI-generated PRs | {ai_count} |",
        f"| Stale PRs (>7 days no activity) | {stale_pr_count} |",
        f"| Draft content items | {draft_count} |",
        f"| Items needing sources | {needs_sources_count} |",
        f"| Stale verifications (>6 months) | {len(stale_items)} |",
        "",
    ])

    # PR Queue
    lines.extend([
        "## Pull Requests Pending Review",
        "",
    ])

    if pr_queue:
        # Sort by priority (highest first)
        sorted_prs = sorted(pr_queue, key=lambda x: x["priority"], reverse=True)

        lines.append("| # | Title | Author | Areas | Age | Flags |")
        lines.append("|---|-------|--------|-------|-----|-------|")

        for pr in sorted_prs:
            flags = []
            if pr["is_ai"]:
                flags.append("🤖 AI")
            if pr["is_stale"]:
                flags.append("⏰ Stale")
            if pr["is_draft"]:
                flags.append("📝 Draft")
            if pr["needs_review"]:
                flags.append("👀 Review")

            areas_str = ", ".join(pr["areas"][:3]) if pr["areas"] else "—"
            flags_str = " ".join(flags) if flags else "—"
            age_str = f"{pr['age_days']}d"

            lines.append(
                f"| [#{pr['number']}](https://github.com/{REPO_OWNER}/{REPO_NAME}/pull/{pr['number']}) "
                f"| {pr['title'][:50]} | @{pr['author']} | {areas_str} | {age_str} | {flags_str} |"
            )
        lines.append("")
    else:
        lines.extend([
            "*No open pull requests. The queue is clear!*",
            "",
        ])

    # Draft Content
    lines.extend([
        "## Draft Content Needing Attention",
        "",
    ])

    if draft_content:
        # Group by status
        by_status: dict[str, list] = defaultdict(list)
        for item in draft_content:
            by_status[item["status"]].append(item)

        for status in ["needs_sources", "in_review", "draft"]:
            items = by_status.get(status, [])
            if not items:
                continue

            status_labels = {
                "draft": "📋 Draft",
                "needs_sources": "📚 Needs Sources",
                "in_review": "🔍 In Review",
            }

            lines.extend([
                f"### {status_labels.get(status, status)} ({len(items)})",
                "",
                "| ID | Title | Path |",
                "|---|-------|------|",
            ])

            for item in items[:20]:
                lines.append(f"| `{item['id']}` | {item['title'][:40]} | `{item['path']}` |")
            lines.append("")

            if len(items) > 20:
                lines.append(f"*...and {len(items) - 20} more*\n")
    else:
        lines.extend([
            "*No draft content found.*",
            "",
        ])

    # Stale Verifications
    lines.extend([
        "## Stale Verifications",
        "",
        "Content with `last_verified` dates older than 6 months:",
        "",
    ])

    if stale_items:
        lines.append("| ID | Title | Last Verified | Days Stale |")
        lines.append("|---|-------|---------------|------------|")

        for item in stale_items[:15]:
            lines.append(
                f"| `{item['id']}` | {item['title'][:40]} | {item['last_verified']} | {item['days_stale']} |"
            )
        lines.append("")

        if len(stale_items) > 15:
            lines.append(f"*...and {len(stale_items) - 15} more needing re-verification*\n")
    else:
        lines.extend([
            "*No stale verifications found.*",
            "",
        ])

    # Actions guide
    lines.extend([
        "## Moderator Actions",
        "",
        "### Reviewing a PR",
        "",
        "1. Click the PR link to view changes on GitHub",
        "2. Check that content follows `RESEARCH_STANDARDS.md`",
        "3. Verify source references are valid and accessible",
        "4. Ensure AI-generated content is properly labeled",
        "5. Approve or request changes via GitHub review",
        "",
        "### Promoting Draft Content",
        "",
        "1. Verify all required metadata fields are present",
        "2. Check that sources meet citation standards",
        "3. Update `status` from `draft` → `in_review` → `verified`",
        "4. Set `last_verified` to today's date",
        "",
        "### Handling Stale Content",
        "",
        "1. Re-check source URLs for availability",
        "2. Verify factual claims are still accurate",
        "3. Update `last_verified` date or flag as `needs_sources`",
        "",
    ])

    return "\n".join(lines)


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Generate OIR moderation queue")
    parser.add_argument("--json", action="store_true", help="Output JSON only")
    parser.add_argument("--stale-days", type=int, default=180, help="Days before verification is stale")
    args = parser.parse_args()

    print("Scanning moderation queue...")

    # Fetch PR data
    pr_data = get_open_prs()
    pr_queue = [classify_pr(pr) for pr in pr_data]

    # Scan local content
    draft_content = scan_draft_content()
    stale_items = scan_stale_verifications(args.stale_days)

    # Build queue data
    queue_data = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "summary": {
            "open_prs": len(pr_queue),
            "ai_prs": sum(1 for pr in pr_queue if pr["is_ai"]),
            "stale_prs": sum(1 for pr in pr_queue if pr["is_stale"]),
            "draft_content": len(draft_content),
            "needs_sources": sum(1 for d in draft_content if d["status"] == "needs_sources"),
            "stale_verifications": len(stale_items),
        },
        "pull_requests": pr_queue,
        "draft_content": draft_content,
        "stale_verifications": stale_items,
    }

    # Write JSON
    MODERATION_JSON.parent.mkdir(parents=True, exist_ok=True)
    MODERATION_JSON.write_text(json.dumps(queue_data, indent=2), encoding="utf-8")

    if args.json:
        print(json.dumps(queue_data, indent=2))
        return 0

    # Generate Markdown page
    content = generate_moderation_page(pr_queue, draft_content, stale_items)
    MODERATION_PAGE.parent.mkdir(parents=True, exist_ok=True)
    MODERATION_PAGE.write_text(content, encoding="utf-8")

    print(f"Generated moderation page: {MODERATION_PAGE}")
    print(f"Generated moderation JSON: {MODERATION_JSON}")
    print(f"  Open PRs: {len(pr_queue)}")
    print(f"  Draft content: {len(draft_content)}")
    print(f"  Stale verifications: {len(stale_items)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
