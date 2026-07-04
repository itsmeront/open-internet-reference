# Open Internet Reference

Evidence over assertion. Knowledge over opinion.

Open Internet Reference (OIR) is an evidence-based knowledge base for the legal, constitutional, historical, technical, and public policy landscape around internet architecture, distributed systems, peer-to-peer networking, cryptography, open source software, privacy, internet governance, and digital rights.

Axona may be documented as a case study, but OIR is designed to stand on its own as a public reference project.

## Project Status

OIR is preparing **Sprint 8: First Public Release Candidate**. See `ROADMAP.md` for milestones.

## Repository Layout

- `PROJECT_CHARTER.md` defines the project mission and operating principles.
- `ROADMAP.md` tracks milestones and sprint sequencing.
- `RESEARCH_STANDARDS.md` defines verification and evidence rules.
- `STYLE_GUIDE.md` defines editorial conventions.
- `CITATION_GUIDE.md` defines source and citation practices.
- `DATA_MODEL.md` defines knowledge page metadata and relationships.
- `TAXONOMY.md` defines the project taxonomy.
- `SOURCE_INTAKE.md` tracks imported project materials and their intake status.
- `RESEARCH_DEBT.md` tracks verification work that remains unresolved.
- `PUBLISHING.md` documents local preview, validation, build output, CI, and production deploy pointers.
- `deploy/README.md` documents production server layout (Docker nginx, webhooks, OAuth, MCP).
- `EDITORIAL_WORKFLOW.md` documents collaboration phases, roles, and topic administration policy.
- `StartLocalServer.bat` and `StartLocalServer.sh` regenerate indexes and start the local MkDocs preview server.
- `intake/` contains unverified candidate topics, entities, and verification queues.
- `knowledge/` contains durable knowledge pages.
- `contacts/` contains outreach and organization records.
- `bibliography/` contains source records and bibliographic data.
- `generated/` is reserved for generated artifacts and must not be manually edited.
- `website/` contains the MkDocs Material site source.
- `tools/` contains validation and publishing utilities.
- `handbook/` contains handbook-oriented source material.

## Local Development

This repository targets Python 3.14.0.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .[docs]
.\.venv\Scripts\python tools\serve.py
```

Or double-click / run from the repo root:

```powershell
.\StartLocalServer.bat
```

Open `http://127.0.0.1:8000`.

Run metadata validation with:

```powershell
python tools/validate_metadata.py
```

## License

Code and documentation are currently licensed under the MIT License. See `LICENSE`.
