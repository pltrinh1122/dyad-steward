# Steward validation infrastructure — the wu-wei level — IDEATE (open)

> **Status: IDEATE — open, no dispose.** Opened 2026-06-02 (FO `[ALIGN]` "reflect on how we prevent
> this" + `[IDEATE]`). Context: dyad-bond is on the frontier of an **independent validator for
> generative work**; dyad-wu-wei has mature `test/` infra *because it generates a lot of code*. Question:
> **the most wu-wei level of validation infra for Steward-generated work.** Complements the (behavioral)
> verify triad in `AGENT.md`; subsumes the queued `validate_registry`/`validate_unit`/`schema.json`.

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
  most wu-wei level."** It also **subsumes** `validate_registry` + the queued `validate_unit`/schema.json.
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

## Feed-back candidate
The pattern — **a repo-invariants checker whose invariants each carry their motivating defect** — is a
library-`discipline` candidate for *every* Dyad (proportioned to each one's generated grain), and it
dovetails with dyad-bond's independent-validator frontier (Tier 3). Flagged, not banked.

> Cross-link: `AGENT.md` §NON-NEGOTIABLE verify triad (the behavioral half) · `contributing-discipline.md`
> (CI=form/FO=substance; `validate_*` ; schema.json) · `universal-contribution-mechanism.md` (3b
> metadata-rep — Tier 1 subsumes it) · `healer-init-join-feedback.md` (the lived defect ledger).
