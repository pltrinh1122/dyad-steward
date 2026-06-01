# Substrate wu-wei — two pulls in tension — QUEUED IDEATION (not yet explored)

> **Status: QUEUED, parked by Steward Operator (2026-06-01).** Captures a wu-wei tension about our
> *own substrate* (git/GitHub) so a cold session inherits it. **Not yet under falsification** — do not
> resolve here; reopen when the Operator does.
>
> **Sibling threads:** `session-ritual.md` (the destructive-push deny-rule + push/PR disciplines that
> created the case-in-point) · `pr-gate-intent.md` (the consumption/guarding intent this rubs against).

## The tension (Operator framing, 2026-06-01)

Two readings of `wu-wei` (minimum force / flow-with-the-grain) **pull opposite ways** on our substrate:

- **Pole A — wu-wei *with the tool*:** let **git (our substrate) do its intended job.** Git's natural
  workflow *includes* deleting merged branches, rebasing, force-updating — fighting that grain with
  blunt guard-rules creates friction and cruft.
- **Pole B — wu-wei *toward clarity & predictability*:** the deeper aim is a substrate that stays
  **clear, predictable, and safe** (the durable record protected from destruction). Gating destructive
  ops serves that even at the cost of manual cleanup.

Which `wu-wei` governs when they collide? (Or is the collision a sign one pole is mis-stated?)

## Case in point (the spark)

The merged remote branch `adopt-pr-audit-bundle` **could not be Agent-pruned** because our
destructive-push deny-rule blocks `git push origin --delete`. So git's *normal* "delete the merged
branch" is blocked by our *clarity/safety* rule → **leftover cruft**. Pole A (let git clean up) vs
Pole B (don't let the Agent issue destructive pushes) meet head-on over a single stale branch.

## When reopened — candidate first moves (NOT committed, not explored)

- **Finer cut on "destructive":** is *deleting an already-merged/integrated branch* genuinely
  destructive, or is it git's safe-cleanup grain mis-classified by a blunt `--delete` deny? Maybe the
  rule should distinguish *merged-branch prune* (safe) from *unmerged-branch / history-rewrite* (loss).
- **Substrate self-cleaning:** GitHub's *auto-delete-head-branch-on-merge* would prune merged branches
  **at the substrate layer**, so the Agent never issues a destructive push at all — Pole A satisfied
  *without* loosening Pole B. (Observation only; routing TBD — it's our own repo setting.)
- **Re-test the framing:** maybe both poles are the *same* wu-wei and the real cut is
  *constructive-vs-destructive force*, not *tool-grain-vs-clarity*. Hold open.
