# Goal Framing — Grounding (WHY · HOW) — audit + lineage

> **Grounding artifact for `GFD`/`GF-UI`** — **not** loaded for execution (the executable spec is
> `goal-framing.md`). Two uses, kept as two sections so they split into two files trivially if access
> patterns ever justify it:
> - **WHY = lineage** — why GFD exists, how it was derived, what the design falsification reclassified.
> - **HOW = audit** — the falsifiable test + evidence by which we judge whether GFD earns its keep.
>
> Split from the WHAT 2026-05-30 (Operator `[FEEDBACK]`: keep execution lean; grounding separate for
> audit/lineage); **2-file split ratified by Steward Operator Y, 2026-05-30.** Same cut as
> README-vs-deep-files and `kb/dfd.md` mode-5 (render the core, ref the rest).

---

# WHY — lineage

## Why GOAL exists (Operator, 2026-05-30)

To **prime the Agent for multiple intents in a single prompt** — `[GOAL]` declares "parse this message
as a *conjunctive list* of outcomes to type + sequence," not as one exchange, pre-empting the Agent's
default of treating a prompt as a single intent.

## The design falsification — the Operator's framing vs. what survived

The Operator proposed GOAL as a third framing region: `GF-UI (show)` / `GFD (flow)`, twin to
`DF-UI/DFD` and `IF-UI/IFD`. Three attacks:

| Attack | Verdict |
|---|---|
| **UI-inflation / over-naming** — `dyad-ui.md`'s pre-registered refutation: *"a **third** region wants a show-name and the split stops earning its keep."* | **Partially survives → reclassified.** GOAL is not a *single-exchange* region (DF = one dispose, IF = one exploration); it governs a *plan* (many future moves). Its precedent is **reflection** — a Dyad Work *act* with a Dyad UI *surface* — **not** DF/IF. So `GF-UI` is the **2nd** (Work, UI) pairing, not a 4th peer single-exchange region; the refutation does not cleanly fire. **But the watch stays armed:** `GF-UI` earns its name only if its show/flow split comes apart in practice. |
| **Mis-homed in Dyad UI** | **Survives → moved.** The *process* (`GFD`) is the long-named **planning-frontier GAP** in `dyad-work.md` — the front-end that *produces the typed nodes* `nba-dag.md` currently "infers ad-hoc per-session." The *surface* (`GF-UI`) stays in Dyad UI. They **pair** — `dyad-work.md`'s predicted pattern ("every Dyad Work type has a Dyad UI surface"), now a **2nd** data point. |
| **`GFD` is not a primitive; it decomposes** | **Survives — and that's the point.** `GFD` = intake → **Telos-gate** → NBA-DAG (*reused*) → DFD (*reused*). A **composed** discipline (library-track recipe), **not** a peer-primitive of DFD/IFD. Its **one new primitive** is the Telos-gate. |

## The load-bearing survivor — the Telos-gate *(the file's softest claim under review)*

Nothing in existing machinery vets *whether a stated outcome should be pursued at all*: DFD disposes a
decision; NBA orders eligible nodes; IFD falsifies candidate *viability*. The `GFD` intake-gate
falsifies each item against the **Telos** — *does this outcome compound the commons' 1+1=3, or is it
scope-creep / busywork / a private-fork temptation / mis-scoped for this dyad?* This is the
**NON-NEGOTIABLE (anti-sycophancy) applied at the intake altitude**: the Agent's empirical-debiasing
half testing the **Operator's premises about what to do**, as rigorously as it tests Agent proposals
(`kb/one-plus-one-equals-three.md`). *Open challenge (from the `[REVIEW]`): is "vet **whether to
pursue**" genuinely distinct from a DFD decision? Defense: DFD **disposes a proposed** decision; the
Telos-gate **generates the vetting** of an Operator-given intent (Generate-side). If this falls →
collapse `GF-UI`, keep the gate as a pre-step to NBA→DFD (see Refuted-if).*

---

# HOW — audit

## Falsifiable claim

Running a session's intent-dump through `GFD` (Telos-gate → typed DAG → one ratification) yields a
session **more Telos-aligned and better-sequenced** than executing the laundry list in declared order.
*Test:* across GOAL-opened sessions, the Telos-gate **at least sometimes** reshapes or rejects an item,
**and** the DAG **at least sometimes** reorders vs. declared order.

**Refuted if:**
- **Gate theatre** — the Telos-gate passes every item unchanged across several sessions → rubber-stamp;
  cut it to a one-line "all aligned" and drop the ceremony.
