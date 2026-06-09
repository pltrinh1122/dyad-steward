# RIFF → DISCOVERY RESOLVED (2026-06-08): mechanical/deterministic commons-repo-audit?

> Status: **RESOLVED — do NOT build now; park defect-earned.** PROBE `probe_commons_repo_audit` ran the
> empirical resting-state sweep (below). The driving-defect gate the riff set was not met → no audit built.

## Discovery result (2026-06-08) — the empirical OBSERVE
Ran every existing validator against the WHOLE resting Commons repo (not a diff), plus the new-coverage
classes preflight structurally cannot check:

| dimension | tool | result |
|---|---|---|
| submodule freshness (commons@HEAD == remote main) | git rev-parse | **IN SYNC** |
| registry validation, all 11 directory entries | `validate_registry.py` | **11/11 PASS** |
| directory index ↔ reality | `regen_directory_index.py --check` | **up to date** |
| falsification ledgers (fr · responses · disposition) | `validate_falsification.py` | **all valid** |
| dead file-path refs in commons `.md` (new coverage) | ad-hoc sweep | **0 dead / 20 checked** |
| cross-file: falsification response → directory dyad (new) | ad-hoc sweep | **0 orphans** |

**Driving-defect verdict:** the strongest case (resting-state drift introduced *outside* a PR) has exactly
**one lived instance — the `DIRECTORY.md` 1-of-9 bug — and it is already guarded** by `regen_index_ci --check`
(DONE). No second, currently-uncaught drift exists. The earned class is already closed.

## Decision
**Do NOT build a comprehensive resting-state audit.** It is speculative coverage — the exact `brake>engine`
over-gating the defect-earned rule resists ([[sharing-is-not-proving]], wu-wei). The one earned defect-class
is already mechanized.

**Park defect-earned, with the trigger pre-named:** *if a SECOND resting-state drift slips through outside a
PR* (a class preflight's slice + per-PR CI both miss), that earns a thin wrapper — and the discovery already
prototyped it: a ~30-line script that **invokes** (never reimplements — single-home) the existing validators
across the whole tree, fast enough to run on demand or in scheduled Commons CI. Home = the Commons
(`scripts/audit.py`, FO-gated), `preflight` calls it. Until that second defect lands, the on-demand sweep in
this doc IS the audit.

---
## (archived riff — the divergent thinking that led here)

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
