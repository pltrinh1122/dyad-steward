# falsify.py — deferred follow-ups (from #47 panel review, 2026-06-03)

Named-not-hidden after the 5-dyad falsification of PR #47. Both were deliberately scoped OUT of the #47
revision to keep it reviewable; capture them here so they aren't dropped.

## 1. Cross-poll repo-reachability CACHE (cost) — bond #1 / touchstone #1
**Problem:** the repo-probe fires on the *benign-404* path, which is the **common steady state** (most dyads
have no `dm/<me>` dir yet), so `inbox` trends to **~2× directory size** in `gh api` calls every poll. The DM
daemon runs every ~60s and its own health-gate is `gh rate_limit` — the fix pushes the poller toward the
exact limit that, when hit, blinds it.
**Mitigation:** cache repo-reachability across polls (reachability is stable minute-to-minute; only the
mailbox *listing* must be fresh). Small state file keyed `owner/repo → (reachable, ts)`, short TTL (~10–15min).
**Trade-off to design:** a repo going private stays falsely-reachable up to the TTL → its own small cycle, not
a #47 add. Home: `commons/scripts/falsify.py` → Commons PR.

## 2. Commons gh-wrapper + unified test-harness — wu-wei's forward question (NOT a #47 blocker)
wu-wei falsified #47 on two "invariants" that **do not exist in this Commons**: an abstraction-doctrine
`github_client` wrapper (today: raw `gh` subprocess everywhere — `falsify.py`, `validate_registry.py`,
`onboard.py`) and a pytest/spao harness (today: co-located no-framework tests — `test_validate_falsification.py`
is the precedent). The PR *follows* the established convention → **refuted as a #47 blocker.**
**But the forward question is legitimate:** *should* the Commons adopt (a) a standardized GitHub-API wrapper
(resilience to `gh` output-format drift — the same stderr-parse brittleness bond #2 flagged) and (b) a unified
test runner? That is a **commons-level convention change → Founding gate**, a separate proposal, not ours to
assume. If pursued: frame as a proposal, cite the existing raw-`gh` + no-framework convention as the baseline
being changed, and weigh migration cost across all `scripts/`.

> Cross-link: PR #47 panel review · `falsification-contract-draft.md`.
