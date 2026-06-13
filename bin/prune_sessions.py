#!/usr/bin/env python3
"""prune_sessions.py — list stale `claude/*` cloud-session branches whose PR is MERGED, so the
periodic branch sweep is one read-only command + one Operator paste.

WHY: Claude Code on the web mints one `claude/<slug>-<id>` branch per cloud session. Merged PRs
don't auto-delete their head branch here, so these accumulate on origin (the lived 2026-06-13
clutter — 25 stale branches). This surfaces the safe-to-delete set; it NEVER deletes.

The delete is the OPERATOR's act, never the Agent's: DYAD.md §NON-NEGOTIABLE keeps destructive git
out of the Agent's hands (.claude/settings.json denies `git push * --delete*`). So this prints the
exact `git push origin --delete …` line for you to run by hand — the covalent gate, same posture as
bin/grant_push.py. Read-only here (git ls-remote + gh reads; no fetch, no mutation).

  python3 bin/prune_sessions.py          # claude/* session branches only (the per-session tap)
  python3 bin/prune_sessions.py --all    # every branch with a merged PR (full sweep)
"""
import shutil
import subprocess
import sys


def out(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout.strip()


def main():
    all_branches = "--all" in sys.argv
    current = out(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    default = out(["git", "symbolic-ref", "--short", "refs/remotes/origin/HEAD"]).split("/")[-1] or "main"

    # origin branch heads, read without a fetch (ls-remote queries origin directly)
    pattern = "refs/heads/*" if all_branches else "refs/heads/claude/*"
    heads = out(["git", "ls-remote", "--heads", "origin", pattern])
    branches = [line.split("refs/heads/", 1)[1] for line in heads.splitlines() if "refs/heads/" in line]
    # never propose deleting the branch we're on or the default branch
    branches = [b for b in branches if b not in (current, default)]

    scope = "all branches" if all_branches else "claude/* session branches"
    print(f"# session-branch sweep — {scope} (queried this run; current={current}, default={default})\n")

    if not branches:
        print("no candidate branches on origin.")
        return

    # merge-classification needs gh; the git-only listing still works without it.
    if not shutil.which("gh"):
        print(f"candidate branches on origin ({len(branches)}):")
        for b in sorted(branches):
            print(f"  • {b}")
        print("\n(install `gh` / run where `gh` is available to classify these by merged-PR state.)")
        return

    merged, kept = [], []
    for b in sorted(branches):
        # authoritative merge signal: a MERGED PR with this head (not `git branch --merged`,
        # which mis-reports squash/auto-merged PRs as unmerged — lived 2026-06-13).
        pr = out(["gh", "pr", "list", "--state", "merged", "--head", b,
                  "--json", "number", "--jq", ".[0].number // empty"])
        if pr:
            merged.append((b, pr))
        else:
            # distinguish "has an OPEN PR" from "no PR at all" so the keep-reason is legible
            openpr = out(["gh", "pr", "list", "--state", "open", "--head", b,
                          "--json", "number", "--jq", ".[0].number // empty"])
            kept.append((b, f"open PR #{openpr}" if openpr else "no merged PR — review by hand"))

    print(f"SAFE TO DELETE — merged PR confirmed ({len(merged)}):")
    for b, pr in merged:
        print(f"  ✓ {b}  (PR #{pr} merged)")
    print(f"\nKEEP — not confirmed merged ({len(kept)}):")
    for b, why in kept:
        print(f"  • {b}  ({why})")

    if merged:
        names = " ".join(b for b, _ in merged)
        print("\n# run by hand (Agent is deny-guarded from destructive push — by design):")
        print(f"git push origin --delete {names}")


if __name__ == "__main__":
    main()
