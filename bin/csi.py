#!/usr/bin/env python3
"""csi.py — Cybernetic Steering Invariant guards: the registry view + the runnable suite.

CSI (adopted from dyad-cairn; we use the "Invariant" expansion): a discipline only holds if it is a
mechanical trap, not a thing to remember — a failing check IS the steering wheel. G+V: every Generate is
paired with a deterministic Validate ("No Pure G"). This reads the catalog `kb/csi_guards.yml`; `--check`
runs the RUNNABLE guards (the preflight Symmetric family) and lists the process-bound ones.

  bin/csi.py            # list the guard registry (Symmetric / Asymmetric; arm-state for SPAOR traps)
  bin/csi.py --check    # run all RUNNABLE guards (delegates to preflight) + name the process-bound ones
  bin/csi.py --arm <id> | --disarm <id>   # toggle a SPAOR-traversal trap's arm-state (comment-safe)
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


def set_armed(gid, armed):
    """Flip a guard's `armed:` field in place via a comment-safe LINE edit (never round-trips the YAML,
    so the registry's header comments survive). The arm/disarm half of a SPAOR trap pair."""
    guards = load()
    if gid not in guards:
        sys.exit(f"[csi] no such guard: {gid}")
    if "armed" not in guards[gid]:
        sys.exit(f"[csi] {gid} has no `armed:` field — only SPAOR-traversal traps are arm/disarm pairs.")
    with open(REG) as f:
        lines = f.readlines()
    in_block = False
    for i, ln in enumerate(lines):
        if ln.startswith(f"  {gid}:"):
            in_block = True
            continue
        if in_block:
            if ln.strip() and not ln.startswith("    "):  # left the block (next guard / section comment)
                break
            if ln.lstrip().startswith("armed:"):
                indent = ln[: len(ln) - len(ln.lstrip())]
                lines[i] = f"{indent}armed: {'true' if armed else 'false'}\n"
                with open(REG, "w") as f:
                    f.writelines(lines)
                print(f"[csi] {gid} -> armed: {str(bool(armed)).lower()}")
                return
    sys.exit(f"[csi] could not locate the `armed:` line for {gid}")


def main():
    args = sys.argv[1:]
    for flag in ("--arm", "--disarm"):
        if flag in args:
            i = args.index(flag)
            if i + 1 >= len(args):
                sys.exit(f"[csi] {flag} needs a guard id")
            set_armed(args[i + 1], flag == "--arm")
            return

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
                arm = ("  [ARMED]" if g.get("armed") else "  [disarmed]") if g.get("spaor") else ""
                print(f"  [{mark}] {gid} — {g['binds']}{arm}")
                print(f"             where: {g['where']}")
        print()


if __name__ == "__main__":
    main()
