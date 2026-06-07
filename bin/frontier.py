#!/usr/bin/env python3
"""frontier.py — the frontier DAG: sovereign `frontier_state.yml` + a REGENERATED `frontier.md` view.

Adopted from dyad-cairn (frontier/node vocab) under our own `summit`, mechanizing patterns we already
hold: source/view split so the view can't drift ([[regenerable-view-not-sovereign-edit]]), and a
deterministic projection checkable in CI ([[verify-with-actual-tool]]). WIP-N=1 (<=1 ACTIVE node) is
enforced at write — a Symmetric CSI guard: the board *cannot* persist a split-brain ACTIVE state.

  bin/frontier.py                 # render the ASCII tree (read; default)
  bin/frontier.py --md            # regenerate frontier.md from the .yml source
  bin/frontier.py --check         # CI gate: validate + fail if frontier.md drifts from source
  bin/frontier.py active <id>     # make <id> the one ACTIVE node (enforces WIP-N=1)
  bin/frontier.py status <id> <STATUS>   # set a node's status (READY|ACTIVE|IN_REVIEW|BLOCKED|DONE)

The .yml is the source of truth; the .md is never hand-edited. Any mutation re-validates and re-projects.
"""
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "frontier_state.yml")
VIEW = os.path.join(ROOT, "frontier.md")

STATUSES = ["READY", "ACTIVE", "IN_REVIEW", "BLOCKED", "DONE"]
ICON = {"READY": "○", "ACTIVE": "▶", "IN_REVIEW": "◔", "BLOCKED": "⊘", "DONE": "✓"}


def load():
    with open(SRC) as f:
        return yaml.safe_load(f)


def validate(state):
    """Return a list of invariant violations (empty == valid). This IS the write-guard."""
    errs = []
    nodes = state.get("nodes", {})
    summits = state.get("summits", {})

    active = [nid for nid, n in nodes.items() if n.get("status") == "ACTIVE"]
    if len(active) > 1:
        errs.append(f"WIP-N=1 violation: {len(active)} ACTIVE nodes {active} (at most one).")

    for nid, n in nodes.items():
        st = n.get("status")
        if st not in STATUSES:
            errs.append(f"{nid}: bad status {st!r} (allowed: {STATUSES}).")
        if n.get("summit") not in summits:
            errs.append(f"{nid}: summit {n.get('summit')!r} not in summits {list(summits)}.")
        for dep in n.get("dependencies", []) or []:
            if dep not in nodes:
                errs.append(f"{nid}: dependency {dep!r} is not a node.")

    # cycle detection (DFS)
    WHITE, GREY, BLACK = 0, 1, 2
    color = {nid: WHITE for nid in nodes}

    def visit(u, trail):
        color[u] = GREY
        for v in nodes[u].get("dependencies", []) or []:
            if v not in nodes:
                continue
            if color[v] == GREY:
                errs.append(f"dependency cycle: {' -> '.join(trail + [u, v])}")
            elif color[v] == WHITE:
                visit(v, trail + [u])
        color[u] = BLACK

    for nid in nodes:
        if color[nid] == WHITE:
            visit(nid, [])
    return errs


