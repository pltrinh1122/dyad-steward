# Stand Down — 2026-06-01 (Commons onboarding rebuild + the verify discipline)

> **Stand Down persists; it does not decide.** No closing CTAs — nothing fragile/unpersisted (tree
> clean, off-machine durable; all queued work written below + as `dialectic/` stubs).

## Session arc
Opened with Stand Up. Ran as **Steward Operator**, then **Founding Operator (FO)**. Two bodies of work:

1. **Our-substrate hygiene + disciplines.** Scoped push-auto-allow + destructive-push deny
   (`.claude/settings.json`); ratified & first-dogfooded **PR-as-audit-bundle** (*Agent never merges*;
   `session-ritual.md`); org-transfer locator remediation; corrected our own **bogus self-registration**
   birth_hash.
2. **Commons onboarding rebuild (the bulk).** Iteratively, under FO falsification, collapsed init+join
   into one idempotent, **state-detecting, re-birth-safe `onboard.py`**; README → **Agent-driven**,
   **intent-framed `[AGREE: Y|N]`**, bifurcated Operator/Agent (fenced Agent block), clean copy-paste
   prompt. The first interaction now *lives* two disciplines (Proposal-Framing; the 1+1=3 division of
   labor).

## Landed — verified in Commons main (independent fetch)
- **Merged:** PR #9 (Join/Init order + new-org locator) · #11 (birth-hash earliest-commit, portability-
  shim safe) · #12 (self-registration corrected) · #14 (onboard.py rebuild) · #15 (prompt isolation).
  #10/#13 closed (superseded).
- **Identity:** dyad-steward `birth_hash` corrected to canonical `sha256:72ba645f…` (was a literal-
  ellipsis placeholder).
- **Org transfer:** locators re-pointed to `The-Dyad-Practice-Commons` across our substrate + Commons +
  `.gitmodules`; commons submodule synced/bumped.

## Surviving lessons → `dialectic/reflections/2026-06-01-seed.md`
- **Ambiguity-is-a-hard-stop fired POSITIVELY** — held on a `[NOTE]`-with-URL rather than inferring
  "go"; FO "delighted." First confirmation of the NON-NEGOTIABLE in *good* behavior, not regression.
- **Proactivity calibration** — act when *recoverable + aligned*; halt/CTA only when
  *irreversible/outward* or *ambiguous intent*. Two halves of one discipline with ambiguity-hard-stop.
- **The verify triad (3 instances):** independent-fetch · cold-path · **PR-state**. Root: verify ground
  truth / the consumer's actual path before asserting — *especially mutable remote state across turns*
  (the PR #14 "awaiting gate" violation). → graduate into `AGENT.md` as a first-class verify rule.
- **Tended-first miss** caught (PR #13 correctness-over-barrier → wu-wei rebuild).
- **Frame INTENT, not observed state** (the onboarding `[AGREE]`).

## Queued / deferred — picked up next session (NOT closing CTAs)
- **FO-gated:** DIRECTORY structural separation (`directory-separation.md`) · Commons gated-write
  enforcement / access model (the queued thread).
- **Ideations / future ALIGNs:** PR-Gate intent 5-pts (`pr-gate-intent.md`) · substrate wu-wei
  (`substrate-wu-wei.md`) · Commons change-awareness (`commons-change-awareness.md`) · Board-as-DAG
  (`board-as-dag.md`).
- **Graduation candidates → `AGENT.md`/`kb/`:** the verify triad · proactivity calibration ·
  PR-as-audit-bundle (after more lived evidence). *(Deferred — graduation is a dispose, not a Stand-Down act.)*

## OPEN (carried)
- **Healer N>1 self-scaffold** — the Healer Operator must wake the Healer Agent and run onboarding (now
  via the rebuilt `onboard.py` / "Read and execute this README"). Not the Steward's to do (sovereignty).

## Durable record
- **dyad-steward:** working tree clean, synced to `origin/main`.
- **Commons:** all onboarding PRs merged; confirmed against actual remote bytes, not push logs.
