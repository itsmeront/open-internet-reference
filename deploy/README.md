# OIR Server Deployment

Deployment configuration for hosting OIR on a Debian/AMD server with nginx.

## Prerequisites

- Debian 11+ (or Ubuntu 22.04+) on AMD64
- nginx installed and running
- Let's Encrypt / certbot configured
- Python 3.12+ installed
- Git installed
- A domain name pointing to the server (e.g., `oir.yourdomain.com`)

## Quick Setup

```bash
# 1. Clone the repo on the server
sudo mkdir -p /opt/oir
sudo chown $USER:$USER /opt/oir
git clone https://github.com/itsmeront/open-internet-reference.git /opt/oir/repo

# 2. Run the setup script
cd /opt/oir/repo/deploy
chmod +x setup.sh deploy.sh
sudo ./setup.sh

# 3. Install nginx config
sudo cp nginx/oir.conf /etc/nginx/sites-available/oir
sudo ln -sf /etc/nginx/sites-available/oir /etc/nginx/sites-enabled/oir
sudo nginx -t && sudo systemctl reload nginx

# 4. Get SSL certificate
sudo certbot --nginx -d openinternetresearch.com -d www.openinternetresearch.com

# 5. Deploy the site for the first time
/opt/oir/repo/deploy/deploy.sh

# 6. Set up the GitHub webhook (optional — enables auto-deploy on push)
sudo systemctl enable --now oir-webhook
```

## Directory Layout on Server

```
/opt/oir/                ← Home directory of 'oir' service user
├── repo/                ← Git clone of the repository
├── site/                ← Generated MkDocs site (served by nginx)
├── venv/                ← Python virtual environment
├── .webhook-secret      ← GitHub webhook HMAC secret
├── webhook.log          ← Webhook handler logs
├── deploy.log           ← Deployment logs
├── url-check.log        ← Weekly URL checker output
└── debt-report.log      ← Weekly research debt report
```

## Service User

All OIR processes run as a dedicated `oir` system user:

- Created by `setup.sh` with `useradd --system`
- Owns `/opt/oir` and all contents
- Added to `www-data` group for nginx interop
- nginx reads the site via world-readable permissions on `/opt/oir/site`

This keeps OIR isolated from other services on the machine.

## Components

| File | Purpose |
|---|---|
| `setup.sh` | One-time server setup (installs deps, creates dirs, configures services) |
| `deploy.sh` | Pulls latest, rebuilds site, deploys (called manually or by webhook) |
| `webhook.py` | Lightweight HTTP server that receives GitHub push webhooks and triggers deploy |
| `nginx/oir.conf` | nginx server block configuration |
| `systemd/oir-webhook.service` | systemd service for the webhook handler |
| `systemd/oir-mcp.service` | systemd service for the MCP server (future) |
| `cron/oir-checks` | Cron jobs for periodic URL checking and site rebuild |

## Manual Deployment

```bash
/opt/oir/repo/deploy/deploy.sh
```

This pulls the latest from GitHub, rebuilds the MkDocs site, and copies it to the served directory.

## Auto-Deploy via GitHub Webhook

1. In GitHub repo settings → Webhooks → Add webhook
2. Payload URL: `https://openinternetresearch.com/webhook/deploy`
3. Content type: `application/json`
4. Secret: (set in `/opt/oir/.webhook-secret`)
5. Events: Just the push event

The webhook handler (`oir-webhook.service`) listens on localhost:9000 and is proxied through nginx.

## Updating Deployment Configuration

After changing files in `deploy/`, pull on the server and re-run setup:

```bash
cd /opt/oir/repo
git pull
sudo ./deploy/setup.sh
```
