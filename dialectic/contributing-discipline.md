# Contributing Discipline + CI-checkable playbook quality — IDEATE (open)

> **Status: IDEATE — open, no dispose.** Opened 2026-06-01 (Founding Operator `[IDEATE]`): *a
> Contributing Discipline dyads self-adopt to produce "high-quality" playbooks, and that we can
> CI-check to reduce the Founding Operator's review burden — instead of relying only on an example
> `playbook.md`.* Slots into `commons-contribution-lifecycle.md` (the channel) + `ontology/discipline/
> schema.md` (the field-schema) — **this is their operationalization, not a new frontier.**

## The reframe — the pieces already exist

1. **The schema already defines "high-quality."** `ontology/discipline/schema.md` (Commons, Founding-
   gated, versioned) = the field-set `{trigger, move, claim, refutation, ledger}`, **explicitly built
   so "Curate is a diff, not a judgment"** — i.e. designed to be mechanized. It even *seeks a second
   discipline to map (n=1)*.
2. **The CI precedent already exists.** `scripts/validate_registry.py` is a field-presence linter for
   directory yaml. A `validate_playbook.py` mirroring it is a small, faithful extension.
3. **The lifecycle already articulated the gate's *shape*.** Its Governance §: the Steward "checks the
   proposal **follows the form** AND carries a **>N=1 testimonial with specific examples**"; and the
   contribution gate is **"mechanical, Steward-authored but not Steward-run … rejected by a predicate,
   not a judgment — Steward owns the *rule*, not performs the *check*."** The FO's IDEATE = extend that
   *registration-verification* predicate to *playbook-quality*, + package the producer side as a
   self-adoptable discipline.

## The load-bearing cut (and the falsification line)

