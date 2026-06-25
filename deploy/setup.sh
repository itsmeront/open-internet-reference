#!/usr/bin/env bash
# OIR Server Setup Script
# Run once (or after deploy config changes) with: sudo ./deploy/setup.sh

set -euo pipefail

OIR_ROOT="/opt/oir"
REPO_DIR="$OIR_ROOT/repo"
SITE_DIR="$OIR_ROOT/site"
VENV_DIR="$OIR_ROOT/venv"
OIR_USER="oir"
OIR_GROUP="oir"

echo "═══════════════════════════════════════════"
echo "  OIR Server Setup"
echo "═══════════════════════════════════════════"

# Create oir service user if it doesn't exist
echo "→ Creating oir service user..."
if ! id "$OIR_USER" &>/dev/null; then
    useradd --system --shell /bin/bash --home-dir "$OIR_ROOT" --create-home "$OIR_USER"
    usermod -aG www-data "$OIR_USER"
    echo "  Created user: $OIR_USER"
else
    echo "  User $OIR_USER already exists"
fi

# Create directories
echo "→ Creating directories..."
mkdir -p "$OIR_ROOT" "$SITE_DIR"

# Install system dependencies
echo "→ Installing system dependencies..."
apt-get update -qq
apt-get install -y -qq python3 python3-venv python3-pip git

# Create Python virtual environment
echo "→ Setting up Python virtual environment..."
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR"
fi
"$VENV_DIR/bin/pip" install --quiet --upgrade pip
"$VENV_DIR/bin/pip" install --quiet pyyaml mkdocs-material mkdocs-glightbox pymdown-extensions pillow

# Set permissions
echo "→ Setting permissions..."
chown -R "$OIR_USER:$OIR_GROUP" "$OIR_ROOT"
chmod +x "$REPO_DIR/deploy/deploy.sh"
chmod +x "$REPO_DIR/deploy/webhook.py"

# Allow nginx to read the site directory
chmod 755 "$SITE_DIR"
setfacl -R -m g:www-data:rX "$SITE_DIR" 2>/dev/null || chmod -R o+rX "$SITE_DIR"

# Install systemd services
echo "→ Installing systemd services..."
cp "$REPO_DIR/deploy/systemd/oir-webhook.service" /etc/systemd/system/
systemctl daemon-reload

# Create webhook secret if it doesn't exist
if [ ! -f "$OIR_ROOT/.webhook-secret" ]; then
    echo "→ Generating webhook secret..."
    openssl rand -hex 32 > "$OIR_ROOT/.webhook-secret"
    chown "$OIR_USER:$OIR_GROUP" "$OIR_ROOT/.webhook-secret"
    chmod 600 "$OIR_ROOT/.webhook-secret"
    echo ""
    echo "  ┌────────────────────────────────────────────────────────────┐"
    echo "  │ WEBHOOK SECRET (add to GitHub repo → Settings → Webhooks) │"
    echo "  ├────────────────────────────────────────────────────────────┤"
    echo "  │ $(cat $OIR_ROOT/.webhook-secret) │"
    echo "  └────────────────────────────────────────────────────────────┘"
    echo ""
fi

# Install cron jobs
echo "→ Installing cron jobs..."
cp "$REPO_DIR/deploy/cron/oir-checks" /etc/cron.d/oir-checks
chmod 644 /etc/cron.d/oir-checks

echo ""
echo "═══════════════════════════════════════════"
echo "  Setup complete!"
echo "═══════════════════════════════════════════"
echo ""
echo "Next steps:"
echo "  1. Copy nginx config:  cp $REPO_DIR/deploy/nginx/oir.conf /etc/nginx/sites-available/oir"
echo "  2. Enable site:        ln -sf /etc/nginx/sites-available/oir /etc/nginx/sites-enabled/oir"
echo "  3. Test & reload:      nginx -t && systemctl reload nginx"
echo "  4. Get SSL:            certbot --nginx -d openinternetresearch.com -d www.openinternetresearch.com"
echo "  5. First deploy:       sudo -u oir $REPO_DIR/deploy/deploy.sh"
echo "  6. Start webhook:      systemctl enable --now oir-webhook"
echo ""
