# Decap CMS GitHub OAuth Setup

This document describes how to set up GitHub OAuth authentication for the
Decap CMS admin interface at `https://openinternetresearch.com/admin/`.

Related files:

- `website/admin/config.yml` — Decap CMS collections and backend settings
- `website/admin/index.html` — loads Decap CMS from CDN
- `deploy/nginx/oir.conf` — nginx location blocks (synced to `yz-webserver` on deploy)

## Architecture

```
Browser → /admin/ → Decap CMS JS → /api/auth/* → OAuth proxy (host) → GitHub OAuth → GitHub API → PRs
```

With `open_authoring: true`, non-collaborators authenticate via OAuth and
Decap CMS creates PRs from their fork automatically.

Production layout:

| Component | Where it runs |
|-----------|---------------|
| Static site + `/admin/` | nginx in Docker container `yz-webserver` |
| OAuth proxy | Host Docker container `oir-oauth` on `127.0.0.1:8110` (see port note below) |
| Secrets | Server environment only — never in Git |

---

## Option A: External OAuth Provider (Recommended)

Use a lightweight OAuth proxy. Decap CMS needs an endpoint that handles the
GitHub OAuth dance (redirect → code → token exchange).

> **Note:** The image `ghcr.io/decap-cms/decap-cms-oauth:latest` is not publicly
> pullable (registry returns `denied`). Build locally from the maintained
> reference implementation instead.

### Step 1: Create GitHub OAuth App

1. Go to https://github.com/settings/developers
2. Click **New OAuth App**
3. Fill in:
   - **Application name:** `OIR Content Editor`
   - **Homepage URL:** `https://openinternetresearch.com`
   - **Authorization callback URL:** `https://openinternetresearch.com/api/auth/callback`
4. Click **Register application**
5. Note the **Client ID**
6. Generate and note the **Client Secret**

Keep the secret out of Git. Store it in server environment variables or Docker `-e` flags only.

### Step 2: One-time server prep (as root)

The OAuth container runs as the `oir` service user. Ensure directories and Docker access exist:

```bash
sudo mkdir -p /opt/oir
sudo chown oir:oir /opt/oir
sudo usermod -aG docker oir
```

If you just added `oir` to the `docker` group, log out and back in (or reboot) before continuing.

Verify Docker works for `oir`:

```bash
sudo -u oir docker ps
```

### Step 3: Build the OAuth proxy image (as `oir`)

Clone the reference implementation and build on the server (works on **arm64** and amd64):

```bash
sudo -u oir git clone https://github.com/vencax/netlify-cms-github-oauth-provider.git /opt/oir/oauth
sudo -u oir bash -lc 'cd /opt/oir/oauth && docker build -t oir-oauth:local .'
```

### Step 4: Run the OAuth container (as `oir`)

> **Run on the server (`boostrap-server`), not in GitHub Actions.** SSH in first:
> `ssh oracle-yz`
>
> **Important:** Use `sudo -u oir docker run ...` (host user). **Do not** add `-u oir`
> to `docker run` — that tries to find user `oir` *inside* the container image.
>
> **Image:** The last argument must be `oir-oauth:local`, **not** `docker` or
> `docker:latest`.
>
> **Port:** Use **8110** (8090 is taken by `yz-dht-node-5` on this host).
>
> **Network:** `yz-webserver` runs on Docker network `yznetwork_yz-network`.
> The OAuth container must join that same network so nginx can reach it as
> `oir-oauth:8110`. Binding only to `127.0.0.1:8110` on the host is **not**
> enough — nginx inside Docker cannot reach host localhost.

**Test in foreground first** (shows errors directly; press `Ctrl+C` to stop):

```bash
sudo -u oir docker run --rm --name oir-oauth-test \
  --network yznetwork_yz-network \
  -e OAUTH_CLIENT_ID='YOUR_REAL_CLIENT_ID' \
  -e OAUTH_CLIENT_SECRET='YOUR_REAL_CLIENT_SECRET' \
  -e GIT_HOSTNAME='https://github.com' \
  -e ORIGINS='openinternetresearch.com' \
  -e REDIRECT_URL='https://openinternetresearch.com/api/auth/callback' \
  -e PORT=8110 \
  -p 127.0.0.1:8110:8110 \
  oir-oauth:local
```

If that stays running, stop it (`Ctrl+C`) and start detached:

