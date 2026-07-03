"""Sync GitHub labels from .github/labels.yml to the repository.

Requires: gh CLI authenticated, or GITHUB_TOKEN environment variable.

Usage:
    python tools/sync_labels.py              # Dry-run (show what would change)
    python tools/sync_labels.py --apply      # Create/update labels on GitHub
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LABELS_FILE = ROOT / ".github" / "labels.yml"
REPO = "itsmeront/open-internet-reference"


def load_desired_labels() -> list[dict[str, str]]:
    """Load label definitions from YAML file."""
    content = LABELS_FILE.read_text(encoding="utf-8")
    labels = yaml.safe_load(content)
    return labels or []


def get_existing_labels() -> list[dict[str, str]]:
    """Fetch existing labels from GitHub using gh CLI."""
    try:
        result = subprocess.run(
            ["gh", "label", "list", "--repo", REPO, "--json", "name,color,description", "--limit", "200"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode == 0:
            return json.loads(result.stdout)
    except (FileNotFoundError, subprocess.TimeoutExpired, json.JSONDecodeError):
        pass
    return []


def update_label(label: dict[str, str], dry_run: bool = True) -> None:
    """Update an existing label on GitHub."""
    name = label["name"]
    color = label["color"]
    desc = label.get("description", "")

    if dry_run:
        print(f"  [UPDATE] {name} (#{color}) — {desc}")
        return

    cmd = ["gh", "label", "edit", name, "--repo", REPO, "--color", color]
    if desc:
        cmd.extend(["--description", desc])

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
    if result.returncode == 0:
        print(f"  ✓ Updated: {name}")
    else:
        print(f"  ✗ Failed to update: {name} — {result.stderr.strip()}")


def create_label(label: dict[str, str], dry_run: bool = True) -> None:
    """Create a label on GitHub."""
    name = label["name"]
    color = label["color"]
    desc = label.get("description", "")

    if dry_run:
        print(f"  [CREATE] {name} (#{color}) — {desc}")
        return

    cmd = ["gh", "label", "create", name, "--repo", REPO, "--color", color]
    if desc:
        cmd.extend(["--description", desc])

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
    if result.returncode == 0:
        print(f"  ✓ Created: {name}")
        return

    stderr = result.stderr.strip()
    if "already exists" in stderr.lower():
        update_label(label, dry_run=False)
        return

    print(f"  ✗ Failed: {name} — {stderr}")


def ensure_gh_authenticated() -> int:
    """Return 0 if gh can access the repo, else print error and return 1."""
    probe = subprocess.run(
        ["gh", "label", "list", "--repo", REPO, "--limit", "1"],
        capture_output=True,
        text=True,
        timeout=15,
    )
    if probe.returncode == 0:
        return 0

    err = probe.stderr.strip() or probe.stdout.strip()
    print(
        "GitHub CLI is not authenticated. Set GH_TOKEN (repo scope) or run "
        f"`gh auth login` before --apply.\n\n{err}",
        file=sys.stderr,
    )
    return 1


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Sync GitHub labels from labels.yml")
    parser.add_argument("--apply", action="store_true", help="Actually create/update labels (default: dry-run)")
    args = parser.parse_args()

    dry_run = not args.apply

    if dry_run:
        print("DRY RUN — use --apply to make changes\n")
    elif ensure_gh_authenticated() != 0:
        return 1

    desired = load_desired_labels()
    existing = get_existing_labels()
    existing_names = {lbl["name"].lower() for lbl in existing}

    print(f"Labels defined in {LABELS_FILE.name}: {len(desired)}")
    print(f"Labels existing on GitHub: {len(existing)}")
    print()

    to_create = []
    to_update = []

    for label in desired:
        if label["name"].lower() not in existing_names:
            to_create.append(label)
        else:
            # Check if update needed
            existing_label = next(
                (l for l in existing if l["name"].lower() == label["name"].lower()),
                None,
            )
            if existing_label:
                if (
                    existing_label.get("color", "").lower() != label["color"].lower()
                    or existing_label.get("description", "") != label.get("description", "")
                ):
                    to_update.append(label)

    if to_create:
        print(f"Labels to create ({len(to_create)}):")
        for label in to_create:
            create_label(label, dry_run=dry_run)
        print()

    if to_update:
        print(f"Labels to update ({len(to_update)}):")
        for label in to_update:
            update_label(label, dry_run=dry_run)
        print()

    if not to_create and not to_update:
        print("All labels are in sync!")

    if dry_run and (to_create or to_update):
        print("\nRun with --apply to make these changes.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
