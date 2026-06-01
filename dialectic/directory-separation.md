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

## Concrete bug to fix alongside (low-hanging)
DIRECTORY.md is internally inconsistent on the entry extension: header says source of truth is
`directory/<dyad>.yaml`, but the Joining steps (line 35) and the table link (line 44) say
`directory/<dyad>.md` / `dyad-steward.md`. The **actual files are `.yaml`** → the `.md` references are
dead. (Folds into the self-registration remedy too.)

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
