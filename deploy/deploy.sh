#!/usr/bin/env bash
# OIR Deploy Script
# Pulls latest from GitHub, rebuilds site, deploys.
# Called by the webhook handler or manually.
#
# Usage:
#   sudo bash /opt/oir/repo/deploy/deploy.sh
#
# Note: For the full restart including nginx reload and MCP restart,
# use RestartAndUpdateOIR.sh instead.

set -euo pipefail

OIR_ROOT="/opt/oir"
REPO_DIR="$OIR_ROOT/repo"
SITE_DIR="$OIR_ROOT/site"
VENV_DIR="$OIR_ROOT/venv"
LOG_FILE="$OIR_ROOT/deploy.log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

# Determine how to run commands as oir
if [ "$(whoami)" = "oir" ]; then
    AS_OIR=""
else
    AS_OIR="sudo -u oir -H"
fi

log "═══ Deploy started ═══"

# Pull latest from GitHub
log "→ Pulling latest from origin/main..."
cd "$REPO_DIR"
$AS_OIR git fetch origin main
$AS_OIR git reset --hard origin/main

# Sync nginx config
log "→ Syncing nginx config..."
cp "$REPO_DIR/deploy/nginx/openinternetresearch.com.conf" /home/ubuntu/yz.network/nginx-oir.conf 2>/dev/null || \
cp "$REPO_DIR/deploy/nginx/oir.conf" /home/ubuntu/yz.network/nginx-oir.conf 2>/dev/null || true

# Validate metadata
log "→ Validating metadata..."
$AS_OIR $VENV_DIR/bin/python tools/validate_metadata.py

# Generate indexes
log "→ Generating indexes..."
$AS_OIR $VENV_DIR/bin/python tools/generate_indexes.py

# Build MkDocs site
log "→ Building MkDocs site..."
export NO_MKDOCS_2_WARNING=1
$AS_OIR $VENV_DIR/bin/mkdocs build --site-dir "$SITE_DIR"

# Reload nginx
log "→ Reloading nginx..."
docker exec yz-webserver nginx -s reload 2>/dev/null || true

# Restart MCP server
log "→ Restarting MCP server..."
systemctl restart oir-mcp 2>/dev/null || true

log "═══ Deploy complete ═══"
log "  Site: https://openinternetresearch.com"
log ""
