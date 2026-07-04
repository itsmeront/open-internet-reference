# OIR Server Deployment

Deployment configuration for hosting OIR on a Debian/AMD server. **Production** serves
the static site through **nginx inside Docker** (`yz-webserver`); the webhook handler,
MCP server, and git operations run on the **host** as the `oir` system user.

## Prerequisites

- Debian 11+ (or Ubuntu 22.04+) on AMD64
- Docker installed (nginx runs in container `yz-webserver`)
- Python 3.12+ installed on the host
- Git installed
- A domain name pointing to the server (production: `openinternetresearch.com`)
- `iptables-persistent` recommended (webhook firewall rules survive reboot)

## Production Docker Architecture

Production on `boostrap-server` splits work between a Docker front end and host services:

```
GitHub push
    │
    ▼
https://openinternetresearch.com/webhook/deploy
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│  Docker: yz-webserver (nginx)                               │
│  Network: yznetwork_yz-network (172.20.0.0/16)                │
│  Config: /home/ubuntu/yz.network/nginx-oir.conf             │
│          → mounted as /etc/nginx/conf.d/oir.conf            │
│  Serves: /usr/share/nginx/oir (static MkDocs site)          │
│  Proxies: /webhook/ → host.docker.internal:9000             │
│           /api/auth/* → oir-oauth:8110 (Docker network)      │
└───────────────────────────┬─────────────────────────────────┘
                            │ host.docker.internal (172.17.0.1)
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  Host (systemd, user oir)                                    │
│  oir-webhook.service  → 0.0.0.0:9000  (GitHub deploy hook)  │
│  oir-mcp.service      → 127.0.0.1:8080 (MCP, not public)    │
│  /opt/oir/repo        → git clone, deploy scripts           │
│  /opt/oir/site        → built MkDocs output                 │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
              Docker: oir-oauth on yznetwork_yz-network :8110
              (Decap CMS GitHub OAuth — see DECAP_CMS_OAUTH.md)
```

| Component | Runs on | Listens | nginx path | Notes |
|-----------|---------|---------|------------|-------|
| Static site | `yz-webserver` | 443 (public) | `/` | Site root `/usr/share/nginx/oir` |
| Webhook handler | **host** (systemd) | `0.0.0.0:9000` | `/webhook/` | Proxied via `host.docker.internal` |
| OAuth proxy | **Docker** `oir-oauth` | `8110` on `yznetwork_yz-network` | `/api/auth/` | Not on host localhost in production |
| MCP server | **host** (systemd) | `127.0.0.1:8080` | *(disabled)* | Intentionally not proxied yet |

**Why nginx-in-Docker matters for webhooks:** A handler bound to `127.0.0.1:9000` on the
host is **not** reachable from inside the nginx container. Production therefore:

1. Sets `WEBHOOK_HOST=0.0.0.0` in `systemd/oir-webhook.service`
2. Proxies `/webhook/` to `http://host.docker.internal:9000` in nginx
3. Adds host **iptables** rules so Docker bridge CIDRs can reach port 9000 (the host
   INPUT chain otherwise rejects non-80/443 traffic)

The container must have `extra_hosts: ["host.docker.internal:host-gateway"]` (already set on
`yz-webserver`). `host.docker.internal` resolves to the host gateway (typically
`172.17.0.1`); nginx runs on `yznetwork_yz-network` (`172.20.0.0/16`).

**Nginx config files:**

| File | Purpose |
|------|---------|
| `deploy/nginx/openinternetresearch.com.conf` | **Production** — copied by `RestartAndUpdateOIR.sh` |
| `deploy/nginx/oir.conf` | Generic template (also copied by `setup.sh` on first install) |

After editing either file, reload nginx inside the container:

```bash
docker exec yz-webserver nginx -t && docker exec yz-webserver nginx -s reload
```

Or run a full deploy as root: `sudo bash /opt/oir/repo/RestartAndUpdateOIR.sh`

## Quick Setup

