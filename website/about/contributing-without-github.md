# Contributing Without a GitHub Account

Not everyone has or wants a GitHub account. OIR supports several paths for non-technical contributors.

**Prefer the phone-friendly guide:** [Suggest Content](suggest.md) — includes GitHub login-first steps and local draft tips.

## Option 1: Decap CMS (Web Editor)

Visit [openinternetresearch.com/admin/](https://openinternetresearch.com/admin/) to use the browser-based content editor.

### Login (important on phones)

1. Open [github.com/login](https://github.com/login) in the **same browser** and sign in.
2. Return to [openinternetresearch.com/admin/](https://openinternetresearch.com/admin/) (trailing slash).
3. Tap **Login with GitHub** and approve access.

If you try the editor before GitHub login, mobile browsers often fail the OAuth step.

### What you need / what it does

- **What you need:** A GitHub account (free) for authentication
- **What it does:** Form-based editor that creates pull requests automatically
- **IDs:** You do not invent record IDs — a temporary ID is assigned on save; editors rename during review
- **Drafts:** The editor autosaves a local draft on your device if you leave to copy a link; use **Delete draft** for a fresh form
- **Best for:** Adding new records, editing existing content, fixing errors

Note: the public [Outreach CRM](../generated/outreach.md) is browse-only and does **not** use GitHub login. Login is only for `/admin/`.

If you don't have a GitHub account, see the options below.

## Option 2: Email Submission

Send structured suggestions to the project maintainer:

**To:** The project owner (see repository contacts)
**Subject:** `[OIR Suggestion] <brief description>`

Include:

- **What to change:** Page title or ID, and what's wrong
- **Correction:** The accurate information with sources
- **Sources:** URLs or document references supporting your correction
- **Your name (optional):** For attribution in the changelog

The maintainer will create an issue or PR on your behalf. Your contribution will be attributed in the commit message.

## Option 3: Structured Intake Form

For proposing new documents or organizations:

Provide the following information (as much as you can):

```
Document/Organization Name:
Type: [organization | case | statute | person | source]
URL (if available):
Summary (1-2 sentences):
Relevance to OIR:
Tags: [from TAXONOMY.md]
Sources/Evidence:
```

## Option 4: Anonymous Suggestions

For corrections where you prefer not to be identified:

- Suggestions without attribution are accepted
- You may use any communication channel
- All suggestions go through the same editorial review process
- AI-assisted suggestions should be noted as such

## What Happens Next

1. **Intake:** Your suggestion is logged as a GitHub issue or draft PR
2. **Triage:** A moderator reviews it within the moderation queue
3. **Validation:** Sources are checked per `RESEARCH_STANDARDS.md`
4. **Publication:** If approved, content is merged and the site updates

## Attribution

Unless you request anonymity:

- Your name appears in the Git commit message
- You're listed in the CHANGELOG for significant contributions
- For ongoing contributors, we can add you to CONTRIBUTORS.md

## Limitations

Non-GitHub contributions:

- May take longer to process (requires manual conversion)
- Cannot be self-served through the automated workflow
- Still require the same editorial standards and source requirements
- Are subject to the same moderation and review process

## Questions?

See [Contributing](https://github.com/itsmeront/open-internet-reference/blob/main/CONTRIBUTING.md) for the full contribution guide, or contact the project maintainer.
