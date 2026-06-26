#!/usr/bin/env bash
# RestartAndUpdateOIR.sh - Pull latest and rebuild the OIR site
# Run from anywhere as: sudo bash /opt/oir/repo/RestartAndUpdateOIR.sh

set -euo pipefail

echo "🔄 OIR Site Update and Restart"
echo "=============================="

cd /opt/oir/repo

echo "→ Pulling latest from GitHub..."
git fetch origin main
git reset --hard origin/main

echo "→ Validating metadata..."
su oir -c "/opt/oir/venv/bin/python tools/validate_metadata.py"

echo "→ Generating indexes..."
su oir -c "/opt/oir/venv/bin/python tools/generate_indexes.py"

echo "→ Building MkDocs site..."
su oir -c "/opt/oir/venv/bin/mkdocs build --site-dir /opt/oir/site"

echo "→ Reloading nginx..."
docker exec yz-webserver nginx -s reload

echo ""
echo "✅ OIR site updated and live at https://openinternetresearch.com"
