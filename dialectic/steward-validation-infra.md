# Steward validation infrastructure — the wu-wei level — IDEATE (open)

> **Status: IDEATE — open, no dispose.** Opened 2026-06-02 (FO `[ALIGN]` "reflect on how we prevent
> this" + `[IDEATE]`). Context: dyad-bond is on the frontier of an **independent validator for
> generative work**; dyad-wu-wei has mature `test/` infra *because it generates a lot of code*. Question:
> **the most wu-wei level of validation infra for Steward-generated work.** Complements the (behavioral)
> verify triad in `AGENT.md`.
>
> **HOME = Steward's repo (FO `[ALIGN]` 2026-06-02).** This is a **Steward *verb*** — validation of *our
> own generation* — so per `nouns-vs-verbs` / single-home it lives **here** (`dyad-steward/`), NOT the
> Commons. It does **NOT** own or subsume the Commons-side validators (`validate_registry`/`validate_unit`/
> `schema.json` are Commons *nouns*, home there, Founding-gated). Our infra **invokes** them as one input
> to our pre-PR preflight and **adds** checks the Commons doesn't (our-repo reference integrity, our
> dialectic/kb structure, Commons-bound artifacts *before* we PR them). *Earlier drift corrected: I had
> it subsuming the Commons validators — wrong home.*

## `[ALIGN]` — the prevention gap (why now)
This session's defects were all caught **reactively**: summit-YAML corruption (Healer cold-path),
CONTRIBUTING 404 (Healer), rename link-breaks (caught by my manual grep), PR-state (FO + the graduated
verify rule), the `yaml.safe_load` corruption (an ad-hoc test I ran by hand). **The verify triad is the
*behavioral* half** (a human/agent grounds reality) — it doesn't scale and keeps an actor in every loop.
The missing half is **mechanical**: a standing invariants check the *artifact runs on itself* before a
PR. Behavioral discipline + mechanical infra = the two halves; the mechanical one is the emergence move
(no Steward in the per-check loop).

## The wu-wei cut — proportion infra to *our* grain, not dyad-wu-wei's
dyad-wu-wei generates **code** → a mature `test/` harness is *its* wu-wei. The Steward generates mostly
**structured artifacts** (YAML registry, markdown knowledge-units, README/CONTRIBUTING prose, the
declaration) **+ small scripts** (`onboard.py`, validators). **Copying a code-test harness wholesale
would be working against our grain (over-force).** Our wu-wei level is an **invariants / conformance
checker** (artifact-shaped), with code-tests a *secondary* tier only for the scripts.

