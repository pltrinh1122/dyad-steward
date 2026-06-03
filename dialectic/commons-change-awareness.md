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

## Reopened 2026-06-03 (Steward Operator `[QUEUE]` — "passive/active") — still IDEATE, no dispose

**The axis named in the ask maps onto the doc's existing one:** *active = pull* (a check the dyad
runs), *passive = push* (the Commons/a daemon emits; the dyad is told). Nothing new to invent there —
the open work is *which, for which relationship, and earned by what*.

**What changed since 2026-06-01: this is now defect-earned at n=1.** At this session's stand-up our
`commons` submodule was silently **4 commits behind main** (`0f1dce7` vs `94e676b`) — the doc's
**borrow-drift** case, lived: we *are* a borrower (the whole Commons, via submodule), and we drifted
stale without knowing. The `bin/preflight.py` **`submodule` check** (shipped this session) is already
the **active-pull, whole-repo** detector: "are you behind main?", on demand, pre-PR. So the IDEATE
**narrows** — "should staleness be detectable?" is settled *yes* (lived); the open forks are the two
escalation axes below, each **defect-gated** (build a rung only when a real drift bites it).

**Candidate shapes (provenance-tagged; none disposed):**
- **C-A · active-pull, whole-repo (BUILT).** preflight `submodule` = our-borrow drift detector.
  *Prov:* lived submodule defect. *Attack:* silent until *run*; coarse (whole repo, not per-item); ours
  only — not a mechanism other dyads inherit.
- **C-B · active-pull, per-item.** directory `borrows: {item, pinned_commit}` → a check reports "the
  playbook you borrowed (v_old) has upstream v_new." *Prov:* the doc's `borrows:`+pin move. *Attack:*
  **n=0** — no dyad has yet been bitten by a *borrowed-playbook* drift (only whole-repo, us) → still
  speculative; don't build until earned.
- **C-C · active-pull, standing.** schedule/`loop` the check on a cadence → digest at stand-up.
  *Prov:* `pull_shares.py` ("run at stand-up") + harness schedule/loop. *Attack:* polling noise; still
  requires the dyad's own infra; over-build absent a real cadence need.
- **C-D · passive-push, Commons-emitted.** Commons publishes a changelog/feed (GH releases / CHANGELOG)
  keyed by area; subscribers are notified. *Prov:* the doc's "digest/notification (push)". *Attack:*
  makes the **Commons owe borrowers infra** → a `nouns-vs-verbs` / governance question (is
  change-awareness a Commons *noun* or each dyad's *verb*?) — Founding-gated, not ours to assume; noise
  unless keyed to declared `subscribes:`/`borrows:`.

**Falsification invariant — how this dies:** *noise* (un-keyed alerts → ignored; the `subscribes:`
filter exists to prevent this) · *over-build* (a push/notification system before drift is lived — and
only the **active-pull whole-repo** rung is lived; C-B/C-D are not) · *ownership drift* (a push
mechanism silently makes the Commons owe borrowers, unratified) · *borrow≠subscribe≠fork conflation*
(the doc's open joint, still open).

**Tended-first:** the consumer-dyad shouldn't crawl the Commons; minimum-friction, low-noise. Today
that's satisfied for *our own* borrow (C-A). Extending awareness *to other dyads* is the unbuilt part —
and whether it's pull (they run a check we'd ship) or push (Commons emits) is the live fork, gated on a
real cross-dyad drift event, not assumed.

> Cross-link: `bin/preflight.py` §submodule (the lived active-pull detector) · `steward-validation-infra.md`
> (where the submodule invariant is defect-ledgered) · `cross-dyad-share-pull.md` (the pull-channel sibling).
