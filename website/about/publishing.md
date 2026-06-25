# Publishing

OIR publishes through MkDocs Material. The generated website is written to `generated/site/` and should not be manually edited.

## Local Preview

Run:

```powershell
.\.venv\Scripts\mkdocs serve --dev-addr 127.0.0.1:8000
```

Then open `http://127.0.0.1:8000`.

## Validation

Publishing checks include:

- Metadata graph validation
- Local Markdown link validation
- Bibliography and glossary index generation
- Strict MkDocs build

The same checks run in GitHub Actions.

## Generated Indexes

The current prototype generator writes:

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
- [`website/generated/bibliography.md`](../generated/bibliography.md)
- [`website/generated/citations.md`](../generated/citations.md)
- [`website/generated/glossary.md`](../generated/glossary.md)
- [`website/generated/handbook.md`](../generated/handbook.md)
- [`website/generated/print-handbook.md`](../generated/print-handbook.md)
- [`website/generated/relationships.md`](../generated/relationships.md)
- [`website/generated/relationship-graph.md`](../generated/relationship-graph.md)
- [`website/generated/outreach.md`](../generated/outreach.md)
- [`website/generated/timeline.md`](../generated/timeline.md)
- [`website/generated/used-for.md`](../generated/used-for.md)
- [`website/generated/review-status.md`](../generated/review-status.md)
