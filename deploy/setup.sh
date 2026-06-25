#!/usr/bin/env bash
# OIR Server Setup Script
# Run once (or after deploy config changes) with: sudo ./deploy/setup.sh

set -euo pipefail

OIR_ROOT="/opt/oir"
REPO_DIR="$OIR_ROOT/repo"
SITE_DIR="$OIR_ROOT/site"
VENV_DIR="$OIR_ROOT/venv"
OIR_USER="${OIR_USER:-www-data}"

echo "═══════════════════════════════════════════"
echo "  OIR Server Setup"
echo "═══════════════════════════════════════════"

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
chown -R "$OIR_USER:$OIR_USER" "$SITE_DIR"
chmod +x "$REPO_DIR/deploy/deploy.sh"
chmod +x "$REPO_DIR/deploy/webhook.py"

# Install systemd services
echo "→ Installing systemd services..."
cp "$REPO_DIR/deploy/systemd/oir-webhook.service" /etc/systemd/system/
systemctl daemon-reload

# Create webhook secret if it doesn't exist
if [ ! -f "$OIR_ROOT/.webhook-secret" ]; then
    echo "→ Generating webhook secret..."
    openssl rand -hex 32 > "$OIR_ROOT/.webhook-secret"
    chmod 600 "$OIR_ROOT/.webhook-secret"
    echo "  ⚠ Webhook secret created at $OIR_ROOT/.webhook-secret"
    echo "  ⚠ Add this as the webhook secret in GitHub repo settings"
    cat "$OIR_ROOT/.webhook-secret"
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
echo "  2. Edit domain name:   nano /etc/nginx/sites-available/oir"
echo "  3. Enable site:        ln -sf /etc/nginx/sites-available/oir /etc/nginx/sites-enabled/oir"
echo "  4. Test & reload:      nginx -t && systemctl reload nginx"
echo "  5. Get SSL:            certbot --nginx -d oir.yourdomain.com"
echo "  6. First deploy:       $REPO_DIR/deploy/deploy.sh"
echo "  7. Start webhook:      systemctl enable --now oir-webhook"
echo ""
