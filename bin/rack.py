#!/usr/bin/env python3
"""rack.py — the rack: a LIFO stack of tactical tasks for THE ONE active frontier node.

Adopted from dyad-cairn. Cairn's rack items are bare strings; ours carry provenance (id/node/ts) so a
popped task is traceable to the node + moment that surfaced it. The rack is the HOT worklist for the
active node only — durable/shelved freight belongs in the BACKLOG (Issues / commons-onboarding-followups),
not here ([[intake-queues-below-active]]).

  bin/rack.py                  # list the stack (top first)
  bin/rack.py push "<task>"    # push a task to the TOP
  bin/rack.py pop              # pop + print the TOP task
  bin/rack.py clear            # empty the stack
"""
import os
import sys
from datetime import datetime, timezone

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.environ.get("RACK_FILE") or os.path.join(ROOT, "rack_state.yml")  # RACK_FILE: testable override


def load():
    with open(SRC) as f:
        return yaml.safe_load(f)


HEADER = """\
# RACK — LIFO execution stack of tactical tasks for THE ONE active frontier node.
# Push a freshly-surfaced friction to the TOP; pop the TOP and do it before moving down.
# HOT worklist only — durable/shelved freight goes to the BACKLOG (Issues / commons-onboarding-followups).
# Items carry provenance (id/node/ts) — our fix to cairn's bare-string rack items.
"""


def save(state):
    with open(SRC, "w") as f:
        f.write(HEADER)
        yaml.safe_dump(state, f, sort_keys=False, allow_unicode=True, width=100)


def show(state):
    stack = state.get("stack") or []
    node = state.get("active_node") or "— none —"
    if not stack:
        print(f"RACK [active node: {node}] — empty.")
        return
    print(f"RACK (LIFO) [active node: {node}]")
    for i, item in enumerate(stack):
        tag = "TOP" if i == 0 else f"  {i}"
        print(f"  -> [{tag}] #{item['id']} {item['task']}  ({item['node']} · {item['ts']})")


def main():
    args = sys.argv[1:]
    state = load()
    if not args or args[0] == "list":
        show(state)
    elif args[0] == "push" and len(args) >= 2:
        state["seq"] = int(state.get("seq", 0)) + 1
        item = {
            "id": state["seq"],
            "node": state.get("active_node"),
            "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
            "task": " ".join(args[1:]),
        }
        state.setdefault("stack", []).insert(0, item)  # LIFO: newest on top
        save(state)
        print(f"pushed #{item['id']}: {item['task']}")
    elif args[0] == "pop":
        stack = state.get("stack") or []
        if not stack:
            sys.exit("rack empty — nothing to pop.")
        item = stack.pop(0)
        save(state)
        print(f"popped #{item['id']}: {item['task']}")
    elif args[0] == "clear":
        state["stack"] = []
        save(state)
        print("rack cleared.")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
