# Remedy dyad-steward's own Commons self-registration — DONE (PR #12 merged)

> **⚠ SUPERSEDED 2026-07-08 — PR #12's value was itself a regression.** Re-derivation (this turn) shows
> the canonical `birth_hash` is **`sha256:4c42be0b…f000`**, NOT `72ba645f`. The caveat formula hashes the
> RAW `git show 2a9dc10:CLAUDE.md` bytes ‖ `%cI` → `4c42be0b`; PR #12's `compute_birth_hash` routed the
> anchor through `run_cmd().strip()`, dropping the trailing newline → the wrong `72ba645f`. Corrected via
> **PR #82** (directory value + the `compute_birth_hash` strip bug + test); recurrence guarded by **PR #83**
> (a CI check recomputing every directory `birth_hash`). The `72ba645f` references below are the mistaken
> value — kept for the record, no longer canonical. See [[verify-with-actual-tool]]: the script was the bug;
> the canonical FORMULA is authoritative.

> **Status: DONE 2026-06-01 (value later found wrong — see banner above).** PR #12 merged by FO.
> `directory/dyad-steward.yaml` `birth_hash` set to `sha256:72ba645f…` (recomputed via a `compute_birth_hash`
> that diverged from the caveat); DIRECTORY.md dead `.md` entry-links fixed to `.yaml`. Original analysis
> retained below.

## The defect (grounded 2026-06-01)
`commons/directory/dyad-steward.yaml` → `birth_hash: "sha256:4c42be0b…f000"` — a **placeholder with a
literal Unicode ellipsis** (`cat -A` = `M-bM-^@M-&`), not a real digest. It does **not** match the
actual computed hash. (The `4c42be0b` prefix collides with unrelated commons ledger ids — likely a
copy-paste seed, not our identity.)

## The real value (pending formula confirmation)
Running the (PR #11-fixed) `compute_birth_hash` against dyad-steward yields:
`sha256:72ba645f3be1cf6c8c38d1082e37dc519556d5139f6007453a9f007b5a927535`
— birth anchor `CLAUDE.md @ 2a9dc10`, formula `sha256(content ‖ %cI)`.
**Confirm before writing identity:** does this match the `IDENTITY CAVEAT`'s intended formula exactly
(concatenation order, date format)? The caveat writes `sha256(git show 2a9dc10:CLAUDE.md ‖ 2026-05-29T…)`
— verify `‖` = plain concat and the date = full `%cI`, so we register the *canonical* hash, not just
whatever the current script emits.

## Scope of the remedy
- Correct `directory/dyad-steward.yaml` `birth_hash` → the confirmed canonical value.
- Verify/fill `summits:` in that yaml (auto_join scaffolds `TODO` placeholders — check they were filled).
- Update the human-readable `DIRECTORY.md` entry to match.
- Propose as a Commons PR; FO merges.

## Sequencing / deps
- **After PR #11 merges** (so the canonical computation is the fixed earliest-commit logic).
- Pairs with `commons-onboarding-followups.md` (the general mechanism) and the existing-dyad invariant
  / State-3 (born, registered) work — dyad-steward is the n=1 that must be *correctly* registered.
