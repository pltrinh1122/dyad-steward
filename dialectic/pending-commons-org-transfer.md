# Pending: Commons org-transfer locator remediation — HELD

> **Status: HELD, awaiting trigger.** Founding Operator is transferring the Commons depot
> (`the-dyad-practice`) to a new **"The Dyad Practice Commons"** org (`[NOTE]` 2026-06-01). Agreed
> sequence (`[ALIGN]`): **Operator finishes the move → then we remediate the fixes to match new state.**
> Do **not** act until the Operator confirms the move is done **and** provides the new org slug/URL.

## Not urgent (why)
GitHub **auto-redirects** transferred repos (web + git); PRs/issues **move with the repo**. So clones,
the `commons/` remote, and **PR #9** keep working via redirect. This remediation is for *canonical
correctness*, not function. **Identity is unaffected** — frozen at `CLAUDE.md@2a9dc10` (content+date
hash, not URL); the IDENTITY CAVEAT holds.

## Blast radius (grounded 2026-06-01 — re-grep at execution time; counts may drift)
Old locator: `pltrinh1122/the-dyad-practice` → new: `<NEW-ORG>/the-dyad-practice`.

**Commons-side (in the transferred depot → Founding gate):**
- `commons/README.md:36` — clone URL (**also in open PR #9**)
- `commons/AGENT.md` (×2) · `commons/scripts/init_dyad.py` (`COMMONS_REPO_URL` + docstring)

**Our own substrate (Steward-disposable):**
- `AGENT.md` (×3) · `README.md` (×4)

**Git remotes:** `commons/` origin → re-point post-transfer (redirect works meanwhile). `dyad-steward` origin unaffected.

## Interactions to decide at execution
- **PR #9** hardcodes the old clone URL — update-before-merge vs merge-then-follow-up vs rely-on-redirect.
- The **org** unlocks teams / branch-protection / ownership-separation → the natural moment to land the
  queued **Commons gated-write enforcement** thread *and* fix safety-finding #3 (auto-allow + `commons/` remote).
