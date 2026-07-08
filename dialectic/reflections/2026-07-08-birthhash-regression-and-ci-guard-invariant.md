# Reflection — 2026-07-08 · read-state audit → birth_hash regression → the CI-guard invariant

> CSS+SH form (bond D3 `kb/reflection-discipline.md@main`, re-oriented 2026-07-08). Lands by being
> committed — no CTA, no ratification. Session arc: DM read-state audit (PR #80) · library testimonial
> pins + spartan CONTRIBUTING (PR #81) · birth_hash regression fix (PR #82) · the CI-guard invariant +
> birth_hash guard (PR #83). All four merged.

## CONTINUE — Agent-observed, worth keeping

- **Re-derive from the canonical spec when the tool and reality disagree.** The birth_hash regression
  surfaced only because the value was recomputed by hand from the IDENTITY CAVEAT formula
  (`sha256(git show 2a9dc10:CLAUDE.md ‖ %cI)`) instead of trusting the directory value *or*
  `compute_birth_hash` — which was itself the bug. When a tool's output and a spec's definition diverge,
  the spec is authoritative and the tool is the suspect. Sharpens [[verify-with-actual-tool]]: the "actual
  tool" can be the defect; the oracle of last resort is the written formula.
- **Ground the full substrate before deciding.** Every correct design turn this session followed a
  grounding pass that changed the plan — `ontology/discipline/SCHEMA.md`, `compute_birth_hash`, the
  frozen-`birth_hash` auto-merge gate. [[grounding-is-full-substrate]] paid out repeatedly.
- **Drive guards end-to-end, not just unit-test them.** `verify_birthhash.py` was exercised live —
  PASS on `4c42be0b`, FAIL on injected `72ba645f`, SKIP on a private anchor — which proved it catches the
  real defect *and* reproduces in CI, before it ever ran as a check. The [[verify]] discipline.

## START — commitments forward

- **Before authoring a Commons rule for a collection, grep the whole collection-space for an existing
  canonical home.** #81 proposed ledger filename + entry-schema rules in `CONTRIBUTING.md` without first
  finding `ontology/discipline/SCHEMA.md`, which *already* defines the universal record shape and the
  ledger entry `{contributor, timestamp, testimonial}`. That created a second-home risk (the very
  `single-home` the library teaches), reconciled only after the Operator's "will it operate on a
  ledger_schema?" forced the grounding. The full-substrate sweep is a **precondition to proposing canon**,
  not a courtesy.

## STOP — failure named + corrected

- **Stated a conclusion about a derivable fact before re-deriving it — twice, confidently, backwards.**
  Told the Operator "4c42be0b is bogus/superseded — re-stamp to `72ba645f`" and framed `4c42be0b` as an
  "orphan," both inferred from the directory value + a stale dialectic note. Re-derivation showed the exact
  opposite. This is the verify NON-NEGOTIABLE's predicate-trigger — a done-claim ("X **is canonical** / **is
  bogus**") about mutable/derivable state — applied to *identity*, and skipped. Corrected same-session, but
  only after the Operator said "re-derive." **The trigger must fire on `is-canonical`/`is-bogus`, not only
  on `merged`/`landed`.**

## SH — the Operator's intent-clarity at the interface (verbatim-grounded; no manufactured balance)

- **Should-Hold** *(credit, standing pattern)* — elevating a specific fix into a general invariant *at the
  moment the fix lands*. Verbatim: *"add/edit commons-invariant: self-reported claims that can be
  mechanically verify should be mechanically verify via CI-check guards."* That directive turned a one-off
  birth_hash guard into a standing Commons bar (now with `validate_ledger.py` as instance #2). Hold it.
  Sibling pattern, same session: *"every declarative statement is a falsifiable statement"* — one directive
  that became the whole CONTRIBUTING rewrite's pruning filter. Load-bearing principles, stated explicitly as
  directives, did more than any amount of local instruction.
- **Should-Have** — **none meeting the materiality bar.** The session's false claims (the `4c42be0b`
  inversion) originated in Agent inference, not ambiguous Operator intent; the Operator's *"i'm confused, is
  the problem that we don't know the owner of the stamp?"* was a clarifying correction of the Agent's frame,
  not an interface miss of the Operator's. Per no-manufactured-balance, nothing is recorded here.
