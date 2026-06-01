# Commons org-transfer locator remediation — EXECUTED (PRs await Founding merge)

> **Status: EXECUTED 2026-06-01.** Move confirmed done (new org `The-Dyad-Practice-Commons`, old path
> redirects, PR #9 moved with the repo). New locator: `The-Dyad-Practice-Commons/the-dyad-practice`.
> - **Unit 1 (our substrate):** AGENT.md + README.md swept → committed direct (`8df6af1`).
> - **Unit 2:** PR #9 clone URL updated; `commons/` remote re-pointed to new org.
> - **Unit 3:** Commons **PR #10** (AGENT.md ×2 + init_dyad.py) opened.
> - **Awaiting:** Founding Operator merges **PR #9** and **PR #10** (Agent never merges).
> - **Still deferred/queued:** org branch-protection/enforcement (gated-write thread); `auto_join.py`
>   `pltrinh1122/{dyad_name}` namespace; init_dyad clone-vs-submodule + join idempotency bugs.

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
