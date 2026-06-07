# Friction intake: Sense → Discern → Intake, materialized by PROBEs running SPAOR

> **Status: CONVERGING (riff/rub, 2026-06-07).** How dyad-steward advances its OWN summits. Premise (FO):
> **observed friction is the fuel** — we cannot ground on *hypothesized* friction. Our board already
> confesses the gap (b2 honesty-bound: "a trail is worn in by walking, not imposed — our trails are
> pre-declared top-down today, not emergent"). This is the mechanism to flip top-down → friction-driven.
> Grounded on dyad-cairn's SPAOR + PROBE (← touchstone lineage); we EXTEND it (cairn runs SPAOR internally;
> we apply it to EXTERNAL Commons work, and build the sensing layer cairn left aspirational).

## The pipeline (the clip): Sense → Discern → Intake
- **Sense** — observe friction. Two kinds of sensor:
  - **passive** (fire-on-defect, automated): `preflight`/CSI guards (inward substrate), `digest.py` (Commons activity).
  - **active** — a **PROBE**: an expedition that goes out and surfaces friction we can't passively monitor
    (cold-path onboarding as a non-techie; the FR awaiting a cross-human response; a consumer dyad's real path).
- **Discern** — is the friction REAL, RECURRING, or STALE? Mechanism: **falsification** + cold-path + a
  recurrence count (one hit = noise; thrice = defect-earned). *We have this.*
- **Intake** — a confirmed friction becomes frontier trail(s). *We have this (frontier/rack).*
  The weak link was **active outward Sense** — that's what the PROBE supplies.

## PROBE — the materialization (a node-TYPE, from cairn)
A **PROBE** is a frontier trail whose job is to **observe / confirm-or-falsify a friction-condition**.
Its *only* allowed outputs (cairn's Probe Invariant):
1. **Confirm** the condition (friction is real) → spawn `PLAN → EXECUTE` trails (the DAG grows fractally).
2. **Falsify** the condition (friction is stale / not-real) → **ABORT the execution trail** (don't build).
   *This is [[cold-path-barriers-are-stale]] made physical — a probe's highest-value output is killing a
   trail we'd otherwise have built on a dead barrier.* (The digest falsifying the cross-human barrier = a probe.)

**PROBE is the only node-type that GROWS the frontier** (intake). **EXECUTE** nodes ship a result and may
NOT spawn nodes. So the frontier flips from top-down-hypothesized to **probe-grown-from-observation**:
a hypothesized friction enters as a PROBE; only a *confirming* probe yields EXECUTE trails.

## SPAOR — the loop each trail runs (applied EXTERNALLY = our extension)
**S**ense · **P**lan · **A**ct · **O**bserve · **R**eflect (the FO's "PLAN → EXECUTE → REFLECT" is the P-A-R
spine; Sense prepends, Observe precedes Reflect). Every node runs SPAOR; a PROBE structurally yields the
next DAG layer. **REFLECT feeds Discern → Intake** (crystallize what the probe observed; spawn or abort).
Cairn runs this on its OWN internal code (branch-per-node, Red/Green TDD gates). **We apply it to EXTERNAL
Commons/consumer friction** — a genuine extension; a probe like "cold-path onboarding" is not a TDD spike.

## Where we stand vs cairn
- **Ahead:** our rack carries provenance; cairn's `rack_state.yml` is an inert unused stub.
- **Extending:** external-SPAOR + the **sensing "S"** — cairn's is its weakest, mostly-unbuilt part
  (`quarry_parser.py` referenced-but-absent; `todo:`→DAG is an open probe). We can't port sensing; we build it.
- **Not porting wholesale:** cairn's `flow_state_manager` engine (git-branch-per-node, Red/Green PR gates,
  `retro_lock` [vapor], derived-status) is *internal-code-shaped* and doesn't fit external stewardship work.

## The fork — RESOLVED (FO "lean", 2026-06-07): (B) light graft, BUILT
- **(A) Full SPAOR engine** — port cairn's `bin/node` lifecycle + Red/Green gates. Rigorous; heavy;
  internal-code-shaped; carries cairn's vapor (retro_lock). **Not chosen.**
- **(B) Light graft** *(chosen + shipped)* — `frontier.py` now carries a **`type` field** (PROBE | PLAN |
  EXECUTE, default EXECUTE) + a **`FALSIFIED`** terminal status (PROBE-only: the probe's condition was
  refuted → trail aborted). PROBE is the only type that grows the DAG; EXECUTE ships. The SPAOR stages
  *are* the existing status flow (READY→ACTIVE→IN_REVIEW→DONE), no separate engine. Negative-controlled
  (bad-type, FALSIFIED-only-for-PROBE). The status flow walked live this session: the
  `friction_intake_probe_spaor` PROBE → confirmed → spawned `frontier_node_types_graft` (EXECUTE) → DONE.

## Node input/output invariants (the rub, 2026-06-07) — what makes the loop rigorous
Each node-type has a TYPED contract: what it may consume, what it may emit. The contract is what makes
"only a PROBE grows the DAG" enforceable and prevents waterfall/scope-creep.

| node | INPUT (consumes) | OUTPUT (emits — exactly) | hard invariant |
|---|---|---|---|
| **PROBE** | **one** *falsifiable* friction-condition (states what would confirm/refute) | exactly one of: **CONFIRM** (real + atomic → spawn ≥1 PLAN/EXECUTE); **FALSIFY** (stale → status `FALSIFIED`, abort); or **DECOMPOSE** (composite — investigating revealed *N* distinct sub-frictions → spawn one **child PROBE** per sub-friction, self → DONE) | verdict **source-grounded**, never asserted; ships **no** functional change; **stays atomic** (investigates one condition); the **only** type that grows the DAG |
| **PLAN** | a CONFIRMED friction (from a PROBE) — the *what/why* | a **spec**: the EXECUTE's acceptance-criterion + falsification_target ("done"=X; refuted if Y); spawn ≥1 EXECUTE | ships no functional change; optional (a PROBE may spawn EXECUTE directly when the *how* is obvious) |
| **EXECUTE** | a PLAN's spec (or a confirmed-simple friction) — **one** acceptance-criterion | **exactly one verified deliverable** meeting the spec (test passes / behavior confirmed; Commons work = a PR for FO gate) | output **verified** (verify-with-actual-tool), never asserted-done; **atomic** (one deliverable); **never** spawns nodes |
| **REFLECT** | a terminal node (DONE/FALSIFIED) | crystallized lesson → durable substrate (ledger/memory/doc) **+** any NEW friction → back to Sense (may spawn a follow-up PROBE) | the **only** place a trail's wisdom enters durable substrate; ships no functional change |

**The spine (4 cross-cutting invariants):** only PROBE grows the DAG · only EXECUTE ships · PROBE-verdict
grounded · EXECUTE-output verified · every node ends in REFLECT.

**EXECUTE plurality + serialization (the count, 2026-06-07 rub).** A PROBE/PLAN spawns **as many EXECUTEs
as there are independent atomic deliverables** — no fewer (bundling several into one mega-EXECUTE violates
atomicity) and no more (artificially splitting one deliverable is busywork). **Dependent ≠ parallel:** if B
needs A first, that's a dependency *edge* (A→B), not parallel siblings. The **DAG holds the plurality;
WIP-N=1 serializes the *doing*** — many EXECUTEs may EXIST (READY/queued), but exactly one is ACTIVE at a
time. So "more than one EXECUTE" never means "work two at once": decompose widely, climb one at a time.

**PROBE input is ONE; output may be MANY — via DECOMPOSE (2026-06-07 rub).** A PROBE *investigates* a single
friction-condition (stays atomic), but investigating can **reveal** the condition is *composite* — several
distinct sub-frictions. Then the PROBE may **not** confirm-the-bundle and jump to EXECUTEs; it must
**DECOMPOSE**: spawn one **child PROBE per sub-friction** (each its own falsifiable condition) and go DONE.
Each child then independently CONFIRMs (→ EXECUTE) or FALSIFYs (→ abort). So there are **two distinct
fan-outs, at different stages:** (1) *friction-space* fan-out = PROBE → N child PROBEs (DECOMPOSE; frictions
discovered-but-unconfirmed); (2) *deliverable* fan-out = one CONFIRMED-atomic friction → N EXECUTEs (the
prior rub). **Shortcut:** if the sub-frictions are *already observed/confirmed* in the same probe (no further
investigation needed), you may collapse straight to EXECUTEs — which is what `probe_csi_armstate` did (both
"daemons disarmed" and "registry incomplete" were directly observed by the read). The DECOMPOSE rule binds
when the discovered sub-frictions are **un**confirmed hypotheses that each need their own grounding.

## Recursive: SPAOR governs sensor-development too (FO, 2026-06-07)
Building a sensor is itself a trail that runs **PROBE → PLAN → EXECUTE → REFLECT** — we do **not** build a
sensor on hypothesized friction. Every candidate sensor enters as a **PROBE** that confirms-or-falsifies
the friction it would catch, *first*. (Demonstrated: `probe_onboarding_friction` is queued as a PROBE to
cold-path the racked Tim signals before any onboarding-UX sensor/fix is built.) The methodology governs
its own tooling — fractal, all the way down.

Cross-refs: `acceleration-thesis-and-steward-summit.md` (the sensing analog of the encode/irreducible cut) ·
`adopt-cairn-frontier-rack-csi.md` · `board.md` b2 · memory [[cold-path-barriers-are-stale]] · [[verify-with-actual-tool]] · [[dont-optimize-the-human-out]].
