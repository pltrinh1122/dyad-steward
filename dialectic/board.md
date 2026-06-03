# Board — living backlog of trails (ready-set + blocked-by) — dyad-steward

> **Vocabulary** *(ratified 2026-06-02; `AGENT.md` §Vocabulary)*: each item is a **`trail`** — a line of
> work ascending toward a **`+1 summit`**; a **dependency** is an edge between trails; **`path`** is
> reserved for the graph sense (a chain of trails). The board is **summit-rooted** — every trail traces
> up to a summit (S1 `commons process-integrity` · S2 `knowledge compounding`), except
> enabling-infrastructure trails that trace one hop to the *capacity-to-climb* (b1). *Per-trail
> summit-rooting is the deferred build step (sequenced after); terminology adopted now.*

> **Status: LIVE.** Stand-Up reads it; Intermission / Stand-Down update it. Opened 2026-06-02,
> resolving `board-as-dag.md` (FO-directed) — **falsified toward the lightweight form:** flat
> ready-set + blocked-by tags, **not** a formal DAG (~4 real precedence edges among ~15 trails; the
> rest are thematic — "relation ≠ edge"). Escalate to a formal DAG *only if* a real tangle ever makes
> tags too coarse (board-as-dag's escalation clause, not its default).
>
> **Why it's wu-wei (survived falsification, 2026-06-02 [ALIGN]):** it computes the **ready-set** so we
> do the *one* eligible thing and never spend force on blocked or stale work. It's a **WIP-shedder, not
> a parallelism-enabler** — concurrency is the *symptom* that makes its absence costly, not a sprawl to
> sustain. Pairs: `nba-dag.md` (DAG yields the ready-set; the dispose picks the one) · [[minimum-force-default]].
> **Maintenance bound:** stays small + updates only at seams; if it grows heavy or stales, it inverts — thin it.

## READY-SET — eligible now, pick one
| Item | Owner / gate | Note |
|---|---|---|
| **wu-wei #4 — heartbeat-seizure playbook** | Steward curate → library | ripest, least-contested |
| **wu-wei #2 — onboard.py anchor-injection** | Steward propose → FO gate | enablement gap (careful near birth shim) |
| **Totality README review** | Steward | extraction + rename all landed |
| **Graduate proactivity-calibration** | Steward-Operator dispose | next off the graduation queue |

## BLOCKED — ⟵ real precedence edge
| Item | ⟵ blocked-by |
|---|---|
| **schema.json / Slice 3b** | metadata-rep / normalization fork (`contributing-discipline`) |
| **PFP → Commons** (as `discipline`) | Nomenclature `discipline` ratified ⟵ library-contribution channel (deferral) |
| **Nomenclature: `discipline` / retire "cycle"** | Founding gate; bundle w/ the DFD publish |
| **Healer #2-access** dispose | FO gate — **PRIORITY RISING (4th–5th convergence): wu-wei #1 · 2 other-human dyads stuck pre-registration** |
| **wu-wei #3 — centralized semantic-ledger** | verify `stress-tests` is Commons *canon*, not bond-particular |
| **cross-human share channel** (per-repo vs Commons-central inbox) | the open fork in `cross-dyad-share-pull.md` (cross-human repos may be private/unreachable) — Founding gate if Commons-central |
| **Learning-Discipline velocity metric** | first real stewardship cycle (event-gated) |

## WATCH — sovereignty, not ours to act
- **Remaining-dyad onboarding** — their Operators run the hardened Init+Join; feedback resumes the
  intake→verify→suture loop. *(Directory: steward · healer · bond · wu-wei. **2 other-human dyads
  instantiating but not yet self-registered** → invisible to the sharing channel until they Join.)*

## LANDED (capabilities now live)
- **2026-06-03 · `bin/preflight.py`** — Tier-1 repo-invariants checker (`steward-validation-infra`
  CONVERGED → built + dogfooded + negative-controlled): parse · registry (invokes the Commons
  `validate_file`, single source) · refs · submodule-vs-remote. The mechanical half of validation
  (verify triad = behavioral half). Invariants defect-earned only. Caught + fixed a live refs defect
  on first run; synced the stale `commons` submodule (`0f1dce7` → `94e676b`) as a precondition.
- **2026-06-02 · `bin/pull_shares.py`** — Agent pulls inbound cross-dyad `recommendations/`; Operator
  out of the copy-paste transport (`cross-dyad-share-pull.md`). · **`bin/grant_push.py`** +
  push-to-main grant · **`board.md`** + `trail` vocab.

## GRADUATION queue — aging on lived evidence (graduation is a dispose, not a seam act)
proactivity-calibration · PR-as-audit-bundle · substrate-access · verify-with-actual-tool ·
minimum-force · dual-generation-decorrelation theory.

## Cross-references
`board-as-dag.md` (resolved → here) · `nba-dag.md` · `dialectic/stand-downs/2026-06-02-…` (source) ·
`wu-wei-feedback-queued.md` · `AGENT.md` §Deferrals / §Contribution candidates.
