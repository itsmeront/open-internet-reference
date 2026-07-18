# Publishing

OIR publishes from source Markdown through MkDocs Material.

## Local Preview

Regenerate indexes and start the dev server:

```powershell
.\StartLocalServer.bat
```

Or:

```powershell
.\.venv\Scripts\python tools\serve.py
```

Open `http://127.0.0.1:8000`.

If indexes are already current, skip regeneration:

```powershell
.\StartLocalServer.bat --skip-generate
```

```bash
./StartLocalServer.sh --skip-generate
```

To run MkDocs directly without the helper:

```powershell
.\.venv\Scripts\mkdocs serve --dev-addr 127.0.0.1:8000
```

## Local Validation

Run all local checks before publishing or opening a pull request:

```powershell
.\.venv\Scripts\python tools\validate_metadata.py
.\.venv\Scripts\python tools\render_brand_assets.py
.\.venv\Scripts\python tools\generate_indexes.py
.\.venv\Scripts\python tools\validate_links.py
.\.venv\Scripts\mkdocs build --strict
```

## Build Output

MkDocs writes the generated website to `generated/site/`.

Generated site files should not be manually edited. Update source files under `website/`, `knowledge/`, `bibliography/`, or other source directories instead.

External `http` and `https` links open in a new tab. Internal site links continue to open in the same tab.

## Tip jar (optional tips, not tax-deductible)

OIR accepts optional one-time tips through Buy Me a Coffee for hosting and maintenance. This is **not** a tax-deductible charitable donation.

- Support page: `website/about/support.md`
- Footer icon: `mkdocs.yml` → `extra.social`
- Keep both URLs in sync when changing the tip link

The index page and Usage Statistics footer link to the support page so the disclaimer stays visible before someone leaves the site.

The index generator writes:

- `generated/bibliography.json`
- `generated/citations.json`
- `generated/glossary.json`
- `generated/handbook.json`
- `generated/relationships.json`
- `generated/retrieval.json`
- `generated/retrieval.jsonl`
- `generated/outreach.json`
- `generated/timeline.json`
- `generated/used-for.json`
- `generated/review-status.json`
- `website/generated/bibliography.md`
- `website/generated/citations.md`
- `website/generated/glossary.md`
- `website/generated/handbook.md`
- `website/generated/print-handbook.md`
- `website/generated/relationships.md`
- `website/generated/relationship-graph.md`
- `website/generated/outreach.md`
- `website/generated/timeline.md`
- `website/generated/used-for.md`
- `website/generated/review-status.md`
- `website/generated/source-docs/`

The generated bibliography and glossary pages link their Path fields to generated source mirrors under `website/generated/source-docs/`. These mirror pages are intentionally not listed in top-level navigation; they are reached from the generated index pages.

Generated source mirrors link `SRC-*` references directly to an external `URL or citation` when the source record provides one. Sources without an external URL fall back to the generated bibliography entry.

## CI Validation

The GitHub Actions workflow in `.github/workflows/validate.yml` runs:

- Metadata validation
- Local Markdown link validation
- Index generation
- Strict MkDocs build

## Release Notes

Until the first public release, changes are tracked under `CHANGELOG.md` in the `Unreleased` section. The project version in `pyproject.toml` (currently `0.1.0`) is shown on generated handbook cover pages together with the generation date.

Formal releases should follow this process once the repository has a stable public publishing target:

1. Move `CHANGELOG.md` items from `Unreleased` into a dated version section.
2. Update `pyproject.toml` to the release version.
3. Regenerate indexes and build the site.
4. Create a Git tag (for example `v0.1.0`).
5. Publish the generated site and attach handbook PDF exports if needed.

Generated handbook and print-handbook pages read the release label automatically from `pyproject.toml` and `CHANGELOG.md`.

## Production Deployment

Production hosting (Oracle Cloud `boostrap-server`, nginx in Docker, GitHub webhook
auto-deploy, Decap CMS OAuth) is documented in [`deploy/README.md`](deploy/README.md).

Key topics there:

- **Docker architecture** — `yz-webserver`, `host.docker.internal`, host vs container services
- **GitHub webhook** — systemd `oir-webhook`, iptables for port 9000, GitHub secret setup
- **Manual / fallback deploy** — `RestartAndUpdateOIR.sh` and 6-hour cron

Decap CMS OAuth (separate Docker container on `yznetwork_yz-network`) is in
[`.github/DECAP_CMS_OAUTH.md`](.github/DECAP_CMS_OAUTH.md).

## Brand Assets

Canonical logo sources live under `website/assets/images/`:

| Asset | Use |
| --- | --- |
| `oir-logo-mark.png` | Site header logo and favicon source |
| `oir-logo-v5-fullmesh.svg` | Legacy print asset (superseded by `oir-logo-mark.png`) |

Raster favicon files are generated from `oir-logo-mark.png`:

```powershell
.\.venv\Scripts\python tools\render_brand_assets.py
```

This writes `favicon.ico`, `favicon.png`, `apple-touch-icon.png`, and `logo-mark.png`.

When updating logo artwork, edit the SVG source files directly. Avoid pasting image files into chat if you need to preserve SVG; paste the SVG source or copy the `.svg` file into `website/assets/images/` instead.
