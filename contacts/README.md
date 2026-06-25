# Contacts

This directory contains outreach-related records and contact research.

Contact data must be handled carefully:

- Do not invent contact information.
- Prefer official organization pages and public professional profiles.
- Record source and access date.
- Distinguish public organizational contacts from personal contact information.
- Mark stale or unverified data clearly.

## Contact Record Policy (2026-06-19)

OIR will not create `contacts/` records until an explicit outreach use case is defined. Organization coverage currently lives in `knowledge/organizations/` with bibliography-backed verification.

Create a contact record only when all of the following are true:

1. A durable OIR outreach or reference need exists beyond the organization knowledge page.
2. At least one verified bibliography source supports each public contact path recorded.
3. The contact path is publicly published by the organization or person (no inferred or private contact data).
4. `last_verified` can be set from a reverification date tied to the supporting source.
5. The record uses `contacts/_templates/contact-record.md` or an equivalent metadata-compliant template.

Defer contact records when:

- Only a homepage exists and no distinct public intake or contact page is available.
- Role, affiliation, or contact path cannot be reverified from an official source.
- The entity is already adequately covered by an organization knowledge page for reference use.

Generated `outreach.json` prototypes may list outreach-tagged metadata, but they are not substitutes for verified contact records.

## Related Paths

- Organization knowledge pages: `knowledge/organizations/`
- Outreach bibliography sources: `bibliography/organizations/`
- Verification queue: `intake/verification-queue.md`
- Contact template: `contacts/_templates/contact-record.md`
