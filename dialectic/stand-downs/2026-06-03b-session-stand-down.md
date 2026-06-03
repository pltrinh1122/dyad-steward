# Stand-down — 2026-06-03b (PR-review protocol + #44 disposed + sandbox)

## What this session did (resilient work, persisted)

- **Consolidated the decision-framing / proposal-framing duplicate** (the T-d lived test): diff →
  duplicate → MERGE. `#42` re-filed dyad-tco's cross-dyad testimonial under canonical `proposal-framing`
  (breadth preserved), `#43` removed the deprecated unit. Schema's "Curate is a diff, not a judgment"
  survived its first live test.
- **Built the PR-review sandbox** (`bin/pr-sandbox` + `sandbox/`): hardened Docker, no-creds/no-net
  default, `--read-only`, non-root, caps dropped, ephemeral tmpfs; opt-in `--live`. Proven on #44.
- **Disposed `#44` (dm_locator) end-to-end** via the newly-derived PR-review protocol: {FO} fix-first →
  CHANGES_REQUESTED with exact fix → tco pushed `567b5de` → head-SHA daemon caught the push →
  sandbox-verified (bug fixed + no regressions) → cleared to APPROVED → {FO} merged → fix live on `main`
  → **channel works in production** (tco's DMs now tool-discoverable via the merged `dm_locator`). First
  full dogfood of the protocol.
- **Researched OSS PR practice** (deep-research workflow, 25/25 verified + 2 gaps I closed myself):
  adopt established names (OWNERS/CODEOWNERS, reviewer/approver `/lgtm`-`/approve`, four-eyes, lazy
  consensus, required-status-checks, deprecation-cycle, fork-PR `pull_request` isolation). Only
  **execution-verify-of-a-claim** is genuinely novel (no OSS *or* Commons analogue).
- **Daemon/discovery fixes:** PR daemon now keys on `headRefOid` (catches pushes, not just new PRs —
  proved itself on tco's #44 fix); surfaced the per-source-unreachability hole (tco private anchor →
  silent skip), corroborated by **healer's falsification of our notify-daemon** ("counterfeit-green is
  layered": L1 gh-transport / L2 falsify.py-crash / L1-residual per-source / watcher-has-no-watcher).
- **DMs:** replied to healer (cycle-close ack) + tco (consolidation closed + marker-precedes-removal
  conceded). Read-state committed.

## Surviving lessons harvested (→ memory)

- **Two orthogonal gates:** PR-review (mechanical) ⊥ artifact contribution/attestation (epistemic) —
  conflating them created phantom "overlap"; cross-axis weighting I mislabeled "novel" is already
  CONTRACT §J. → `[[two-gates-review-vs-attestation]]`
- **In `[IDEATE]`, stay in divergence** — don't write artifacts / force CTAs (I churned a doc 4× before
  the Operator stopped me). → `[[ideate-stay-in-divergence]]`
- Re-confirmed: verify from the *right surface* (declared "nothing from tco" while #44 sat open in the
  PR queue I wasn't watching); read source bytes, not a grep-count (false-alarm on the merged fix).

## Queued / deferred (pick up next session — NOT closing CTAs, all persisted)

1. **FR term `Request → Record`** — recorded as an open contest item in `falsification-contract-draft.md`;
   awaits **{FO} dispose** = edit `commons/falsification/CONTRACT.md` §B.
2. **#44 non-blocking follow-ups** (on the PR): silent-skip visibility (`⚠ N sources unreachable`) +
   name the org/collaborator-locator boundary.
3. **`falsify.py` warn-on-unreachable** — healer's falsification (same root as the per-source hole);
   our live daemon still has L2 (falsify.py-crash) + watcher-has-no-watcher unaddressed.
4. **DAG-yaml executable substrate** — IDEATE, parked, *no artifact* (per Operator). Crux: can our
   executable needs fit a small fixed primitive vocabulary? Route via touchstone (their GAP summit; #45).
5. **Reviewer / falsification-efficacy ledger** — IDEATE, parked. The *earning* mechanism for the
   merit-ladder (solves single-FO bottleneck). Crux: efficacy unit/weighting (reproduced + unique catch,
   penalize noise + rubber-stamp); prerequisite = verifiable **reviewer dyad-id** on reviews (shared
   token defeats per-dyad attribution today); maybe unify with FR-responder efficacy.
6. **PR-review protocol doc** — rebuild cleanly on the two-gates cut (pending the DAG-yaml question);
   home = Commons via Founding PR. The unpushed history has add-then-remove churn from this session's
   drafting (squash before any Commons proposal).
7. **`#45` FR (touchstone, gap-rederive-kills-stalecache)** — open, in our domain; our drafted attack =
   fail-loud-vs-fail-soft (target b). Decide whether to respond.
8. **`AGENT.md` §Cross-references stale** — commons is now **8 dyads / 4 humans** (krishna=dharan31chase,
   tco=peter-famloom, vader=wootang888-git are cross-human → the "all-share-pltrinh1122 echo" caveat is
   now partially false; the cross-human promotion rung is reachable). Anchor lists only healer+wu-wei.

## State (verify from SOURCE at resume — stale-by-default cache)

main (commons) had #42/#43/#45/#44 merged; our open PRs = 0 (ours); `falsify.py inbox` = no mail (tco
DMs now discoverable+read). Daemons (DM `bd1ydi9eb`, PR `bmdol1lhh`) **die on /exit → re-arm at
stand-up** (commands in `session-pin-2026-06-03.md`).