## Tiers (escalate only as the grain demands — minimum force first)
- **Tier 1 — repo-invariants checker (the wu-wei sweet spot).** ONE plain-Python script (mirroring
  `validate_registry.py`'s no-framework style), run **pre-PR**, asserting the structural invariants we
  actually depend on. Catches the artifact defect-classes we've *lived*. **This is the answer to "the
  most wu-wei level."** Homes in **our** repo; **invokes** `commons/scripts/validate_registry.py` (reuse,
  don't reimplement — single-source the Commons rule) and **adds** our-side checks. The Commons-side
  `validate_unit`/`schema.json` (3b) stay a **separate, Commons-owned, Founding-gated** track.
- **Tier 2 — script behavioral tests.** As our *code* surface grows (`onboard.py` is already non-trivial),
  a light test for cold-path behaviors (plain-clone-vs-submodule, idempotent re-run, the YAML-corruption
  case). *Here* dyad-wu-wei's `test/` pattern fits — scoped to our small script surface, not their large
  one. Escalate when script complexity bites (we're near it).
- **Tier 3 — independent generative validator (dyad-bond frontier).** For what structural checks
  *can't* reach: does a unit's claim/refutation actually hold, is a testimonial real. This is the
  `contributing-discipline` **CI=form / FO=substance** cut — the validator does **form**; **substance
  stays the irreducible human/Founding gate** (mistaking the two is 1+1=2). Borrow dyad-bond's when it
  matures; **do not build now** (it's the frontier, not the baseline).

## The invariants list — each EARNED by a lived defect (verify-triad-ledger style)
*Wu-wei: an invariant enters only when a real defect proves it missing — not speculative coverage.*
1. **Parse validity** — every YAML/JSON parses. *(latent; cheap.)*
2. **Schema conformance + per-element types** — registry entries & front-matter match required field-sets;
   each list element is the right type. *(defect: summit-YAML corruption — PR #20.)*
3. **Universal record shape** — every knowledge-unit dir = body + append-only `ledger/`; no flat-file
   shortcut. *(defect-risk: the schema's own invariant; 3b metadata-rep.)*
4. **Reference integrity** — every relative link / referenced path in `.md` resolves to an existing
   file. *(defects: CONTRIBUTING 404; the rename link-break risk.)*
5. **Identity gate** — `origin ∈ directory/`; birth-hash recomputes. *(existing mechanical gate.)*
6. *(Tier 2, behavioral)* **onboard cold-path** — fresh dir → real submodule; idempotent re-run.
   *(defect: plain-clone-vs-submodule, PR #14 miss.)*

## Falsification — how this idea dies
- **Over-build** — a test *framework* (pytest harness, CI matrix) before the need → anti-wu-wei, the
  speculative-build refutation our threads keep hitting. Tier 1 is one script.
- **Speculative invariants** — invariants not earned by a lived defect → coverage theatre; bloat.
- **Form mistaken for substance** — the checker passing read as "the work is good" → 1+1=2 (it only
  certifies *shape*; the contest's reality is the human gate). Same guard as `contributing-discipline`.
- **Wrong grain** — importing dyad-wu-wei's code-test maturity onto our artifact-grain → force against
  the grain; the exact thing this IDEATE exists to avoid.

## Sub-thread — where does a Commons script's regression test home? (FO `[IDEATE]` 2026-06-02)
*`validate_registry.py`'s verification should be durable so script modifications pass "regression."
Steward or Commons?*

**Answer: Commons — co-located with the script** (`commons/scripts/test_validate_registry.py` or
`commons/tests/`). **Principle: a test homes with the thing it guards, owned by whoever owns that
thing.** `validate_registry.py` is a Commons *noun* → its regression test is Commons-owned, in the
Commons.
- **Co-location** — the test travels with the artifact; whoever has the script has its guard.
- **Guards *any* modifier** — other dyads, or the FO editing directly — **not only when the Steward is in
  the loop.** A test homed in *our* repo would leave a non-Steward modification unguarded → the
  regression is fiction exactly when the Steward steps out (the emergence breach). **This is the decider.**
- **Authorship ≠ home** — we authored the script *and* the test, but it homes with the Commons noun it
  guards (same as the declaration units we authored that home in the Commons).
- **No duplication** — the Steward Tier 1 preflight **invokes** it (as it invokes `validate_registry`
  itself); single-home preserved.

**Refines the tiers: Tier 2 (script behavioral tests) splits by the script's OWNERSHIP.** `onboard.py`
*and* `validate_registry.py` are **Commons scripts** → their tests home in the **Commons** (Founding-
gated). The Steward's Tier 2 covers only *our-repo* scripts (currently ~none). So **most testing infra
for the code we generate homes in the Commons**, because that code is Commons-owned — the Steward-repo
infra (Tier 1) is mostly our-artifact conformance + orchestration.

**Mechanical note:** no Commons CI workflow exists yet → "pass regression" means a **runnable co-located
test now**; wiring it to CI on script-touching PRs is the eventual Commons-side enforcement (a
Founding-gated escalation, the real "reduce FO burden" payoff).

## CONVERGED (FO "converge", 2026-06-02)
*A committed candidate — falsifiable, no longer diverging. Not a dispose; the build is a separate
Steward-Operator go.*

**The design — "validation by ownership, minimum force, defect-earned":**
1. **Two homes (nouns-vs-verbs).** *Steward repo (verb):* a Tier 1 invariants checker over **our**
   generation + a preflight that **invokes** Commons validators on Commons-bound artifacts before we PR.
   Steward-Operator-gated; ours to build. *Commons (nouns + their guards):* the Commons scripts, **their
   regression tests** (co-located), and the `schema.json`/`validate_unit` (3b) — all Founding-gated.
2. **Three tiers, escalate by need.** **T1** = Steward invariants checker (plain Python, pre-PR — the
   wu-wei level, ready now). **T2** = behavioral/regression tests **homed by each script's ownership**
   (mostly Commons — `onboard.py`/`validate_registry.py` are Commons scripts). **T3** = dyad-bond's
   independent generative validator = **form, not substance** (substance stays the human/Founding gate;
   conflation = 1+1=2). T3 is frontier — watch dyad-bond, don't build.
3. **Invariants are defect-earned** (verify-triad-ledger model): one enters only when a lived defect
   proves it missing. Ledger so far: per-element types · reference integrity · record-shape · cold-path.
4. **Two halves.** Behavioral (the verify triad in `AGENT.md`, an actor grounds reality) + mechanical
   (the invariants infra, the artifact self-checks). The mechanical half is the **emergence move** — no
   Steward in the per-check loop.

**Settled:** the home cut · tier structure + wu-wei proportioning to *our* grain · defect-earned
invariants · test-homes-with-the-artifact-it-guards · CI=form / FO=substance.

**Open (deferred, NOT converged):** 3b metadata-rep normalization (Founding-gated; blocks Commons
`schema.json`/`validate_unit`) · T3 timing (waits on dyad-bond) · Commons **CI-wiring** (the real
"reduce FO burden" payoff; Founding escalation) · the #2-access Joining fork (separate Healer thread).

**Single next action:** stand up the **lean Tier 1 invariants checker in our repo** — earned by ≥3 lived
defects, Steward-Operator-gated, **decoupled** from the blocked 3b. A Steward-Operator *go* proceeds;
everything else is gated/deferred.

## Feed-back candidate
The pattern — **a repo-invariants checker whose invariants each carry their motivating defect** — is a
library-`discipline` candidate for *every* Dyad (proportioned to each one's generated grain), and it
dovetails with dyad-bond's independent-validator frontier (Tier 3). Flagged, not banked.

> Cross-link: `AGENT.md` §NON-NEGOTIABLE verify triad (the behavioral half) · `contributing-discipline.md`
> (CI=form/FO=substance; `validate_*` ; schema.json) · `universal-contribution-mechanism.md` (3b
> metadata-rep — a *Commons-side*, Founding-gated track, distinct from this Steward-repo infra) ·
> `healer-init-join-feedback.md` (the lived defect ledger) · `AGENT.md` §Ontology (nouns-vs-verbs —
> *why* this homes here).
