#!/usr/bin/env bash
# bin/standup.sh — dyad-steward stand-up / resume automation.
#   Borrowed from dyad-bond's K6 stand-up spine (2026-07-04, fresh-fetched from its remote); adapted to
#   steward's substrate — frontier + bin/state.py, no carry-forward.md / bin/git.sh.
#
# WHY: the stand-up ritual opens with DETERMINISTIC checks a fresh steward otherwise hand-runs every
#   session — the durability read-back (clean+pushed = grounded memory, [[gate-durability-as-hard-
#   condition]]), the substrate probe (is the DM daemon even armable here?), and the frontier ready-set.
#   As a Claude Code SessionStart hook, `--hook` emits the result as additionalContext so it loads at
#   boot without a manual read. Kept LOCAL-fast (no network) so it never delays boot — the live pulls
#   (PR/inbox/origin-sync via bin/state.py + falsify.py) are the agent's stand-up act, reminded below.
#
# NOT auto-judgment (bond's K6-b): it SURFACES state + the re-arm reminder and hands disposition to the
#   agent. auto-trigger != auto-judgment.
#
# TRIGGER (2026-07-04): this is now the mechanical spine of the **`d-start`** marker (the Operator's
#   portable session-OPEN trigger — dialectic/session-lifecycle-discipline.md), NOT a live Claude hook.
#   The Claude SessionStart hook was RETIRED for portability (agy exposes no startup-hook analog; the
#   marker fires on every substrate). `--hook` mode is kept DORMANT — re-wire it if a substrate exposes
#   a startup-hook analog. NOT auto-judgment (bond's K6-b): it SURFACES; the agent disposes.
#
# Usage:  bin/standup.sh          # d-start spine — human-readable resume report (stdout)
#         bin/standup.sh --hook   # DORMANT: emit SessionStart additionalContext JSON (for re-wiring)

set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"; cd "$ROOT" || exit 0

lines=(); add(){ lines+=("$1"); }

# -- Substrate probe (durable home + gh + falsify.py -> is the DM daemon armable?) --
home_ok=0; gh_ok=0; falsify_ok=0
[[ -d /mnt/shared_data/dzw ]] && home_ok=1
command -v gh >/dev/null 2>&1 && gh_ok=1
[[ -e commons/scripts/falsify.py ]] && falsify_ok=1
if ((home_ok && gh_ok && falsify_ok)); then
  add "Substrate: OK — durable home + gh + falsify.py -> DM daemons armable."
else
  miss=(); ((home_ok))||miss+=("no /mnt/shared_data/dzw"); ((gh_ok))||miss+=("no gh"); ((falsify_ok))||miss+=("no commons/falsify.py")
  add "Substrate: WARN — partial (${miss[*]}) -> DM daemons NOT armable; DM-watch is dark this session."
fi

# -- Durability (uncommitted/unpushed = ungrounded memory) --
dirty="$(git status --porcelain 2>/dev/null || true)"
branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo '?')"
unpushed="$(git log --oneline '@{u}..' 2>/dev/null | wc -l | tr -d ' ' || echo 0)"
if [[ -n "$dirty" ]]; then
  add "Durability: WARN — working tree DIRTY on '$branch' ($(printf '%s\n' "$dirty" | wc -l | tr -d ' ') paths) — commit before trusting the record as memory."
elif [[ "$unpushed" != "0" ]]; then
  add "Durability: WARN — $unpushed unpushed commit(s) on '$branch' — push so the remote backs the memory."
else
  add "Durability: OK — clean + in sync on '$branch'."
fi

# -- Frontier ready-set (local frontier.md view; no network) --
active="$(grep -m1 'ACTIVE (WIP-N=1' frontier.md 2>/dev/null | sed 's/\*\*//g' || true)"
ready="$(grep -c '\[READY\]' frontier.md 2>/dev/null || echo '?')"
add "Frontier: ${active:-ACTIVE: —} · ${ready} READY node(s) — bin/frontier.py for the tree."

# -- The agent's stand-up actions (session-only daemons die on restart; live pulls are network) --
add "RE-ARM (session-only Monitors died on restart — dm-daemon-rearm): DM-inbox · commons-PR · peer-review daemons; commands in the session-pin."
add "PULL live state this turn (network, not in this hook): bin/state.py (PRs · origin-sync) · falsify.py inbox · falsify.py list (FR) · reviews on our open PRs."

header="dyad-steward stand-up (bin/standup.sh) — mechanical resume checks. Ground in the FULL substrate (DYAD.md · frontier · session-pin · dialectic/) — anchor-only is half-grounded — then take the frontier ready-set."
body="$(printf '%s\n' "$header" '' "${lines[@]}")"

if [[ "${1:-}" == "--hook" ]]; then
  CTX="$body" python3 -c 'import json,os; print(json.dumps({"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":os.environ["CTX"]}}))'
else
  printf '%s\n' "$body"
fi
