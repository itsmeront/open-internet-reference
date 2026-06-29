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
    else:
        # Label might exist, try edit
        cmd[2] = "edit"
        cmd.insert(3, name)
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        if result.returncode == 0:
            print(f"  ✓ Updated: {name}")
        else:
            print(f"  ✗ Failed: {name} — {result.stderr.strip()}")


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Sync GitHub labels from labels.yml")
    parser.add_argument("--apply", action="store_true", help="Actually create/update labels (default: dry-run)")
    args = parser.parse_args()

    dry_run = not args.apply

    if dry_run:
        print("DRY RUN — use --apply to make changes\n")

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
            create_label(label, dry_run=dry_run)
        print()

    if not to_create and not to_update:
        print("All labels are in sync!")

    if dry_run and (to_create or to_update):
        print("\nRun with --apply to make these changes.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
