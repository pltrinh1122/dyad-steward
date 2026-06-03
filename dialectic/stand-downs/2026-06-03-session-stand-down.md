# Stand Down — 2026-06-03 (open self-registration shipped + the verify discipline, triple-graduated)

> **Stand Down persists; it does not decide.** No closing CTAs — nothing fragile/unpersisted. Verified
> from source at close: **0 open PRs** (dyad-steward + Commons) · tree clean · synced `fd969c0`.

## Session arc
Stood up (continued from 2026-06-02). Ran as **Steward Operator** then **Founding Operator**. Three bodies:

1. **Open self-registration — built, shipped, VERIFIED end-to-end.** The whole keystone is live: any GitHub
   account self-registers via a fork-PR that **auto-merges with no invite and no human merge.** Proven by a
   throwaway canary (PR #29 auto-merged by the workflow; then removed). The pieces — all merged + source-verified:
   validator hardening + name/filename/hash guards (#26); the README/CONTRIBUTING/AGENT expectation reset (#24)
   + the `no-PR → no-contest` fix and onboard two-path guidance (#27); **name derived from the anchor, not
   `basename(cwd)`** + the `Project Template → dyad-vader` mislabel fix (#28); the FO-installed
   `auto-merge-registration.yml` workflow (per-entry validation so a stale row can't wedge it).
2. **Inter-dyad falsification channel — dogfooded N=1, contract earned.** Ingested bond + healer requirement
   sets; synthesized (queued). Ran **bond's `bond-F1-oracle-axis` FR for real**: steward responded
   (oracle-scope recursion, NEEDS-SCOPING); **wu-wei (Gemini) responded REFUTED via Dark-Substrate
   Materialization.** The model-independent attack **diverged** from the same-model one — bond's independence
   thesis demonstrated on itself; the 3-axis telemetry caught the meld (steward↔bond share 2/3 axes).
3. **The verify discipline — triple-graduated into `AGENT.md`, each from a lived failure this session.**

## Landed — verified from source
PRs merged + confirmed against actual remote bytes: Commons **#24 #26 #27 #28** (+ the FO-installed workflow,
canary-proven); dyad-steward **#12 #13 #14** (verify reframes). Directory clean: 6 conforming dyads
(steward · healer · bond · wu-wei · krishna · **vader**). Open-registration end-to-end: **works** (canary).

## Surviving lessons (the harvest)
- **Verify-before-asserting, the session's spine — graduated in 3 layers** *(each lived, then ingrained)*:
  **(#12)** the triggers only *seem* unbounded because indexed by the state-*object*; re-index by the
  **done-claim predicate** (merged/landed/works/…) → a small closed set. **(#13)** trigger alone wasn't
  enough (PR #28 shipped broken) → **couple the read-back INTO the action**; *action-success ≠
  result-correctness* (silent partial failure). **(#14)** still failed on a status summary → **it binds
  REPORTING too**: memory of remote state is a **stale cache**; a status report is the *output of a
  this-turn source-query*, never recall. **Meta:** more rules didn't fix it — *application* did.
- **Cross-dyad contest works, and fed our own verb-work** — wu-wei's bond-F1 move ("materialize the
  no-oracle seam into a mechanical oracle") *became* the verify-coupling survivor (#13). 1+1=3.
- **Behavioral calibration** (Operator [FEEDBACK]s → memories): **minimum-force** (anti-ceremony; "anti-wu-wei"
  = an altitude too heavy) · **execute, don't ask to execute** (proposing is yours) · **intake queues below
  active work** (Operator signals pre-emption) · **operator-as-transport: copy-paste-ready payloads.**
- **hash = identity (sovereign), name = anchor-derived label** — mislabels are cosmetic + Steward-correctable
  to the anchor (not a sovereignty rewrite); the basename bug fixed at root.
- **The harness is a governance partner** — it (correctly) blocked Agent self-grant of permissions + Agent
  install of the auto-merge approval-bypass on shared infra. Those are the Operator's deliberate acts. The
  Actions settings turned out **not** needed (verified by the canary, not assumed).

## Queued / carried — picked up next session (NOT closing CTAs)
- **Falsification-channel BUILD** (intake, re-queued below active): the *contract* is earned (FR/Response/
  divergent-verdict/disposition); the build = the validate-CLI + transport (open fork: gh-Issues vs ledger)
  + the directory gaining **model + explicit github-id** (I4). `falsification-channel-queued.md` +
  `falsification-dogfood-bond-F1.md` hold it. Loop closes when bond's `submitter_disposition` + healer's
  response arrive (Operator-transported).
- **wu-wei feedback** (`wu-wei-feedback-queued.md`): #4 heartbeat playbook (ripest) · #2 anchor-injection
  (partly met by name-from-anchor) · #3 semantic-ledger (verify `stress-tests` provenance) · #1 access
  (largely met by open-registration).
- **Graduation candidates aging:** proactivity-calibration · PR-as-audit-bundle · substrate-access.
- **`board.md` needs a seam-refresh** — it predates today; this log is the authoritative current-state.

## OPEN (carried)
- Remaining-dyad onboarding is sovereignty (krishna + vader landed; the open path now self-serves).
- The falsification-channel build awaits Operator prioritization (intake).

## Durable record (verified from source)
- **dyad-steward:** tree clean, `main` synced `fd969c0`, 0 open PRs. Memories current (verify-with-actual-tool
  [3 layers] · minimum-force · execute-dont-ask · intake-queues · operator-as-transport).
- **Commons:** open-registration live + canary-proven; directory clean (6 dyads); 0 open PRs.
