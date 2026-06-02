#!/usr/bin/env python3
"""Grant dyad-steward direct push-to-main in a Claude Code settings file.

Borrowed from dyad-bond@bin/grant_push.py (which inherited the form from
dyad-healer). **steward-particular allow-rule:** we do NOT wrap git in a
bin/git.sh choke-point (bond/healer do, for foreign-substrate boundary integrity
we don't have). Our friction is narrower — administrative durability (reflections,
stand-downs, session logs) to our OWN main — so we grant the precise rule the
harness carve-out asks for: `Bash(git push origin main)`.

Adds that allow-rule (+ the HEAD:main form) plus steward's destructive-push
deny-list (defense-in-depth), idempotently, with an atomic, non-clobbering write.

NOTE: executing this against the real settings file IS the permission grant — by
the covalent gate that is the OPERATOR'S act, never the Agent's self-grant (the
move the classifier correctly blocks). The Agent authors this tool; the Operator
runs it.  Reason + the two per-dyad questions live in dialectic/substrate-access.md.
"""
import argparse
import json
import os
import pathlib
import sys
import tempfile

# steward-particular: direct push to our own main (no wrapper). NOT bond's Bash(bin/git.sh:*).
ALLOW = ["Bash(git push origin main)", "Bash(git push origin HEAD:main)"]
DENY = [
    "Bash(git push --force*)",
    "Bash(git push * --force*)",
    "Bash(git push -f*)",
    "Bash(git push * -f*)",
    "Bash(git push --delete*)",
    "Bash(git push * --delete*)",
    "Bash(git push * -d*)",
    "Bash(git push +*)",
    "Bash(git push * +*)",
    "Bash(git push * :*)",
]


def grant(path):
    p = pathlib.Path(path)
    raw = p.read_text() if p.exists() else ""
    try:
        cfg = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError as e:
        sys.exit(f"REFUSED: {p} is not valid JSON ({e}); leaving it untouched.")
    if not isinstance(cfg, dict):
        sys.exit(f"REFUSED: top-level of {p} is not a JSON object; leaving it untouched.")

    perms = cfg.setdefault("permissions", {})
    allow = perms.setdefault("allow", [])
    deny = perms.setdefault("deny", [])
    if not isinstance(allow, list) or not isinstance(deny, list):
        sys.exit(f"REFUSED: permissions.allow/deny in {p} are not lists; leaving it untouched.")

    added = []
    for a in ALLOW:
        if a not in allow:
            allow.append(a)
            added.append(("allow", a))
    for d in DENY:
        if d not in deny:
            deny.append(d)
            added.append(("deny", d))

    # atomic write: tmp in same dir + os.replace (never clobber on failure)
    p.parent.mkdir(parents=True, exist_ok=True)
    out = json.dumps(cfg, indent=2) + "\n"
    fd, tmp = tempfile.mkstemp(dir=str(p.parent), prefix=".settings-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w") as f:
            f.write(out)
        os.replace(tmp, p)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise

    if added:
        print(f"✓ {p}: added {len(added)} entr{'y' if len(added) == 1 else 'ies'}:")
        for kind, v in added:
            print(f"    +{kind}: {v}")
    else:
        print(f"✓ {p}: already complete — no change (idempotent).")
    print("\n--- resulting file ---")
    print(p.read_text(), end="")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--path", default=".claude/settings.json",
                    help="settings file to update (default: .claude/settings.json; "
                         "use .claude/settings.local.json for the gitignored local tier)")
    grant(ap.parse_args().path)


if __name__ == "__main__":
    main()
