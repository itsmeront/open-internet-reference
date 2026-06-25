"""Prepare generated site assets and run MkDocs local preview."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"


def mkdocs_executable() -> str:
    name = "mkdocs.exe" if sys.platform == "win32" else "mkdocs"
    candidate = Path(sys.executable).with_name(name)
    if candidate.exists():
        return str(candidate)
    return "mkdocs"


def run_step(label: str, command: list[str]) -> None:
    print(f"==> {label}")
    result = subprocess.run(command, cwd=ROOT)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate OIR indexes and run MkDocs local preview.",
    )
    parser.add_argument(
        "--dev-addr",
        default="127.0.0.1:8000",
        help="Address for mkdocs serve (default: 127.0.0.1:8000)",
    )
    parser.add_argument(
        "--skip-generate",
        action="store_true",
        help="Skip brand asset rendering and index generation",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    python = sys.executable

    if not args.skip_generate:
        run_step("Rendering brand assets", [python, str(TOOLS / "render_brand_assets.py")])
        run_step("Generating indexes", [python, str(TOOLS / "generate_indexes.py")])

    host, _, port = args.dev_addr.rpartition(":")
    url = f"http://{host}:{port or '8000'}"
    print(f"==> Starting MkDocs at {url}")

    try:
        return subprocess.call(
            [mkdocs_executable(), "serve", "--dev-addr", args.dev_addr],
            cwd=ROOT,
        )
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
