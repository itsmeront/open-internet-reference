#!/usr/bin/env bash
# RestartAndUpdateOIR.sh - Pull latest and rebuild the OIR site
#
# Usage (run as root or with sudo):
#   sudo bash /opt/oir/repo/RestartAndUpdateOIR.sh
#
# Or run as oir user directly (nginx reload will be skipped):
#   sudo -u oir bash /opt/oir/repo/RestartAndUpdateOIR.sh

set -euo pipefail

echo "🔄 OIR Site Update and Restart"
echo "=============================="

OIR_HOME="/opt/oir"
REPO="$OIR_HOME/repo"
VENV="$OIR_HOME/venv/bin"

cd "$REPO"

# Determine how to run commands as oir
if [ "$(whoami)" = "oir" ]; then
    AS_OIR=""
else
    AS_OIR="sudo -u oir -H"
fi

echo "→ Pulling latest from GitHub..."
$AS_OIR git fetch origin main
$AS_OIR git reset --hard origin/main

echo "→ Validating metadata..."
$AS_OIR $VENV/python tools/validate_metadata.py

echo "→ Generating indexes..."
$AS_OIR $VENV/python tools/generate_indexes.py

echo "→ Building MkDocs site..."
$AS_OIR $VENV/mkdocs build --site-dir "$OIR_HOME/site"

echo "→ Reloading nginx..."
if [ "$(whoami)" = "root" ]; then
    docker exec yz-webserver nginx -s reload
else
    echo "   (skipped — run as root to reload nginx)"
fi

echo "→ Updating systemd services..."
if [ "$(whoami)" = "root" ]; then
    cp "$REPO/deploy/systemd/"*.service /etc/systemd/system/
    systemctl daemon-reload
else
    echo "   (skipped — run as root to update services)"
fi

echo "→ Restarting MCP server..."
if [ "$(whoami)" = "root" ]; then
    systemctl restart oir-mcp 2>/dev/null || echo "   (oir-mcp service not yet enabled — run: systemctl enable --now oir-mcp)"
else
    echo "   (skipped — run as root to restart MCP server)"
fi

echo ""
echo "✅ OIR site updated and live at https://openinternetresearch.com"
echo "   MCP server: systemctl status oir-mcp"
