# STAGED Commons PR candidate — DFD discipline + `discipline`/"cycle" term

> **Status: STAGED in dyad-steward's substrate — NOT submitted.** Node **N4** of the dogfood DAG
> (`commons-contribution-lifecycle.md`). This is the *proposal artifact* the Steward (proposer) drafts;
> the **merge is the Founding-Operator gate** (N5) — not ours to dispose. It bundles the **`term`
> prerequisite** (discipline/cycle) with the **DFD discipline** (DFD crosses *as a* `discipline`), one
> gate. **First lived dogfood of the Commons Contribution Lifecycle's Publish role.**
>
> **Library structure RATIFIED (Founding Operator dispose, 2026-05-31):** L3 + consumer-grain —
> each discipline is a **directory**: `library/<name>/playbook.md` (stable body, Founding-gated) +
> `library/<name>/ledger/<contributor-hash>-<n>.md` (append-only testimonials, mechanical contribution-
> gate, conflict-free). Part B below is now **materialized** at
> `dialectic/staged-commons/library/decision-framing/` (body + n=5 ledger seed). The declaration gets
> only the **one-line index entry**; the record + ledger live in `library/`.
>
> **Joining gate satisfied:** `origin` = dyad-steward, registered in `DIRECTORY.md` (N1), birth-hash
> `sha256:4c42be0b…f000` — verifiable. So this contribution is admissible to *propose*.

---

## Provenance envelope (the proposal metadata)

- **origin (proposer Dyad-ID):** `sha256:4c42be0b…f000` (dyad-steward; `git@github.com:pltrinh1122/dyad-steward.git`)
- **unit-kind:** bundle — one `term` + one `discipline`
- **schema-version:** discipline-ontology @ 2026-05-31 (field-set {trigger, move, claim, refutation, ledger})
- **target:** the Commons declaration (`the-dyad-practice` README — §The cycles, to be renamed §The disciplines)
- **lineage:** none (origin proposals, not variants)

---

## Part A — `term` (prerequisite): adopt `discipline`, retire best-practice "cycle"

**Proposed change to the declaration:**
- Rename README §"The cycles" → **§"The disciplines"**.
- Define **`discipline` = a series of dyadic-cycles** (a proven, *repeated* practice). Keep **`dyadic
  cycle`** as the *unit* (one generate→validate turn). Retire the *best-practice* sense of "cycle".

**Why (testimonial — the form's own overload):** README line 5 says *"the unit is the **dyadic
cycle**"* while §The cycles says *"a **cycle** is a proven recipe"* — "cycle" is overloaded (atom +
recipe). `discipline` de-overloads it, **and composes with the ledger**: a discipline = a series of
dyadic-cycles; its evidence-ledger = the accumulated survived dyadic-cycles → *weight = series-length ×
survival*. The term and the survival-mechanism are one object.

**Bar:** this is a `term` contribution → declaration change → **Founding-Operator gate**.

---

## Part B — `discipline`: Decision-Framing (the DFD entry)

**Proposed §The disciplines entry (form voice, one line):**

> - You're surfacing a decision to your partner — render it as **one** proposition they can answer
>   **Y/N**, with its strongest counter and a proposed reconciliation, so they **validate** instead of
>   **author**. *(decision-framing — falsify + minimum-force)*

**The orthogonality cut (what crosses vs stays home):** the **general recipe** crosses (above); the
dyad-steward **slot-vocabulary** (`[CTA·Y/N]/[THESIS]/[ANTI-THESIS]/[SYNTHESIS] → ref`) stays a
**local delta** in our `AGENT.md` §DFD. Commons owns the general recipe; each dyad owns its
specialization.

**Travelling testimonial (the >N=1 admission bar) — n=5 survived corrections, none refuting** (`kb/dfd.md`):

| # | correction | what it caught |
|---|---|---|
| 1 | Agent-voice CTA | proposer→disposer collapse (1+1=2) |
| 2 | either/or CTA | disguised authoring migrated back to Operator |
| 3 | omitted SYNTHESIS | dropped the Agent's generate-half; overturned an over-collapse (SYNTHESIS ⊥ CTA) |
| 4 | multiple asks per surfacing | forced Operator to author prioritization |
| 5 | decidable-out-of-flow | drift jumped from the CTA to the *show* (retrieval cost) |

Mapped to the discipline-ontology field-set (via **YAML Frontmatter**):
```yaml
---
origin: "sha256:4c42be0b…f000"
unit-kind: "playbook"
schema-version: "discipline-ontology@2026-05-31"
lineage: "none"
trigger: "surfacing a decision to your partner"
claim: "framing-as-validate (not author) makes the partner's dispose cheap while keeping the contest real"
refutation: "cost migrates back to the disposer (author-not-validate) · becomes a rubber-stamp (no real counter) · sprouts markers that don't earn their keep"
mechanism: "falsify + minimum-force"
---
```
*(The pedagogical move and ledger remain in rich Markdown below the frontmatter).*

**HONESTY FLAG (stated in the PR, not hidden):** the n=5 ledger is **all one dyad**. §Growing's bar is
*"synergy demonstrated"* and `kb/dfd.md` itself names the higher bar *"across more dyads than just us."*
So this is **strong on depth, single-dyad on breadth** — its survival depends on other dyads
subscribing-and-reporting (Participate). That is exactly what the lifecycle predicts: **Publish seeds
n=1-dyad; Participate compounds.** Not a weakness to hide — the mechanism's design.

---

## Submission checklist (when the Founding hat is worn)

- [ ] confirm the Commons write-path / branch (form repo `the-dyad-practice`)
- [ ] open as ONE bundled PR (term A is prerequisite to discipline B)
- [ ] PR body carries the n=5 testimonial **and** the single-dyad-breadth honesty flag
- [ ] **merge = Founding-Operator dispose** (Steward proposes only; never self-ratify)
- [ ] on merge: dyad-steward immediately *subscribes* to its own published discipline (proposer eats
      its cooking); hand dyad-bond the Participate note (N6)

---
*Cross-link: `commons-contribution-lifecycle.md` (the mechanism this dogfoods) · `discipline-ontology.md`
(the field-set) · `kb/dfd.md` (the n=5 ledger) · `DIRECTORY.md` (the Joining gate) · `AGENT.md` §DFD
(the local-delta slot-vocabulary).*
