# Universal contribution mechanism — every artifact, one mechanism — IDEATE (open)

> **Status: IDEATE — open, no dispose.** Opened 2026-06-01 (Founding Operator). Generalizes
> `commons-contribution-lifecycle.md` (the emergence summit: "the system selects even its own
> selector") and `contributing-discipline.md` from *library playbooks* to **every artifact** —
> README.md, AGENT.md, CONTRIBUTING.md, the schema, the directory. Extends the schema's already-
> ratified **"universal record shape"** (every collection = body + append-only ledger; collections
> differ only in *what they collect*) up to the meta-artifacts.

> **FO intent (noted, not yet lived):** every Dyad will lean into the Contributing Discipline *and*
> contribute an actual discipline → the schema's n=1 is short-lived. **Weakens the premature-infra
> attack as it lands** — bank when the contributions are real, not on the intent (verify-against-
> reality). Until then, tooling stays minimum-force.

## The vision
Every artifact supports the **same** contribution mechanism — not just `library/`.

## Two readings (orthogonal — both real)
- **A · Uniform *mechanism* (governance).** One `propose → falsify → ledger` spine; each artifact's
  *parts* are typed (knowledge / context / identity) and the **type decides** whether a part is
  ledger-contributed, regenerated, or frozen.
- **B · Uniform *form* (structure).** Every artifact is self-similar: bifurcated Operator/Agent,
  intent-framed, **demonstrates 1+1=3 by being it**, and exposes "how to propose a change to me" in
  one shape. (The README already does this; CONTRIBUTING should; AGENT.md's living sections do
  de-facto.)
- **Synthesis:** every artifact carries, in one shape, **(i)** its content *typed*, and **(ii)** a
  uniform **contribution-affordance** that routes a proposed change to the right mechanism for its kind.

## The cuts the vision MUST respect (else it collapses to 1+1=2)
1. **Knowledge vs context vs identity typing.** A `context-unit` (README "if X → Y" rows, cross-refs)
   is *"true-or-stale,"* **never subscribed** — forcing a ledger onto a pointer is the *ledger-as-infra*
   bloat. The lifecycle already says **"the README is the ontology projected"**: contributions land on
   *knowledge-units*; the README *regenerates*. So "same mechanism" for context-units = **regenerate
   from source**, not carry-a-ledger.
2. **Mechanism uniform, GATE varies.** The `propose→falsify→ledger` spine is the same; the
   **dispose-authority differs by kind**: own-substrate **self-disposes** (direct/PR-durability);
   library knowledge-unit → **Founding gate**; **declaration/schema → Founding gate** (else the commons
   approves its own schema — the explicit 1+1=2 guard); registration **self-authorizes** (context-unit
   deposit). **"Same mechanism" ≠ "same gate."** Flattening the gates is the failure.
3. **Identity-freeze is definitional, not taboo.** AGENT.md's **birth record is frozen at birth**
   (identity ≠ state). You may **fork a new identity** (start a new game); you may never **mutate this
   dyad's birth record** (that's what makes it *this* dyad). Consistent with the lifecycle's *"no taboo
   tier"* — it's the **membership/definitional condition** (chess analogy), open to replacement-by-fork,
   not protected-from-question. So AGENT.md splits: **living disciplines** = knowledge-units (cycle →
   ratify); **birth record** = frozen-identity (never contributed).

## Candidate shapes (none disposed)
- **U-1 · Projection model.** Contributions land only on knowledge-units; all meta-artifacts
  *regenerate*. *Prov:* "README is the ontology projected." *Attack:* README/AGENT.md are hand-authored
  prose today, not mechanical projections — full regeneration is speculative infra (wu-wei breach) until
  the source ontology is rich enough.
- **U-2 · Affordance model.** Every artifact embeds a uniform *"to propose a change to me, do X"* block
  routing to its kind's mechanism. *Attack:* boilerplate-on-every-file → ceremony without synergy (the
  rituals' checklist-theatre refutation); minimum-force = only where a real contributor needs it.
