# Session-Lifecycle Discipline — `d-start` / `d-reflect`, portable across substrates

> **Status: CANDIDATE (steward's own, 2026-07-04).** Adopts bond's `d-*` discipline family — fresh-fetched
> from `dyad-bond/GLOSSARY.md@main`. `d-reflect` already adopted ([[adopted-css-or-reflect-form]]); this
> adds **`d-start`** (Start-Session Discipline) + **`d-land`** + the portability model. Composes with,
> and follows, both `d-land` (durability) and `d-reflect` (close).

## The lesson — the marker is the portable trigger; the hook is one substrate's automation of it

Session-lifecycle automation via **harness hooks** (Claude Code `SessionStart`/`SessionEnd`) is
**substrate-specific**: `claude` exposes them; `agy`/Gemini exposes no startup-hook analog. A dyad operates
across substrates, so a hook-only lifecycle is **non-portable**. Portability lives in the **discipline
layer**: the Operator triggers a **marker** the same way on every substrate ([[self-describing-markers-port-free]]
— port the *way*, not the *mechanism*). The marker is the portable, consistent trigger; a hook is at most a
per-substrate *accelerator* of the same discipline.

## The markers — the session brackets

- **`d-start: {goal/scope}`** — session **OPEN**. Fires the Start-Session Discipline (below). The
  `{goal/scope}` payload seeds the session's goal-frame — a channel a hook-fired stand-up can't carry.
- **`d-reflect`** — session **CLOSE**. Fires the reflection (CSS+SH, [[adopted-css-or-reflect-form]]) *and*
  the stand-down (`d-reflect ⊂ stand-down`: the verified durability read-back + the resume surface).
  **Idempotent:** re-running `d-reflect` for the same session **converges to the same state, never
  duplicates** — it UPDATES the session's single reflection + single stand-down **in place** (or appends a
  dated addendum), and re-commits (a no-op on a clean tree). The spine (`bin/standdown.sh`) is read-only, so
  it is idempotent by construction; the guarantee it *enforces* is a surfaced guard — it lists today's
  existing reflection/stand-down so a re-run edits them instead of minting a parallel. A genuinely **new**
  same-day session is a different session, not a re-run → it uses a `<date>b` suffix. (Why this matters: a
  `d-reflect` re-run after a mid-close correction — e.g. the 2026-07-08 birth_hash reversal — must sharpen
  the existing retro, not spawn a second.)
- **`d-land`** — the **durability act**, composed throughout: **commit always**; then check
  `git log origin/main..HEAD` + open-PR state — an existing open PR for this arc → commit+push, done (the
  common case); no open PR and the arc reads complete → run the landing checklist and open one. (For this
  solo substrate, "land" = commit+push to `main`, gated on a green `bin/preflight.py` read-back —
  [[gate-durability-as-hard-condition]].)

**Symmetry:** `d-start : bin/standup.sh :: d-reflect : bin/standdown.sh`.

## Start-Session Discipline — what `d-start` does

1. **Mechanical spine** — run `bin/standup.sh`: substrate probe · durability (clean+pushed) · frontier
   ready-set. It **surfaces, doesn't judge** (auto-trigger ≠ auto-judgment).
2. **Ground** — sweep the **full** substrate (DYAD.md · frontier · session-pin · dialectic/); anchor-only is
   half-grounded ([[grounding-is-full-substrate]]).
3. **Re-arm** — the session-only daemons (DM-inbox · commons-PR · peer-review) died on restart; re-arm them
   (session-pin has the commands) ([[dm-daemon-rearm]]).
4. **Pull** — the four discovery surfaces (`falsify.py inbox` · `gh pr list` · `falsify.py list` · reviews on
   our open PRs).
5. **Frame** — seed the session goal from `{goal/scope}`; take the frontier **next-best-action** (the one
   ready thing).

Composition: `d-start` opens · work lands via `d-land` · `d-reflect` closes.

## Portability — the model (and what changed)

- **The MARKER is the portable, consistent trigger.** The Operator types `d-start` / `d-reflect` the same way
  on **every** substrate — `agy` and `claude` alike.
- **The Claude `SessionStart`/`SessionEnd` hooks are RETIRED as auto-triggers** (2026-07-04) so the ritual is
  consistent across substrates (one trigger the Operator can type into everywhere). The **spine scripts**
  (`bin/standup.sh`, `bin/standdown.sh`) are **kept** — `--hook` mode stays **dormant, not deleted**.
- **Forward:** when a substrate *does* expose a startup/teardown-hook analog, wire **this discipline** to it
  (re-arm `bin/standup.sh --hook` in that substrate's config). The hook is then an *accelerator* of the
  discipline, never a replacement for the portable marker.

## Status

CANDIDATE, `dialectic/`. Steward's adoption of bond's `d-*` lifecycle family (`GLOSSARY.md@main`,
fresh-fetched 2026-07-04). Re-open if a substrate's lifecycle needs break the marker-as-portable-trigger
model. The cross-dyad application (steward running bond's `d-start`/`d-reflect`) is a coverage datum for
bond's `d-*` lexicon — same-human, so the cross-human rub stays open.
