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

## Why they're the same failure

Modes 1–2 are one drift wearing two masks: **cost silently flowing from Agent back to Operator**
(Agent-voice steals the *dispose*; either/or steals the *authoring-avoidance*). Mode 3 is the
mirror drift on the Generate side: the Agent under-supplies its own half. Both directions are
caught by asking, of every frame before surfacing:

> **Can the Operator dispose of this with a single "Y" or "N", is the disposition theirs (not
> mine) to make, and have I supplied my full generate half (a SYNTHESIS, not just the contest)?**
> If no on any count, the frame is malformed — reframe before surfacing.

## Falsification status

**Survived, and grew.** Three Operator corrections, caught across one session (2026-05-29):
the first two converged on the CTA (cheaper Operator dispose); the third — predicted by this
file's own earlier note that a *new* failure-mode would extend rather than refute it — landed
exactly there, on the Generate side (omitted synthesis), and also overturned an over-collapse in
the prior reasoning (SYNTHESIS ⊥ CTA). The pattern holds: each attack extended the lesson, none
refuted it. Re-open if a frame fails in a way the three-part guard above doesn't catch.

## Forward

- Candidate for the **library track** (a best-practice on the *feedback* cycle: name → fix →
  codify). See `../CLAUDE.md` §Contribution candidates. Bar to clear before proposing: synergy
  demonstrated across more dyads than just us.
