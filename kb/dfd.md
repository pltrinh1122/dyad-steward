# DFD — the CTA failure-mode

*Settled knowledge. First harvest of the Learning Discipline. The rule lives in
`../CLAUDE.md` §DFD; this file holds the **lesson behind the rule** — why the rule exists and
how it was earned.*

## The lesson

**DFD's `[CTA]` is the component that fails first under pressure — and it always fails the same
way: by quietly migrating decision-cost back onto the Operator.** DFD's whole purpose is to move
the Operator from *authoring* (costly) to *validating* (cheap). The CTA is where that purpose is
either delivered or betrayed. Every other component (CLAIM/EVIDENCE/SELF-ATTACK/REFERENCE)
supplies the Operator's validation; the CTA is the ask itself, so a malformed CTA defeats the
frame no matter how good the rest is.

## The two failure-modes (each caught in real use, 2026-05-29)

1. **Agent-voice CTA** — *"Re-route our candidates…", "I'll resolve…"*. Phrases the disposition
   as the Agent's own next action. Collapses proposer→disposer: the Agent both proposes and
   (implicitly) disposes. That is 1+1=2 — the exact collapse the NON-NEGOTIABLE guards.
   **Fix:** the CTA is addressed *TO* the Operator and names the disposition *they* make.

2. **Either/or CTA** — *"Commit now or hold?"*. Offers alternatives, forcing the Operator to
   *author* a selection — re-importing the very cost DFD removes. A two-option ask looks like
   validation but is disguised authoring.
   **Fix:** the CTA proposes a *single* disposition, answerable **Y/N**. Genuine alternatives go
   in the SELF-ATTACK; the recommended path is the Y.

## Why they're the same failure

Both are the same drift wearing two masks: **cost silently flowing from Agent back to Operator.**
Agent-voice steals the *dispose*; either/or steals the *authoring-avoidance*. The guard is one
test, applied to every CTA before surfacing:

> **Can the Operator dispose of this with a single "Y" or "N", and is the disposition theirs to
> make rather than mine?** If no on either count, the CTA is malformed — reframe before surfacing.

## Falsification status

**Survived.** Two independent Operator corrections converged on the same component and the same
direction (cheaper Operator dispose). Convergence-from-independent-attacks is the signal that
promoted this from `../dialectic/` straight to settled. Re-open if a future CTA fails in a *new*
way the one-test above doesn't catch — that would be a third failure-mode, not a refutation.

## Forward

- Candidate for the **library track** (a best-practice on the *feedback* cycle: name → fix →
  codify). See `../CLAUDE.md` §Contribution candidates. Bar to clear before proposing: synergy
  demonstrated across more dyads than just us.
