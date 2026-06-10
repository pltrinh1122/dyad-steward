# The steering invariant — documents + tools (clipped 2026-06-10)

> **CLIP** (Operator, closing the riff on the FO edit-pass arc): the governing invariant covers
> **documents AND tools** — even tools "steer". **A set of instructions is received as a list of
> GUARDS for agents to execute and reflect against.** Never a command script.

## The invariant, assembled

**Everything an Agent receives is a list of guards — declarative invariants to execute against and
reflect against.** The two surfaces differ only in *when* the guard evaluates:

| Surface | Guard form | Evaluation | The imperative residue |
|---|---|---|---|
| **Document at rest** (canon) | falsifiable declarative claims — true independent of when/who/where read | by any reader, any time (the falsification channel) | none — a sentence with no truth value is outside the dispose⊥falsify game |
| **Tool in flow** | mechanical check (CSI guard) | at the action's edge (pre-commit, validate, gate) | legitimate **only as a steering vector bound to the guard**: the named gap + target state + "rerun" — the agent acts, then *reflects* (does the guard pass now?) |

The loop a guard induces: **execute → guard evaluates → vector names the gap → agent acts → re-check.**
The agent self-heals along vectors; the Operator is not in the loop ([[cut-burden-not-awareness]]
still binds: the *digest* of what was steered remains owed).

## Where each piece came from (the inference trail)

1. **FO edit-pass arc (this session, our canon):** status-true-at-rest (PROTOCOL.md) ·
   invariants-not-instructions (DIRECTORY.md) · cross-file coherence · imperatives→declaratives
   (all three docs). Inferred: *every sentence in canon bears a truth value that holds at rest* —
   indexicality (temporal/personal/positional) is the defect class; truth-valueless sentences are
   unfalsifiable, hence outside the Commons' contest mechanism.
2. **Riff's open question:** do tools get an imperative exemption (rest vs flow boundary)?
   **Operator: NO** — even tools steer.
3. **dyad-cairn prior art (grounded from remote, commit `d28bd2f`, 2026-06-10):** "Refactor CSI
   Guards to emit semantic steering" — *"from dumb blockers into semantic steerers… actionable
   topological remediation steps so the Agent can self-heal without Operator intervention."*
   Pattern live across 9 files (`bin/pr`, `bin/retro`, `bin/mason`, `skills/*`): every
   `🚨 GUARDRAIL BLOCK` pairs with a `[STEERING VECTOR] <target state>, then rerun.` Their own
   vector states the received-form rule: *"The constraints above define your next move. Consume the
   error trace, align your synthesis, and act."*

## Convergence note ([[convergence-check-transmission]])

Same-day parallel forms, same human (pltrinh1122), divergent Agent-built shapes: steward arrived via
a **canon edit-pass** (de-imperativize documents), cairn via a **guard refactor** (vectorize tool
blocks). Same-human ≠ independent lineage — the FO plausibly carried the frame between dyads
(Operator-as-bus). Divergent forms still strengthen the pattern; cross-human evidence would graduate
it.

## What this re-classifies (honest debt list, not built this turn)

- **`onboard.py` completion output** — bare imperatives ("restart or /clear", "run these commands").
  Correct form: each instruction a guard the consuming Agent can check ("the anchor auto-loads only
  in a future session — a restart is the state-change that activates it") + vector. The riff's
  "tools in flow may command" exemption is REFUTED debt, not correct form.
- **Our own `bin/` guards** (`preflight.py`, `frontier.py` validate, pre-commit hook) — they BLOCK
  correctly (armed traps) but emit failure *reasons*, not steering *vectors*. Gap: name the target
  state + re-check, per failure. → frontier node `steering_vectors_local`.
- **Future doc/tool authoring rule (mine, effective now):** instructions are authored as guards —
  the invariant first, the vector second, never a bare command.
