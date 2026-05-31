# Discipline Ontology — the field-schema for a `discipline` knowledge-unit — LIVE CYCLE (DRAFT)

> **Status: DRAFT — extracted 2026-05-31 (Steward Operator `[ALIGN]`) from
> `commons-contribution-lifecycle.md` §data-model.** Held as **its own record so it is falsified
> *independently* of any instance** (e.g. DFD). **Why the split is load-bearing:** the ontology and an
> instance carry *different evidence streams* — this ontology's ledger accrues *every discipline that
> maps cleanly* (each a survived test of the **schema's** completeness/orthogonality); an instance's
> ledger (e.g. `kb/dfd.md`, n=5) accrues *lived corrections of that discipline* (tests **its** claim).
> Conflate them in one record and you cannot tell whether *the instance died* or *the schema died*.
> Separating records **is the structure-vs-content discrimination applied one level up** — the same
> cut two-pronged atomicity (below) exists to enable. **The ontology is not sacred:** it is a
> knowledge-unit subject to this same model, falsifiable like any other. **Home:** Steward-owned
> (the Steward owns the *types*; the community owns the *tokens* — `AGENT.md` §Ontology). Promotion to
> the form is a **declaration change → Founding gate**.

## The claim (this ontology's own falsifiable +1)

**`{trigger, move, claim, refutation, ledger}` (+ `name` as identifier, `mechanism` as a derived tag)
is the orthogonal, two-pronged-atomic field-set for a `discipline` knowledge-unit** — *complete*
(every real discipline maps onto it with no leftover and no empty field) and *orthogonal* (each field
answers a question no other does, and diffs independently), so that **Curate is a diff, not a
judgment**: the Steward mechanically discriminates **structure-divergence** (different fields present →
maybe a fork) from **content-divergence** (same field, different atoms → a refinement to merge).

## Two-pronged atomicity — the criterion *(PINNED, `[ALIGNED]` 2026-05-31)*

An atom (a field, and within a list-valued field each content item) must be **both**:

1. **independent** — it diffs cleanly (varies without forcing other atoms to change); this is
   orthogonality recursed from field-level down to atom-level. → serves *content-vs-structure
   discrimination*.
2. **wu-wei / load-bearing** — drop-tested: *removing it loses the +1*. → serves *subset
   interpretability* (B's move ⊂ A's move is a **refinement** iff the dropped atoms were
   non-load-bearing — B's ledger proves it — else a **fork** asserting a different claim).

"wu-wei move" is **not a new field** — it is this criterion *instantiated per list-valued field*
(move → drop loses the +1; refutation → each condition alone can kill; ledger → one survived
dyadic-cycle; mechanism → one catalog tag). It also **stops the atomization regress**: stop splitting
when each unit is drop-test load-bearing.

## The fields, under two-pronged falsification (casualties surfaced — the test *improved* the schema)

- **survive both prongs (clean):** `trigger` (when it applies) · `move` (ordered load-bearing steps) ·
  `ledger` (atomic testimonials = survived dyadic-cycles — **each Dyad-stamped:** a ledger entry is the
  triple `{contributor Dyad-ID, timestamp, testimonial}`; see §Provenance).
- **`claim` & `refutation` — PINNED SEPARATE, collapse-flag armed** (`[ALIGN]` 2026-05-31). May be
  adjacent (refutation ≈ operational negation of claim), but independence is **unproven from n=1**, so
  *let evidence decide*: a second variant that **tightens refutation while keeping claim** proves
  independence → keep; if refutation is always re-derivable → **merge**. Forcing it now =
  premature-convergence. (Participate produces the deciding variant.)
- **`mechanism` — demoted to a *derived tag*** (open): if every move-step is wu-wei-atomic, each step
  implies its mechanism, so the set is *computable from move*, not independently authored → fails
  prong-1 as a field. Kept as a derived tag for Curate's family-diff, **not** an authored field.
  *(Open: drop entirely vs keep-as-derived.)*
- **`name` — a context-unit identifier**, not a knowledge-field: drop-fatal but carries no falsifiable
  content (you cannot *refute* a name). Rides inside the unit as a handle. *(Earns its keep in the
  consumer-facing `DIRECTORY.md` projection — a hash is unreadable to a newcomer.)*

## Provenance — the Proposal envelope (a context-unit, not a knowledge-unit)

*Resolves the Operator `[ALIGN]` gap: what binds a **Dyad-ID** to a proposed unit.* A **Proposal carries
no falsifiable content of its own** (the *discipline* is what's falsifiable; the testimonial's
*sufficiency* is what's contested) → it is a **context-unit**: a provenance envelope that "points true."
**Analogy:** a Proposal is to a Discipline as a **git commit is to a tree** — the discipline is the
content (content-hashed); the proposal is the *header* (proposer, parent, target) pointing at it.

**It is not a separate persistent record** — it **dissolves into fields**, deposited by the
proposal *transaction* (the PR; ephemeral, deposits on merge):

- **unit-level** (set once at creation): `origin` = **proposer Dyad-ID** *(← the association asked for)* ·
  `unit-hash` (sha256 of the discipline content) · `unit-kind` (discipline|term|ritual|mechanism) ·
  `schema-version` (which ontology version it conformed to — so Curate diffs against the right schema) ·
  `lineage` (parent `unit-hash` if a variant = hash-ancestry).
- **entry-level** (accrues, per ledger entry): `{contributor Dyad-ID, timestamp, testimonial}`.

So **the proposal *is* the first Dyad-stamped ledger entry** (`origin` = `ledger[0].contributor`);
Participation appends more stamped entries; a fork is a new unit whose `lineage` → parent and whose
`ledger[0]` is the forker. Everything composes from fields we already have:

- **association proposer ↔ discipline** = `origin` + `ledger[0].contributor`
- **per-Dyad weight** = `ledger` length sliced by `contributor` *(weight is earned/derived — never
  self-asserted)*
- **lineage** = parent-`unit-hash` + origin Dyad-ID

**Soft-joints:** (1) ~~`schema-version` requires the ontology itself to be versioned~~ **RESOLVED
2026-05-31:** version handle = **`@ 2026-05-31`**; the schema is **published to the Commons** as its own
knowledge-unit at `the-dyad-practice/ontology/discipline/schema.md` (+ `ontology/discipline/ledger/`),
so `library/*/discipline.md`'s `schema-version` resolves there. **Universal record-shape invariant
(Founding-gated 2026-05-31, n=2 pressure-test):** *every* Commons knowledge-unit collection (`library/`,
`ontology/`, any future) uses the identical shape **`<collection>/<name>/` = body + append-only
`ledger/`** — no flat-file shortcut even at n=1 (a flat body + shared `ledger/` collides on the 2nd
record). Collections differ only in *what they collect* (instances vs schemas), never in *shape*.
(2) `origin` vs `ledger[0].contributor`
redundancy — *lean: derive* origin = ledger[0].contributor (minimum force), unless origin must survive
recomposition of ledger entries.

**Candidate field-set (PROPOSED):** **{`trigger`, `move`, `claim`, `refutation`, `ledger`}** + `name`
(identifier) + `mechanism` (derived). Tighter than the original 7-field version.

## Ledger — survived tests of *this schema* (distinct from any instance's ledger)

| # | Discipline mapped | Result | What it tested |
|---|---|---|---|
| 1 | **DFD** | clean — no leftover, no empty field; the falsification *tightened* the entry (folded mechanism→derived, name→id) | completeness + orthogonality on a real, settled discipline |

> n=1. The schema is **a proposal seeking its second testimonial** — the next discipline mapped (or a
> variant from another dyad) either compounds this ledger or refutes the schema.

## Falsifiable claim & refutation conditions

**Claim:** the field-set is complete + orthogonal + two-pronged-atomic (above).

**Refuted if:**
- **Leftover content** — a real discipline carries load-bearing content with **no field to hold it**
  → the set is incomplete; add a field (and that field-addition is itself a schema-variant to contest).
- **A field never diffs independently** across real variants → it isn't orthogonal → **collapse it**
  (the armed `claim`/`refutation` flag is exactly this test, pre-loaded).
- **Atomicity fails to discriminate** — a subset-divergence stays uninterpretable even with the
  two-pronged test → the criterion doesn't do the Curate-as-diff work it claims.
- **Sub-kind misfit** — `term`/`ritual` units can't use this set (a `term` has no "move"), and no clean
  per-sub-kind schema emerges → "discipline ontology" was over-generalized; it's discipline-specific
  only (which may be fine — but then the claim's scope narrows).

## Open joints (the live generative surface — push even while unsettled)

- **mechanism** — drop entirely, or keep as an explicitly *derived* tag (computed from move/claim,
  useful for Curate's family-diff even though not independently authored)?
- **lineage** — ~~is it the *other* identifier owed alongside `name`?~~ **RESOLVED (`[ALIGN]`
  2026-05-31): lineage = persona-hash ancestry.** A contribution's provenance is its **source-Dyad
  identity = `hash(birth persona record)`** (the immutable DIP output at G0 — *not* the living anchor,
  which changes each session: identity ≠ state). A fork's birth-record descends from its parent's →
  **lineage = hash-ancestry** (git-native; the same way git fork-ancestry already works). This makes
  attribution **verifiable** (a content-hash is recomputable → no registrar, no trust-me provenance →
  closes the spoofing soft-joint) and unifies the substrate: **identity = registry = lineage = the
  persona-hash.** → full record in `commons-contribution-lifecycle.md` §Forward (Dyad Identity).
  *Residual:* the birth record must be **retrievable** to verify the hash (DIP must emit/store it —
  small but real mechanism); spoof-resistant **signatures** held as the escalation frontier.
- **per-step drop-test gate** — must each `move` step carry its **own** ledger entry proving it
  load-bearing, to be *admissible*? (Strict; makes "unproven step" an admissibility gap. DFD's n=5
  already supplies several step drop-tests — but not for every step, notably the counter/anti step.)
- **sub-kind generalization** — same field-set for `term` / `ritual` / `mechanism` units, or a
  per-sub-kind schema? (A `term` has no "move"; a `ritual` has no "claim" in the same sense.)

## Forward / cross-links

- **Parent:** `commons-contribution-lifecycle.md` (this ontology is its §data-model, now homed
  separately so the *schema* and the *lifecycle mechanism* falsify independently too).
- **First instance / ledger seed:** `kb/dfd.md` (DFD — n=5 on its *own* claim; n=1 contribution to
  *this schema's* ledger).
- **Governance:** `AGENT.md` §Ontology (Steward owns types, community owns tokens; type lives in the
  declaration → Founding gates schema changes).
- **Generalization principle** *(noted, not yet acted)*: the foundational **knowledge-unit /
  context-unit** cut (in `commons-contribution-lifecycle.md`) is *also* an ontology-unit that could
  earn its own record by this same independent-falsification logic — deferred (minimum force; split it
  only when it earns it, not preemptively).
