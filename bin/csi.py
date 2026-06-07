#!/usr/bin/env python3
"""csi.py — Cybernetic Steering Invariant guards: the registry view + the runnable suite.

CSI (adopted from dyad-cairn; we use the "Invariant" expansion): a discipline only holds if it is a
mechanical trap, not a thing to remember — a failing check IS the steering wheel. G+V: every Generate is
paired with a deterministic Validate ("No Pure G"). This reads the catalog `kb/csi_guards.yml`; `--check`
runs the RUNNABLE guards (the preflight Symmetric family) and lists the process-bound ones.

  bin/csi.py            # list the guard registry (Symmetric / Asymmetric)
  bin/csi.py --check    # run all RUNNABLE guards (delegates to preflight) + name the process-bound ones
"""
import os
import subprocess
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "kb", "csi_guards.yml")


def load():
    with open(REG) as f:
        return yaml.safe_load(f)["guards"]


def main():
    guards = load()
    passthru = [a for a in sys.argv[1:] if a != "--check"]

    if "--check" in sys.argv[1:]:
        r = subprocess.run([sys.executable, os.path.join(ROOT, "bin", "preflight.py")] + passthru)
        print("\n[CSI] process-bound guards (enforced by process/discipline, not auto-run here):")
        for gid, g in guards.items():
            if g.get("mechanism") != "runnable":
                print(f"  · {gid} [{g['kind']}/{g['mechanism']}] — {g['binds']}")
        sys.exit(r.returncode)

    print("CSI GUARDS — Cybernetic Steering Invariants (kb/csi_guards.yml)")
    print("  runnable = a real check fires · discipline = enforced by process, not yet mechanized\n")
    for kind in ("Symmetric", "Asymmetric"):
        print(f"== {kind} ({'state-bound' if kind == 'Symmetric' else 'process-bound: G paired with V'}) ==")
        for gid, g in guards.items():
            if g["kind"] == kind:
                mark = "✓runnable" if g.get("mechanism") == "runnable" else "○discipline"
                print(f"  [{mark}] {gid} — {g['binds']}")
                print(f"             where: {g['where']}")
        print()


if __name__ == "__main__":
    main()
