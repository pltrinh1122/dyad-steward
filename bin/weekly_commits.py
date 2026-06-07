#!/usr/bin/env python3
"""weekly_commits.py — recruitment signal: commits-per-week across the Commons dyads.

Reads each registered dyad's `locator` from commons/directory/*.yaml and reports the
number of commits on its default branch within a given ISO week. This is a LIVENESS
signal for a *potential* operator ("is anyone home?") — deliberately NOT a productivity
metric: it counts only PUBLIC commit activity on each dyad's anchor repo, and a private
or unreachable repo is reported as such, never as zero.

Usage:
  bin/weekly_commits.py                  # rolling: commits in the last 7 days from now (UTC)
  bin/weekly_commits.py --days 30        # rolling: last N days
  bin/weekly_commits.py --week 2026-W23  # a specific fixed ISO week (Mon-Sun)

The DEFAULT is a window of [update-timestamp - 7d, update-timestamp] — the rolling form the
directory will carry. The window is stamped into the header ("activity as of <ts>, trailing Nd")
so a generated DIRECTORY.md block is honest about its own freshness and a drift-check can verify
correctness *as of the stated time* rather than demanding the count equal "now".
"""
import os
import sys
import glob
import subprocess
from datetime import date, datetime, timedelta, timezone

import yaml

DIRDIR = os.path.join(os.path.dirname(__file__), "..", "commons", "directory")


def window_bounds(week_arg, days):
    """(start, end, label) for the activity window.

    Default (week_arg None): a rolling window of the last `days` ending at the update
    timestamp `now` — this is the form the directory carries, and `end` IS the stamped
    as-of time. `--week` selects a fixed ISO week instead (end = exclusive next-Monday)."""
    if week_arg:
        y, w = week_arg.upper().split("-W")
        monday = date.fromisocalendar(int(y), int(w), 1)
        start = datetime(monday.year, monday.month, monday.day, tzinfo=timezone.utc)
        end = start + timedelta(days=7)
        return start, end, f"ISO week {monday.isocalendar()[0]}-W{monday.isocalendar()[1]:02d}"
    end = datetime.now(timezone.utc).replace(microsecond=0)
    start = end - timedelta(days=days)
    return start, end, f"trailing {days}d as of {end.isoformat()}"


def repo_from_locator(loc):
    """owner/repo from a 'github.com/owner/repo' locator, else None (private/placeholder)."""
    loc = (loc or "").strip().rstrip("/")
    prefix = "github.com/"
    if not loc.startswith(prefix):
        return None
    rest = loc[len(prefix):]
    return rest if rest.count("/") == 1 and "<" not in rest else None


def commit_count(repo, start, end):
    """(count, None) on success; (None, reason) on error. Counts default-branch commits."""
    cmd = [
        "gh", "api", "--paginate",
        f"repos/{repo}/commits?since={start.isoformat()}&until={end.isoformat()}",
        "--jq", ".[].sha",
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        # an empty repo (no commits at all) is liveness 0, not an error
        if "Git Repository is empty" in r.stderr:
            return 0, None
        # 404 = private or no public access — to a recruit it's simply unreachable,
        # the same as a declared-private locator. Don't leak the raw gh error.
        if "Not Found" in r.stderr or "404" in r.stderr:
            return None, "private/unreachable"
        return None, (r.stderr.strip().splitlines() or ["error"])[-1]
    return len([s for s in r.stdout.splitlines() if s.strip()]), None


def main():
    week_arg = None
    days = 7
    argv = sys.argv[1:]
    for i, a in enumerate(argv):
        if a.startswith("--week"):
            week_arg = a.split("=", 1)[1] if "=" in a else argv[i + 1]
        elif a.startswith("--days"):
            days = int(a.split("=", 1)[1] if "=" in a else argv[i + 1])
    start, end, label = window_bounds(week_arg, days)

    rows = []
    for path in sorted(glob.glob(os.path.join(DIRDIR, "*.yaml"))):
        with open(path, encoding="utf-8") as f:
            entry = yaml.safe_load(f) or {}
        name = entry.get("name") or os.path.splitext(os.path.basename(path))[0]
        repo = repo_from_locator(entry.get("locator"))
        if not repo:
            rows.append((name, None, "private/unreachable"))
            continue
        count, err = commit_count(repo, start, end)
        rows.append((name, count, err))

    counted = [c for _, c, _ in rows if isinstance(c, int)]
    total = sum(counted)
    active = sum(1 for c in counted if c > 0)

    print(f"Commons recruitment signal — commits, {label}\n")
    rows.sort(key=lambda r: (-1 if r[1] is None else r[1]), reverse=True)
    for name, count, note in rows:
        if count is None:
            print(f"  {name:<26} —      ({note})")
        else:
            print(f"  {name:<26} {count:>4}" + (f"   ({note})" if note else ""))
    print(f"\n  {len(rows)} dyads registered · {active} active in window · "
          f"{total} commits total ({len(counted)} repos reachable)")


if __name__ == "__main__":
    main()
