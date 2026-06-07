#!/usr/bin/env python3
"""preflight.py — Tier-1 repo-invariants checker (steward-validation-infra, CONVERGED 2026-06-02).

The MECHANICAL half of validation (the behavioral half is the verify triad in AGENT.md): a standing
invariants check the artifacts run on themselves BEFORE a PR — the emergence move, no Steward in the
per-check loop. Plain Python, no framework (mirrors the Commons' validate_registry.py grain).

Two homes (nouns-vs-verbs): this is a Steward *verb* and homes HERE. It INVOKES the Commons
validate_registry.py (single source of truth — never reimplements the Commons rule; that is the
verify-with-actual-tool trap) and ADDS our-side checks the Commons doesn't carry.

The wu-wei rule: an invariant enters ONLY when a real defect proved it missing — not speculative
coverage. Each check below is tagged with the lived defect that earned it:

  parse      every *.yaml/*.json (ours + commons/directory) parses     (latent; the cheap floor)
  registry   commons/directory/*.yaml pass the Commons validate_file —  (PR#20 summit-YAML corruption;
             the EXACT call the auto-merge workflow makes                 9c28f03 birth_hash fix)
  refs       every relative markdown link in our .md resolves to a file  (CONTRIBUTING 404; rename
                                                                          link-breaks)
  submodule  commons checkout == remote main (a stale checkout makes     (lived 2026-06-03: submodule
             the local validator a DIFFERENT rule than the live           4 commits behind main →
             workflow's — a false single-source-of-truth)                 local validator was stale)

Deferred — NOT yet earned / blocked / behavioral (do not add speculatively):
  - universal record-shape   → blocked on 3b metadata-rep (Commons-side, Founding-gated)
  - birth-hash RECOMPUTE     → needs the canonical concat formula (CLAUDE.md identity caveat); escalation
  - onboard cold-path        → Tier 2 (behavioral); homes in the Commons by script-ownership

  python3 bin/preflight.py            # run all; exit 1 if any invariant fails
  python3 bin/preflight.py --offline  # skip the one network check (submodule-vs-remote)
"""
import json
import os
import re
import subprocess
import sys

# Don't dirty the substrate we check: importing the Commons validator must not write __pycache__
# into the commons/ submodule working tree (it surfaces as untracked content inside the submodule).
sys.dont_write_bytecode = True

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMMONS_REMOTE = "The-Dyad-Practice-Commons/the-dyad-practice"
# Our-repo markdown surface for reference integrity (our generation; commons/ is Commons-owned).
MD_DIRS = ["", "dialectic", "kb"]
LINK_RE = re.compile(r"\[[^\]]*\]\(\s*<?([^)>\s]+)>?\s*\)")
# Strip code (fenced + inline) before link extraction: literal markup quoted as code is not a
# navigable link — counting it is the false positive a doc that *documents* link syntax would trip.
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`]*`")


def extract_links(text):
    """Markdown link targets, code (fenced + inline) stripped FIRST — a link quoted as code is not
    navigable and must not be flagged. (Testable seam guarding the quoted-link false-positive fix.)"""
    return LINK_RE.findall(INLINE_CODE_RE.sub("", FENCE_RE.sub("", text)))


def fail(check, msg):
    print(f"  FAIL [{check}] {msg}")


def list_md():
    files = []
    for d in MD_DIRS:
        base = os.path.join(ROOT, d)
        if not os.path.isdir(base):
            continue
        for name in sorted(os.listdir(base)):
            if name.endswith(".md"):
                files.append(os.path.join(base, name))
    return files


def check_parse():
    """Every YAML/JSON we own (+ the Commons-bound directory) parses."""
    import yaml
    ok = True
    targets = []
    # Our repo, excluding the commons submodule (Commons-owned) and .git.
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "commons")]
        for f in filenames:
            if f.endswith((".yaml", ".yml", ".json")):
                targets.append(os.path.join(dirpath, f))
    # Plus the Commons-bound registry (our registration homes here before we PR it).
    dirp = os.path.join(ROOT, "commons", "directory")
    if os.path.isdir(dirp):
        targets += [os.path.join(dirp, f) for f in os.listdir(dirp) if f.endswith(".yaml")]
    for path in targets:
        try:
            with open(path, encoding="utf-8") as fh:
                (json.load if path.endswith(".json") else yaml.safe_load)(fh)
        except Exception as e:
            ok = False
            fail("parse", f"{os.path.relpath(path, ROOT)}: {e}")
    return ok


