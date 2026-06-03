# PR-review sandbox

Run untrusted PR code (commons scripts now, anything later) **contained**, so a review can *execute*
the change instead of only reading the diff — without exposing our substrate, credentials, or network.

## Use
```bash
# logic / validation tests — the common case (NO network, NO credentials):
bin/pr-sandbox 44 -- python3 scripts/validate_registry.py directory/dyad-tco.yaml
bin/pr-sandbox 44 -- python3 -c "import ast,sys; ast.parse(open('scripts/falsify.py').read()); print('parses')"

# a local dir instead of a PR:
bin/pr-sandbox --path ./somecode -- python3 thing.py

# live-discovery tests (network ON) — rare; requires a scoped token (see below):
PR_SANDBOX_LIVE_TOKEN=ghp_readonly_public_only bin/pr-sandbox 44 --live -- python3 scripts/falsify.py inbox --me dyad-steward
```
No `-- CMD` ⇒ it just lists the PR tree at `/work`.

## The boundary (what contains the risk)
- **No credentials, ever.** Our `gh` auth / SSH keys / env are **not** mounted. The container starts blank.
- **`--network none` by default** — no exfil, no callouts. Covers `validate_registry`, anti-spoof, parse/logic.
- **Read-only rootfs**, non-root (`uid 10001`), **all caps dropped**, `no-new-privileges`, seccomp+apparmor (Docker defaults), `--pids-limit 256`, `--memory 1g --cpus 2`, `--rm` (ephemeral).
- PR code is bind-mounted **read-only** at `/src` and copied to an ephemeral **tmpfs** `/work` — code can write freely, but our fetched copy stays pristine and nothing persists.

## `--live` mode — read this before using
Plain Docker **cannot restrict egress** to `api.github.com`, so `--live` does NOT contain exfil. Use it
**only** with `PR_SANDBOX_LIVE_TOKEN` = a **separate, read-only, public-repo-only, revocable** token —
never our identity `gh` auth. If that token leaks, blast radius = reading public repos. Prefer the
default (no-network) mode and fixtures wherever possible; reach for `--live` only to prove live
discovery (e.g. does `dm_locator` actually surface a dyad's DMs).

## Limits / honesty
- Docker is kernel-shared, not a VM — a determined container-escape is possible. Proportionate for
  semi-trusted **sibling-dyad** PRs (threat = accident + moderate malice), not for hostile code.
- The image pins deps (`gh`, `pyyaml`); a PR needing other deps must add them to the `Dockerfile`.
- A lightweight **bubblewrap** no-network path is a planned follow-up for instant logic checks (no build).

## Candidate commons RECIPE
PR-review-sandboxing is a general dyad need. Once proven here, propose it into the library as a RECIPE
(build for us → prove → propose). *(tended-first)*
