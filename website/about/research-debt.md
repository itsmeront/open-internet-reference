# Research Debt

Research debt tracks useful leads and gaps that should not yet be treated as part of OIR’s scarce **verified core**.

Under the [human-directed / AI-processed model](how-we-work.md), humans periodically direct debt sweeps; AI usually executes the sourcing work. Closing debt improves draft quality — it does not automatically promote a page to `verified`.

## Current Focus

- Decompose imported manual claims into candidate topics and claims.
- Verify outreach contacts against official public sources.
- Compare imported governance documents against the root repository docs.
- Create external source records for primary legal, technical, historical, and policy authorities.

Debt is resolved by adding verified source records, linking claims to evidence, or removing unsupported material.

## Open cases

Watching a live docket is not research debt. A case page sets `monitor: true` while an appeal, merits order, or criminal case can still change. Each week, GitHub Actions updates the issue **chore: monitor open cases** with the pages that are due for a check (`last_verified` missing or older than 14 days).

On a check: if the docket changed, add the source and update the facts. If it did not, set `last_verified` to the check date. Remove `monitor` when the case is over. A named missing filing (“add the complaint PDF”, “add the merits opinion when it issues”) stays research debt.
