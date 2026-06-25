#!/usr/bin/env bash
# OIR Deploy Script
# Pulls latest from GitHub, rebuilds site, deploys to served directory.
# Can be called manually or triggered by the webhook handler.
# Run as: sudo -u oir /opt/oir/repo/deploy/deploy.sh

set -euo pipefail

OIR_ROOT="/opt/oir"
REPO_DIR="$OIR_ROOT/repo"
SITE_DIR="$OIR_ROOT/site"
VENV_DIR="$OIR_ROOT/venv"
LOG_FILE="$OIR_ROOT/deploy.log"
PYTHON="$VENV_DIR/bin/python"
MKDOCS="$VENV_DIR/bin/mkdocs"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

log "═══ Deploy started ═══"

# Pull latest from GitHub
log "→ Pulling latest from origin/main..."
cd "$REPO_DIR"
git fetch origin main
git reset --hard origin/main

# Validate metadata
log "→ Validating metadata..."
"$PYTHON" tools/validate_metadata.py >> "$LOG_FILE" 2>&1

# Generate indexes
log "→ Generating indexes..."
"$PYTHON" tools/generate_indexes.py >> "$LOG_FILE" 2>&1

# Build MkDocs site
log "→ Building MkDocs site..."
"$MKDOCS" build --strict --site-dir "$SITE_DIR" >> "$LOG_FILE" 2>&1

# Ensure nginx can read the output
chmod -R o+rX "$SITE_DIR"

log "═══ Deploy complete ═══"
log "  Site deployed to: $SITE_DIR"
log ""