def check_registry():
    """Run the Commons validator (single source of truth) on each directory entry."""
    scripts = os.path.join(ROOT, "commons", "scripts")
    dirp = os.path.join(ROOT, "commons", "directory")
    if not os.path.isdir(scripts) or not os.path.isdir(dirp):
        fail("registry", "commons submodule not checked out (run: git submodule update --init)")
        return False
    sys.path.insert(0, scripts)
    try:
        from validate_registry import validate_file  # the EXACT symbol the workflow imports
    except Exception as e:
        fail("registry", f"cannot import Commons validate_registry: {e}")
        return False
    ok = True
    for name in sorted(os.listdir(dirp)):
        if name.endswith(".yaml") and not validate_file(os.path.join(dirp, name)):
            ok = False  # validate_file already printed its own FAIL line
    return ok


def check_refs():
    """Every relative markdown link in our docs resolves to a real file."""
    ok = True
    for md in list_md():
        with open(md, encoding="utf-8") as fh:
            text = fh.read()
        base = os.path.dirname(md)
        for target in extract_links(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path = target.split("#", 1)[0]  # drop in-page anchor
            if not path:
                continue
            if not os.path.exists(os.path.normpath(os.path.join(base, path))):
                ok = False
                fail("refs", f"{os.path.relpath(md, ROOT)} → {target} (no such file)")
    return ok


def check_submodule(offline):
    """The commons checkout must equal remote main, or the local validator is a stale rule."""
    try:
        head = subprocess.check_output(
            ["git", "-C", os.path.join(ROOT, "commons"), "rev-parse", "HEAD"], text=True).strip()
    except Exception as e:
        fail("submodule", f"cannot read commons HEAD: {e}")
        return False
    if offline:
        print("  SKIP [submodule] --offline (remote not checked)")
        return True
    try:
        remote = subprocess.check_output(
            ["gh", "api", f"repos/{COMMONS_REMOTE}/commits/main", "--jq", ".sha"], text=True).strip()
    except Exception as e:
        fail("submodule", f"cannot read remote main (use --offline to skip): {e}")
        return False
    if head != remote:
        fail("submodule", f"commons@{head[:7]} != remote main@{remote[:7]} — "
                          "run: git submodule update --remote commons")
        return False
    return True


def check_frontier():
    """Frontier source must be valid + `frontier.md` in sync — run the real tool, not a reimpl."""
    r = subprocess.run([sys.executable, os.path.join(ROOT, "bin", "frontier.py"), "--check"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        for line in (r.stdout + r.stderr).strip().splitlines():
            fail("frontier", line.strip())
        return False
    return True


TOPOLOGY_CAPS = {"bin": 25, "kb": 25}  # csi_topology_mass — generous tripwires vs future bloat


def check_topology():
    """Code/knowledge dirs stay lean (file-count <= cap) — CSI guard csi_topology_mass."""
    ok = True
    for d, cap in TOPOLOGY_CAPS.items():
        path = os.path.join(ROOT, d)
        if not os.path.isdir(path):
            continue
        n = len([f for f in os.listdir(path)
                 if os.path.isfile(os.path.join(path, f))
                 and not f.startswith(".") and not f.endswith(".pyc")])
        if n > cap:
            fail("topology", f"{d}/ has {n} files > cap {cap} — COMPRESS, or raise the cap deliberately")
            ok = False
    return ok


def main():
    offline = "--offline" in sys.argv[1:]
    checks = [
        ("parse", check_parse),
        ("registry", check_registry),
        ("refs", check_refs),
        ("submodule", lambda: check_submodule(offline)),
        ("frontier", check_frontier),
        ("topology", check_topology),
    ]
    all_ok = True
    for name, fn in checks:
        print(f"[{name}]")
        if not fn():
            all_ok = False
    print("\nPREFLIGHT PASS" if all_ok else "\nPREFLIGHT FAIL")
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
