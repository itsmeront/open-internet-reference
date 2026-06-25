# Tools

This directory contains repository maintenance, validation, publishing, and export tools.

Current tools:

- `validate_metadata.py`: checks Markdown front matter in OIR content directories.
- `validate_links.py`: checks local Markdown links in authored documentation.
- `generate_indexes.py`: generates JSON exports and MkDocs pages under `generated/` and `website/generated/`.
- `render_brand_assets.py`: rasterizes favicon assets from `website/assets/images/oir-logo-mark.svg`.
- `serve.py`: renders brand assets, regenerates indexes, and starts MkDocs local preview.

Local preview:

```powershell
.\.venv\Scripts\python tools\serve.py
```

Skip regeneration when indexes are already current:

```powershell
.\.venv\Scripts\python tools\serve.py --skip-generate
```

Typical validation workflow before publishing:

```powershell
.\.venv\Scripts\python tools\validate_metadata.py
.\.venv\Scripts\python tools\render_brand_assets.py
.\.venv\Scripts\python tools\generate_indexes.py
.\.venv\Scripts\python tools\validate_links.py
.\.venv\Scripts\mkdocs build --strict
```
