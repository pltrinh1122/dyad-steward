# Board — living backlog of trails (ready-set + blocked-by) — dyad-steward

> ## ⚠️ RETIRED 2026-06-06 → the live backlog is now the **frontier**
> The READY-SET / BLOCKED / LANDED trails moved to **`frontier_state.yml`** (sovereign DAG) →
> regenerated **`frontier.md`** (projection). Read: `bin/frontier.py` · stack: `bin/rack.py`.
> Single-source now — **do not edit the tables below; edit the frontier** (adopted from dyad-cairn,
> 2026-06-06; `dialectic/adopt-cairn-frontier-rack-csi.md`). The tables below are **FROZEN** as of the
> migration. Sections the frontier DAG does *not* model (⟳ RE-ARM daemon · WATCH · GRADUATION queue) are
> retained here as the live home; LANDED prose stays as the archive (compact DONE nodes live in the frontier).

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
| **Learning-loop scaffold → seed** (build) | Steward propose → FO gate; **co-sequence w/ cairn** | *Investigation DONE — survived-falsification candidate (`dialectic/learning-loop-scaffold.md`): N=2 independent derivations (wu-wei ⟂ steward-lineage), portable, substrate-forced.* Build = add the missing **verbs** to `onboard.py`: harvest-trigger + reload-ritual + empty store (seed ships nouns, not verbs). **Same architecture surface as cairn** — left apart, cairn's PR sets the library architecture this lives inside. Felt-+1 cycle-two crux still open (riff). |
| **DISCOVERY: async-event context-switch efficiency** *(retro 2026-06-06, Operator)* | Steward discovery | *Is our servicing of async interrupts (DM daemon fires) efficient — esp. for the **Operator**, who can't context-switch fast (the scarce resource — [[fo-motivation-prioritization-key]])?* Lived this session: daemon fired ~4× incl. mid-riff; some high-value (cairn's real proposal), some noise (repeat `unreachable:N` re-confirms after my sync). Q: triage/batch to a rest-point vs interrupt? Prior art to harvest: touchstone `dialectic/event-interrupt-servicing.md`; ours [[intake-queues-below-active]]. |
| **Wire `regen_directory_index.py --check` into Commons CI** | Steward propose → FO installs | the no-drift durability half of #52 (script landed; CI hook is a separate `.github/` workflow) |
| **Re-derive onboarding from the human-need frame** | Steward | now cold-path-informed: the 9th dyad is a *non-technical human* — lead from her grain |
| **wu-wei #4 — heartbeat-seizure playbook** | Steward curate → library | ripest, least-contested (but ripest ≠ highest-leverage — [[fo-motivation-prioritization-key]]) |
| **wu-wei #2 — onboard.py anchor-injection** | Steward propose → FO gate | enablement gap (careful near birth shim) |
| **Totality README review** | Steward | extraction + rename all landed |
| **Graduate proactivity-calibration** | Steward-Operator dispose | next off the graduation queue |
| **Steward summit — RATIFIED 2026-06-06** ✅ | done (FO gavel) | AGENT.md §Telos sharpened + `commons/directory/dyad-steward.yaml` summit #3 (Commons PR #56 merged) + pushed `066cca0`. Record: `dialectic/acceleration-thesis-and-steward-summit.md`. README front-door updated to match. |
| **Extend `auto-merge-registration.yml` → cover own-entry UPDATES** *(survivor: "directory update should auto-merge")* | Steward propose → FO installs (protected `.github/`) | **Verified gap (read the workflow):** the Action auto-merges pure ADDs only (`status: added`); modify-existing routes to human review *by design* → my summit-update PR #56 was merged **manually**, not auto. Extend to auto-merge a *modify* iff: (a) touches only the author's OWN `directory/<entry>.yaml`, (b) PR author == entry owner, (c) **birth_hash + name UNCHANGED** (only summits/locator/dm_locator mutable), (d) `validate_file` PASS. Strictly harder than the add-case (must guard frozen fields + ownership). |
| **`dfd`→`pfp` ref-decay (repo-wide) + preflight refs-coverage gap** *(survivor: README falsification, peer-confirmed)* | Steward curate — **grain-confirm first** | README locally fixed (3 dead refs + dangling `§DFD` anchor ×2). Decay is repo-wide: `AGENT.md:248`, `contributing-discipline.md:144`, `commons-contribution-lifecycle.md:181,299`, `dyad-ui.md:40,57,74,142`. Confirm **DFD-vs-PFP are distinct concepts vs a rename** before any mass-fix ([[ingraining-lives-in-substrate]]: fix the source, but only once the grain's confirmed). Also: `preflight.py [refs]` passed clean despite the dead README links → it doesn't lint `.md`-prose links or `§`-anchors; widen coverage. |

## BLOCKED — ⟵ real precedence edge
| Item | ⟵ blocked-by |
|---|---|
| **cairn Commons-architecture proposal** (DM `2026-06-06-commons-architecture-proposal.md`) — *referee pass → FO gate* | queued behind active minimum-scaffold thread. cairn proposes bifurcating commons into `bin/` (Chisel: `mason` CLI + `stone.yaml` validators) vs `stones/` (Library). **Steward read (verified):** (1) **not ours to ratify** — Commons architecture = FO dispose; we falsify-as-peer → carry survivor to FO. (2) principle is sound but **already instantiated** — `commons/scripts/` ⊥ `library/`/`falsification/`/`ontology/`; `bin/`+`stones/` are *parallel renames* → forks the tree it wants to unify (single-home). (3) `stone.yaml` likely **dup/forks our CONVERGED library schema** `{trigger,move,claim,refutation,ledger}` — needs the field-diff. Note: cairn's +1 summit #1 = cross-dyad distillation → **directly the minimum-scaffold thread.** |
| **schema.json / Slice 3b** | metadata-rep / normalization fork (`contributing-discipline`) |
| **PFP → Commons** (as `discipline`) | Nomenclature `discipline` ratified ⟵ library-contribution channel (deferral) |
| **Nomenclature: `discipline` / retire "cycle"** | Founding gate; bundle w/ the DFD publish |
| **Healer #2-access** dispose | FO gate — **PRIORITY RISING: wu-wei #1** *(the "2 other-human dyads stuck pre-registration" convergence was FALSIFIED 2026-06-05 — all 9 registered; the real barrier was directory *visibility*, fixed by #52 — [[cold-path-barriers-are-stale]])* |
| **wu-wei #3 — centralized semantic-ledger** | verify `stress-tests` is Commons *canon*, not bond-particular |
| **cross-human share channel** (per-repo vs Commons-central inbox) | the open fork in `cross-dyad-share-pull.md` (cross-human repos may be private/unreachable) — Founding gate if Commons-central |
| **Learning-Discipline velocity metric** | first real stewardship cycle (event-gated) — *= the acceleration-meter half of testing the Steward Invariant* |
| **Causal attribution of acceleration** *(wu-wei-deferred)* | **event-gate: first sustained acceleration PLATEAU.** Operator SEES acceleration, can't establish causation (model-improvement + N are confounds). Build NO causal instrumentation until the plateau binds (premature = anti-wu-wei). → `acceleration-thesis-and-steward-summit.md` §Deferred |
| **Portfolio-compounding → form `README`/declaration** *(survivor: "update the-dyad-practice/README.md?" → NO, not yet)* | the form's OWN bar (form README:14–16): a tenet **composes over a canonical falsifiable home** (claim·refutation·ledger, survived contest), e.g. `declaration/one-plus-one-equals-three/`. The portfolio-compounding *"why-the-Commons-at-multi-dyad-scale"* has **no such home** — n=1, observed-not-established, causal-link plateau-deferred. Gated on: **earn a mechanism-home → survive cross-dyad/cross-human contest → THEN compose into the form** (FO dispose; steward *proposes*, never edits form-canon — [[regenerable-view-not-sovereign-edit]]). Form README has **zero mechanical defects** (all refs resolve, 2026-06-06). |
| **Steering-load meter** (Σ depth on the Operator) | needed to falsify the Steward Invariant; build co-timed with the plateau, not before |
| **Falsification contract → promotable** (v4 is provisional) | a **cross-human** responder — all current dyads share `pltrinh1122`; external/adoption-gated, not ours to manufacture |
| **falsify.py / validate_falsification CI on `falsification/` PRs** | Founding gate (Commons enforcement; the "reduce FO burden" payoff) |

## WATCH — sovereignty, not ours to act
- **Remaining-dyad onboarding** — their Operators run the hardened Init+Join; feedback resumes the
  intake→verify→suture loop. *(Directory now holds **9** self-registered dyads — steward · healer ·
  bond · wu-wei · touchstone · tco · krishna · vader · personal-growth-ai. Registration barrier is
  CLEARED; remaining cross-human gap is *reachability* — see `dm_locator` trail in READY-SET.)*

## LANDED (capabilities now live)
- **2026-06-05 · `onboard.py` teaches the `dm_locator` remedy (Commons PR #53, FO-gated, merge `898dcea`).**
  Cold-path reframe: not "universality" — `dm_locator` is needed **only for a PRIVATE anchor** (`falsify.py`:
  absent ⇒ `locator` is the mailbox); the 8 public dyads need nothing, and the 2 UNREACHABLE sources
  (krishna, personal-growth-ai) are private-anchor-with-no-mailbox — **sovereign to fix, not ours**
  ([[commons-multihuman-is-a-human-need]]). #53 is **enablement**: the scaffold + completion message now
  surface the remedy (PUBLIC mailbox, SAME owner as `locator`) so the next private-anchor dyad self-serves
  instead of registering silently unreachable. Verified vs `validate_registry.validate_file` (same-owner
  PASS · wrong-owner FAIL). +7 −0, one file.
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
PR-as-audit-bundle · substrate-access · verify-with-actual-tool ·
minimum-force · dual-generation-decorrelation theory.
*(Graduated: proactivity-calibration → `AGENT.md` §NON-NEGOTIABLE, 2026-06-10, Steward-Operator gate.)*

## Cross-references
`board-as-dag.md` (resolved → here) · `nba-dag.md` · `dialectic/stand-downs/2026-06-02-…` (source) ·
`wu-wei-feedback-queued.md` · `AGENT.md` §Deferrals / §Contribution candidates.
