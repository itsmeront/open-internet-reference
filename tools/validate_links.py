"""Validate local Markdown links in OIR documentation."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {
    ".git",
    ".venv",
    "__pycache__",
    "generated",
}
MARKDOWN_LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
EXTERNAL_SCHEMES = {
    "http",
    "https",
    "mailto",
}


@dataclass(frozen=True)
class LinkError:
    path: Path
    message: str


def iter_markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not SKIP_PARTS.intersection(path.relative_to(ROOT).parts)
    )


def strip_link_title(target: str) -> str:
    if " " not in target:
        return target
    if target.count('"') >= 2 or target.count("'") >= 2:
        return target.split(" ", 1)[0]
    return target


def target_path(source: Path, raw_target: str) -> Path | None:
    target = strip_link_title(raw_target.strip())
    parsed = urlparse(target)

    if parsed.scheme in EXTERNAL_SCHEMES or target.startswith("#"):
        return None

    link_path = unquote(parsed.path)
    if not link_path:
        return None

    candidate = Path(link_path)
    if not candidate.is_absolute():
        candidate = source.parent / candidate

    return candidate.resolve()


def validate_file(path: Path) -> list[LinkError]:
    errors: list[LinkError] = []
    text = path.read_text(encoding="utf-8")

    for match in MARKDOWN_LINK_PATTERN.finditer(text):
        resolved = target_path(path, match.group(1))
        if resolved is None:
            continue
        if not resolved.exists():
            errors.append(
                LinkError(
                    path,
                    f"missing local link target: {match.group(1)}",
                )
            )

    return errors


def main() -> int:
    files = iter_markdown_files()
    errors: list[LinkError] = []

    for path in files:
        errors.extend(validate_file(path))

    if errors:
        for error in errors:
            print(f"{error.path.relative_to(ROOT)}: {error.message}")
        return 1

    print(f"Validated local Markdown links for {len(files)} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
