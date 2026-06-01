# Commons change-awareness for member dyads — QUEUED IDEATION (not yet explored)

> **Status: QUEUED, parked by FO (2026-06-01).** Captures the question so a cold session inherits it.
> **Not yet under falsification** — do not resolve here.
>
> **Sibling threads:** `commons-contribution-lifecycle.md` (already gestures at *ledger/subscription*) ·
> `sharing-discipline.md` (access map) · `pr-gate-intent.md` (the Operator's *consumption* grain) ·
> `commons-onboarding-followups.md`.

## The question (FO framing, 2026-06-01)

How do member dyads become **aware of changes to the Commons** — especially distinguishing areas they
**subscribe** to vs. library items they've **borrowed**?

## The distinction to preserve (a handle, NOT a resolution)

Two *different relationships* to Commons content → likely two *different* awareness mechanisms:

- **Subscribe (area / standing interest):** a dyad declares ongoing interest in an area or summit and
  wants to be told when *that area* changes. No copy is held; they track upstream. → resembles a
  **topic/path watch**; the risk is **noise** (only signal changes to what they actually subscribe).
- **Borrow (library item / snapshot):** a dyad has taken a copy of a proven playbook/discipline into
  its own substrate. A Commons change to that item means their **copy may have drifted / gone stale**.
  → resembles a **dependency-version drift signal**: "the playbook you borrowed (v_old) has a new
  upstream version (v_new)." Needs an item + version/commit pin to detect drift.

## When reopened — candidate first moves (NOT committed)

- **Declared interest in the directory entry?** e.g. each `directory/<name>.yaml` gains `subscribes:`
  (areas/paths) and `borrows:` (item + pinned version/commit) → makes "what changed that *you* care
  about" *computable* rather than manual.
- **Push vs pull:** digest/notification (push) vs a `what-changed-for-me` check the dyad runs (pull).
  Tended-first: minimum-friction, low-noise; the consumer-dyad should not have to crawl the Commons.
- **Tie to the Telos:** awareness feeds **Resonating** (shared understanding that survived contest) and
  same-summit matchmaking — change-awareness is partly how Resonating stays live, not stale.
- **Borrow ≠ subscribe ≠ fork:** decide whether "borrow" implies a maintained link (drift alerts) or a
  clean snapshot (no obligation). The answer shapes whether the Commons owes borrowers anything.
