# Cross-dyad share-pull — the Operator out of the transport loop — LIVE

> **Status: implemented (v0.1), the fork below open.** Survivor of the 2026-06-02 Steward-Operator
> `[ALIGN]`: *"it's not wu-wei for the Operator to copy-paste the sharing of dyadic validation —
> falsify and implement the survivor."*

## Falsification result
The claim **survives**: manual copy-paste of cross-dyad shares is friction, not wu-wei. Reframed by the
attacks:
- **F1 (it's a gate, not friction)** → resolved by the **durability ⊥ ratification cut**: the Operator
  keeps the **gate** (which shares to engage); the Agent takes the **transport** (fetching them).
- **F2 (premature?)** → dies: `recommendations/` is **convergent** across every sibling (healer 5,
  bond 1, wu-wei 1); it's the Commons' *Resonating* channel; relayed ~4× in one session.
- **F3 (too contextual to fetch)** → dies: the channel + `gh` fetch already exist (I pulled wu-wei's
  feedback in one call).
- **F4 (the real move removes the relay, not eases it)** → **the survivor**, and it *is* the Telos
  ("no Steward in every loop").

## The mechanism (v0.1) — `bin/pull_shares.py`
Reads the **Commons directory** (registered dyads + locators) live, lists each sibling's
`recommendations/`, **auto-shows** shares addressed to us (`*steward*`), lists general ones for the
Operator to pick. `--since` (new-only), `--repo` (transition handle for a not-yet-registered dyad),
`--fetch` (one body). Read-only `gh`. **Verified by execution** 2026-06-02 (reproduced the exact
wu-wei feedback the Operator had hand-pasted). Partially realizes `commons-change-awareness.md`'s
*"pull / what-changed-for-me"* candidate.

## The convention (emergent, now named)
Cross-dyad shares are **posted as files** at `recommendations/<date>-<topic>[-for-<dyad>].md` in the
author's repo (healer's carry structured provenance headers: Type · Channel · Authored/Surfaced ·
Source-of-grain · Discipline). The target's **Agent pulls**; the Operator no longer carries. *Reciprocal
duty: when WE validate/recommend to a sibling, we post to our own `recommendations/` so their Agent can
pull — never relay live.*

## Constraint + open fork *(Steward-Operator [IDEATE], 2026-06-02: two other-human dyads not yet self-registered)*
The pull is **directory-driven → reaches only registered dyads.** Implications:
- **Registration is the prerequisite to the sharing network** — arguably correct (you're not in the
  Resonating loop until you Join). The two unregistered dyads' next step is to *register*, not for the
  channel to chase them. → **escalates the `Healer #2-access` trail** (now the 4th–5th convergence on
  registration/access friction; *and ask why they're stuck — same no-write friction, or just incomplete?*).
- **OPEN FORK — per-repo vs Commons-central.** The emergent channel is **per-dyad-repo**
  `recommendations/`, which assumes the repo is **public + readable to my `gh` token**. **Cross-human
  dyads may be private / under other accounts** → unreadable. So: does cross-dyad sharing stay per-repo
  (needs public repos + registration) or move to a **Commons-central inbox** (works across humans/accounts,
  but a Commons change → Founding gate)? Per-repo is emergent + liveness-free; Commons-central is the
  cross-human frontier. **Not resolved — held as the next falsification.**

## Cross-references
`sharing-discipline.md` (outbound access-map — the other half of the Sharing verb) ·
`commons-change-awareness.md` (subscribe/borrow; this realizes its "pull" leg) · `board.md` (the
`#2-access` escalation) · `bin/pull_shares.py`.
