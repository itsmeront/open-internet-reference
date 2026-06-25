"""Validate OIR Markdown metadata front matter."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - exercised only when setup is incomplete.
    print("PyYAML is required. Install docs dependencies with: python -m pip install -e .[docs]")
    raise SystemExit(2)


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIRS = [
    ROOT / "knowledge",
    ROOT / "contacts",
    ROOT / "bibliography",
]
VALID_TYPES = {
    "topic",
    "organization",
    "person",
    "attorney",
    "judge",
    "court",
    "case",
    "statute",
    "regulation",
    "technology",
    "protocol",
    "academic_paper",
    "book",
    "historical_event",
    "source",
}
VALID_STATUSES = {
    "draft",
    "needs_sources",
    "in_review",
    "verified",
    "deprecated",
}
VALID_PREDICATES = {
    "represented_by",
    "argued",
    "decided",
    "interprets",
    "cites",
    "authored",
    "published",
    "implements",
    "standardizes",
    "funded_by",
    "affiliated_with",
    "opposes",
    "supports",
    "related_to",
}
ID_PATTERN = re.compile(
    r"^(TOPIC|ORG|PERSON|ATT|JUDGE|CASE|COURT|STAT|REG|TECH|PROTOCOL|PAPER|BOOK|EVENT|SRC)-[A-Z0-9-]+$"
)
TAG_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
REQUIRED_FIELDS = {
    "id",
    "title",
    "type",
    "status",
    "summary",
    "tags",
    "sources",
    "relationships",
    "last_verified",
}


@dataclass(frozen=True)
class ValidationError:
    path: Path
    message: str


@dataclass(frozen=True)
class ParsedFile:
    path: Path
    metadata: dict[str, Any] | None


def iter_markdown_files() -> list[Path]:
    files: list[Path] = []
    for content_dir in CONTENT_DIRS:
        if not content_dir.exists():
            continue
        files.extend(
            path
            for path in content_dir.rglob("*.md")
            if "_templates" not in path.parts and path.name != "README.md"
        )
    return sorted(files)


def load_front_matter(path: Path) -> dict[str, Any] | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None

    try:
        _, raw_metadata, _ = text.split("---\n", 2)
    except ValueError:
        return None

    metadata = yaml.safe_load(raw_metadata)
    if metadata is None:
        return {}
    if not isinstance(metadata, dict):
        return {"__invalid__": "front matter must be a mapping"}
    return metadata


def validate_metadata(
    path: Path,
    metadata: dict[str, Any] | None,
    known_ids: set[str],
) -> list[ValidationError]:
    errors: list[ValidationError] = []

    if metadata is None:
        return [ValidationError(path, "missing YAML front matter")]

    invalid = metadata.get("__invalid__")
    if invalid:
        return [ValidationError(path, invalid)]

    missing = sorted(REQUIRED_FIELDS - metadata.keys())
    for field in missing:
        errors.append(ValidationError(path, f"missing required field: {field}"))

    identifier = metadata.get("id")
    if identifier is not None and not (isinstance(identifier, str) and ID_PATTERN.match(identifier)):
        errors.append(ValidationError(path, "id must use a valid uppercase OIR prefix"))

    page_type = metadata.get("type")
    if page_type is not None and page_type not in VALID_TYPES:
        errors.append(ValidationError(path, f"invalid type: {page_type}"))

    status = metadata.get("status")
    if status is not None and status not in VALID_STATUSES:
        errors.append(ValidationError(path, f"invalid status: {status}"))

    tags = metadata.get("tags")
    if tags is not None:
        if not isinstance(tags, list):
            errors.append(ValidationError(path, "tags must be a list"))
        else:
            for tag in tags:
                if not isinstance(tag, str) or not TAG_PATTERN.match(tag):
                    errors.append(ValidationError(path, f"invalid tag: {tag}"))

    for list_field in ("sources", "relationships"):
        value = metadata.get(list_field)
        if value is not None and not isinstance(value, list):
            errors.append(ValidationError(path, f"{list_field} must be a list"))

    sources = metadata.get("sources")
    if isinstance(sources, list):
        for source in sources:
            if not isinstance(source, str):
                errors.append(ValidationError(path, f"source reference must be a string: {source}"))
            elif source not in known_ids:
                errors.append(ValidationError(path, f"unknown source reference: {source}"))

    relationships = metadata.get("relationships")
    if isinstance(relationships, list):
        for index, relationship in enumerate(relationships):
            if not isinstance(relationship, dict):
                errors.append(ValidationError(path, f"relationship {index} must be a mapping"))
                continue

            for field in ("subject", "predicate", "object", "sources"):
                if field not in relationship:
                    errors.append(ValidationError(path, f"relationship {index} missing field: {field}"))

            subject = relationship.get("subject")
            if not isinstance(subject, str):
                errors.append(ValidationError(path, f"relationship {index} subject must be a string"))
            elif subject not in known_ids:
                errors.append(ValidationError(path, f"relationship {index} unknown subject: {subject}"))

            predicate = relationship.get("predicate")
            if not isinstance(predicate, str):
                errors.append(ValidationError(path, f"relationship {index} predicate must be a string"))
            elif predicate not in VALID_PREDICATES:
                errors.append(ValidationError(path, f"relationship {index} invalid predicate: {predicate}"))

            obj = relationship.get("object")
            if not isinstance(obj, str):
                errors.append(ValidationError(path, f"relationship {index} object must be a string"))
            elif obj not in known_ids:
                errors.append(ValidationError(path, f"relationship {index} unknown object: {obj}"))

            relationship_sources = relationship.get("sources")
            if not relationship_sources:
                errors.append(ValidationError(path, f"relationship {index} must include at least one source"))
            elif not isinstance(relationship_sources, list):
                errors.append(ValidationError(path, f"relationship {index} sources must be a list"))
            else:
                for source in relationship_sources:
                    if not isinstance(source, str):
                        errors.append(ValidationError(path, f"relationship {index} source must be a string: {source}"))
                    elif source not in known_ids:
                        errors.append(ValidationError(path, f"relationship {index} unknown source: {source}"))

    return errors


def main() -> int:
    parsed_files = [
        ParsedFile(path=path, metadata=load_front_matter(path))
        for path in iter_markdown_files()
    ]
    errors: list[ValidationError] = []
    ids_by_path: dict[Path, str] = {}
    paths_by_id: dict[str, Path] = {}

    for parsed_file in parsed_files:
        metadata = parsed_file.metadata
        if not metadata:
            continue
        identifier = metadata.get("id")
        if not isinstance(identifier, str):
            continue
        ids_by_path[parsed_file.path] = identifier
        existing_path = paths_by_id.get(identifier)
        if existing_path:
            errors.append(
                ValidationError(
                    parsed_file.path,
                    f"duplicate id also used in {existing_path.relative_to(ROOT)}: {identifier}",
                )
            )
        else:
            paths_by_id[identifier] = parsed_file.path

    known_ids = set(paths_by_id)

    for parsed_file in parsed_files:
        errors.extend(validate_metadata(parsed_file.path, parsed_file.metadata, known_ids))

    if errors:
        for error in errors:
            relative_path = error.path.relative_to(ROOT)
            print(f"{relative_path}: {error.message}")
        return 1

    print(f"Validated metadata for {len(parsed_files)} Markdown files and {len(known_ids)} IDs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
