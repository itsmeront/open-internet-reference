#!/usr/bin/env bash
# Regenerate website/generated/stats.md from nginx and MCP logs.
# Called by deploy.sh and RestartAndUpdateOIR.sh before MkDocs build.

set -euo pipefail

OIR_ROOT="${OIR_ROOT:-/opt/oir}"
REPO_DIR="${REPO_DIR:-$OIR_ROOT/repo}"
VENV_PYTHON="${VENV_PYTHON:-$OIR_ROOT/venv/bin/python}"
NGINX_CONTAINER="${NGINX_CONTAINER:-yz-webserver}"

STATS_NGINX_LOG=$(mktemp /tmp/oir-nginx-XXXXXX.log)
trap 'rm -f "$STATS_NGINX_LOG"' EXIT

docker logs "$NGINX_CONTAINER" 2>/dev/null >"$STATS_NGINX_LOG" || true

"$VENV_PYTHON" "$REPO_DIR/tools/generate_stats.py" \
  --nginx-log "$STATS_NGINX_LOG" \
  --mcp-log "$OIR_ROOT/mcp-requests.log"
