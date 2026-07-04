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
    useradd --system --shell /bin/bash --home-dir "$OIR_ROOT" "$OIR_USER"
    echo "  Created user: $OIR_USER"
else
    echo "  User $OIR_USER already exists"
fi

# Create directories
echo "→ Creating directories..."
mkdir -p "$SITE_DIR"

# Install system dependencies
echo "→ Installing system dependencies..."
apt-get update -qq
apt-get install -y -qq python3.12 python3.12-venv python3.12-dev git

# Create Python virtual environment
echo "→ Setting up Python virtual environment..."
if [ ! -d "$VENV_DIR" ]; then
    python3.12 -m venv "$VENV_DIR"
fi
"$VENV_DIR/bin/pip" install --quiet --upgrade pip
"$VENV_DIR/bin/pip" install --quiet pyyaml mkdocs-material mkdocs-glightbox pymdown-extensions pillow "mcp[cli]"

# Set permissions
echo "→ Setting permissions..."
chown -R "$OIR_USER:$OIR_GROUP" "$OIR_ROOT"
chmod +x "$REPO_DIR/deploy/deploy.sh" 2>/dev/null || true
chmod +x "$REPO_DIR/deploy/webhook.py" 2>/dev/null || true
chmod +x "$REPO_DIR/RestartAndUpdateOIR.sh" 2>/dev/null || true

# Install systemd services
echo "→ Installing systemd services..."
cp "$REPO_DIR/deploy/systemd/oir-webhook.service" /etc/systemd/system/
cp "$REPO_DIR/deploy/systemd/oir-mcp.service" /etc/systemd/system/
systemctl daemon-reload
systemctl enable oir-webhook

# Allow nginx-in-Docker to reach the webhook handler on port 9000
echo "→ Configuring firewall for webhook (Docker → host:9000)..."
for cidr in 172.17.0.0/16 172.20.0.0/16; do
    if ! iptables -C INPUT -s "$cidr" -p tcp --dport 9000 -j ACCEPT 2>/dev/null; then
        iptables -I INPUT 1 -s "$cidr" -p tcp --dport 9000 -j ACCEPT
    fi
done
if command -v netfilter-persistent >/dev/null 2>&1; then
    netfilter-persistent save
fi

# Webhook log (owned by oir — service runs as oir, not www-data)
touch "$OIR_ROOT/webhook.log"
chown "$OIR_USER:$OIR_GROUP" "$OIR_ROOT/webhook.log"
chmod 644 "$OIR_ROOT/webhook.log"

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

# Copy nginx config (production file preferred when present)
echo "→ Copying nginx config..."
if [ -f "$REPO_DIR/deploy/nginx/openinternetresearch.com.conf" ]; then
    cp "$REPO_DIR/deploy/nginx/openinternetresearch.com.conf" /home/ubuntu/yz.network/nginx-oir.conf
else
    cp "$REPO_DIR/deploy/nginx/oir.conf" /home/ubuntu/yz.network/nginx-oir.conf
fi

echo ""
echo "═══════════════════════════════════════════"
echo "  Setup complete!"
echo "═══════════════════════════════════════════"
echo ""
echo "Services:"
echo "  Start webhook:    systemctl start oir-webhook   # already enabled by setup"
echo "  Enable MCP:       systemctl enable --now oir-mcp"
echo ""
echo "Deploy site:"
echo "  sudo bash $REPO_DIR/RestartAndUpdateOIR.sh"
echo ""
echo "Webhook URL:  https://openinternetresearch.com/webhook/deploy"
echo ""
