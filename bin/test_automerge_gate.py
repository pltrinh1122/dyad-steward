#!/usr/bin/env python3
"""No-Pure-G validate for the self-update auto-merge gate. Run: python3 bin/test_automerge_gate.py

Tests the PURE decision function `decide()` over the adversarial surface — the safety claim of the
staged Commons workflow lives or dies here, so this is the real gate, not the YAML.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "dialectic", "staged-commons", "scripts"))
from automerge_self_update_gate import decide, owner_of  # noqa: E402

ok = True


def check(name, cond):
    global ok
    print(f"  {'PASS' if cond else 'FAIL'} {name}")
    ok = ok and cond


BASE = {"name": "dyad-steward", "birth_hash": "sha256:" + "a" * 64,
        "locator": "github.com/pltrinh1122/dyad-steward", "summits": ["s1"]}
MOD = [{"filename": "directory/dyad-steward.yaml", "status": "modified"}]


def head(**over):
    h = dict(BASE)
    h.update(over)
    return h


# owner parsing
check("owner_of parses locator", owner_of("github.com/pltrinh1122/dyad-steward") == "pltrinh1122")
check("owner_of strips scheme", owner_of("https://github.com/foo/dyad-bar") == "foo")
check("owner_of rejects non-github", owner_of("gitlab.com/x/y") == "")

# the happy path: owner self-updates summits, identity intact, valid
m, r = decide(MOD, BASE, head(summits=["s1", "s2-new"]), "pltrinh1122", True)
check("own-entry summit update -> MERGE", m is True)

# locator update by owner is allowed (mutable)
m, r = decide(MOD, BASE, head(locator="github.com/pltrinh1122/dyad-steward-moved"), "pltrinh1122", True)
check("own-entry locator update -> MERGE", m is True)

# attacker editing someone else's entry
m, r = decide(MOD, BASE, head(summits=["evil"]), "mallory", True)
check("author != owner -> REJECT", m is False and "owner" in r)

# frozen identity
m, r = decide(MOD, BASE, head(birth_hash="sha256:" + "b" * 64), "pltrinh1122", True)
check("birth_hash change -> REJECT", m is False and "birth_hash" in r)
m, r = decide(MOD, BASE, head(name="dyad-stewardX"), "pltrinh1122", True)
check("name change -> REJECT", m is False and "name" in r)

# an ADD is the registration workflow's job, not this one
m, r = decide([{"filename": "directory/dyad-new.yaml", "status": "added"}], None, head(), "x", True)
check("added (not modified) -> REJECT", m is False)

# multi-file PR
m, r = decide(MOD + [{"filename": "directory/dyad-x.yaml", "status": "modified"}], BASE, head(), "p", True)
check("multi-file -> REJECT", m is False)

# non-directory path
m, r = decide([{"filename": "README.md", "status": "modified"}], BASE, head(), "pltrinh1122", True)
check("non-directory path -> REJECT", m is False)

# validator failed on head
m, r = decide(MOD, BASE, head(summits=["s1"]), "pltrinh1122", False)
check("validate_ok False -> REJECT", m is False and "valid" in r)

# missing base (cannot authorize an update with no prior state)
m, r = decide(MOD, None, head(), "pltrinh1122", True)
check("no base entry -> REJECT", m is False)

print("\nAUTOMERGE-GATE TESTS PASS" if ok else "\nAUTOMERGE-GATE TESTS FAIL")
sys.exit(0 if ok else 1)
