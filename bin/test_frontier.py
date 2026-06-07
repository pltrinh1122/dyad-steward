#!/usr/bin/env python3
"""Negative-controls for the frontier write-guard + drift gate. Run: python3 bin/test_frontier.py"""
import copy
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frontier as F  # noqa: E402

REAL = F.load()
ok = True


def check(name, cond):
    global ok
    print(f"  {'PASS' if cond else 'FAIL'} {name}")
    ok = ok and cond


# the live source is valid
check("real frontier_state.yml validates clean", F.validate(REAL) == [])

# WIP-N=1: a second ACTIVE is rejected
s = copy.deepcopy(REAL)
actives = [n for n in s["nodes"].values() if n["status"] == "ACTIVE"]
victim = next(nid for nid, n in s["nodes"].items() if n["status"] != "ACTIVE")
s["nodes"][victim]["status"] = "ACTIVE"
check("WIP-N=1 rejects a 2nd ACTIVE", any("WIP-N=1" in e for e in F.validate(s)))

# bad status enum is rejected
s = copy.deepcopy(REAL)
s["nodes"][victim]["status"] = "WIBBLE"
check("bad status rejected", any("bad status" in e for e in F.validate(s)))

# dangling dependency is rejected
s = copy.deepcopy(REAL)
s["nodes"][victim]["dependencies"] = ["no_such_node"]
check("dangling dependency rejected", any("not a node" in e for e in F.validate(s)))

# dependency cycle is rejected
s = copy.deepcopy(REAL)
a, b = list(s["nodes"])[0], list(s["nodes"])[1]
s["nodes"][a]["dependencies"] = [b]
s["nodes"][b]["dependencies"] = [a]
check("dependency cycle rejected", any("cycle" in e for e in F.validate(s)))

# projection is deterministic (idempotent render)
check("render_md is deterministic", F.render_md(REAL) == F.render_md(REAL))

# the on-disk view is in sync with source (the --check invariant)
check("frontier.md in sync with source", os.path.exists(F.VIEW) and open(F.VIEW).read() == F.render_md(REAL))

print("\nFRONTIER TESTS PASS" if ok else "\nFRONTIER TESTS FAIL")
sys.exit(0 if ok else 1)
