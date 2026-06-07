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

# WIP-N=1: two ACTIVE is rejected (force two, independent of REAL's current ACTIVE count)
s = copy.deepcopy(REAL)
two = list(s["nodes"])[:2]
for nid in two:
    s["nodes"][nid]["status"] = "ACTIVE"
check("WIP-N=1 rejects two ACTIVE", any("WIP-N=1" in e for e in F.validate(s)))
victim = list(s["nodes"])[0]  # a node id reused by the checks below (deepcopy per-check)

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

# node-type: a bad type is rejected
s = copy.deepcopy(REAL)
s["nodes"][victim]["type"] = "WIBBLE"
check("bad node-type rejected", any("bad type" in e for e in F.validate(s)))

# FALSIFIED is a PROBE-only terminal — rejected on a non-PROBE
s = copy.deepcopy(REAL)
s["nodes"][victim]["type"] = "EXECUTE"
s["nodes"][victim]["status"] = "FALSIFIED"
check("FALSIFIED on a non-PROBE rejected", any("only a PROBE may be FALSIFIED" in e for e in F.validate(s)))

# FALSIFIED on a PROBE is allowed (a probe that falsified its friction-condition)
s = copy.deepcopy(REAL)
s["nodes"][victim]["type"] = "PROBE"
s["nodes"][victim]["status"] = "FALSIFIED"
check("FALSIFIED on a PROBE allowed", not any("FALSIFIED" in e for e in F.validate(s)))

# projection is deterministic (idempotent render)
check("render_md is deterministic", F.render_md(REAL) == F.render_md(REAL))

# the on-disk view is in sync with source (the --check invariant)
check("frontier.md in sync with source", os.path.exists(F.VIEW) and open(F.VIEW).read() == F.render_md(REAL))

# --- SPAOR-traversal CSI traps (arm/disarm pairs) — armed-state monkeypatched, registry untouched ---
_orig_armed = F.armed_spaor_guards

# csi_probe_invariant ARMED: a PROBE missing its single `invariant:` is trapped
F.armed_spaor_guards = lambda: {"csi_probe_invariant"}
s = copy.deepcopy(REAL)
a_probe = next(nid for nid, n in s["nodes"].items() if n.get("type") == "PROBE")
s["nodes"][a_probe].pop("invariant", None)
check("armed csi_probe_invariant traps a PROBE with no invariant",
      any("csi_probe_invariant armed" in e for e in F.validate(s)))

# DISARMED: the very same missing-invariant PROBE is NOT trapped (registered but inert)
F.armed_spaor_guards = lambda: set()
check("disarmed csi_probe_invariant is inert",
      not any("csi_probe_invariant" in e for e in F.validate(s)))

# every real PROBE carries its single invariant, so the armed trap passes on the live board
F.armed_spaor_guards = lambda: {"csi_probe_invariant"}
check("armed csi_probe_invariant passes on the live board",
      not any("csi_probe_invariant" in e for e in F.validate(copy.deepcopy(REAL))))

# csi_execute_tested ARMED: a DONE EXECUTE with no `tests:` ref is trapped
F.armed_spaor_guards = lambda: {"csi_execute_tested"}
s = copy.deepcopy(REAL)
a_exec = next(nid for nid, n in s["nodes"].items()
              if n.get("type", "EXECUTE") == "EXECUTE" and n.get("status") == "DONE")
s["nodes"][a_exec].pop("tests", None)
check("armed csi_execute_tested traps a DONE EXECUTE with no tests",
      any("csi_execute_tested armed" in e for e in F.validate(s)))

F.armed_spaor_guards = _orig_armed

print("\nFRONTIER TESTS PASS" if ok else "\nFRONTIER TESTS FAIL")
sys.exit(0 if ok else 1)
