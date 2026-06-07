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
CSI_REG = os.path.join(ROOT, "kb", "csi_guards.yml")

STATUSES = ["READY", "ACTIVE", "IN_REVIEW", "BLOCKED", "DONE", "FALSIFIED"]
ICON = {"READY": "○", "ACTIVE": "▶", "IN_REVIEW": "◔", "BLOCKED": "⊘", "DONE": "✓", "FALSIFIED": "✗"}
TERMINAL = {"DONE", "FALSIFIED"}

# Node-type (SPAOR, from dyad-cairn, applied EXTERNALLY). SPAOR has FIVE phases (commons/AGENT.md:43);
# the cycle PROBE -> PLAN -> EXECUTE -> OBSERVE -> REFLECT is a FALSIFIABILITY pipeline that carries ONE
# falsifiable condition from end to end. Default EXECUTE so existing nodes need no field.
#   PROBE   (Sense)   — output is the trail's ONE single falsifiable INVARIANT (its hypothesis), or a
#             FALSIFY (-> status FALSIFIED, abort the trail — cold-path-barriers-are-stale, mechanized).
#             The ONLY type that grows the frontier (intake). Cannot ship functional change.
#   PLAN    (Plan)    — decompose the PROBE's single invariant into the EXECUTION invariants (testable
#             properties), then propose + create the EXECUTE node(s). Designs the how; cannot ship.
#   EXECUTE (Act)     — generate the required CODE *and* the TEST CODE encoding PLAN's execution invariants.
#             EXIT INVARIANT = all execution invariants pass (test code green). May NOT spawn nodes.
#   OBSERVE (Observe) — RUN the test code / measure the exit invariant AGAINST REALITY (verify-with-actual-tool).
#             The empirical gate; cannot ship.
#   REFLECT (Reflect) — ASSERT only the SINGLE PROBE invariant holds (the execution invariants are already
#             discharged by EXECUTE's passing tests), and codify the OUTCOME over the output into durable
#             substrate (memory/library). May spawn the next PROBE. Closure: DONE only after OBSERVE+REFLECT.
TYPES = ["PROBE", "PLAN", "EXECUTE", "OBSERVE", "REFLECT"]
DEFAULT_TYPE = "EXECUTE"
TYPE_TAG = {"PROBE": " [PROBE]", "PLAN": " [PLAN]", "EXECUTE": "",
            "OBSERVE": " [OBSERVE]", "REFLECT": " [REFLECT]"}


def load():
    with open(SRC) as f:
        return yaml.safe_load(f)


def armed_spaor_guards():
    """Ids of SPAOR-traversal CSI guards that are ARMED in kb/csi_guards.yml (spaor: true, armed: true).
    A disarmed guard is registered but inert; a missing registry installs no traps. This is the arm/disarm
    pair: the trap's CHECK lives here in validate(); its ARM-STATE lives (toggleable) in the registry."""
    try:
        with open(CSI_REG) as f:
            guards = (yaml.safe_load(f) or {}).get("guards", {})
    except FileNotFoundError:
        return set()
    return {gid for gid, g in guards.items() if g.get("spaor") and g.get("armed")}


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
        ntype = n.get("type", DEFAULT_TYPE)
        if ntype not in TYPES:
            errs.append(f"{nid}: bad type {ntype!r} (allowed: {TYPES}).")
        if st == "FALSIFIED" and ntype != "PROBE":
            errs.append(f"{nid}: only a PROBE may be FALSIFIED (you falsify a probe's condition, not a {ntype}).")
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

    # SPAOR-traversal CSI traps — fire ONLY when armed in kb/csi_guards.yml (arm/disarm pairs).
    # Disarmed traps are registered but inert: ship the trap before the substrate is fully compliant.
    armed = armed_spaor_guards()
    if "csi_probe_invariant" in armed:
        # PROBE (Sense) must state the trail's ONE falsifiable invariant — a single non-empty string.
        for nid, n in nodes.items():
            if n.get("type") == "PROBE":
                inv = n.get("invariant")
                if not isinstance(inv, str) or not inv.strip():
                    errs.append(f"{nid}: PROBE must declare a single falsifiable `invariant:` "
                                "(string) [csi_probe_invariant armed].")
    if "csi_execute_tested" in armed:
        # EXECUTE (Act) exit invariant: a DONE code-trail EXECUTE references its passing tests.
        for nid, n in nodes.items():
            if n.get("type", DEFAULT_TYPE) == "EXECUTE" and n.get("status") == "DONE" and not n.get("tests"):
                errs.append(f"{nid}: DONE EXECUTE must reference passing `tests:` [csi_execute_tested armed].")
    if "csi_trail_closure" in armed:
        # Closure: a node is not DONE while an OBSERVE/REFLECT successor is unclosed (outcome>output).
        for nid, n in nodes.items():
            if n.get("status") != "DONE":
                continue
            for sid, s in nodes.items():
                if (nid in (s.get("dependencies") or []) and s.get("type") in ("OBSERVE", "REFLECT")
                        and s.get("status") not in TERMINAL):
                    errs.append(f"{nid}: DONE but its {s.get('type')} successor {sid} is unclosed "
                                "[csi_trail_closure armed].")
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
                tt = TYPE_TAG[n.get("type", DEFAULT_TYPE)]
                lines.append(f"- {ICON[st]} **[{st}]**{tt} `{nid}` — {n['title']}{deptag}")
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
                tt = TYPE_TAG[n.get("type", DEFAULT_TYPE)]
                out.append(f"  {ICON[st]} {nid}{tt}: {n['title']}{deptag}")
        out.append("")
    return "\n".join(out)


