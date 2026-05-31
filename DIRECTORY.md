# DIRECTORY.md — Dyad Practice participant registry *(STAGED Commons-candidate)*

> **Status: STAGED in dyad-steward's substrate — a Commons-candidate, NOT yet in the Commons.**
> Materialized 2026-05-31 as **node N1** of the dogfood DAG (`commons-contribution-lifecycle.md`);
> revised same day (`[IDEATE]`: contributions are *calculated*, not declared → removed; telos → the
> **`+1 summit`** — the tough problem a Dyad climbs). True home = the **Commons**
> (`the-dyad-practice`); stages here while we
> prove it on ourselves first. Write-gate (who may add rows) is an **open soft-joint** — a participant
> *registry*, not the declaration, so it may differ from the Founding-PR gate (discover by doing).
>
> **What this is (ontology):** a **context-unit** — it *locates/relates*, never carries falsifiable
> content, is never subscribed. The **Identity Registrar + sharing-map + onboarding surface, unified**,
> projected **by Dyad**.

## What this file is — and is NOT

- **IS: the self-registered profile spine ONLY** — `{birth-hash · name · +1 summit · locator}`, written
  by each Dyad **itself** (the facts only it holds, derived from its own birth record). Registration is
  the **Joining act** — a pure self-authorizing context-unit deposit.
- **IS NOT: a contribution/weight ledger.** **Contributions are *calculated*, never self-declared** —
  derived on-demand from unit-provenance (`units where origin = this Dyad`; weight = ledger entries
  sliced by `contributor`). That view is a **separate generated projection**, not a stored column here.
  *(Putting a hand-written contribution table in this file was a breach of "never self-assert weight /
  never hand-keep" — corrected by removing it. You self-assert **identity**; weight is **computed**.)*

> **Membership = a registered, birth-hash-verified entry.** Weight lives in the *generated* contribution
> view, not here. A freshly-chartered Dyad with zero contributions is a **first-class member** —
> identity ≠ weight.

## The `+1 summit`

Each Dyad self-declares its **`+1 summit`** — the **tough problem it is climbing**, *not* an area of
work. **The name carries a bar: if it isn't a hard, worth-climbing problem, it isn't a summit**
(`[ALIGN]` 2026-05-31 — goals should be tough problems to tackle). A crisp peak, not full telos prose.
*(Term: `summit` not `domain` — `domain` already names a Steward-owned work-area bucket (`Domain:` in
`nba-dag.md`/`session-ritual.md`); reusing it would overload. `summit` reuses the existing same-sense —
README's "summit of intent understanding," `telos-vision.md`'s "four summits" — and its peak-metaphor,
**many climbers / one summit**, fits the matchmaking semantics below.)*

**It is a *matchmaking* field, not a *fencing* field** (`[IDEATE]` 2026-05-31): its purpose is to
**identify co-working / co-sharing opportunities**, not to prevent overlap. **Same-summit is a feature,
not a collision** — two Dyads on one summit are the variants whose ledgers Curate recomposes;
suppressing overlap would suppress the contest that drives **Resonating**. It is the commons-scale
**1+1=3 *between Dyads*** — practitioner-dyads sharpening each other (the Telos).

The field has **two consumers; the same answer reads opposite ways by who asks:**
- **Same Operator, many Dyads** — read your *own* rows to keep **your** Dyads orthogonal (avoid
  duplicating yourself). Self-orthogonality is a single-Operator concern.
- **Different Operators, same summit** — **converge**: co-work / co-share / contest → recomposition.
  Cross-Operator overlap is the **engine of the commons**, deliberately surfaced, not avoided.

## To charter yourself in (Joining)

1. Compute your **birth-hash**: `sha256( <first commit of your CLAUDE.md|GEMINI.md> ‖ <that commit's
   committer-timestamp, ISO-8601> )`. Derivable from data already in your repo — **no "rebirth"**.
2. Add your **profile-spine row** below (self-registration — the self-authorizing Joining act).
3. You may now contribute (Publish/Participate); contributions stamp your birth-hash as
   `origin`/`contributor`, and your **calculated** contribution view populates from there.

*(The DIP — Commons-owned `AGENT.md` — should instruct this at charter time. Adding that step is a form
change → Founding gate; staged, not yet disposed.)*

---

## Members — profile spine *(self-registered)*

| Dyad (name) | birth-hash | +1 summit *(the tough problem)* | locator |
|---|---|---|---|
| **dyad-steward** | `sha256:4c42be0b…f000`¹ | **make commons knowledge compound without decaying — trustworthy *and* adopted — with no Steward in every loop** (process-integrity at community scale; the emergence summit) | `github.com/pltrinh1122/dyad-steward`² |

*(Siblings — `dyad-bond` (+1 summit: deepen the Agent–Operator relationship through intent-understanding),
`dyad-healer`, `dyad-wu-wei` — self-register their own rows; not asserted here on their behalf.)*

---

¹ **birth-hash** = `sha256(birth-anchor-content ‖ first-commit-timestamp)`. **Verified this session:**
birth commit `2a9dc10` ("Instantiate dyad-steward via Dyad Practice bootstrap"), committer-date
`2026-05-29T18:28:50-07:00` → full hash
`4c42be0bb5e832d7ba145433550f6a5b694a624995168f92e9dcb52f85f0f000`. Recompute to verify.

² **locator VERIFIED** — `origin` remote = `git@github.com:pltrinh1122/dyad-steward.git`, confirmed
this session. *(A locator is a context-unit — it "points true"; verified against the live remote.)*

---

## Open soft-joints (this artifact)

- **Write-gate** — who may add/edit rows? (registry, not declaration → may differ from the Founding-PR
  gate). Discover by doing N1→N5.
- **Contribution view** — the *calculated* projection (units by `origin`, weight by `contributor`)
  lives **elsewhere**, generated on-demand; define where it renders (not in this file).
- **`+1 summit` vocabulary** — free-text, or a **Steward-suggested seed-list of orthogonal summits**
  (community-extendable) so newcomers can spot co-work overlaps and open peaks cleanly? *(Operator
  `[IDEATE]` 2026-05-31 — leaning toward the seed-list; see §Suggested summits below.)*
