# RIFF (RACKED 2026-06-07 — discovery tomorrow): mechanical/deterministic commons-repo-audit?

> Status: **OPEN / divergent** — parked mid-riff by Operator `rack:`. Not a conclusion; the frame hasn't
> settled. Resume as a discovery (→ `probe_commons_repo_audit` on the frontier). Do **not** build until un-racked.

## The question
Should we have a mechanical/deterministic audit of the Commons repo to ensure "everything is how it should be"?

## Surfaced lean (held loosely)
**Yes to a thin, defect-earned, Commons-homed, resting-state audit that wraps the existing validators —
NO to a comprehensive steward-side correctness spec.**

## Why the impulse is sound
On-summit S1: integrity is *the brake that lets the portfolio go fast* — mechanical checks make cross-dyad
borrowing safe. Process-integrity is the steward's verb-domain, so this isn't a stretch.

## What already exists (don't restart cold)
- `bin/preflight.py` already audits part of the Commons: **invokes** the Commons' own
  `validate_registry.validate_file` on every `commons/directory/*.yaml`, and checks `commons@HEAD == remote main`.
- Commons CI checks PR **diffs**: auto-merge registration (adds + own-entry updates), frozen-field immutability,
  index regen (`regen_index_ci` DONE).
- So a "commons audit" partly **exists** in distributed, defect-earned form. The riff is *consolidate + extend*,
  not *start*.

## The strongest NEW-coverage case
Everything today checks a **diff** (per-PR CI) or a **slice** (preflight's directory subset). Nothing checks
the **resting state of the whole repo**. Different failure class — and we LIVED it: the `DIRECTORY.md` 1-of-9
bug was *drift between index and reality*, introduced by no PR. A full-repo audit catches accumulated/cross-file
drift that diff-checks structurally cannot.

## Three cautions (the push-backs)
1. **Single-home / no-fork** — must *invoke* the Commons' own validators, never reimplement (else a second
   source of truth drifts — the trap `preflight` exists to avoid). Pulls toward: the audit **homes in the
   Commons** (`scripts/audit.py` + scheduled CI); steward *proposes*, FO gates; `preflight` just calls it.
2. **Sovereignty** — assert *structural/process* invariants only (validates · refs resolve · index in sync ·
   frozen fields immutable · ledger well-formed); never judge *content-correctness* of sovereign per-dyad entries.
3. **wu-wei** — "ensure *everything*" is the speculative-coverage framing the defect-earned rule resists; a
   comprehensive audit is how a brake grows past the engine (`brake>engine` failure signal). Some audit is
   earned (directory drift · summit-YAML corruption · dead refs · stale submodule); *everything* is not.

## Open questions for tomorrow's discovery
- **Driving defect?** Is there a lived case where the Commons **resting-state** drifted and nothing caught it
  (beyond the directory bug we already fixed)? Without one, this is speculative coverage.
- **Home?** Commons (proposed → FO-gated → scheduled CI, with `preflight` calling it) vs steward-side. Lean: Commons.
- Coverage gaps vs current: Commons `.md` ref-resolution (preflight checks OUR refs only); falsification-ledger
  validation in CI (board item, BLOCKED on Founding gate); cross-file consistency (directory ↔ falsification ↔ library).

## Adjacent noticing (not part of this riff)
This is the **2nd** node I've wanted a true `RACKED` status for (after `csi_complete_armstate`) — the frontier
has no RACKED status, so I'm encoding rack-as-BLOCKED. Defect-earned signal that the frontier may want a
RACKED status / rack-kind node (matching touchstone's lexicon). Noted, not acted.
