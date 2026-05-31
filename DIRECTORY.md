# DIRECTORY.md — Dyad Practice participant registry *(STAGED Commons-candidate)*

> **Status: STAGED in dyad-steward's substrate — a Commons-candidate, NOT yet in the Commons.**
> Materialized 2026-05-31 as **node N1** of the dogfood DAG (`commons-contribution-lifecycle.md`).
> This file's true home is the **Commons** (`the-dyad-practice`); it stages here while we prove it on
> ourselves first. Its write-gate (who may add rows) is an **open soft-joint** — it is a participant
> *registry*, not the declaration, so it may differ from the Founding-PR gate (discover by doing).
>
> **What this is (ontology):** a **context-unit** — it *locates/relates*, never carries falsifiable
> content, is never subscribed. The **README-is-the-ontology-projected** pattern, projected **by Dyad**.
> It is the **Identity Registrar + sharing-map + onboarding surface, unified**.

## How to read this (for a chartering Dyad)

Each row joins two halves:
- **Self-registered profile spine** — `{birth-hash · name · telos/role · locator}`, written by the
  Dyad **itself** (the facts only it holds, derived from its own birth record). **Registration is the
  Joining act** — a pure self-authorizing context-unit deposit (you accept falsifiability; you enter the
  contest). *No registration → no contribution* (enforced by a mechanical gate: `origin ∈ DIRECTORY` +
  birth-hash recompute-verification; Steward authors the rule, doesn't run the check).
- **Generated contribution columns** — derived from unit-provenance ledgers (`units where origin = this
  Dyad`, weight = ledger entries sliced by `contributor`). **You self-assert your identity; you never
  self-assert your weight** — weight is earned/derived. *(Generated-on-demand, not hand-maintained.)*

> **Membership = a registered, birth-hash-verified entry. Weight = the contribution columns.**
> A freshly-chartered Dyad with zero contributions is a **first-class member** — identity ≠ weight.

## To charter yourself in (Joining)

1. Compute your **birth-hash**: `sha256( <first-commit of your CLAUDE.md|GEMINI.md> ‖ <that commit's
   committer-timestamp, ISO-8601> )` — e.g. `git show <first>:CLAUDE.md` piped with the timestamp.
   *(Derivable from data already in your repo — no "rebirth" required.)*
2. Add your **profile-spine row** below (self-registration — the self-authorizing Joining act).
3. You may now contribute (Publish/Participate); contributions stamp your birth-hash as `origin` /
   `contributor`, and your contribution columns populate from there.

*(The DIP — Commons-owned `AGENT.md` — should instruct this at charter time. Adding that step is a form
change → Founding gate; staged, not yet disposed.)*

---

## Members

### Profile spine *(self-registered)*

| Dyad (name) | birth-hash | telos / role | locator |
|---|---|---|---|
| **dyad-steward** | `sha256:4c42be0b…f000`¹ | **Steward** — keeper of the commons' *process-integrity*; telos: make the commons a self-cultivating ecosystem (falsifiability × enablement across Joining·Sharing·Resonating → compounding) | `github.com/pltrinh1122/dyad-steward`² |

### Contributions *(generated from unit-provenance — `origin` = this Dyad)*

| Dyad | unit | kind | status | ledger-weight (own) |
|---|---|---|---|---|
| **dyad-steward** | Decision-Framing (DFD) | discipline | staged for Founding gate (N4) | n=5 |
| **dyad-steward** | `discipline`/"cycle" nomenclature | term | staged for Founding gate (N3) | n=1 |
| **dyad-steward** | Commons Contribution Lifecycle | discipline (cycle) | DRAFT (Publish n=1; Participate/Curate awaiting 2nd Dyad) | n=1 |

---

¹ **birth-hash** = `sha256(birth-anchor-content ‖ first-commit-timestamp)`. **Verified this session:**
birth commit `2a9dc10` ("Instantiate dyad-steward via Dyad Practice bootstrap"), committer-date
`2026-05-29T18:28:50-07:00` → full hash
`4c42be0bb5e832d7ba145433550f6a5b694a624995168f92e9dcb52f85f0f000`. Recompute to verify.

² **locator VERIFIED** — `origin` remote = `git@github.com:pltrinh1122/dyad-steward.git`
(`github.com/pltrinh1122/dyad-steward`), confirmed this session. *(A locator is a context-unit — it
"points true"; verified by reading the live remote.)*

---

## Open soft-joints (this artifact)

- **Write-gate** — who may add/edit rows? (registry, not declaration → may differ from the Founding-PR
  gate). Discover by doing N1→N5.
- **Generation** — contribution columns should be *derived*, not hand-kept; at n=1 Dyad this is manual,
  but flag the auto-generation requirement before the registry grows (anti-stale-map).
- **Locator verification** — see ² above.
