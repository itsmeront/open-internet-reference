# Axona Manual Claim Queue

This queue decomposes `Axona Constitutional & Public Policy Reference Manual.docx` into auditable verification tasks. Nothing in this file is verified OIR knowledge.

Source record: `SRC-AXONA-CONSTITUTIONAL-MANUAL-DOCX`.

## Decomposition Rules

- One claim or topic candidate per task.
- Do not copy manual language into general knowledge pages without external verification.
- Axona-specific pages must be labeled as case-study material.
- Prefer primary legal, technical, historical, or policy sources over internal draft language.

## Volume and Theme Tasks

| Task ID | Manual theme | Verification target | Status |
| --- | --- | --- | --- |
| AXONA-LEGAL-01 | Volume 2 constitutional law framing | Map to existing OIR constitutional topics; add only externally sourced case and statute records | Open |
| AXONA-TECH-01 | Peer-to-peer networking | Add RFC or canonical paper sources before any Axona architecture page | Open |
| AXONA-TECH-02 | Serverless networking | Define scope; add standards or paper sources before drafting | Open |
| AXONA-TECH-03 | Content addressing | Add IPFS, CID, or other standards source before drafting | Open |
| AXONA-TECH-04 | Onion routing | Extend `TOPIC-ONION-ROUTING` with NRL or early onion routing papers | Partial |
| AXONA-TECH-05 | Noise Protocol | Add official Noise Protocol specification source before drafting | Open |
| AXONA-TECH-06 | Signal Protocol | Extend `ORG-SIGNAL` with additional per-spec sources beyond X3DH and Double Ratchet | Partial |
| AXONA-POLICY-01 | Encryption policy positions | Add primary regulatory or case sources before drafting | Open |
| AXONA-POLICY-02 | Privacy policy framing | Link to `TOPIC-FOURTH-AMENDMENT` and add surveillance case law sources | Partial |
| AXONA-POLICY-03 | Open source relationship framing | Add independent sources on open source legal risk before drafting | Open |
| AXONA-CASE-01 | Axona architecture case study | Verify against project code, specs, or design docs only; label as case study | Open |
| AXONA-CASE-02 | Axona threat model | Require explicit threat-model sources; no unsupported security claims | Open |
| AXONA-CASE-03 | Axona governance | Require official Axona governance or charter sources if distinct from this manual | Open |
| AXONA-CASE-04 | Axona public communications | Archive or official communications sources only; mark time-sensitive claims | Open |

## Relationship to OIR Seed Coverage

The manual's general legal themes overlap with existing OIR seed work:

- First Amendment and internet speech: `TOPIC-FIRST-AMENDMENT`, `CASE-RENO-V-ACLU`
- Fourth Amendment and digital privacy: `TOPIC-FOURTH-AMENDMENT`, `CASE-CARPENTER-V-US`
- Copyright safe harbor: `TOPIC-SAFE-HARBOR`, `STAT-DMCA-512`, `CASE-PERFECT10-V-CCBILL`
- Computer crime: `TOPIC-COMPUTER-FRAUD`, `STAT-CFAA-1030`, `CASE-VAN-BUREN-V-US`
- Onion routing and Tor: `TOPIC-ONION-ROUTING`, `ORG-TOR-PROJECT`
- Secure messaging: `ORG-SIGNAL`, `SRC-SIGNAL-X3DH`, `SRC-SIGNAL-DOUBLE-RATCHET`

Do not treat manual overlap as verification. Use external sources to close each task.

## Expected Output

- New bibliography records under `bibliography/`
- Draft knowledge pages under `knowledge/` only after source records exist
- Axona case-study pages clearly separated from general reference pages
