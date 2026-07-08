# Stand-down — 2026-07-08

Reflection (CSS+SH): `dialectic/reflections/2026-07-08-birthhash-regression-and-ci-guard-invariant.md`.

> **⚠ CORRECTION (post-d-reflect).** PR #82/#83's derivation was WRONG — steward's canonical `birth_hash`
> is `72ba645f` (`onboard.py`, the definitive engine; reproduces bond/touchstone exactly), not the raw
> `4c42be0b` those PRs wrote. Correction split in two (the base-validator chicken-and-egg — a PR can't fix
> both a validator and the data it checks): **#84 = code** (re-home `auto_share` + the audit on onboard.py's
> algorithm) **MERGED** `e0422d4`; **#85 = data** (directory value → `72ba645f`) **open**, verify GREEN. The
> **invariant + workflow** from #83 stand; only the derivation was wrong.

## What closed (all merged to Commons main)
- **PR #80** — `falsify.py` `⟳ edited-since-read` vs `• new` (DM read-state truth-in-labeling). Root of the
  thread: a read-state audit found 6 of 8 "unread" DMs were already processed.
- **PR #81** — spartan `CONTRIBUTING.md` (declarative, pronoun-free, falsifiable-invariants-only) + revise-a-
  Playbook-in-place pin rule + ledger filename convention + minimal entry schema.
- **PR #82** — `directory/dyad-steward.yaml` `birth_hash` → canonical `4c42be0b` (revert the #12 `72ba645f`
  regression) + the root-cause `.strip()` bug in `auto_share.compute_birth_hash` + test.
- **PR #83** — the invariant *"mechanically-verifiable self-reports are CI-guarded"* + `verify_birthhash.py`
  (instance #1) + `validate-directory-birthhash.yml`.
- **PR #84** (MERGED `e0422d4`) — code half of the correction: `auto_share` + the audit re-homed on
  onboard.py's algorithm (single-homed derivation).
- **d-reflect idempotency** (our substrate, `d9010d4`) — `standdown.sh` surfaces today's artifacts + steers
  update-in-place; contract stated in `session-lifecycle-discipline.md`. Dogfooded by this session's re-runs.

## The +1
**The CI-guard invariant** — the session's unifying principle. Read-state, ledger fields, and birth_hash were
all *self-reported claims trusted without a mechanical check*; the invariant makes "recompute-and-fail, flag
the unverifiable" the standing bar. `ci_guard_invariant` DONE on the frontier.

## FO-gate
- **PR #85** — data half: `directory/dyad-steward.yaml` → canonical `72ba645f` (verify check GREEN, since
  main now has onboard-based code). **Priority:** Commons `main` still carries the wrong `4c42be0b` (from #82)
  until #85 lands.

## OPEN / resume (single-homed on the frontier — don't restate)
- **PR #85** (above) — the birth_hash *value* correction; FO gate.
- `validate_ledger_schema` (READY) — `validate_ledger.py`, **instance #2** of the CI-guard invariant; the
  direct sibling of what just landed.
- **cairn commission-protocol proposal (2026-07-05 DM)** — a referee pass still owed; queued since the
  read-state audit pre-empted it.
- Touchstone's `⟳`-rub verdict — passive; arrives via the DM daemon if it bites.

## State (verified this run, not cached)
- steward main SYNCED; commons pin `e0422d4` (has #84's onboard-based code; directory value fixed by #85).
- Open Commons PRs (ours): **#85** (birth_hash value → FO gate, verify green).
- Daemons (DM-inbox · commons-PR · peer-review) are session-only — **re-arm at next d-start** (commands in
  `session-pin-2026-06-03.md`).
- 1 unreachable DM source (`dyad-personal-growth-ai`, private/absent locator) — persistent, not new.
