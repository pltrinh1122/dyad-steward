#!/usr/bin/env python3
"""state.py — emit canonical live state so a "where-things-stand" recap is THIS TOOL'S OUTPUT,
not prose from a stale context-cache.

The MECHANICAL half of the verify-reporting discipline (AGENT.md §NON-NEGOTIABLE; [[verify-with-actual-
tool]], n≥3): the context window is a stale-by-default cache of mutable remote state — PR open/merged,
local↔origin sync — and I have mis-reported it from memory repeatedly across sessions. This queries the
SOURCE this run and prints it. Run it at the seams the slip fires — the closing recap, Stand-Up,
Stand-Down — and read/paste its output instead of narrating from the cache. Read-only (git/gh reads,
no mutation; `ls-remote` reads origin without even a fetch).

  python3 bin/state.py
"""
import subprocess


def out(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout.strip()


def main():
    repo = out(["gh", "repo", "view", "--json", "nameWithOwner", "-q", ".nameWithOwner"]) or "?"
    root = out(["git", "rev-parse", "--show-toplevel"])

    print(f"# live state — {repo} (queried this run, NOT cached)\n")

    # main: local vs origin truth (ls-remote = origin without a fetch)
    local = (out(["git", "rev-parse", "main"]) or "?")[:9]
    remote_line = out(["git", "ls-remote", "origin", "refs/heads/main"])
    remote = remote_line.split()[0][:9] if remote_line else "?"
    print(f"main: local {local} / origin {remote}  "
          f"[{'SYNCED' if local == remote and local != '?' else 'DIVERGED — fetch'}]")

    # working tree
    dirty = out(["git", "status", "--short"])
    print(f"working tree: {'clean' if not dirty else 'DIRTY'}")
    for line in dirty.splitlines():
        print(f"  {line}")

    # open PRs (live)
    prs = out(["gh", "pr", "list", "--state", "open", "--json", "number,title,headRefName",
               "--jq", r'.[] | "  #\(.number) [\(.headRefName)] \(.title)"'])
    print(f"\nopen PRs: {'none' if not prs else ''}")
    if prs:
        print(prs)

    # frontier: ACTIVE node + READY-SET (the live source is frontier_state.yml, not the retired board.md)
    print("\nfrontier (ACTIVE + READY-SET — `bin/frontier.py tree` for the full DAG):")
    try:
        import yaml
        with open(f"{root}/frontier_state.yml", encoding="utf-8") as f:
            nodes = (yaml.safe_load(f) or {}).get("nodes", {})
        active = [nid for nid, n in nodes.items() if n.get("status") == "ACTIVE"]
        ready = sorted(nid for nid, n in nodes.items() if n.get("status") == "READY")
        print(f"  ACTIVE [WIP-N=1]: {active[0] if active else '— none (idle)'}")
        print("  READY-SET (pick one):")
        for nid in ready:
            print(f"    ○ {nid} — {nodes[nid].get('title', '')}")
        if not ready:
            print("    (none)")
    except FileNotFoundError:
        print("  (frontier_state.yml not found)")


if __name__ == "__main__":
    main()