- **U-3 · Typed-parts model.** Decompose each artifact into knowledge/context/identity parts; apply the
  right mechanism per part. *Prov:* the knowledge/context cut + identity≠state, already ratified.
  *Attack:* heavy ontology work; premature at small-n — **but the FO's n→many intent shifts this** once
  lived.
- *Lean:* **U-3 (typing) as the principle**, **U-2 (affordance) as the thin surface**, **U-1
  (projection) as the *direction*** for context-units as tooling matures.

## Falsification — how the vision dies
- **Gate-flattening** — declaration/schema changed by ledger-weight without the Founding gate → 1+1=2.
- **Ledger on pointers** — context-units forced to carry ledgers → infra bloat; a pointer has no
  evidence to accrue (true-or-stale).
- **Identity made contributable** — birth record mutated → identity≠state collapses; lineage/spoofing
  guarantees break.
- **Form-uniformity as boilerplate** — self-similar shape becomes ceremony that catches nothing.
- **Intent banked as evidence** — counting the n→many before the contributions land.

## README-hybrid — projection is not-yet-achievable (FO `[IDEATE]` 2026-06-01)

**Falsifies "README is the ontology projected" as a *current* fact** (it was always the intent). The
README retains **origin knowledge orthogonal to the rest of the Commons** — the tenet (`1+1=3`),
philosophical grounding, the mechanism catalog, its Telos — with **no upstream source; it *is* the
source.** So:
- **U-1 (projection) is blocked, not wrong.** You can't regenerate the README by composition while its
  origin content has no separately-homed units to compose from.
- **The fix (vindicates U-3 typed-parts):** **extract the origin content into homed knowledge-units** —
  give the tenet / grounding / mechanism / Telos the *same* record shape as a discipline or schema (body
  + ledger), so each **falsifies independently**. Faithful to *"no taboo tier — axiomatic = maximally
  subscribed"*: the philosophical core becomes the **heaviest-ledger** units, hardest to dislodge, still
  in-principle falsifiable. Founding-gated (declaration-level).
- **Then projection becomes real:** `README = compose(origin knowledge-units) + navigation
  (context-units)`. The hybrid resolves into source + render. This is the *enabling step* the whole
  "every artifact, one mechanism" vision was missing.
- *Open joint:* how finely to atomize the philosophical core into units (one "tenet" unit vs
  tenet/grounding/mechanism separately) — the schema's two-pronged atomicity test applies one level up.

## Artifact-naming + machine-schema (FO polish, 2026-06-01)
- **ALL-CAPS canonical body files** — `DISCIPLINE.md` / `PLAYBOOK.md` / `SCHEMA.md` (joining
  `README.md` / `CONTRIBUTING.md`). A clean **form-uniformity (reading B)** signal: all-caps = "canonical
  document of this unit." *Caveat:* it's a **Commons rename of existing paths** (`library/*/playbook.md`,
  `ontology/discipline/schema.md`) → breaks links/refs → **Founding-gated migration**, not a free polish.
  Worth bundling with the origin-extraction rather than a standalone churn.