```bash
sudo -u oir docker rm -f oir-oauth oir-oauth-test 2>/dev/null || true

sudo -u oir docker run -d --name oir-oauth --restart unless-stopped \
  --network yznetwork_yz-network \
  -e OAUTH_CLIENT_ID='YOUR_REAL_CLIENT_ID' \
  -e OAUTH_CLIENT_SECRET='YOUR_REAL_CLIENT_SECRET' \
  -e GIT_HOSTNAME='https://github.com' \
  -e ORIGINS='openinternetresearch.com' \
  -e REDIRECT_URL='https://openinternetresearch.com/api/auth/callback' \
  -e PORT=8110 \
  -p 127.0.0.1:8110:8110 \
  oir-oauth:local
```

**One-line version** (easier to paste in bash):

```bash
sudo -u oir docker run -d --name oir-oauth --restart unless-stopped --network yznetwork_yz-network -e OAUTH_CLIENT_ID='YOUR_REAL_CLIENT_ID' -e OAUTH_CLIENT_SECRET='YOUR_REAL_CLIENT_SECRET' -e GIT_HOSTNAME='https://github.com' -e ORIGINS='openinternetresearch.com' -e REDIRECT_URL='https://openinternetresearch.com/api/auth/callback' -e PORT=8110 -p 127.0.0.1:8110:8110 oir-oauth:local
```

Required environment variables:

| Variable | Value |
|----------|-------|
| `OAUTH_CLIENT_ID` | From GitHub OAuth App |
| `OAUTH_CLIENT_SECRET` | From GitHub OAuth App |
| `GIT_HOSTNAME` | `https://github.com` |
| `ORIGINS` | `openinternetresearch.com` (mandatory — CORS allow-list for Decap CMS) |
| `REDIRECT_URL` | `https://openinternetresearch.com/api/auth/callback` (must match GitHub OAuth App callback URL) |
| `PORT` | `8110` on production server (`3000` is the upstream default) |

Quotes around secrets are optional unless the value contains shell-special characters (`$`, `!`, spaces). Single quotes are safest.

**Verify the container:**

```bash
sudo -u oir docker ps --filter name=oir-oauth
sudo -u oir docker logs --tail 30 oir-oauth
curl -s -o /dev/null -w "host :8110 → %{http_code}\n" http://127.0.0.1:8110/
curl -s -o /dev/null -w "public /api/auth/ → %{http_code}\n" https://openinternetresearch.com/api/auth/
```

Success indicators:

- `docker run -d` prints a long container ID (hex string)
- `docker ps` shows `Up` and `127.0.0.1:8110->8110/tcp`
- Host curl to `:8110` returns **200**
- Public `/api/auth/` returns **200** (not **502**)

### Step 5: Configure nginx

Production config lives in `deploy/nginx/openinternetresearch.com.conf` and is synced to
`/home/ubuntu/yz.network/nginx-oir.conf` on deploy. nginx runs inside `yz-webserver` on
`yznetwork_yz-network` and proxies to the OAuth container by name:

```nginx
    location = /api/auth {
        resolver 127.0.0.11 ipv6=off valid=10s;
        set $oauth_upstream oir-oauth:8110;
        proxy_pass http://$oauth_upstream/auth;
        ...
    }

    location /api/auth/callback {
        resolver 127.0.0.11 ipv6=off valid=10s;
        set $oauth_upstream oir-oauth:8110;
        proxy_pass http://$oauth_upstream/callback$is_args$args;
        ...
    }
```

The `resolver` line uses Docker's embedded DNS so nginx can resolve `oir-oauth` even if
the container starts after nginx.

Reload nginx after updating the config:

```bash
sudo bash /opt/oir/repo/RestartAndUpdateOIR.sh
# or, config-only reload:
docker exec yz-webserver nginx -t && docker exec yz-webserver nginx -s reload
```

### Step 6: Decap CMS config

`website/admin/config.yml` already has the correct backend settings:

```yaml
backend:
  name: github
  repo: itsmeront/open-internet-reference
  branch: main
  open_authoring: true
  base_url: https://openinternetresearch.com
  auth_endpoint: /api/auth
```

Redeploy the site so `/admin/` and `config.yml` are live under `/opt/oir/site/admin/`.

---

## Option B: Netlify Identity

Not recommended — OIR hosts on Oracle Cloud, not Netlify.

---

## Option C: PKCE (Client-side OAuth, no server proxy)

Simplest setup if you do not want a server-side OAuth container. Decap CMS handles OAuth in the browser; no client secret is stored on the server.

1. Create a GitHub OAuth App with callback URL:
   `https://openinternetresearch.com/admin/`
2. Update `website/admin/config.yml`:

