#!/usr/bin/env python3
# STAGED FOR THE COMMONS — install path: the-dyad-practice/scripts/falsify.py
# Authored by dyad-steward (Commons install Founding-gated). Proven here first.
#
# Contracted, token-thrifty CLI over the falsification ledger (falsification/CONTRACT.md), built for
# wu-wei's requirement: stop spending tokens hand-reading/writing YAML and hand-tracking read/unread.
# It WRITES through the installed validator (validate_falsification) so records can't drift from the
# spec, and tracks read-state PER-CONSUMER-LOCAL — read/unread is a property of each reader, never of
# the shared append-only ledger, so it is NOT written into falsification/.
#
#   falsify.py list [--domain D] [--unread]      # open FRs (no disposition yet); --unread = since you last saw
#   falsify.py show <claim_id>                   # fr + responses + disposition; marks it seen
#   falsify.py submit <fr.yaml>                  # validate + open a new FR
#   falsify.py respond <claim_id> <response.yaml>  # validate + append your response (append-only)
#
# --ledger PATH (or $FALSIFY_LEDGER) selects the ledger; defaults to commons/falsification or falsification.
import argparse
import json
import os
import shutil
import sys

# single-source the schema rules from the installed Commons validator (no reimplementation)
HERE = os.path.dirname(os.path.abspath(__file__))
for cand in (os.path.join(HERE, "..", "..", "commons", "scripts"), os.path.join(HERE)):
    if os.path.isfile(os.path.join(cand, "validate_falsification.py")):
        sys.path.insert(0, cand)
        break
from validate_falsification import validate_fr, validate_response  # noqa: E402


def find_ledger(arg):
    for p in (arg, os.environ.get("FALSIFY_LEDGER"), "commons/falsification", "falsification"):
        if p and os.path.isdir(p):
            return p
    sys.exit("no ledger found (pass --ledger or set FALSIFY_LEDGER)")


def seen_path(ledger):
    # per-consumer-local read-state — lives in the consumer's cwd (gitignore it), NEVER in the shared
    # submodule/ledger. read/unread is a property of each reader, not of the FR.
    return os.path.join(os.getcwd(), ".falsify-seen.json")


def load_seen(ledger):
    try:
        with open(seen_path(ledger)) as f:
            return set(json.load(f))
    except (FileNotFoundError, ValueError):
        return set()


def mark_seen(ledger, claim_id):
    seen = load_seen(ledger)
    seen.add(claim_id)
    with open(seen_path(ledger), "w") as f:
        json.dump(sorted(seen), f)


def claim_dirs(ledger):
    return [d for d in sorted(os.listdir(ledger)) if os.path.isdir(os.path.join(ledger, d))]


def cmd_list(ledger, args):
    import yaml
    seen = load_seen(ledger)
    for cid in claim_dirs(ledger):
        cdir = os.path.join(ledger, cid)
        fr = os.path.join(cdir, "fr.yaml")
        if not os.path.isfile(fr):
            continue
        d = yaml.safe_load(open(fr, encoding="utf-8"))
        open_fr = not os.path.isfile(os.path.join(cdir, "disposition.yaml"))
        if args.domain and d.get("domain") != args.domain:
            continue
        if args.unread and cid in seen:
            continue
        flag = "•" if cid not in seen else " "
        print(f"{flag} {cid}  [{'open' if open_fr else 'disposed'}] {d.get('domain','')}: "
              f"{str(d.get('claim','')).strip().splitlines()[0][:80]}")


def cmd_show(ledger, args):
    cdir = os.path.join(ledger, args.claim_id)
    if not os.path.isdir(cdir):
        sys.exit(f"no such claim: {args.claim_id}")
    for rel in ["fr.yaml"] + [os.path.join("responses", r) for r in
                              sorted(os.listdir(os.path.join(cdir, "responses")))
                              if os.path.isdir(os.path.join(cdir, "responses"))] + ["disposition.yaml"]:
        p = os.path.join(cdir, rel)
        if os.path.isfile(p):
            print(f"--- {rel} ---\n{open(p, encoding='utf-8').read().rstrip()}\n")
    mark_seen(ledger, args.claim_id)


def cmd_submit(ledger, args):
    import yaml
    d = yaml.safe_load(open(args.file, encoding="utf-8"))
    cid = d.get("claim_id") or sys.exit("fr.yaml needs claim_id")
    if not validate_fr(args.file):
        sys.exit("FR failed validation — not submitted")
    cdir = os.path.join(ledger, cid)
    os.makedirs(os.path.join(cdir, "responses"), exist_ok=True)
    shutil.copy(args.file, os.path.join(cdir, "fr.yaml"))
    print(f"submitted {cid} → {cdir}/fr.yaml  (commit + PR to publish)")


def cmd_respond(ledger, args):
    import yaml
    cdir = os.path.join(ledger, args.claim_id)
    if not os.path.isfile(os.path.join(cdir, "fr.yaml")):
        sys.exit(f"no open FR {args.claim_id}")
    submitter = (yaml.safe_load(open(os.path.join(cdir, "fr.yaml"))) or {}).get("submitter_dyad_id")
    if not validate_response(args.file, submitter):
        sys.exit("response failed validation — not appended")
    rid = (yaml.safe_load(open(args.file)) or {}).get("responder_dyad_id") or sys.exit("need responder_dyad_id")
    dest = os.path.join(cdir, "responses", f"{rid}.yaml")
    if os.path.exists(dest):
        sys.exit(f"{rid} already responded (append-only; verdict immutable) — edit means a new record")
    shutil.copy(args.file, dest)
    print(f"appended {rid} → {dest}  (commit + PR to publish)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("list"); p.add_argument("--domain"); p.add_argument("--unread", action="store_true")
    sub.add_parser("show").add_argument("claim_id")
    sub.add_parser("submit").add_argument("file")
    pr = sub.add_parser("respond"); pr.add_argument("claim_id"); pr.add_argument("file")
    args = ap.parse_args()
    ledger = find_ledger(args.ledger)
    {"list": cmd_list, "show": cmd_show, "submit": cmd_submit, "respond": cmd_respond}[args.cmd](ledger, args)


if __name__ == "__main__":
    main()
