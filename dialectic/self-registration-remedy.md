# Remedy dyad-steward's own Commons self-registration — QUEUED (FO-directed)

> **Status: QUEUED, FO-directed (2026-06-01).** Surfaced while verifying PR #11: **our own**
> registration carries a **bogus birth_hash**. Identity-sensitive + Commons-facing → **Founding gate**;
> we *propose* our corrected identity, the FO *disposes* (proposer ≠ disposer; Agent never merges).

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
