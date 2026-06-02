# Is the Board a dependency-DAG? — RESOLVED (falsified toward the lightweight form)

> **Status: RESOLVED 2026-06-02 (Steward-Operator [ALIGN], "falsify").** The proposition (*the Board is
> a formal DAG*) was **falsified toward the lightweight form**: a flat **ready-set + blocked-by tags**
> carries the ~4 real precedence edges (among ~15 items) at lower cost; the rest are thematic
> ("relation ≠ edge"). Surviving wu-wei justification = the **ready-set** (do the one eligible thing,
> shed blocked/stale work — a WIP-shedder, not a parallelism-enabler). → **Living board: `board.md`.**
> A formal DAG stays an *escalation* slot only if a real tangle makes tags too coarse. *Seed retained below.*

---

> **Original (QUEUED) seed — FO-directed 2026-06-01.** Proposition to *falsify*: **the
> Board (our running queue of open/queued work) is organized per a dependency graph (DAG).** Not to be
> resolved now — captured so the future ALIGN can attack it. Tightly coupled to `nba-dag.md` (NBA→DFD:
> the DAG computes the ready-set, DFD disposes the pick) — this is essentially *dogfooding nba-dag on
> our own backlog.*

## Seed for the falsification (both sides — do NOT resolve here)

**Why it might hold (the thesis):** Board items already carry real dependency edges —
- self-registration remedy ⟵ PR #11 (birth-hash logic must land first)
- existing-dyad README fix ⟵ existing-dyad *invariant* settled (the 3-state model)
- DIRECTORY separation ⟷ change-awareness (machine fields live in the generated index)
- onboarding-followups ⟵ … etc.
If items have deps and a ready-set, a DAG is the honest structure, and `nba-dag.md` already says how to
prioritize over one. Organizing the Board as a DAG = the first lived instance of that discipline.

**Where it might break (the antithesis to mount):**
- **Relation ≠ dependency edge.** Many "links" between items are *thematic* (same area), not *ordering
  constraints*. A DAG needs true precedence edges, not "these are related."
- **Cycles / mutual shaping.** e.g. DIRECTORY-separation ⟷ change-awareness ⟷ self-registration may
  co-shape rather than strictly order → not acyclic → not a DAG.
- **Over-ontology (the `dyad-work.md` refutation).** A flat priority list + a handful of "blocked-by"
  tags may carry the same weight at lower cost; formalizing a DAG could be ceremony that adds
  navigation cost without making the next pick cheaper.
- **Typing the nodes.** nba-dag's open gap is *types-of-work* to type DAG nodes; without it the Board-DAG
  infers nodes ad-hoc — the very thing nba-dag flags as unfinished.

**The test (nba-dag's own claim):** does organizing the Board as a DAG make *next-pick* demonstrably
cheaper/clearer than a flat queue + blocked-by tags? If not → drop it (don't codify).

> Sibling: `nba-dag.md` (the discipline) · `dyad-work.md` (types-of-work gap, over-ontology refutation).
