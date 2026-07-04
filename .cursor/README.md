# Cursor MCP — OIR Knowledge Base

This project includes a local MCP server (`oir_mcp/`) for querying the Open Internet Reference knowledge base from Cursor.

## One-time setup

From the repo root:

```powershell
# Windows
.\.venv\Scripts\pip install "mcp[cli]" pyyaml
```

```bash
# Linux / macOS
.venv/bin/pip install "mcp[cli]" pyyaml
```

If you do not have a venv yet:

```powershell
python -m venv .venv
```

## Linux / macOS path

`.cursor/mcp.json` points at the Windows venv Python path (`.venv/Scripts/python.exe`). On Linux or macOS, change the `command` to:

```json
"command": "${workspaceFolder}${/}.venv${/}bin${/}python"
```

## Enable in Cursor

1. **Reload the window** — `Ctrl+Shift+P` → **Developer: Reload Window**
2. Open **Settings → Tools & MCP** and confirm `oir-knowledge-base` shows a green status
3. In Agent chat, the tools (`query_knowledge`, `get_research_debt`, `find_help`, etc.) should appear when relevant

## Troubleshooting

- **Red / failed server:** Confirm `.venv` exists and `mcp` is installed (`pip show mcp`).
- **Wrong Python:** GUI apps often miss your shell `PATH`. Use the full venv path in `mcp.json` (as committed).
- **Logs:** **View → Output** → channel **MCP** (or **Cursor MCP**).

See [`MCP_SERVER.md`](../MCP_SERVER.md) for tool descriptions and production deployment notes.
