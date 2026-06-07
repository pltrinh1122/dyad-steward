# Adopt cairn's frontier/rack + CSI guards — plan & lineage

> **Status: ADOPTING (FO "clip and lean", 2026-06-06).** Cross-dyad pull from **dyad-cairn** (`9bcff9c`),
> grounded fresh. Port the *way*, not the machine ([[self-describing-markers-port-free]]). Sovereign build
> (our substrate, our dispose). **Vocabulary call (FO-ratified):** adopt cairn's `frontier / rack / node`
> **verbatim** — a *shared* model across the fleet is itself the summit (shared model → lower per-dyad
> steering-bandwidth → **raise N\***) — grafted under our own `summit` (kept; Commons-canon).

## Honesty / lineage (keep us honest)
- **Shared-lineage convergence, NOT independent validation:** cairn ← dyad-touchstone; the pattern echoes
  our own [[regenerable-view-not-sovereign-edit]] / [[verify-with-actual-tool]] / [[ingraining-lives-in-substrate]].
  Adopt as "a sibling's better-mechanized form of what we already hold" ([[convergence-check-transmission]]).
- **Spell it CSI** (Cybernetic Steering Invariant) — cairn enforces lexicon fidelity. Its corpus is
  self-inconsistent (Invariant vs Vector); **we pick Invariant** (matches our `preflight` "invariant" language).
- **Don't adopt vapor:** cairn's flagship `retro_lock` runtime guard is **unbuilt** (`bin/retro-start` absent,
  lockfile never written/read). Adopt the **two working CI guards** + the **taxonomy**, not the lockfile.
- **Fix cairn's gaps in our port** (node-mutation is a stub there; rack items are bare strings, no provenance).
  If our port *improves* on cairn, that IS the cross-dyad **improvement-transfer** = the compounding signature
  (make-or-break test #1, `acceleration-thesis-and-steward-summit.md`).

## Model adopted (cairn ↔ ours)
| Ours (was) | Adopted form |
|---|---|
| summits S1/S2/S3 | **kept** as frontier roots (each node roots to a summit / `b1` capacity) |
| `board.md` READY-SET + BLOCKED (flat) | **`frontier_state.yml`** — DAG of nodes (`title·goal·summit·status·dependencies`), **regenerated** into `frontier.md` (DO-NOT-EDIT projection) |
| "pick one" | **WIP-N=1** mechanically enforced at write (≤1 ACTIVE) |
| racked-intake / shelved | **backlog** (stays in `commons-onboarding-followups.md` / Issues) — distinct from rack |
| (none) | **`rack_state.yml`** — LIFO tactical tasks for the ONE active node; items carry **provenance** (id·node·ts — our fix to cairn's bare strings) |
| `bin/state.py`, `regen_directory_index.py` | **extended** — don't copy cairn's files |

Status enum: `READY → ACTIVE → IN_REVIEW → BLOCKED → DONE`. Presentation: `bin/frontier.py` (ASCII tree +
materialized view + `--check` drift gate) · `bin/rack.py` (push/pop/list).

## CSI guards (P2 — G+V guardrails)
- **Taxonomy:** Symmetric (state-bound) vs Asymmetric (process-bound); registry `kb/csi_guards.yml` + reader.
- **Reframe what we already have:** `preflight.py` invariants = Symmetric guards; the PR-gate (auto-mode
  classifier + `grant_push`) = a guard. The WIP-N=1 frontier write-guard is itself a new Symmetric CSI guard.
- **Port (adapted):** topology-mass cap (serves the board's own "if it grows heavy, thin it" maintenance-bound);
  submodule-vs-remote → Asymmetric *commons-drift* (force a synthesis-anchor on sync). **Negative-control each.**
- **Skip** `retro_lock` (vapor); build our own runtime guard only if a defect earns it.

## Phases
- **P1 — frontier/rack mechanism — ✅ LANDED 2026-06-06.** `frontier_state.yml` (board migrated) +
  `bin/frontier.py` (read·regen·**WIP-N=1 write-guard**·mutate·`--check`) + `rack_state.yml` +
  `bin/rack.py` (LIFO **with provenance** — our fix to cairn's bare strings) + regenerated `frontier.md`
  (DO-NOT-EDIT projection) + `bin/test_frontier.py` (negative-controls: WIP-N=1, bad-status, dangling-dep,
  cycle, determinism) + `preflight.py` `[frontier]` drift gate. `dialectic/board.md` → **retired to a
  pointer**. *Improvements over cairn (compounding signal): node-mutation implemented (cairn's was a stub);
  rack items carry provenance; `--md` is view-only so the source is never clobbered.*
- **P2 — CSI guards — ✅ LANDED 2026-06-06.** `kb/csi_guards.yml` registry + `bin/csi.py` (list +
  `--check` umbrella). All our guards reframed under the **Symmetric/Asymmetric** taxonomy — 7 Symmetric
  *runnable* (parse·registry·refs·submodule·frontier-WIP1·frontier-sync·**topology-mass** [new, ported,
  negative-controlled]) + 3 Asymmetric (PR-gate *runnable*; No-Pure-G + commons-sync *discipline*,
  honestly marked **not** mechanized — no vaporware). Added `bin/test_rack.py` to satisfy No-Pure-G for
  `rack.py`. **Skipped `retro_lock`** (cairn-vapor). Honesty kept: `mechanism: runnable` vs `discipline`
  is explicit in the registry; we did not dress up un-built guards as if they ran.
- **P3 — verify + watch**: dogfood, negative-control, log whether our port improved on cairn (compounding signal).
