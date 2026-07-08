# Stand-down — 2026-07-08

Reflection (CSS+SH): `dialectic/reflections/2026-07-08-birthhash-regression-and-ci-guard-invariant.md`.

> **⚠ CORRECTION (post-d-reflect).** PR #82/#83's derivation was WRONG — steward's canonical `birth_hash`
> is `72ba645f` (`onboard.py`, the definitive engine; reproduces bond/touchstone exactly), not the raw
> `4c42be0b` those PRs wrote. **PR #84** reverts the value + re-homes `auto_share` and the audit on
> `onboard.py`'s algorithm. The **invariant + workflow** from #83 stand; only the derivation was wrong.
> The "+1" and OPEN list below still hold; the birth_hash *value* line is corrected by #84.

## What closed (all merged to Commons main)
- **PR #80** — `falsify.py` `⟳ edited-since-read` vs `• new` (DM read-state truth-in-labeling). Root of the
  thread: a read-state audit found 6 of 8 "unread" DMs were already processed.
- **PR #81** — spartan `CONTRIBUTING.md` (declarative, pronoun-free, falsifiable-invariants-only) + revise-a-
  Playbook-in-place pin rule + ledger filename convention + minimal entry schema.
- **PR #82** — `directory/dyad-steward.yaml` `birth_hash` → canonical `4c42be0b` (revert the #12 `72ba645f`
  regression) + the root-cause `.strip()` bug in `auto_share.compute_birth_hash` + test.
- **PR #83** — the invariant *"mechanically-verifiable self-reports are CI-guarded"* + `verify_birthhash.py`
  (instance #1) + `validate-directory-birthhash.yml`.

## The +1
**The CI-guard invariant** — the session's unifying principle. Read-state, ledger fields, and birth_hash were
all *self-reported claims trusted without a mechanical check*; the invariant makes "recompute-and-fail, flag
the unverifiable" the standing bar. `ci_guard_invariant` DONE on the frontier.

## FO-gate
None open — all four PRs merged.

## OPEN / resume (single-homed on the frontier — don't restate)
- `validate_ledger_schema` (READY) — `validate_ledger.py`, **instance #2** of the CI-guard invariant; the
  direct sibling of what just landed.
- **cairn commission-protocol proposal (2026-07-05 DM)** — a referee pass still owed; queued since the
  read-state audit pre-empted it.
- Touchstone's `⟳`-rub verdict — passive; arrives via the DM daemon if it bites.

## State (verified this run, not cached)
- main `e7a4352` local==origin==SYNCED; commons pin `718b4b7`; 0 open PRs (ours).
- Daemons (DM-inbox · commons-PR · peer-review) are session-only — **re-arm at next d-start** (commands in
  `session-pin-2026-06-03.md`).
- 1 unreachable DM source (`dyad-personal-growth-ai`, private/absent locator) — persistent, not new.
