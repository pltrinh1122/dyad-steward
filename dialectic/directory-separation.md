# Separate DIRECTORY concerns — QUEUED (FO-directed; Commons → Founding gate)

> **Status: QUEUED, FO-directed (2026-06-01):** *"DIRECTORY.md is trying to do too many things… if
> necessary separate into DIRECTORY.yaml/json + DIRECTORY.md."* Grounded read says **separation is
> necessary.** Commons-structural → we *propose*, FO *disposes*.

## Grounded: four conflated concerns in `commons/DIRECTORY.md`
1. **Index data** — the registered-Dyads table (machine data; regenerable from `directory/*.yaml`).
2. **Mechanism / governance** — "how registration works" (self-registering, conflict-free, the
   falsified-D1 rationale).
3. **Joining how-to** — step-by-step instructions (compute birth-hash, create entry, commit).
4. **Definitions** — context-unit, `+1 summit` semantics, source-of-truth declaration.

## The self-contradiction (why it's *necessary*, not just tidy)
The doc warns **"No flat shared table"** (falsified `D1`: a shared table collides on concurrent joins
and lets a Dyad edit another's row) — yet the **index table in DIRECTORY.md *is* a hand-maintained flat
shared table.** Per-Dyad `directory/*.yaml` solved registration, but the `.md` index re-introduces the
very shared-edit surface it forbids. So the index must be **generated**, not hand-edited.

## Concrete bug to fix alongside (low-hanging) — ✅ DONE (PR #12)
~~DIRECTORY.md `.md` vs `.yaml` entry-extension inconsistency.~~ Fixed in PR #12 (the self-registration
remedy): joining step, dyad-steward row, and siblings note now point at `.yaml`. The *structural*
separation below is still open.

## Proposed split (NOT executed)
- **`DIRECTORY.yaml` (or `.json`)** — machine-readable aggregate index, **generated** deterministically
  from `directory/*.yaml` (never hand-edited → no collision). Truth stays the per-Dyad files; this is
  the compiled view. *(Natural home for future machine fields — e.g. `subscribes:`/`borrows:` from
  `commons-change-awareness.md`.)*
- **`DIRECTORY.md`** — human-readable only: what the registry is + the Joining how-to + definitions.
  Governance/mechanism prose may move to `CONTRIBUTING.md`. Table becomes a generated section or a
  pointer to the yaml.

## Deps / siblings
`self-registration-remedy.md` (the dyad-steward entry + the `.md`/`.yaml` bug) · `commons-change-
awareness.md` (machine fields belong in the generated index) · onboarding follow-ups.
