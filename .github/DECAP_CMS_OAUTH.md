# Decap CMS GitHub OAuth Setup

This document describes how to set up GitHub OAuth authentication for the
Decap CMS admin interface at `https://openinternetresearch.com/admin/`.

## Architecture

```
Browser → /admin/ → Decap CMS JS → GitHub OAuth → GitHub API → Creates PRs
```

With `open_authoring: true`, non-collaborators authenticate via OAuth and
Decap CMS creates PRs from their fork automatically.

## Option A: External OAuth Provider (Recommended)

Use a lightweight OAuth proxy. Decap CMS needs an OAuth endpoint that handles
the GitHub OAuth dance (redirect → code → token exchange).

### Step 1: Create GitHub OAuth App

1. Go to https://github.com/settings/developers
2. Click "New OAuth App"
3. Fill in:
   - **Application name:** `OIR Content Editor`
   - **Homepage URL:** `https://openinternetresearch.com`
   - **Authorization callback URL:** `https://openinternetresearch.com/api/auth/callback`
4. Click "Register application"
5. Note the **Client ID**
6. Generate and note the **Client Secret**

### Step 2: Deploy OAuth Proxy

Deploy the `decap-cms-oauth` proxy alongside the existing Docker setup.

Add to the server's Docker Compose or run standalone:

```bash
docker run -d \
  --name oir-oauth \
  --restart unless-stopped \
  -e OAUTH_CLIENT_ID=<your-client-id> \
  -e OAUTH_CLIENT_SECRET=<your-client-secret> \
  -e GIT_HOSTNAME=https://github.com \
  -p 127.0.0.1:8090:8090 \
  ghcr.io/decap-cms/decap-cms-oauth:latest
```

Or use the Node.js reference implementation:
```bash
git clone https://github.com/decaporg/decap-cms-oauth.git /opt/oir/oauth
cd /opt/oir/oauth && npm install
# Set environment variables and run with systemd
```

### Step 3: Configure Nginx

Add to the nginx config in the Docker container:

```nginx
location /api/auth/ {
    proxy_pass http://host.docker.internal:8090/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```

### Step 4: Update Decap CMS Config

The `website/admin/config.yml` already has the correct backend settings.
Add the base_url if using an external OAuth provider:

```yaml
backend:
  name: github
  repo: itsmeront/open-internet-reference
  branch: main
  open_authoring: true
  base_url: https://openinternetresearch.com
  auth_endpoint: /api/auth
```

## Option B: Netlify Identity (if applicable)

Not recommended for this project since we host on Oracle Cloud.

## Option C: pkce (Client-side OAuth, no server needed)

For simpler setups, Decap CMS supports PKCE OAuth which doesn't require a server-side proxy:

```yaml
backend:
  name: github
  repo: itsmeront/open-internet-reference
  branch: main
  open_authoring: true
  auth_type: pkce
  app_id: <your-oauth-app-client-id>
```

**Note:** PKCE requires the OAuth App to be configured as a "public" client
(no client secret). The callback URL should be `https://openinternetresearch.com/admin/`.

This is simpler but slightly less secure than a server-side proxy.

## Verification

After setup:

1. Navigate to `https://openinternetresearch.com/admin/`
2. Click "Login with GitHub"
3. Authorize the OAuth App
4. You should see the CMS collections
5. Create a test draft → verify it creates a PR in the repo
6. For non-collaborators: verify open_authoring forks and PRs work

## Security Notes

- The OAuth Client Secret must never be committed to the repo
- Store it in server environment variables or Docker secrets
- The OAuth proxy should only be accessible via the nginx reverse proxy
- Rate-limit the auth endpoint to prevent abuse
