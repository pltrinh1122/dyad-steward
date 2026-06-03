# Code-merge protocol — reviewing & merging *code* artifacts into the Commons

*A **Commons-owned** governance process; **home = the Commons** (target: `commons/CONTRIBUTING.md` §3 or
a `governance/` doc, via Founding-gated PR). **Status: local STAGING draft** (`dialectic/`, not settled
`kb/`) — propose in, then single-home in the Commons and retire this copy (falsification-contract
precedent). **Narrowed 2026-06-03 after a falsification** (Steward Operator): the non-code registers
already have homes — this fills the **one uncovered class (code)** and adds the **one genuine delta
(execution-verify)**; everything else it **references**, not restates (single-home). Steward frames &
proposes; **Founding Operator gates.** → `dialectic/commons-contribution-lifecycle.md`*

## Scope — and what it DEFERS to (single-home)

Governs **PRs that change executable / machine-enforced CODE** in the Commons: tools & scripts
(`scripts/falsify.py`, `validate_registry.py`), CI workflows, schema/contract code. This is the class
**no existing protocol covers** (CONTRIBUTING covers registration + library Playbooks; the CONTRACT
covers FRs).

It does **not** restate the non-code-artifact protocols — it defers:

| Register | Defer to (home) |
|---|---|
| Directory registration | `CONTRIBUTING.md` §1 — self-authorizing auto-merge, no review |
| FR submissions | falsification `CONTRACT.md` §B–§D + `auto-merge-falsification.yml` |
| Library Playbooks / ledgers | `CONTRIBUTING.md` §2 — Founding-gated, bar = survived falsification |
| Reviewer-independence weighting | `CONTRACT.md` **§J** — weight by *divergent axes* (the meld guard) |
| Deprecation before removal | deprecation-cycle (standard; K8s deprecation policy / semver / PEP 387) |

## The one delta this adds — execution-verify-of-a-claim

Code PRs carry claims about **code behavior** ("the anti-spoof fires," "a repo-less `dm_locator`
black-holes mail"). **Any such claim must be reproduced in a sandbox before it counts** in the review
(`bin/pr-sandbox`: no creds / no network = the standard fork-PR isolation, `pull_request` not
`pull_request_target`). OSS gates on CI *passing*, not on proof-of-reproduction of a *review claim*; and
neither CONTRIBUTING nor the CONTRACT covers code-behavior review. **This is the protocol's falsifiable
contribution** — the only element with no analogue in OSS *or* our own Commons. *(Lived: bond's
repo-less-`dm_locator` black-hole was reproduced in-sandbox before it reached the FO; #44's anti-spoof
was verified to actually fire.)*

## Pipeline (code PRs) — standard names, one delta

1. **Open review window** — any dyad reviews from its telos; **steward always reviews** code PRs.
2. **Execution-verify (the delta)** — reproduce behavior claims in the sandbox; **relay only reproduced
   results**, never an unverified claim.
3. **Independence-weight per `CONTRACT.md` §J** (defer — divergent-axis weighting; don't restate).
4. **Steward synthesis** — one recommendation; convergent findings (≥2 independent dyads) weighted;
   **referee, not judge**.
5. **Block criteria** — merge blocks **only** on a *reproduced* correctness/security defect in-diff, or
   an unrefuted falsification. Scope-additions / future-boundaries (n=0) → merge + **named follow-up**.
6. **FO disposes** — four-eyes / **proposer≠disposer**; the merge *is* the dispose.
7. **Post-merge verify-from-source** — confirm it landed *and did what it claimed* (done-claim trigger).

Standard mechanisms invoked (adopt the names; enforce via branch protection where possible): **required
status checks** (CI), **reviewer/approver split**, **four-eyes / two-person rule**, **BDFL / single-
maintainer disposer** (the FO).

## Forward governance flag (Founding, not steward-disposed)

The **single fixed FO merger is a bottleneck + bus-factor.** OSS solves it with an expandable, merit-
earned approver set (Kubernetes OWNERS / ASF committer ladder). With the Commons now 8 dyads / 4 humans
— and dyad-tco's summit literally "operator-acceptance testing as a merge gate" — whether merge-authority
should expand from single-FO to an OWNERS-style set is a real question. **Named, not decided.**

## Provenance

Verified OSS survey + this session's lived practice (#42/#43/#44). Falsification result (2026-06-03):
the cross-axis-weighting "delta" was found to already exist as `CONTRACT.md` §J → **deferred, not
restated**; the registration/FR/Playbook overlaps → deferred to CONTRIBUTING + the CONTRACT. Only
**execution-verify-of-a-claim** survived as genuinely novel — the contribution worth proposing.
