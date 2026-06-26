#!/usr/bin/env bash
# RestartAndUpdateOIR.sh - Pull latest and rebuild the OIR site
#
# Usage (run as root or with sudo):
#   sudo bash /opt/oir/repo/RestartAndUpdateOIR.sh
#
# Or run as oir user directly (skips nginx reload):
#   sudo -u oir bash /opt/oir/repo/RestartAndUpdateOIR.sh

set -euo pipefail

echo "🔄 OIR Site Update and Restart"
echo "=============================="

OIR_HOME="/opt/oir"
REPO="$OIR_HOME/repo"
VENV="$OIR_HOME/venv/bin"

cd "$REPO"

# Determine if we're already running as oir or need sudo -u oir
if [ "$(whoami)" = "oir" ]; then
    RUN=""
else
    RUN="sudo -u oir"
fi

echo "→ Pulling latest from GitHub..."
$RUN git fetch origin main
$RUN git reset --hard origin/main

echo "→ Validating metadata..."
$RUN $VENV/python tools/validate_metadata.py

echo "→ Generating indexes..."
$RUN $VENV/python tools/generate_indexes.py

echo "→ Building MkDocs site..."
$RUN $VENV/mkdocs build --site-dir "$OIR_HOME/site"

echo "→ Reloading nginx..."
docker exec yz-webserver nginx -s reload 2>/dev/null || echo "   (nginx reload requires root — run with sudo)"

echo ""
echo "✅ OIR site updated and live at https://openinternetresearch.com"
