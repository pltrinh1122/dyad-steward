#!/usr/bin/env python3
# Regression test for bin/preflight.py — locks the quoted-link false-positive fix (a markdown link
# quoted INSIDE a code span/fence is documentation, not a navigable link, so must NOT be flagged).
# Lived defect: commons-contributing-md-gap.md quoted README link-markup and preflight flagged it.
# Plain Python, no framework — `python3 bin/test_preflight.py`. Runs the REAL extract_links.
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from preflight import extract_links

CASES = [
    ("bare link IS a link",        "see [x](missing.md) here",        ["missing.md"]),
    ("inline-code link is NOT",    "see `[x](missing.md)` here",      []),
    ("fenced link is NOT",         "```\n[x](missing.md)\n```",       []),
    ("real link beside code one",  "`[a](q.md)` but [b](r.md)",       ["r.md"]),
    ("external link extracted",    "[h](https://e.com)",              ["https://e.com"]),
]


def main():
    failures = 0
    for label, text, expected in CASES:
        got = extract_links(text)
        ok = got == expected
        print(f"{'ok' if ok else 'XX'}  {label}: {got} (want {expected})")
        failures += not ok
    print("OK" if not failures else f"{failures} FAILED")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
