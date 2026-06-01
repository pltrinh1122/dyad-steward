# Commons onboarding follow-ups — QUEUED (Founding-gated)

> **Status: QUEUED.** Concrete Commons onboarding/script defects surfaced 2026-05-31..06-01 while
> fixing the Join/Init order (PR #9) and the org-transfer locator. Each is a **Commons change →
> Founding gate**; the Steward proposes, the Founding Operator disposes. Not urgent (redirects + the
> README fix make onboarding workable), but they undermine the **idempotency** existing Dyads expect.

## Open items

1. **`auto_join.py` namespace assumption.** Scaffolds `locator: github.com/pltrinh1122/{dyad_name}`
   for the *joining* dyad — hardcodes the `pltrinh1122` namespace. With dyads no longer necessarily
   under one account (and the Commons now an org), the locator should be the dyad's *own* repo
   namespace, not assumed. *(Surfaced during the org-transfer sweep — distinct from the depot URL.)*

2. **`init_dyad.py` clone-vs-submodule.** README bootstrap does `git clone … commons`; the script does
   `git submodule add`. On a pre-existing `commons/` the submodule path is a no-op. The DIP "submodule"
   intent and the clone bootstrap need reconciling so init actually produces the intended structure.

3. **Join-push not idempotent.** `auto_join.py`'s final step `git checkout -b join/<name>` **errors on
   re-run** if the branch exists — contradicting the idempotency existing Dyads are told to expect.
   Make it re-runnable (reuse/refresh the branch).

> Sibling: `pending-commons-org-transfer.md` (the locator sweep, EXECUTED) ·
> `pr-gate-intent.md` (3)/(4) guarding · the queued Commons gated-write enforcement thread.