**CI/predicate can verify falsifiability's *form*; it can NEVER verify the contest was *real*.**
- CI checks (mechanizable, the schema's structure-side): record-shape, all five fields present + well-
  formed, `claim` distinct from `refutation`, ledger has ≥N Dyad-stamped `{contributor, timestamp,
  testimonial}` entries, `origin` birth-hash recompute-verifies, schema-version pinned.
- The Founding gate keeps (irreducible, the content-side): *did the cycles actually happen and survive*,
  are the kill-conditions genuine. **Collapsing this into CI is the 1+1=2 breach** — the commons
  approving itself by checklist, the NON-NEGOTIABLE's sycophancy guard switched off.
- **And even the FO-read doesn't certify quality.** Per the lifecycle's own core claim, real quality is
  decided **downstream** — by the *accruing cross-dyad ledger* (Participate/Curate), not at admission.
  So CI + discipline are an **admission floor**, not a quality guarantee: they (a) keep malformed /
  unfalsifiable units out, and (b) shrink the FO's residual judgment to its irreducible, cheap core.

**Burden reduction is real but bounded — and has its own failure mode:** if CI removes the *malformed*-
burden but the FO then *trusts* CI and stops reading substance, net integrity drops while burden drops.
The burden removed must be exactly the mechanizable part, leaving the substance-read intact.

## Tended-first nudge on the framing

The IDEATE led with *"reduce my (FO) burden."* The **primary tended is the contributor dyad** producing
the playbook. Design the discipline from *their* enablement first — a routine that makes producing a
falsifiable unit easy + a local self-check they run before proposing — and **the FO-burden-reduction
falls out as the consequence** (CI pre-filters → the gate shrinks to substance). Designing from the
FO-burden grain first risks building a *gate* (filter) and under-building the *producer routine* (the
generative half the FO also asked for: "self-adopt to **produce**").

## Candidate shapes (provenance-tagged; none disposed)

- **C-A · Schema-as-gate (thin CI only).** `validate_playbook.py` enforces the schema field-set +
  universal record shape; rejects non-conformant PRs. *Prov:* `validate_registry.py` + lifecycle
  predicate-gate. *Attack:* checks presence, not quality; it's a *filter*, not the *producer routine*
  the FO asked for → necessary infra, under-delivers the "discipline" half.
- **C-B · Contributing Discipline as a self-applied meta-cycle.** The producer routine = run the Dyad
  Practice on the candidate playbook: draft `claim` → arm `refutation` → run dyadic-cycles attacking it
  → append each *survived* cycle to `ledger` → self-run the linter before proposing. *Prov:* our own
  **Learning Discipline** + the schema's `ledger`. *Attack:* intra-dyad self-attack can be sycophantic
  and is invisible to CI; the *real* falsifier is cross-dyad (Resonating). Stronger bar: a **>N=1 ledger
  of dated lived cycles** (harder to fake than a claimed self-attack; already the lifecycle's bar).
- **C-C · Two-layer (synthesis direction).** Layer-1 CI = form (C-A); Layer-2 Founding = substance
  (reads testimonials); the **Contributing Discipline (C-B)** is the producer routine targeting Layer-1
  as definition-of-done and producing genuine entries for Layer-2. *Prov:* the lifecycle Governance §
  ("follows-form" → CI; ">N=1 testimonial w/ examples" → FO) made operational. *Attack:* even Layer-2
  can be fooled by well-written fake testimonials → admission is a floor; quality is earned downstream.
- **C-D · CI as coach, not just gate.** `validate_playbook.py --explain` tells a contributor *which*
  falsifiability-form requirement is missing; optional `scaffold_playbook.py` emits the skeleton.
  *Prov:* enablement / tended-first. *Attack:* over-build — linter + explainer + scaffolder at **n=1
  real playbook** (only `proposal-framing` exists) repeats the lifecycle's own *speculative-build /
  Ledger-as-infra* refutation. Minimum force: ship the bare linter first; add explain/scaffold only when
  a real contributor stumbles.

## Falsification invariant — how this idea dies

- **CI-as-judge** — predicate mistaken for *the* gate → 1+1=2 (checklist-approval, sycophancy unguarded).
- **Premature infra** — tooling built before a second real playbook exists (schema is itself n=1).
- **Self-attack certification** — "quality" rests on intra-dyad falsification, bypassing the cross-dyad
  ledger that actually falsifies.
- **Burden-shift illusion** — FO trusts CI and stops reading substance → integrity drops with burden.

## The meta-dogfood (open joint, attractive)

The **Contributing Discipline would itself be a `discipline` conforming to the schema** → a candidate
for the schema's *sought second instance (n=2)*, advancing the schema's own falsification *while*
defining the contribution process. Clean, faithful home — but exactly the kind of self-reference to keep
falsifiable, not assume elegant.

## Sub-thread — who owns each action? (FO `[IDEATE]`, 2026-06-01; open)

*CONTRIBUTING.md serves **both** a new Operator and a new Agent (like the rebuilt README), and it's
unclear who owns the mechanism for the individual actions of the Contributing playbook.*

**The load-bearing principle (candidate): own the action your *partner* is bias-prone on.** This is
`kb/one-plus-one-equals-three.md` applied per-action. The contribution process debiases each half:
- **Operator owns *lived attestation*** (the `ledger` testimonial: "I practiced this, it survived").
  Irreducibly Operator-sole — the **Agent's native bias is sycophancy; it would fabricate survival.**
  This is the anti-1+1=1 anchor. Mirrors onboarding's *"the birth commit is a human act."* The Agent
  records/formats the entry; it cannot *attest* it.
- **Agent owns *falsification*** (the `refutation` kill-conditions; the aggressive attack on the claim).
  The **Operator's native bias is defending their own claim**; an Operator-owned refutation softens into
  rubber-stamp → 1+1=2. The Operator *validates* the kill-conditions are lived/real; the Agent generates
  them adversarially.
- **Everything else is a normal dyadic cycle** (Agent generates → Operator validates), because the Agent
  carries load and the Operator debiases: `claim` (Operator originates the intent/value → Agent
  formalizes falsifiably → Operator validates), `move`/`trigger` (Agent distills to wu-wei-atomic steps →
  Operator validates against lived practice).

**So the answer to "who owns each action" is not a fixed table — it's a cut:** the only *sole-owned*
acts are the two the other half's bias would corrupt — **Operator-sole: the ledger attestation;
Agent-sole(-led): the refutation/attack.** All other actions are generate→validate, Agent-led-by-load.

**Audience bifurcation (mirrors the README):** CONTRIBUTING.md splits into an Operator-facing part
("your part: the intent behind the claim, the lived testimonial, the dispose") + a fenced Agent block
("carry the load: formalize the claim, generate refutations, distill the move, draft the ledger entry,
run the linter, open the PR"), with the **one Operator-sole act flagged** the way onboarding flags the
birth commit. Because it serves a dyad that *hasn't yet internalized the Practice*, the doc should
**demonstrate 1+1=3 by its own structure** — the contribution process *is* a dyadic cycle.

### Candidate shapes (none disposed)
- **C-1 · Bifurcated doc (README pattern).** Operator section + fenced Agent block. *Attack:* a rigid
  two-list freezes ownership and hides the handoffs/co-ownership (claim) → loses the dialectic.
- **C-2 · Per-field owner tags on the schema.** Annotate each schema field with an owner. *Attack:*
  over-ontology at n=1; ownership varies by dyad (a technical Operator) → premature.
- **C-3 · The principle, not a table (lean).** State the debiasing cut + show the bifurcation as the
  *worked example*, not the law; a dyad applies/deviates. *Attack:* a principle with no *default* may
  leave a new dyad unsure — an enablement gap in the very doc meant to close it → pair with a default.
- **C-4 · It's a dialectic, not a split.** Most actions are generate→validate; the only sole-owned acts
  are the two bias-corrupted ones (ledger=Operator, refutation=Agent). *Attack:* under-specifies *who
  drafts first* (generate-leadership matters for load/cost).
- *Lean:* **C-3 + C-4** — the debiasing cut as the rule, a README-style bifurcation as the default
  worked-example, the two sole-owned acts flagged.

### Falsification — how the ownership model dies
- **Agent owns the ledger** → fabricated testimonials → sycophancy → **1+1=1** (the core breach).
- **Operator owns the refutation** → defensive softening → contest unreal → **1+1=2**.
- **Rigid ownership table** → freezes a dialectic, misses handoffs → over-ontology at n=1.
- **Over-bifurcation** → a hard two-doc split hides that each action's halves *interact* per cycle.

> Cross-link: `commons-contribution-lifecycle.md` (parent channel; Governance § predicate-gate) ·
> `ontology/discipline/schema.md` (Commons; the "high-quality" field-spec, n=1) ·
> `scripts/validate_registry.py` (Commons; the CI precedent) · `DYAD.md` §NON-NEGOTIABLE (the
> 1+1=2 / sycophancy guard the CI-as-judge failure trips) · `kb/dfd.md` (the n=5 ledger exemplar).