```yaml
backend:
  name: github
  repo: itsmeront/open-internet-reference
  branch: main
  open_authoring: true
  auth_type: pkce
  app_id: YOUR_GITHUB_OAUTH_APP_CLIENT_ID
```

Remove `base_url` and `auth_endpoint` if switching fully to PKCE. No nginx `/api/auth/` block or Docker container is needed.

PKCE is simpler to operate but keeps the OAuth client ID public in the browser (expected for public OAuth clients).

---

## Verification

After setup (Option A or C):

1. Navigate to `https://openinternetresearch.com/admin/`
2. Click **Login with GitHub**
3. Authorize the OAuth App
4. Confirm CMS collections load (Organizations, Law, Sources, etc.)
5. Create a test draft → verify it opens a PR in the repo
6. For non-collaborators: verify `open_authoring` forks and PRs work

**Option A only** — confirm the auth proxy path:

```bash
curl -I https://openinternetresearch.com/api/auth/
```

You should get an HTTP response routed through nginx (not connection refused).

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `unable to find user oir` | Used `docker run -u oir` or wrong image `docker:latest` | Use `sudo -u oir docker run ... oir-oauth:local` — no `-u` on docker run |
| `Conflict. The container name "/oir-oauth" is already in use` | Failed container still exists | `sudo -u oir docker rm -f oir-oauth` then re-run |
| `docker pull … denied` | GHCR image is private/unavailable | Build `oir-oauth:local` from vencax repo (Step 3) |
| No container ID after `docker run -d` | Multiline paste broke in PowerShell, or pull failed | Use one-line bash command; run foreground test first |
| `No such container: oir-oauth` | Container never created | Check `docker ps -a`; re-run Step 4 |
| `port is already allocated` | Host port in use (8090 is taken by `yz-dht-node-5`) | Use **8110** or another free port; match nginx `proxy_pass` |
| `permission denied` on `docker` | `oir` not in `docker` group | `sudo usermod -aG docker oir`, re-login |
| Login redirects but fails / CORS error | Missing or wrong `ORIGINS` | Set `-e ORIGINS='openinternetresearch.com'` |
| `/admin/` works but auth hangs | nginx cannot reach OAuth (502 on `/api/auth/`) | Add `--network yznetwork_yz-network` to OAuth container; nginx must proxy to `oir-oauth:8110` |
| OAuth callback mismatch | Wrong callback URL in GitHub App | Must be `https://openinternetresearch.com/api/auth/callback` for Option A |
| Blank `/admin/` screen; config not yaml | `config.yml` served as `application/octet-stream` | nginx must set `Content-Type: text/yaml` for `/admin/config.yml` (see `deploy/nginx/openinternetresearch.com.conf`) |
| Blank `/admin/`; `appendChild` null | Decap script loaded in `<head>` before `<body>` exists | Move `<script>` to end of `<body>` in `website/admin/index.html` |
| Blank `/admin/`; JS 404s | Missing trailing slash on `/admin` | Use `https://openinternetresearch.com/admin/` (nginx redirects `/admin` → `/admin/`) |

---

## Security Notes

- The OAuth Client Secret must never be committed to the repo
- Store secrets in server environment variables or Docker `-e` flags
- Bind OAuth to localhost only: `-p 127.0.0.1:8110:8110` (not `0.0.0.0`)
- The OAuth proxy should only be reachable via the nginx reverse proxy
- Consider rate-limiting `/api/auth/` in nginx to prevent abuse

---

## Optional: systemd instead of Docker

If you prefer Node.js directly (no Docker):

```bash
sudo -u oir git clone https://github.com/vencax/netlify-cms-github-oauth-provider.git /opt/oir/oauth
cd /opt/oir/oauth && sudo -u oir npm install --production
```

Create `/etc/systemd/system/oir-oauth.service`:

```ini
[Unit]
Description=Decap CMS GitHub OAuth proxy for OIR
After=network.target

[Service]
Type=simple
User=oir
WorkingDirectory=/opt/oir/oauth
Environment=NODE_ENV=production
Environment=PORT=8110
Environment=ORIGINS=openinternetresearch.com
Environment=REDIRECT_URL=https://openinternetresearch.com/api/auth/callback
Environment=GIT_HOSTNAME=https://github.com
Environment=OAUTH_CLIENT_ID=YOUR_REAL_CLIENT_ID
Environment=OAUTH_CLIENT_SECRET=YOUR_REAL_CLIENT_SECRET
ExecStart=/usr/bin/npm start
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now oir-oauth
sudo systemctl status oir-oauth
```

nginx configuration is the same — proxy `/api/auth/` to `127.0.0.1:8110`.
