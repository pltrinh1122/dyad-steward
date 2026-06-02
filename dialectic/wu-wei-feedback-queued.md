# wu-wei feedback for steward — QUEUED INTAKE (triaged, not disposed)

> **Status: queued.** Source: `dyad-wu-wei@recommendations/2026-06-02-feedback-for-steward.md` (sibling
> grain, intake→verify→suture loop). Operator direction 2026-06-02: **queue, do not act yet.** Triaged
> from the **Commons/tended grain** (lower the consumer-dyad's barrier), verified where checkable against
> actual bytes. Disposition (any Commons change) is the **Founding gate's**, not ours.

| # | wu-wei item | Verdict (verified) | Disposition |
|---|---|---|---|
| 1 | `onboard.py` final step = direct `git push` to Commons `main`; fails for a dyad without write access | **Real, KNOWN deferral.** `DIRECTORY.md` already names "write access = coarse gate; signatures = escalation frontier." *Convergent* with our own substrate-access push-authorization friction. | → fold into the **Commons access-model thread** (not a quick patch). |
| 2 | "Tip: record birth-hash in your anchor" left manual; wu-wei missed it, needed a patch cycle. Rec: auto-inject hash into anchor | **Real enablement gap** (Tip line confirmed in `onboard.py`). Caveat: auto-editing a dyad's *anchor* is sovereignty-sensitive (safe for `AGENT.md`; careful near the birth shim). Same "record-so-verifiable" instinct as our (retracted-but-directionally-right) marker idea. | **Library candidate** → onboarding-improvement, Founding gate. |
| 3 | Vocabulary collision: their Agent used deprecated `probes` not Commons `stress-tests` (from bond playbook). Rec: centralized `semantic_ledger.yml` inherited via submodule | **Substantive — lands on our "knowledge compounding" summit.** BUT **unverified provenance:** is `stress-tests` Commons *canon* or bond-particular wu-wei adopted? Verify before endorsing a ledger built on it. | **Verify term provenance first**, then library candidate. |
| 4 | "Heartbeat seizures": Agent left a background cron polling in a wait-state, burning compute. Rec: Commons anti-pattern playbook | **Real, generalizes** (mirrors our own `ScheduleWakeup` "don't short-poll harness-tracked work" guidance). Cheapest + least-contested to curate. | **Ripest library candidate** → anti-pattern playbook. |

**Steward read (not a dispose):** #4 + #2 ripe; #1 folds into access-model; #3 needs provenance check.
None urgent/fragile. Pick up alongside the dyad-bond + Healer intake items when the Operator directs.

## Cross-references
- `commons/scripts/onboard.py` (#1, #2) · `dialectic/substrate-access.md` (#1 convergence) ·
  the Commons access-model / gated-write thread (#1) · `DIRECTORY.md` §registration (#1).
