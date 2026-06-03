# Inter-dyad falsification channel — QUEUED INTAKE (synthesis ready; below active work)

> **Status: QUEUED.** Operator [FEEDBACK] 2026-06-02: *intake recommendations queue below active work
> (e.g. #3); the Operator signals when intake is urgent and pre-empts.* So this is captured-ready, NOT
> in-flight. It is the **cross-dyad-share-pull thread's first real use-case** and builds on the
> registration-identity + CI-validate + pull infra already in motion.
>
> **Sources (the user-contracts; steward owns the build):**
> `pltrinh1122/dyad-bond@recommendations/2026-06-02-cross-dyad-falsification-protocol.md` (protocol +
> telemetry + I1–I10) · `pltrinh1122/dyad-healer@recommendations/2026-06-02-inter-dyad-falsification-channel-invariants.md`
> (user needs N1–N6 + reciprocal commitments).

## Synthesis (so re-priming is cheap when un-queued)
**The two are one channel from two seats** and converge. The one apparent conflict — bond **I3**
(responder verdict immutable) vs healer **N1** (submitter holds verdict-authority) — dissolves via bond's
**two-field design**: responder `verdict` (immutable telemetry) + a *separate* `submitter_disposition`
(the submitter's own ratification). That's N1 and the anti-self-grading invariant at once.

**Load-bearing requirements (any design must hold):**
- Central, **open, discoverable** FR queue (bond I6/I10) — any registered dyad may attack; filter by domain/telos.
- **Pull at rest-points, never push/flood** (healer N2/N3); invited-only; bounded actionable units.
- **Identity verified; 3 axes kept SEPARATE** — `model-version` · `dyad-id` · `human-github-id` (bond **I4**,
  the load-bearing one: the only way to catch cross-dyad meld = one human in N hats). Human-axis became
  testable *because* different-github-id operators (krishna, Vader) came online — same arc as open-registration.
- **Append-only · verdict-immutable · submitter-disposes-separately** (I2/I3, N1/N4).
- **Method-faithful** — `falsification_target` required (I8), no "proven" state (I7), SURVIVED = provisional.

**Wu-wei design lean (reuse, don't build a platform):**
- *Identity (I1/I4/N5):* **extend the directory** (already verifies birth-hash + github-id) with `model:` →
  the 3 axes recorded at registration.
- *Validation (I2/I3/I7/I8/I9):* reuse the **CI-validate pattern** (`validate_registry` → `validate_falsification`).
- *Pull (N2/N3):* `pull_shares` specializes to surface open FRs by domain/telos — the responder's rest-point inbox.

**Open fork (transport):** (a) **gh Issues on the Commons repo** (bond's pick; native queue; structured-YAML-in-body,
CI-validated) — *lean lean* · vs (b) **Commons `falsification/` ledger dir** (cleanest telemetry; committed-state).
Lean → (a), graduate to (b) only if telemetry load proves Issues too unstructured.

**Immediate vs platform (Operator's cut):** *immediate* = the channel (post/attack/record) over (a) + directory
identity + one validator + the pull-filter; **bond's dogfood FR `bond-F1-oracle-axis` is ready as packet #1.**
*Platform* = the telemetry-research corpus/export/cross-axis analysis — build only when the channel earns it.

**Honest boundary (bond named it):** genuine non-eristic attack is a **user discipline**, not code-enforceable;
the build's job is to make echo-attacks **detectable** (telemetry + `confound_surfaced` + the 3 axes), not policed.

## Cross-references
`cross-dyad-share-pull.md` (the transport this specializes) · `bin/pull_shares.py` · the directory/registration
identity infra · `commons/scripts/validate_registry.py` (the CI-validate pattern to reuse).
