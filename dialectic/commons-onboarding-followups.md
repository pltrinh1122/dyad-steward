# Commons onboarding follow-ups — SUBSUMED by PR #14 (awaiting FO merge)

> **Status: SUBSUMED by the wu-wei onboarding rebuild (PR #14, `onboard.py`).** All three items below
> dissolve in the single idempotent tool rather than getting patched piecemeal: (1) namespace → the
> tool scaffolds a `<your-namespace>` placeholder, not a hardcoded account; (2) clone-vs-submodule →
> the tool's `ensure_commons` does submodule-add with a clone fallback; (3) join idempotency → the
> tool is re-runnable and joining is self-authorizing direct-deposit (no fragile `checkout -b join`).
> Pending FO merge of PR #14. Original analysis retained below for the reviewer.

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

---

## Live intake — racked, not yet worked *(post-#14, distinct from the subsumed items above)*

> **PROBED 2026-06-07** (`probe_onboarding_friction`, the first friction-PROBE under the new intake;
> `dialectic/friction-intake-probe-spaor.md`). Both items below are **CONFIRMED real** (cold-path of the
> onboarding flow + claude-code-guide), so both spawned EXECUTE trails (`onboarding_btw_pointer`,
> `onboarding_anchor_activation_note` — Steward propose → FO gate). **Item 2 was REFINED:** a restart is
> *not* needed for in-session usability (the agent `Read`s the anchor; identity = git-hash needs no load)
> — it's needed only so the anchor **auto-injects as system instructions in FUTURE sessions** (restart /
> `/clear` / `/compact`; per Claude Code's prompt-cache docs). The hypothesis "restart needed after birth"
> was too broad. So neither racked item was stale — but the probe shrank #2 from "required" to "conditional."

1. **`/btw` as the new-operator's non-blocking question side-channel during onboarding execution.**
   *(Racked 2026-06-04, Steward-Operator observation — LIVED, not hypothetical.)* Tim (a new operator
   being onboarded) is leaning **heavily** on `/btw` to ask questions *after the Operator directed him
   there*. The lived shape: onboarding has long **execution-pauses** while the Agent runs work (submodule
   add, validate, push, etc.), and the new operator accumulates questions *about the onboarding itself*
   during that dead-time. `/btw` lets them surface those questions **without blocking/derailing** the
   Agent's in-flight work. **Recommendation to design:** a way to *proactively direct* new operators to
   `/btw` for onboarding-questions-during-execution — i.e., bake the side-channel pointer into the
   onboarding flow (onboard.py output? the Join walkthrough?) rather than relying on the sponsoring
   Operator to discover and relay it (as happened with Tim). *Evidence value:* a real enablement signal
   from an actual non-techie onboardee — exactly the consumer-grain the tended-first discipline asks us
   to lead from. **Open:** is this a Steward-owned onboarding-UX delta, or a Commons-`onboard.py` change
   (Founding-gated)? Decide when worked. *(Note: independent of the parked Commons-invariants alignment —
   it's an execution-pause UX item, not an identity/posture item, so it queues without waiting on that.)*

2. **"Restart needed after birth" — necessity under falsification.** *(Racked 2026-06-04, Steward-Operator
   observation — LIVED: Tim's onboarding.)* Observation: a **restart appears to be needed** for the new
   dyad's anchor to take effect after the birth commit, **but Tim's Claude instance never prompted for
   one** — so a non-techie wouldn't know to do it, potentially leaving the new identity un-activated.
   **Falsify-necessity task:** is a restart actually *required*?
   - *Grounded prior (pending claude-code-guide confirmation):* necessity is **conditional, not
     absolute.** (a) **Identity** = `birth_hash`, git-content-derived → needs **no load at all**;
     (b) the anchor's **content** is fully usable in-session via `Read` (the Agent can follow AGENT.md
     without a restart); (c) a restart is needed **only** to get the anchor *auto-injected as system
     instructions* for the new session — a convenience, not an identity or usability requirement.
   - *Why it resolves the missing-prompt sub-observation:* if a restart **isn't** necessary, the
     instance correctly didn't ask → no bug. If it **is** (for reliable activation), the absent prompt
     **is** an onboarding-flow gap → onboard.py / the Join walkthrough should emit a "restart to activate
     your anchor" instruction. The falsification verdict *decides* whether this is a bug to fix.
   - **Status:** claude-code-guide spawned to ground Claude Code's CLAUDE.md reload behavior (restart vs
     mid-session pickup). Verdict to be folded back here.
