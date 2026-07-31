# Suggest Content / Intake

Use this page when you want to propose a new organization, person, case, source, or correction — especially from a phone.

## Fastest path: web editor

1. **Log into GitHub first** in the same browser: [github.com/login](https://github.com/login).  
   If you skip this, “Login with GitHub” on the editor often fails on mobile.
2. Open the editor: [openinternetresearch.com/admin/](https://openinternetresearch.com/admin/) (keep the trailing slash).
3. Tap **Login with GitHub** and approve access, then return to the editor.
4. Choose a collection (for example **Organizations**) → **New Organization**.
5. Fill in **Title**, **Summary**, and optional **Body** (paste article links in the summary or body).  
   You do **not** invent an ID — a temporary `*-PENDING-*` ID is assigned on save; editors/AI replace it during review.
6. Tap Decap’s **Save**. That opens a draft pull request for review.

### Leaving the form to copy a link

On a phone you often need to leave the editor to copy a URL. The editor now:

- **Autosaves a local draft** on this device while you type
- **Restores that draft** when you come back to the same form
- Shows **Delete draft** on the bottom bar if you want a fresh empty form

Tip: when possible, open the article in a **new tab**, copy the link, then return to the editor tab so you do not lose your place.

## Outreach CRM vs editor login

| Surface | What it is | Login? |
|---|---|---|
| [Outreach CRM](../generated/outreach.md) | Read-only contact / outreach index | **No** — browse only |
| [Content editor `/admin/`](https://openinternetresearch.com/admin/) | Suggest or edit knowledge records | **Yes** — GitHub account |

If the CRM “didn’t log in,” you were likely looking for the **editor**. Use `/admin/` after logging into GitHub first.

## Other ways to suggest (no editor)

- [Intake proposal issue](https://github.com/itsmeront/open-internet-reference/issues/new?template=intake-document.yml) — paste a document URL and notes
- [Suggest an edit issue](https://github.com/itsmeront/open-internet-reference/issues/new?template=suggest-edit.yml) — fix an existing page
- [Contributing without GitHub](contributing-without-github.md) — email / structured text options

## What happens after you submit

1. Your suggestion becomes a draft PR (or issue).
2. A research editor or AI assistant processes it (canonical ID, sources, formatting).
3. A human reviews before merge.
4. The public site updates after merge.

See also: [Contributing guide](https://github.com/itsmeront/open-internet-reference/blob/main/CONTRIBUTING.md) · [Editorial workflow](editorial-workflow.md)
