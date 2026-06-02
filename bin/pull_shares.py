#!/usr/bin/env python3
"""pull_shares.py — pull inbound cross-dyad shares so the Operator isn't the copy-paste transport.

Reads the Commons directory (the registered dyads + their locators) live, then lists each sibling's
`recommendations/` — the convergent cross-dyad sharing channel (healer/bond/wu-wei all use it). Shares
ADDRESSED to us (filename contains "steward") are auto-fetched and printed; general recommendations are
listed for the Operator to pick. Run at Stand-Up or on demand.

  python3 bin/pull_shares.py                 # list all; auto-show *for-steward*
  python3 bin/pull_shares.py --since 2026-06-02   # only shares dated on/after
  python3 bin/pull_shares.py --repo owner/repo    # also pull a NOT-yet-registered dyad (transition
                                                  #   handle; only works if its repo is readable to gh)
  python3 bin/pull_shares.py --fetch <owner/repo:path>   # print one share's body

Survivor of the 2026-06-02 [ALIGN] ("not wu-wei for the Operator to copy-paste the sharing of dyadic
validation"): the Operator keeps the GATE (which to engage); the Agent takes the TRANSPORT. Uses `gh`
(read-only). Partially implements commons-change-awareness.md's "pull / what-changed-for-me" candidate.
"""
import json
import subprocess
import sys

SELF = "dyad-steward"
COMMONS = "The-Dyad-Practice-Commons/the-dyad-practice"


def gh(path, jq=None):
    cmd = ["gh", "api", path]
    if jq:
        cmd += ["--jq", jq]
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def b64_decode(content):
    import base64
    return base64.b64decode(content).decode("utf-8", "replace")


def directory_dyads():
    """Live from the Commons: [(name, owner/repo)] for every registered dyad except self."""
    names = gh(f"repos/{COMMONS}/contents/directory?ref=main",
               '.[].name | select(endswith(".yaml"))')
    out = []
    for fn in (names or "").splitlines():
        name = fn[:-len(".yaml")]
        if name == SELF:
            continue
        c = gh(f"repos/{COMMONS}/contents/directory/{fn}?ref=main", ".content")
        if not c:
            continue
        loc = next((l.split("locator:", 1)[1].strip() for l in b64_decode(c).splitlines()
                    if l.strip().startswith("locator:")), None)
        if loc:  # github.com/<owner>/<repo> -> owner/repo
            out.append((name, loc.replace("github.com/", "").strip().rstrip("/")))
    return out


def list_recs(repo):
    """[(filename, addressed_to_steward)] from a sibling's recommendations/ dir."""
    listing = gh(f"repos/{repo}/contents/recommendations?ref=main", ".[].name")
    files = [f for f in (listing or "").splitlines() if f.endswith(".md")]
    return [(f, "steward" in f.lower()) for f in files]


def main():
    args = sys.argv[1:]
    if "--fetch" in args:
        spec = args[args.index("--fetch") + 1]          # owner/repo:path
        repo, path = spec.split(":", 1)
        c = gh(f"repos/{repo}/contents/{path}?ref=main", ".content")
        print(b64_decode(c) if c else f"[pull_shares] not found: {spec}")
        return
    since = args[args.index("--since") + 1] if "--since" in args else None
    extra = [(f"{r} (unregistered)", r) for i, r in enumerate(args)
             if i > 0 and args[i - 1] == "--repo"]

    print(f"[pull_shares] inbound recommendations across the Commons directory"
          f"{f' since {since}' if since else ''}:\n")
    addressed = []
    for name, repo in directory_dyads() + extra:
        recs = list_recs(repo)
        if since:
            recs = [(f, a) for (f, a) in recs if f[:10] >= since]
        if not recs:
            continue
        print(f"  {name}  ({repo})")
        for fn, to_us in sorted(recs):
            tag = "  ← FOR STEWARD" if to_us else ""
            print(f"    {fn}{tag}")
            if to_us:
                addressed.append((repo, f"recommendations/{fn}"))
        print()

    for repo, path in addressed:
        print("=" * 78)
        print(f"ADDRESSED — {repo}:{path}")
        print("=" * 78)
        c = gh(f"repos/{repo}/contents/{path}?ref=main", ".content")
        print(b64_decode(c) if c else "[unreadable]")
        print()
    if not addressed:
        print("[pull_shares] no shares addressed to steward; general recs listed above "
              "(the Operator picks which to engage — the gate stays yours).")


if __name__ == "__main__":
    main()
