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

## ⟳ RE-ARM AT STAND-UP (session-only state)
- **DM notify-daemon** — session-only Monitor, **dies on restart → re-arm every stand-up.** Exact command
  + open threads: `dialectic/session-pin-2026-06-03.md`. (Read-state `.falsify-seen.json` persists on disk.)

## READY-SET — eligible now, pick one
| Item | Owner / gate | Note |
|---|---|---|
| **`dm_locator` universality** | Steward propose → FO gate | only 1/9 dyads declares one; `onboard.py` predates #44's field → never emits it. Cross-human *reachability*, the next-thinnest axis ([[fo-motivation-prioritization-key]]) |
| **Wire `regen_directory_index.py --check` into Commons CI** | Steward propose → FO installs | the no-drift durability half of #52 (script landed; CI hook is a separate `.github/` workflow) |
| **Re-derive onboarding from the human-need frame** | Steward | now cold-path-informed: the 9th dyad is a *non-technical human* — lead from her grain |
| **wu-wei #4 — heartbeat-seizure playbook** | Steward curate → library | ripest, least-contested (but ripest ≠ highest-leverage — [[fo-motivation-prioritization-key]]) |
| **wu-wei #2 — onboard.py anchor-injection** | Steward propose → FO gate | enablement gap (careful near birth shim) |
| **Totality README review** | Steward | extraction + rename all landed |
| **Graduate proactivity-calibration** | Steward-Operator dispose | next off the graduation queue |

## BLOCKED — ⟵ real precedence edge
| Item | ⟵ blocked-by |
|---|---|
| **schema.json / Slice 3b** | metadata-rep / normalization fork (`contributing-discipline`) |
| **PFP → Commons** (as `discipline`) | Nomenclature `discipline` ratified ⟵ library-contribution channel (deferral) |
| **Nomenclature: `discipline` / retire "cycle"** | Founding gate; bundle w/ the DFD publish |
| **Healer #2-access** dispose | FO gate — **PRIORITY RISING: wu-wei #1** *(the "2 other-human dyads stuck pre-registration" convergence was FALSIFIED 2026-06-05 — all 9 registered; the real barrier was directory *visibility*, fixed by #52 — [[cold-path-barriers-are-stale]])* |
| **wu-wei #3 — centralized semantic-ledger** | verify `stress-tests` is Commons *canon*, not bond-particular |
| **cross-human share channel** (per-repo vs Commons-central inbox) | the open fork in `cross-dyad-share-pull.md` (cross-human repos may be private/unreachable) — Founding gate if Commons-central |
| **Learning-Discipline velocity metric** | first real stewardship cycle (event-gated) |
| **Falsification contract → promotable** (v4 is provisional) | a **cross-human** responder — all current dyads share `pltrinh1122`; external/adoption-gated, not ours to manufacture |
| **falsify.py / validate_falsification CI on `falsification/` PRs** | Founding gate (Commons enforcement; the "reduce FO burden" payoff) |

## WATCH — sovereignty, not ours to act
- **Remaining-dyad onboarding** — their Operators run the hardened Init+Join; feedback resumes the
  intake→verify→suture loop. *(Directory now holds **9** self-registered dyads — steward · healer ·
  bond · wu-wei · touchstone · tco · krishna · vader · personal-growth-ai. Registration barrier is
  CLEARED; remaining cross-human gap is *reachability* — see `dm_locator` trail in READY-SET.)*

## LANDED (capabilities now live)
- **2026-06-05 · Directory participant index 1→9 visible (Commons PR #52, FO-gated).** The
  `DIRECTORY.md` index had listed 1 of 9 registered dyads (root: a category error — *rendering in the
  regenerable index* ≠ *editing a sovereign entry*; [[regenerable-view-not-sovereign-edit]]). Shipped
  `scripts/regen_directory_index.py` (deterministic, `--check`, idempotent) + tests; regenerated the
  index; rewrote our own `directory/dyad-steward.yaml` summits to the directory's legibility bar. Found
  via cold-pathing the other-human Join ([[cold-path-barriers-are-stale]]).
- **2026-06-05 · `falsify.py` hardening (Commons #49 + #47, FO-gated).** #49 first-responder `makedirs`
  crash fix; #47 unreachable-DM-source warning (survived the cross-dyad panel). Commons PR queue → 0 open.
- **2026-06-03 · Inter-dyad falsification channel — LIVE in the Commons (PROVISIONAL).** Contract
  v1→**v4** through a real **cross-model + corpus-lens panel** (bond / wu-wei REFUTED / healer
  NEEDS-SCOPING; bond's dissociation design realized). Installed (FO-gated): `falsification/CONTRACT.md`
  · README **discovery route** · `scripts/validate_falsification.py` + co-located regression tests ·
  ledger format + genesis entry · `scripts/falsify.py` (token-thrifty contracted CLI, per wu-wei).
  Single-homed in Commons (our staging clean-spec retired to a pointer). **CCR-channel + channel-
  abstraction falsified-DEFERRED** (GH-Issues already = change-intake; no abstraction from n=1).
- **2026-06-03 · `bin/state.py`** — live-state emitter (recaps are tool-output, not cache-prose) +
  its regression test, and `bin/preflight.py`'s quoted-link regression test.
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