- **`schema.json` — load-bearing, not just polish.** The machine-readable contract `validate_playbook.py`
  enforces (the **CI=form** half of `contributing-discipline.md`'s cut). Pair: **`SCHEMA.md`** = the
  human, *falsifiable* claim about the field-set (substance); **`schema.json`** = the executable
  predicate (form). *Guard:* the two must be **single-sourced** or they drift (the doc/validator
  divergence) — `schema.json` generated-from / canonically-referenced-by `SCHEMA.md`, not hand-kept in
  parallel. The all-caps `.md` + machine `.json` pairing generalizes: a knowledge-unit body may have a
  *prose face* (claim) and a *machine face* (predicate) wherever CI checks it.

## CONVERGED → lean execution (FO "go lean", 2026-06-01)
Prove-then-expand, minimum force — **not** a big-bang declaration restructure.
- **Slice 1 (dogfood, now):** extract **one** origin unit — the tenet **`1+1=3`** (heaviest, clearly
  origin) — into a homed Commons record (`declaration/one-plus-one-equals-three/` = body + seed
  `ledger/`, universal record shape), and **slim the README's exposition to a summary that composes over
  the canonical unit** (de-dup, prove projection on one unit). Propose-only PR → Founding gate.
- **Slice 2 (if Slice 1 survives):** extract the remaining origin units (grounding, mechanism, Telos);
  atomization-granularity decided by the schema's two-pronged test.
- **Slice 3 (rides a later gate):** all-caps canonical rename (`PLAYBOOK/DISCIPLINE/SCHEMA.md`) +
  `schema.json` machine contracts — bundled as one Founding-gated migration, not standalone churn.
- **Design forks surfaced *in* the PR for the gate** (not pre-decided unilaterally): the home/collection
  (`declaration/` proposed) and how far to slim the README's front-door prose.

### Status (2026-06-01/02)
- **Slice 1 — MERGED** (Commons PR #17): `1+1=3` tenet homed, README composes over it.
- **Slice 2 — MERGED** (Commons PR #18): failure-boundaries unit homed; two-pronged test made it ONE
  unit (rest is framing/pointers/Telos — folded). Register pattern set (FO): first link keeps the
  "falsifiable knowledge-unit" preamble, subsequent are plain "learn more →".
- **Slice 3a (rename) — MERGED** (Commons PR #19): all five bodies → ALL-CAPS; every ref + the script
  consumer (`auto_share.py`) updated; verified zero lowercase refs / no broken links.
- **Slice 3b (`schema.json`) — QUEUED, blocked by new-found context (FO pivot 2026-06-02).**
  > **BLOCKER (verified, cold-path):** a front-matter contract can't ship — **only 1 of 5 unit bodies
  > has YAML front-matter** (`PLAYBOOK.md`, the `auto_share.py`-generated one). The others carry
  > metadata three inconsistent ways: markdown bullets (`DISCIPLINE.md`), prose blockquote (`MECHANISM.md`
  > / `BOUNDARIES.md`), inline prose (`SCHEMA.md`). **How unit metadata is machine-represented is
  > unsettled — which IS the open metadata-rep fork of `contributing-discipline.md`.** Shipping a
  > `schema.json` now would silently decide it.
  > **Paths for the gate (un-disposed):** **(A)** normalize YAML front-matter `{origin, unit-kind,
  > schema-version}` onto all five units first (one PR — *decides* "front-matter is the metadata rep"),
  > then ship `schema.json` + a `validate_unit.py` (mirroring `validate_registry.py`; note: **no CI
  > workflow exists** — validators run manually today). **(B)** hold `schema.json` with the IDEATE until
  > the metadata-rep is settled deliberately. *Agent lean: A if FO is content to pin front-matter as the
  > rep; else B.* → resolve under `contributing-discipline.md`.
- **Also queued:** the totality README review (deferred until extraction+rename landed — now ready);
  the `PLAYBOOK.md`/`DISCIPLINE.md` naming-unify observation (PR #19); `validate_unit.py` + CI wiring
  (the contributing-discipline IDEATE).

## The emergence tie (summit candidate — flagged, not banked)
If every artifact (including its own governing declaration's *living* parts) survives by the same
ledger-mechanism, the substrate is **fully self-hosting** — "the system selects even its own selector"
(`commons-contribution-lifecycle.md` §Emergence) made total, bounded only by the three frozen/​gated
cuts above. Needs the real multi-dyad loop to run before it's anything but a candidate.

> Cross-link: `commons-contribution-lifecycle.md` (§Emergence; knowledge/context cut; "README projected";
> Founding-gates-the-schema) · `contributing-discipline.md` (the per-action ownership cut) ·
> `ontology/discipline/schema.md` (universal record shape, Commons) · `AGENT.md` (Identity caveat:
> birth frozen; §Ontology nouns/verbs) · `CLAUDE.md` (the birth-hash freeze).