HEADER = """\
# FRONTIER — sovereign DAG of strategic nodes (trails toward our summits).
# SOURCE OF TRUTH. `frontier.md` is a REGENERATED projection — never edit the .md.
# Vocabulary adopted from dyad-cairn (frontier/node/rack) under our own `summit`.
# WIP-N=1: at most one node may be ACTIVE — enforced mechanically by bin/frontier.py at write.
# status: READY -> ACTIVE -> IN_REVIEW -> BLOCKED -> DONE | FALSIFIED (PROBE-only terminal: condition refuted)
# type (default EXECUTE): SPAOR = FIVE phases, a FALSIFIABILITY pipeline carrying ONE invariant end-to-end:
#   PROBE (states the trail's ONE falsifiable `invariant:`; only type that grows the DAG) · PLAN (decomposes
#   it into execution invariants + creates EXECUTE) · EXECUTE (code + test code; EXIT = all execution
#   invariants pass) · OBSERVE (run tests / test against reality) · REFLECT (CLOSE: assert ONLY the single
#   PROBE invariant + codify outcome>output; may spawn the next PROBE).
# SPAOR-traversal CSI traps live in kb/csi_guards.yml as arm/disarm pairs (spaor: true, armed: bool);
#   an ARMED trap fires in bin/frontier.py validate(); a DISARMED trap is registered but inert.
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


def render_dag_tree(state):
    """Outstanding work (non-DONE) as a directory-style DAG tree: summits are roots, nodes nest under
    the dependency that blocks them (a dependent shows beneath its blocker, even across summits)."""
    nodes = state["nodes"]
    summits = state["summits"]
    live = {nid: n for nid, n in nodes.items() if n["status"] not in TERMINAL}
    children = {nid: [] for nid in live}
    nested = set()
    for nid, n in live.items():
        for dep in n.get("dependencies") or []:
            if dep in live:
                children[dep].append(nid)
                nested.add(nid)
    lines = ["FRONTIER · outstanding work as a DAG   (▶ ACTIVE  ○ READY  ◔ IN_REVIEW  ⊘ BLOCKED  ·  [PROBE] grows the DAG)", "│"]

    def emit(nid, prefix, last, under_summit):
        n = live[nid]
        conn = "└── " if last else "├── "
        tag = "" if n["summit"] == under_summit else f"   [{n['summit']} · blocked-by ↑]"
        tt = TYPE_TAG[n.get("type", DEFAULT_TYPE)]
        lines.append(f"{prefix}{conn}{ICON[n['status']]}{tt} {nid} — {n['title']}{tag}")
        kids = sorted(children[nid])
        ext = "    " if last else "│   "
        for i, k in enumerate(kids):
            emit(k, prefix + ext, i == len(kids) - 1, n["summit"])

    skeys = [s for s in sorted(summits)
             if any(n["summit"] == s and nid not in nested for nid, n in live.items())]
    for si, skey in enumerate(skeys):
        roots = sorted(nid for nid, n in live.items() if n["summit"] == skey and nid not in nested)
        s_last = si == len(skeys) - 1
        lines.append(f"{'└── ' if s_last else '├── '}{skey} · {summits[skey]}")
        s_ext = "    " if s_last else "│   "
        for i, nid in enumerate(roots):
            emit(nid, s_ext, i == len(roots) - 1, skey)
        if not s_last:
            lines.append("│")
    return "\n".join(lines)


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
    if cmd == "tree":
        print(render_dag_tree(load()))
        return
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