def render_md(state):
    """Deterministic projection (NO timestamp — so --check is a clean drift gate)."""
    nodes = state["nodes"]
    summits = state["summits"]
    lines = [
        "# Frontier — REGENERATED projection · DO NOT EDIT",
        "",
        "> Source of truth: `frontier_state.yml`. Regenerate: `bin/frontier.py --md`. "
        "Drift gate: `bin/frontier.py --check` (wired into `bin/preflight.py`). "
        "WIP-N=1 (`<=1 ACTIVE`) is mechanically enforced at write.",
        "",
    ]
    active = [nid for nid, n in nodes.items() if n["status"] == "ACTIVE"]
    lines.append(f"**ACTIVE (WIP-N=1):** {active[0] if active else '— none —'}")
    lines.append("")
    # group by summit, then by status order, node ids sorted for determinism
    for skey in sorted(summits):
        members = sorted(nid for nid, n in nodes.items() if n.get("summit") == skey)
        if not members:
            continue
        lines.append(f"## {skey} — {summits[skey]}")
        for st in STATUSES:
            for nid in members:
                n = nodes[nid]
                if n["status"] != st:
                    continue
                dep = n.get("dependencies") or []
                deptag = f"  ⟵ {', '.join(dep)}" if dep else ""
                lines.append(f"- {ICON[st]} **[{st}]** `{nid}` — {n['title']}{deptag}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_tree(state):
    nodes = state["nodes"]
    summits = state["summits"]
    active = [nid for nid, n in nodes.items() if n["status"] == "ACTIVE"]
    out = ["FRONTIER  (▶ACTIVE ○READY ◔REVIEW ⊘BLOCKED ✓DONE)",
           f"ACTIVE [WIP-N=1]: {active[0] if active else '— none —'}", ""]
    for skey in sorted(summits):
        members = sorted(nid for nid, n in nodes.items() if n.get("summit") == skey)
        if not members:
            continue
        out.append(f"{skey}: {summits[skey]}")
        for st in STATUSES:
            for nid in members:
                n = nodes[nid]
                if n["status"] != st:
                    continue
                dep = n.get("dependencies") or []
                deptag = f"  ⟵ {','.join(dep)}" if dep else ""
                out.append(f"  {ICON[st]} {nid}: {n['title']}{deptag}")
        out.append("")
    return "\n".join(out)


HEADER = """\
# FRONTIER — sovereign DAG of strategic nodes (trails toward our summits).
# SOURCE OF TRUTH. `frontier.md` is a REGENERATED projection — never edit the .md.
# Vocabulary adopted from dyad-cairn (frontier/node/rack) under our own `summit`.
# WIP-N=1: at most one node may be ACTIVE — enforced mechanically by bin/frontier.py at write.
# status: READY -> ACTIVE -> IN_REVIEW -> BLOCKED -> DONE
# `summit`: which +1 summit (or b1=capacity-to-climb) the node roots to.
# `dependencies`: REAL precedence edges only (relation != edge — board-as-dag).
# Edit by hand OR via `bin/frontier.py status|active`; then `bin/frontier.py --md` reprojects.
"""


def write_view(state):
    with open(VIEW, "w") as f:
        f.write(render_md(state))


def write_source(state):
    with open(SRC, "w") as f:
        f.write(HEADER)
        yaml.safe_dump(state, f, sort_keys=False, allow_unicode=True, width=100)


def save(state):
    """Mutation path: validate (the write-guard) -> write source + view. Refuses on any violation."""
    errs = validate(state)
    if errs:
        print("REFUSED — frontier invariants violated (write-guard):", file=sys.stderr)
        for e in errs:
            print(f"  ✗ {e}", file=sys.stderr)
        sys.exit(1)
    write_source(state)
    write_view(state)


def main():
    args = sys.argv[1:]
    if not args:
        print(render_tree(load()))
        return
    cmd = args[0]
    if cmd == "--md":
        state = load()
        errs = validate(state)
        if errs:
            for e in errs:
                print(f"  ✗ {e}", file=sys.stderr)
            sys.exit(1)
        write_view(state)  # view-only: never rewrites the hand-authored source
        print(f"regenerated {os.path.relpath(VIEW, ROOT)}")
    elif cmd == "--check":
        state = load()
        errs = validate(state)
        drift = (not os.path.exists(VIEW)) or open(VIEW).read() != render_md(state)
        if errs or drift:
            for e in errs:
                print(f"  ✗ invariant: {e}")
            if drift:
                print("  ✗ frontier.md is STALE — run `bin/frontier.py --md`")
            sys.exit(1)
        print("frontier OK (valid + view in sync)")
    elif cmd == "status" and len(args) == 3:
        state = load()
        nid, st = args[1], args[2].upper()
        if nid not in state["nodes"]:
            sys.exit(f"no such node: {nid}")
        state["nodes"][nid]["status"] = st
        save(state)
        print(f"{nid} -> {st}")
    elif cmd == "active" and len(args) == 2:
        state = load()
        nid = args[1]
        if nid not in state["nodes"]:
            sys.exit(f"no such node: {nid}")
        for other, n in state["nodes"].items():  # demote any current ACTIVE (keep WIP-N=1)
            if n["status"] == "ACTIVE":
                n["status"] = "READY"
        state["nodes"][nid]["status"] = "ACTIVE"
        save(state)
        print(f"ACTIVE -> {nid}")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