> **Production (`boostrap-server`):** nginx and TLS are already managed in Docker
> (`yz-webserver`). After step 2, run `sudo bash /opt/oir/repo/RestartAndUpdateOIR.sh`
> and configure the GitHub webhook (step 6 + [Auto-Deploy](#auto-deploy-via-github-webhook)).
> Steps 3–4 below apply to a **bare-metal nginx** install only.

```bash
# 1. Clone the repo on the server
sudo mkdir -p /opt/oir
sudo chown $USER:$USER /opt/oir
git clone https://github.com/itsmeront/open-internet-reference.git /opt/oir/repo

# 2. Run the setup script
cd /opt/oir/repo/deploy
chmod +x setup.sh
sudo ./setup.sh

# 3. Configure your domain
sudo cp nginx/oir.conf /etc/nginx/sites-available/oir
sudo ln -sf /etc/nginx/sites-available/oir /etc/nginx/sites-enabled/oir
# Edit the file to set your domain name
sudo nano /etc/nginx/sites-available/oir
sudo nginx -t && sudo systemctl reload nginx

# 4. Get SSL certificate
sudo certbot --nginx -d oir.yourdomain.com

# 5. Deploy the site for the first time
/opt/oir/repo/deploy/deploy.sh

# 6. Set up the GitHub webhook (optional — enables auto-deploy on push)
sudo systemctl enable --now oir-webhook
```

## Directory Layout on Server

```
/opt/oir/
├── repo/              ← Git clone of the repository
├── site/              ← Generated MkDocs site (copied into yz-webserver volume)
├── venv/              ← Python virtual environment (webhook handler)
├── .webhook-secret    ← HMAC secret for GitHub webhooks (600, owner oir)
├── webhook.log        ← Webhook handler logs
└── deploy.log         ← Deployment logs (from deploy.sh / cron)
```

## Components

| File | Purpose |
|---|---|
| `setup.sh` | One-time server setup (installs deps, creates dirs, configures services) |
| `deploy.sh` | Pulls latest, rebuilds site, deploys (called manually or by webhook) |
| `webhook.py` | Lightweight HTTP server that receives GitHub push webhooks and triggers deploy |
| `nginx/oir.conf` | Generic nginx server block template |
| `nginx/openinternetresearch.com.conf` | Production nginx block for `yz-webserver` |
| `systemd/oir-webhook.service` | systemd service for the webhook handler |
| `systemd/oir-mcp.service` | systemd service for the MCP server (localhost :8080) |
| `cron/oir-checks` | Cron jobs for periodic URL checking and site rebuild |

## MCP server

The MCP server runs on **localhost:8080** on the server (`systemctl status oir-mcp`). It is intentionally **not** proxied through nginx — there is no authentication or rate limiting yet.

- **Cursor (local dev):** use [`.cursor/mcp.json`](../.cursor/mcp.json) — stdio mode, no public URL needed.
- **Remote agents (future):** expose via `/mcp/` only after API keys and rate limits are implemented. See [`MCP_SERVER.md`](../MCP_SERVER.md).

Enable on server: `sudo systemctl enable --now oir-mcp`

## Decap CMS / OAuth

The browser editor at `/admin/` requires GitHub OAuth. See [`.github/DECAP_CMS_OAUTH.md`](../.github/DECAP_CMS_OAUTH.md) for full setup (build OAuth proxy, nginx `/api/auth/` block, verification).

After changing nginx config under `deploy/nginx/`, redeploy or reload nginx:

```bash
sudo bash /opt/oir/repo/RestartAndUpdateOIR.sh
# or reload only:
docker exec yz-webserver nginx -t && docker exec yz-webserver nginx -s reload
```

## Manual Deployment

```bash
/opt/oir/repo/deploy/deploy.sh
```

This pulls the latest from GitHub, rebuilds the MkDocs site, and copies it to the served directory.

## Auto-Deploy via GitHub Webhook

Auto-deploy runs on every **push to `main`**. A **cron fallback** also runs
`deploy.sh` every 6 hours (`deploy/cron/oir-checks`).

### 1. Host service (`oir-webhook`)

`setup.sh` installs and enables the systemd unit. Requirements:

| Setting | Value | Why |
|---------|-------|-----|
| `User` / `Group` | `oir` | Must read `/opt/oir/.webhook-secret` and write `webhook.log` |
| `WEBHOOK_HOST` | `0.0.0.0` | Required when nginx runs in Docker (see architecture above) |
| `WEBHOOK_PORT` | `9000` (default) | Matches nginx `proxy_pass` target |

```bash
sudo systemctl enable --now oir-webhook
sudo systemctl status oir-webhook
curl -s https://openinternetresearch.com/webhook/health   # expect: OK
```

**Endpoints:**

| Method | Path | Response |
|--------|------|----------|
| `GET` | `/webhook/health` | `200 OK` — health check (no auth) |
| `POST` | `/webhook/deploy` | Validates HMAC signature, runs deploy on push to `main` |

**Event handling:**

- **`ping`** (GitHub test on webhook creation) → `200` body `Ignored` — signature verified, no deploy
- **`push`** to `refs/heads/main` → runs `deploy/deploy.sh`, returns `200 Deploy successful` or `500` on failure
- **`push`** to other branches → `200 Ignored (not main)`
- Bad signature → `403 Invalid signature`

### 2. nginx (Docker)

Production block in `deploy/nginx/openinternetresearch.com.conf`:

```nginx
location /webhook/ {
    proxy_pass http://host.docker.internal:9000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    client_max_body_size 10m;
}
```

If nginx runs **directly on the host** (no Docker), use `http://127.0.0.1:9000` instead and
set `WEBHOOK_HOST=127.0.0.1` in the systemd unit.

### 3. Host firewall (iptables)

The host INPUT chain allows only 22/80/443/8080 from the internet. Docker bridge traffic
to port 9000 would otherwise be **rejected**, causing nginx **502** responses.

`setup.sh` inserts rules (and saves them if `netfilter-persistent` is installed):

```bash
# Allow Docker bridge networks → host webhook port
iptables -I INPUT 1 -s 172.17.0.0/16 -p tcp --dport 9000 -j ACCEPT
iptables -I INPUT 1 -s 172.20.0.0/16 -p tcp --dport 9000 -j ACCEPT
sudo netfilter-persistent save   # if not run by setup.sh
```

Port 9000 remains **unreachable from the public internet**; only Docker-internal nginx
proxies `/webhook/` over HTTPS.

### 4. GitHub repository webhook

1. Repo **Settings → Webhooks → Add webhook**
2. **Payload URL:** `https://openinternetresearch.com/webhook/deploy`
3. **Content type:** `application/json`
4. **Secret:** contents of `/opt/oir/.webhook-secret` on the server:
   ```bash
   ssh oracle-yz 'sudo cat /opt/oir/.webhook-secret'
   ```
5. **Events:** Just the **push** event
6. Save, then **Recent Deliveries → Redeliver** the ping — expect **200** (not 502/403)

**Secret lifecycle:** `setup.sh` generates `.webhook-secret` **once** (when the file is
missing). Re-running setup or restarting the service does **not** rotate the secret. If you
regenerate the file manually, update the secret in GitHub to match.

### 5. Verification

```bash
# Service and health
systemctl is-active oir-webhook          # active
curl -s https://openinternetresearch.com/webhook/health

# From inside nginx container (after iptables rules)
docker exec yz-webserver curl -s http://host.docker.internal:9000/webhook/health

# After a push to main
sudo tail -20 /opt/oir/webhook.log
sudo tail -20 /opt/oir/deploy.log
```

### Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| **502** on webhook delivery | Service down, wrong bind address, or iptables blocking Docker→host | `systemctl status oir-webhook`; confirm `0.0.0.0:9000` in `ss -tlnp`; add iptables rules above |
| **403** Invalid signature | GitHub secret ≠ `/opt/oir/.webhook-secret` | Update secret in GitHub repo webhook settings |
| Service crash `Permission denied: webhook.log` | Running as `www-data` instead of `oir` | Use `User=oir` in `oir-webhook.service`; `chown oir:oir /opt/oir/webhook.log` |
| Cron deploy fails `Permission denied` | `deploy.sh` not executable | `chmod +x /opt/oir/repo/deploy/deploy.sh` |
| Ping **200** but push doesn't deploy | Push not to `main`, or deploy script error | Check `webhook.log` and `deploy.log` for branch filter / deploy stderr |

See also [`.github/DECAP_CMS_OAUTH.md`](../.github/DECAP_CMS_OAUTH.md) for OAuth Docker
network requirements on the same nginx container.

## Updating Deployment Configuration

After changing files in `deploy/`, pull on the server and re-run setup:

```bash
cd /opt/oir/repo
git pull
sudo ./deploy/setup.sh
```
