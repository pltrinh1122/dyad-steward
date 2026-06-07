#!/usr/bin/env python3
"""No-Pure-G validate for rack.py — LIFO order + provenance. Run: python3 bin/test_rack.py"""
import os
import subprocess
import sys
import tempfile

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RACK = os.path.join(ROOT, "bin", "rack.py")
ok = True


def check(name, cond):
    global ok
    print(f"  {'PASS' if cond else 'FAIL'} {name}")
    ok = ok and cond


tmp = os.path.join(tempfile.mkdtemp(), "rack_state.yml")
with open(tmp, "w") as f:
    f.write("active_node: test_node\nseq: 0\nstack: []\n")
env = {**os.environ, "RACK_FILE": tmp}


def run(*a):
    return subprocess.run([sys.executable, RACK, *a], env=env, capture_output=True, text=True)


run("push", "first")
run("push", "second")
state = yaml.safe_load(open(tmp))
top = state["stack"][0]
check("LIFO: newest on top", top["task"] == "second")
check("provenance: id is monotonic", top["id"] == 2 and state["seq"] == 2)
check("provenance: node + ts attached", top["node"] == "test_node" and "ts" in top)

r = run("pop")
check("pop returns the TOP", "second" in r.stdout)
state = yaml.safe_load(open(tmp))
check("pop removes only the top", len(state["stack"]) == 1 and state["stack"][0]["task"] == "first")

print("\nRACK TESTS PASS" if ok else "\nRACK TESTS FAIL")
sys.exit(0 if ok else 1)