- **Sequence-degeneracy** — the DAG never reorders the declared list → the list was already a plan;
  `GFD` adds nothing `NBA→DFD` didn't.
- **Over-naming fires** — `GF-UI`'s show/flow split never comes apart (surface is *always* just IF-UI +
  DAG + CTA) → collapse `GF-UI`; keep only the Telos-gate as a pre-step to `NBA→DFD`.
- **Premature-structure / wu-wei breach** — the shape, written early, is contradicted by real GOALs.
  *Mitigation:* DRAFT; distilled-from-practice, not legislated (IFD/DFD each came from ~7 lived instances).

## Seed evidence

**n=1 — first real GOAL run (2026-05-30).** Laundry list: spin off Intent-Understanding · onboard
brother (⏰ 2026-05-31) · onboard co-founder (⏰ 2026-06-01). Both claim-halves fired on the **first** run:
- **Telos-gate did real work** (not theatre): *qualified* the spin-off with two flags (no-private-fork;
  Founding-gate — later *de-escalated* by grounding once "you operate it" was clarified) and *blocked*
  on an undefined "support" → forced clarification (resolved: support = shared scaffolding).
- **DAG reordered the declared list:** the Operator listed the spin-off **first**, but the DAG demoted
  it (no external deadline) below N1+N2 (gated by tomorrow's onboarding). NBA earned its keep.
- **Gate held under "implement" pressure** (twice): an `[IDEATE]` and a deadline both pushed toward
  immediate execution; GFD step-5 held until plan-Y.
- **Produced, then mostly RETRACTED — the strongest evidence.** N2 first shipped as a scaffold +
  `SHARING.md`; same-session falsification killed most of it (the kit **forked the Common's DIP** —
  caught via an Operator `[NOTE]` + a `gh` fetch; `SHARING.md` was **anti-wu-wei**). **Survivors:** the
  root `README.md` + `sharing-discipline.md` + the lesson *instantiation = DIP, don't fork it*. The gate
  catching N2's own over-production **after** ratification = the NON-NEGOTIABLE working **downstream**.

**Known blind spot (the n=2 crux):** this laundry list **collapsed into one shared-upstream node** (N2)
that then largely dissolved — so the "better-sequenced than declared order" claim was tested on a list
with *real dependency structure*. A list of **independent** goals might not reorder at all (→
sequence-degeneracy). **Watch on a less-tractable GOAL.**

## Open questions (attack surface)

- **Override discipline** — when the Operator overrides a `fails`, record it as a Telos-gate exception
  (repeated same-kind overrides = the gate is mis-calibrated), not silently honor it. *(n=1: not
  exercised — no `fails` was overridden; the Founding-gate flag was de-escalated by grounding.)*
- **types-of-work pull** — step-3 typing is the concrete *demand* for the `dyad-work.md` types-of-work
  typology. Does GOAL finally force that typology into being? *(n=1 didn't — N2 collapsed; carried to n=2.)*
- **Granularity** — how fine does a list-item decompose before it is a DAG node?
- **RESTART coupling** — strictly post-RESTART, or any session-planning seam (post-Intermission too)?
  *(n=1: fired post-RESTART, multi-intent purpose confirmed; the Intermission-seam variant untested.)*
- **Generalization** — Steward-specific, or a form-library candidate (every Dyad opens sessions with intent)?
- **Doc-split pattern** — this WHAT|grounding split (Operator `[FEEDBACK]`, 2026-05-30) is a candidate
  pattern for **all** cycle docs (execution lean; grounding separate for audit/lineage). Prove on GFD,
  then propagate — do not retrofit all docs unilaterally.

## Forward

- ✓ **First real GOAL run** (n=1). **n=2 watch:** an independent-goal laundry list (no shared upstream);
  a real Telos-gate **override**; the **Intermission-seam** trigger variant.
- **Promotion gate** — graduation to `kb/` + anchor §Vocabulary/§Ontology promotion **HELD until n≥2**
  (per discipline; reinforced by this session's over-production lesson). *Operator may override.*
- `dyad-work.md`: goal-intake/planning sub-area inhabited; the **types-of-work** GAP gains its step-3
  puller — *still unbuilt* (carried to n=2).

## Cross-links

- **WHAT (executable):** `goal-framing.md`.
- `dyad-work.md` (home domain) · `nba-dag.md` (the DAG/dispose GOAL feeds) · `ideation-framing.md`
  (`IF-UI`, the N-listing borrowed) · `kb/dfd.md` (terminal CTA) · `kb/one-plus-one-equals-three.md`
  (the Telos-gate = anti-sycophancy at intake) · `ingraining.md` (the context-economy rationale for
  this very split).
