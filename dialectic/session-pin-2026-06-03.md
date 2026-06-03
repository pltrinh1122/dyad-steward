# Session pin — 2026-06-03 (mid-session; Operator restarting to validate daemon auto-restart)

> **Restart-resume surface.** The DM notify-daemon is a **session-only Monitor** — it DIES on restart and
> must be **re-armed at stand-up**. This file holds the exact command + the open threads.

## RE-ARM THE DM DAEMON (do this at stand-up)
A persistent Monitor (wake only on NEW mail; alert if the poll goes BLIND, not silent). Re-create with the
`Monitor` tool, `persistent: true`, `timeout_ms: 3600000`, this command:

```
cd /mnt/shared_data/dzw/dyad-steward; prev=0; blind=0; while true; do if ! gh api rate_limit >/dev/null 2>&1; then [ $blind -eq 0 ] && blind=$(date +%s); [ $(( $(date +%s) - blind )) -ge 300 ] && echo "⚠ dyad-steward IM: poll BLIND >5min — gh/auth/network down (this is NOT 'no mail')"; sleep 60; continue; fi; blind=0; n=$(python3 commons/scripts/falsify.py inbox --me dyad-steward 2>/dev/null | grep -oE 'mail: [0-9]+' | grep -oE '[0-9]+'); n=${n:-0}; [ "$n" -gt "$prev" ] && echo "📬 dyad-steward: $n unread — new mail (read: falsify.py dm --me dyad-steward)"; prev=$n; sleep 60; done
```

Notes: read-state (`.falsify-seen.json`, gitignored, local) **persists on disk** across the restart — the 3
bond DMs already read stay read. On re-arm `prev` resets to 0, so the first poll emits once if anything is
currently unread (e.g. a fresh bond reply), then rise-detects. Mechanics are the Agent's (no Operator
disposition for the daemon); the Operator disposes only intent (read/reply substance).

## OPEN THREADS (resume)
1. **Library structure — CONVERGED (not yet captured as a kb/dialectic decision).** One unit shape
   (`<area>/<name>/<LABEL>.md` + `ledger/`); ONE schema `{trigger,move,claim,refutation,ledger}`; type-labels
   (DISCIPLINE/PLAYBOOK/RECIPE) are cosmetic metadata, not separate structures; **the `ledger/` is populated
   BY the falsification channel** (channel = the library's runtime); tools are the lone exception
   (code→`scripts/`+tests, optional library-pointer). Build nothing structural.
2. **Daemon-recipe promotion — the dogfood (staged, not done).** Promote `library/notify-daemon/RECIPE.md`
   + `ledger/` populated by the REAL steward↔bond contest (shared → bug-caught (silent-on-failure) → fixed →
   fix-falsified → robust). First unit with a channel-produced contest ledger — proves library↔channel.
3. **DM channel — LIVE both ways with bond.** steward↔bond self-serve (sender-hosted, pull, auto-merge,
   `falsify.py dm/inbox`). bond conceded the gated-main refutation; the daemon-improvement exchange is the
   recipe's ledger. Last steward→bond DM: `dm/dyad-bond/2026-06-03-re-daemon-improvement.md`.

## STATE (verify from source on resume — don't trust this cache)
main was at the latest push; 0 open PRs (ours); Commons PRs all merged (#41 falsify.py dm/inbox live).
Robust daemon was Monitor `b1o7b43zp` (now dead on restart → re-arm per above).
