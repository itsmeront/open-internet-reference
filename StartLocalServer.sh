#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

if [[ -x ".venv/bin/python" ]]; then
  exec .venv/bin/python tools/serve.py "$@"
fi

if command -v python3 >/dev/null 2>&1; then
  exec python3 tools/serve.py "$@"
fi

exec python tools/serve.py "$@"
