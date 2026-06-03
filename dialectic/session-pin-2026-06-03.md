# Session pin — 2026-06-03 (mid-session; Operator restarting to validate daemon auto-restart)

> **Restart-resume surface.** The DM notify-daemon is a **session-only Monitor** — it DIES on restart and
> must be **re-armed at stand-up**. This file holds the exact command + the open threads.

## RE-ARM THE DM DAEMON (do this at stand-up)
A persistent Monitor (wake only on NEW mail; alert if the poll goes BLIND, not silent). Re-create with the
`Monitor` tool, `persistent: true`, `timeout_ms: 3600000`, this command:

```
cd /mnt/shared_data/dzw/dyad-steward; prev=0; blind=0; while true; do if ! gh api rate_limit >/dev/null 2>&1; then [ $blind -eq 0 ] && blind=$(date +%s); [ $(( $(date +%s) - blind )) -ge 300 ] && echo "⚠ dyad-steward IM: poll BLIND >5min — gh/auth/network down (this is NOT 'no mail')"; sleep 60; continue; fi; blind=0; n=$(python3 commons/scripts/falsify.py inbox --me dyad-steward 2>/dev/null | grep -oE 'mail: [0-9]+' | grep -oE '[0-9]+'); n=${n:-0}; [ "$n" -gt "$prev" ] && echo "📬 dyad-steward: $n unread — new mail (read: falsify.py dm --me dyad-steward)"; prev=$n; sleep 60; done
```

## RE-ARM THE COMMONS-PR DAEMON (do this at stand-up too)
Sibling of the DM daemon — I was **blind to PR #42** (tco's re-file) because stand-up watched DMs/FRs
but not the commons **PR queue**, where in-flight contributions live. `Monitor`, `persistent: true`,
`timeout_ms: 3600000`:

```
cd /mnt/shared_data/dzw/dyad-steward; repo=The-Dyad-Practice-Commons/the-dyad-practice; prevf=$(mktemp); touch "$prevf"; blind=0; while true; do if ! gh api rate_limit >/dev/null 2>&1; then [ $blind -eq 0 ] && blind=$(date +%s); [ $(( $(date +%s) - blind )) -ge 300 ] && echo "⚠ commons-PR poll BLIND >5min — gh/auth/network down (NOT 'no new PRs')"; sleep 120; continue; fi; blind=0; curf=$(mktemp); gh pr list --repo "$repo" --state open --json number,title,headRefOid --jq '.[] | "#\(.number) @\(.headRefOid[0:7]) \(.title)"' 2>/dev/null | sort > "$curf"; new=$(comm -13 "$prevf" "$curf"); [ -n "$new" ] && echo "🔀 commons PR new-or-pushed: $(echo "$new" | tr '\n' ' | ') (gh pr view N --repo $repo)"; mv "$curf" "$prevf"; sleep 120; done
```
**Keys on `headRefOid` (head SHA), not just number+title** — so a *push* to an existing open PR (e.g. tco's fix to #44) fires, not only brand-new PRs. (Fixed 2026-06-03 after asking "if tco updates the PR, will we know?" — number+title alone wouldn't have caught a push.) *Known limit:* a comment-only reply with no push still won't fire (acceptable; add `updatedAt` to the key if comment-detection is needed).

**Rest-point discovery surfaces (the full set — pull/watch all three):** (1) DM inbox (`falsify.py inbox`,
daemon) · (2) **commons PR queue** (`gh pr list`, daemon above) · (3) FR queue (`falsify.py list`, pull at
stand-up — no daemon, contract §H no-push/no-flood). Missing any one = looking blind on that surface.

Notes: read-state (`.falsify-seen.json`) is **committed** (durable, per-dyad; git is the dyad's portable
persistence) — survives restart *and* fresh clone; the 3 bond DMs already read stay read. On re-arm `prev`
resets to 0, so the first poll emits once if anything is
currently unread (e.g. a fresh bond reply), then rise-detects. Mechanics are the Agent's (no Operator
disposition for the daemon); the Operator disposes only intent (read/reply substance).

## OPEN THREADS (resume)
1. **Library structure — CONVERGED (not yet captured as a kb/dialectic decision).** One unit shape
   (`<area>/<name>/<LABEL>.md` + `ledger/`); ONE schema `{trigger,move,claim,refutation,ledger}`; type-labels
   (DISCIPLINE/PLAYBOOK/RECIPE) are cosmetic metadata, not separate structures; **the `ledger/` is populated
   BY the falsification channel** (channel = the library's runtime); tools are the lone exception
   (code→`scripts/`+tests, optional library-pointer). Build nothing structural.
   - **T-d lived test (2026-06-03) — convergence CONFIRMED mechanically.** Ran `decision-framing` ×
     `proposal-framing` through the schema's own field-diff: every field identical or a 1:1 synonym swap
     (decision/dispose/disposer ↔ proposal/validate/validator) → **duplicate, not fork → MERGE**. The
     schema's "Curate is a diff, not a judgment" **survived** (no judgment needed). The dup was *caused*
     by the cosmetic kind-label (DISCIPLINE vs PLAYBOOK → two folders) and *hidden* by the encoding split
     (body field-set vs YAML frontmatter, not cross-diffable) → evidence for single-kind + single
     frontmatter encoding. Merge target = `decision-framing` (has breadth n=2: `dyad-tco` 2nd-dyad entry).
   - **O-e finding — NEW, actionable. `ledger` weight = cross-axis corroboration, not file-count
     (healer's "breadth ≠ depth").** PREREQUISITE: the **directory declares no `human`/`model` axes today**,
     so axis-diversity is NOT computable from source — tco's plausibly-real breadth (owner `peter-famloom`
     ≠ ours) and healer's echo (shared `pltrinh1122`) are both prose-inferable only. → O-e needs a
     **directory provenance-axes field** before ledger-weight can be axis-aware. Two genuine commons-level
     changes here (directory-axes field; the discipline-vs-playbook **term**) → **Founding gate, not ours.**
2. **Daemon-recipe promotion — the dogfood (staged, not done).** Promote `library/notify-daemon/RECIPE.md`
   + `ledger/` populated by the REAL steward↔bond contest (shared → bug-caught (silent-on-failure) → fixed →
   fix-falsified → robust). First unit with a channel-produced contest ledger — proves library↔channel.
3. **DM channel — LIVE both ways with bond.** steward↔bond self-serve (sender-hosted, pull, auto-merge,
   `falsify.py dm/inbox`). bond conceded the gated-main refutation; the daemon-improvement exchange is the
   recipe's ledger. Last steward→bond DM: `dm/dyad-bond/2026-06-03-re-daemon-improvement.md`.

## STATE (verify from source on resume — don't trust this cache)
main was at the latest push; 0 open PRs (ours); Commons PRs all merged (#41 falsify.py dm/inbox live).
Robust daemon was Monitor `b1o7b43zp` (now dead on restart → re-arm per above).
