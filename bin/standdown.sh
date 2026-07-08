#!/usr/bin/env bash
# bin/standdown.sh — dyad-steward stand-down ritual.
#   Borrowed from dyad-bond's K6 stand-down spine (2026-07-04, fresh-fetched from its remote); adapted to
#   steward — frontier + bin/state.py, the D3 reflection component, no carry-forward.md / bin/git.sh.
#
# WHY: close the session so the next recovers-forward without re-deriving. A MECHANICAL half (the
#   verified durability read-back + frontier drift — automate it) and a JUDGMENT half (resume surface;
#   the reflection; the resume-worthy filter — the agent's covalent act, NOT automatable).
#
# HOOK BOUNDARY (Claude Code contract): SessionEnd is TEARDOWN-ONLY — it fires after the agent is gone
#   and CANNOT inject context back; Stop fires every turn-end (cannot mean "stand-down"). So the
#   SessionEnd hook runs `--log` only (the mechanical line -> debug log); the AGENT runs this at close
#   and fills the JUDGMENT template. (bond's K6-b: auto-trigger != auto-judgment.)
#
# TRIGGER (2026-07-04): this is now the mechanical spine of the **`d-reflect`** marker (the Operator's
#   portable session-CLOSE trigger — dialectic/session-lifecycle-discipline.md), NOT a live Claude hook.
#   The Claude SessionEnd hook was RETIRED for portability. `--log` mode is kept DORMANT for re-wiring.
#
# Usage:  bin/standdown.sh         # d-reflect spine — read-back + the stand-down template (agent runs at close)
#         bin/standdown.sh --log   # DORMANT: mechanical durability line only (for re-wiring a teardown hook)

set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"; cd "$ROOT" || exit 0

# -- Mechanical durability read-back (verified, not cached — gate-durability-as-hard-condition) --
dirty="$(git status --porcelain 2>/dev/null || true)"
branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo '?')"
unpushed="$(git log --oneline '@{u}..' 2>/dev/null | wc -l | tr -d ' ' || echo 0)"
pin="$(git -C commons rev-parse --short HEAD 2>/dev/null || echo '?')"
dur="OK — clean + in sync on '$branch' · commons pin $pin"
[[ -n "$dirty" ]] && dur="WARN — DIRTY on '$branch' ($(printf '%s\n' "$dirty" | wc -l | tr -d ' ') paths) — commit + push; done is reachable only through a clean+pushed read-back"
[[ -z "$dirty" && "$unpushed" != "0" ]] && dur="WARN — $unpushed unpushed commit(s) on '$branch' — push"
frdrift="$(python3 bin/frontier.py --check >/dev/null 2>&1 && echo 'OK — in sync' || echo 'WARN — DRIFT (run bin/frontier.py --md)')"

mech="$(printf '%s\n' "dyad-steward stand-down — mechanical read-back (verified, not cached):" "  Durability: $dur" "  Frontier: $frdrift")"

if [[ "${1:-}" == "--log" ]]; then printf '%s\n' "$mech"; exit 0; fi

state="$(timeout 25 python3 bin/state.py 2>/dev/null || echo '(run bin/state.py by hand — live PR/sync state)')"
# DM read-state surface (non-consuming — inbox counts, never marks read): makes read-state divergence
# VISIBLE at close so processed-but-uncommitted DMs can't silently accumulate (read-state-diverges-from-
# processing, 2026-07-08). RC1 splits '• new' vs '⟳ edited-since-read'; a ⟳ re-surface is not new mail.
dm="$(timeout 25 python3 commons/scripts/falsify.py inbox --me dyad-steward 2>/dev/null | grep -E 'mail:|no mail|unreachable:' || echo '(run falsify.py inbox — DM read-state surface)')"

cat <<TEMPLATE
$mech

  DM read-state (non-consuming surface): $(printf '%s' "$dm" | head -1)
$(printf '%s' "$dm" | tail -n +2 | sed 's/^/  /')

$state

dyad-steward stand-down — JUDGMENT (the agent fills; auto-trigger != auto-judgment):
  Resume-worthy filter — record an item ONLY if (a) in-flight (a live front, not closed), (b) not already
    single-homed elsewhere (point to frontier/dialectic, don't restate), (c) load-bearing for resume.
    Else DROP. The frontier is the memory, not a journal.

  Checklist:
   1. Durability (above): if DIRTY/unpushed — commit + push FIRST; "done" is reachable only through the
      clean+pushed read-back (DYAD.md §NON-NEGOTIABLE). Advance the commons pin if a Commons PR merged.
   2. Frontier: set ACTIVE->DONE / statuses; drop what closed; add only in-flight resume-worthy nodes.
   2b. DM read-state (above): if you PROCESSED any DM this session, consume + commit it (falsify.py dm
      -> commit .falsify-seen.json) so read-state doesn't lag processing (read-state-diverges-from-
      processing). A '⟳ edited-since-read' re-surface is NOT new mail — a peer's in-place edit, re-check
      but don't re-process. Do NOT blind-consume unread you didn't engage; surface it as an OPEN thread.
   3. Resume surface: FO-gate (open PRs awaiting the gavel) · open threads · live follow-up nodes.
   4. Reflection (d-reflect ⊂ stand-down): if the session harvested lessons, run the D3 CSS+SH retro
      -> dialectic/reflections/<date>.md. CSS = Agent (Continue/Start/Stop); SH = Operator-provenance
      (Should-Have/Should-Hold, descriptive, verbatim-quoted; Should-Have needs the materiality bar).
   5. Daemons: session-only (die on restart) — note in the session-pin for next stand-up re-arm.
   6. Stand-down note: dialectic/stand-downs/<date>-session-stand-down.md — what closed · the +1 ·
      FO-gate · OPEN/resume · State (verified, not cached). Commit + push.
TEMPLATE
