#!/usr/bin/env python3
"""digest.py — what the self-operating Commons did lately, batched for the Operator.

The directory triad runs WITHOUT the FO (auto-merge ADDs + auto-merge own-entry UPDATEs + index self-heal).
Cutting that burden frees steering bandwidth — but only becomes leverage if the Operator keeps SIGHT of
what ran ([[cut-burden-not-awareness]]). This surfaces it, batched, to read at a rest-point — the answer to
async-interrupt thrash (don't interrupt per event; digest at a seam). Read-only: fetches the Commons remote
then queries origin/main + gh.

  bin/digest.py              # roster/drift + recent directory activity + index self-heals + merged PRs
  bin/digest.py --since 7.days   # window passed to `git log --since` (default: last 40 directory commits)
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMMONS = os.path.join(ROOT, "commons")
REMOTE = "The-Dyad-Practice-Commons/the-dyad-practice"


def out(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw).stdout.strip()


def main():
    since = sys.argv[sys.argv.index("--since") + 1] if "--since" in sys.argv else None
    out(["git", "-C", COMMONS, "fetch", "-q", "origin"])
    print("# Commons digest — what self-operation did (queried this run, NOT cached)\n")

    # roster + index drift
    ddir = os.path.join(COMMONS, "directory")
    n = len([f for f in os.listdir(ddir) if f.endswith(".yaml")])
    drift = subprocess.run([sys.executable, "scripts/regen_directory_index.py", "--check"],
                           capture_output=True, text=True, cwd=COMMONS).returncode
    print(f"roster: {n} registered dyads · public index: {'in sync ✓' if drift == 0 else 'STALE ⚠'}")

    # recent directory activity — A = registered, M = updated (index self-heals don't touch directory/)
    print("\nrecent directory activity (origin/main):")
    log = ["git", "-C", COMMONS, "log", "origin/main", "--name-status",
           "--pretty=format:@@%ad|%h|%s", "--date=short"]
    log += [f"--since={since}"] if since else ["-n", "40"]
    raw = out(log + ["--", "directory/"])
    rows, cur = [], None
    for line in raw.splitlines():
        if line.startswith("@@"):
            cur = line[2:].split("|")
        elif line and line[0] in "AM" and cur:
            verb = "registered" if line[0] == "A" else "updated"
            dyad = os.path.basename(line.split("\t")[-1]).replace(".yaml", "")
            rows.append(f"  {cur[0]}  {verb:<10} {dyad}  ({cur[1]})")
    print("\n".join(rows[:15]) if rows else "  (none in window)")

    # index self-heals (the auto-regen commits)
    print("\nindex self-heals (auto):")
    heals = out(["git", "-C", COMMONS, "log", "origin/main", "-n", "5", "--date=short",
                 "--pretty=format:  %ad  %h  %s", "--grep=regenerate DIRECTORY.md"])
    print(heals or "  (none yet — verified-by-execution pending the first post-install directory change)")

    # recent merged Commons PRs (live)
    print("\nrecent merged Commons PRs:")
    prs = out(["gh", "pr", "list", "-R", REMOTE, "--state", "merged", "--limit", "8",
               "--json", "number,title,mergedAt,author",
               "--jq", r'.[] | "  #\(.number)  \(.mergedAt[0:10])  \(.title)  (\(.author.login))"'])
    print(prs or "  (none / gh unavailable)")


if __name__ == "__main__":
    main()
