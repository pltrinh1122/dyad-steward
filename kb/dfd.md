# DFD — the CTA failure-mode

*Settled knowledge. First harvest of the Learning Discipline. The rule lives in
`../CLAUDE.md` §DFD; this file holds the **lesson behind the rule** — why the rule exists and
how it was earned.*

## The lesson

**DFD's `[CTA]` is the component that fails first under pressure — and it always fails the same
way: by quietly migrating decision-cost back onto the Operator.** DFD's whole purpose is to move
the Operator from *authoring* (costly) to *validating* (cheap). The CTA is where that purpose is
either delivered or betrayed. The other slots (THESIS / ANTI-THESIS / SYNTHESIS / ref) supply the
Operator's validation; the CTA is the ask itself, so a malformed CTA defeats the frame no matter
how good the rest is. *(The frame has since evolved to `[CTA·Y/N] / [THESIS] / [ANTI-THESIS] /
[SYNTHESIS] → ref` — see `../CLAUDE.md` §DFD; the failure-modes below predate the rename but
transfer directly.)*

## The two failure-modes (each caught in real use, 2026-05-29)

1. **Agent-voice CTA** — *"Re-route our candidates…", "I'll resolve…"*. Phrases the disposition
   as the Agent's own next action. Collapses proposer→disposer: the Agent both proposes and
   (implicitly) disposes. That is 1+1=2 — the exact collapse the NON-NEGOTIABLE guards.
   **Fix:** the CTA is addressed *TO* the Operator and names the disposition *they* make.

2. **Either/or CTA** — *"Commit now or hold?"*. Offers alternatives, forcing the Operator to
   *author* a selection — re-importing the very cost DFD removes. A two-option ask looks like
   validation but is disguised authoring.
   **Fix:** the CTA proposes a *single* disposition, answerable **Y/N**. Genuine alternatives go
   in the ANTI-THESIS; the recommended path is the Y.

3. **Omitted SYNTHESIS** — surfacing a frame with thesis + anti-thesis but *no* proposed
   reconciliation (the Agent's pre-rename habit, caught while ratifying the four-slot frame). Drops
   a half of the dyad's **Generate** move: the Agent stops at staging the contest and never offers
   the candidate +1 that grafts the anti-thesis's surviving bits.
   **Fix:** SYNTHESIS is a *mandatory slot*, present even when thin.
   **Doctrinal correction this earned:** an earlier pass reasoned "the synthesis must *be* the
   Operator's Y/N" — an over-collapse. Falsified in use: **SYNTHESIS ⊥ CTA.** SYNTHESIS is the
   Agent-*proposed* content (Generate); the CTA's Y/N is the Operator's *dispose* on it (Validate).
   They are orthogonal, and the CTA is exactly what keeps a synthesis a *proposal*, not a verdict —
   so a synthesis no longer threatens the gate the way the first reasoning feared.

4. **Multiple asks per surfacing** — presenting two CTAs at once (or a CTA bundled with an open
   elicitation), as in the *"Two things for you: (a) your POV (b) the decision…"* surface caught
   2026-05-29. Even when each ask is individually well-formed, stacking them forces the Operator to
   first author a *prioritization/sequencing* — the same cost DFD removes, one level up.
   **Fix:** **at most one CTA per surfacing.** Queue the rest *by name* (not framed) and surface
   them one at a time as each clears. A non-CTA ask bundled with a CTA dilutes the CTA — keep the
   surface single-ask.

5. **Decidable-out-of-flow surface** (DF-UI self-sufficiency; caught 2026-05-30) — surfacing a CTA
   whose disposed content lives only in a referenced artifact, not *rendered in the show* — worse
   when the `→ ref` is path-wrong. The Operator is forced out-of-band to retrieve, locate, and read
   before they can dispose. *Lived:* a CTA pointed to `ideation-framing.md` (wrong path; full
   content in-file only) → the Operator was **blocked from reviewing in-flow**.
   **Fix:** the show must be **decidable in-flow** — the `[THESIS]` renders the disposed content's
   *decidable core*; every `→ ref` is **path-correct and supplementary**, never the sole home of
   what's disposed. When the dispose is *on a document*, render its decidable core in-flow — the
   *core*, not the whole artifact (full-inline re-bloats the show; see mode-adjacent "too busy").

## Why they're the same failure

Modes 1–2, 4, and 5 are one drift wearing four masks: **cost silently flowing from Agent back to
Operator** (Agent-voice steals the *dispose*; either/or steals the *authoring-avoidance*; multiple
asks steal the *prioritization*; decidable-out-of-flow steals the *retrieval*). Mode 3 is the mirror
drift on the Generate side: the Agent under-supplies its own half. All are caught by asking, of every
surface before sending:

> **Is there exactly ONE ask here; can the Operator dispose of it with a single "Y" or "N"
> *without leaving the flow* (THESIS renders the decidable core; refs are correct + supplementary);
> is the disposition theirs (not mine) to make; and have I supplied my full generate half (a
> SYNTHESIS, not just the contest)?** If no on any count, the surface is malformed — reframe before
> sending.

## Falsification status

**Survived, and grew — twice.** Five corrections across two sessions. *2026-05-29:* the first two
converged on the CTA (cheaper Operator dispose); the third — predicted by this file's own earlier
note that a *new* failure-mode would extend rather than refute it — landed on the Generate side
(omitted synthesis) and overturned an over-collapse (SYNTHESIS ⊥ CTA); the fourth (multiple asks)
extended the cost-migration drift to *prioritization*. *2026-05-30:* the fifth (decidable-out-of-flow)
extended the **same drift to a new surface** — not the CTA but the **show** (DF-UI self-sufficiency):
cost migrating back as *retrieval*. The pattern holds: each attack extended the lesson, none refuted
it — and it has now jumped from the CTA slot to the show, confirming the drift is a property of the
*whole surface*, not one slot. Re-open if a frame fails in a way the guard above doesn't catch.

## Forward

- Candidate for the **library track** (a best-practice on the *feedback* cycle: name → fix →
  codify). See `../CLAUDE.md` §Contribution candidates. Bar to clear before proposing: synergy
  demonstrated across more dyads than just us.
