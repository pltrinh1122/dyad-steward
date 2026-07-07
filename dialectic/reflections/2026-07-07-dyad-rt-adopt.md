# d-reflect — the dyad-rt adopt arc *(2026-07-07; CSS+SH, first instance of the incorporated bond D3 form)*

**Scope:** grounded cairn's `dyad-rt` → designed steward's own (inverse) landing → built `.githooks/pre-push`
+ standup Push-guard + reframed `bin/claude` + `§Operating mode` → merged (PR #30) → restart-readiness, which
caught a fail-open bug. Also the vehicle for migrating steward's reflection discipline to bond's D3 (this
file is the first CSS+SH instance; `retro:`/`reflect:` → `d-reflect:`).

## CONTINUE *(Agent-observed)*

- **Grounding-first, full-substrate — including our OWN.** Swept cairn + bond + steward's live substrate
  before building. That is *what surfaced* that the copied `bin/claude` was wrong-for-steward: bond's
  push-model is the **inverse** of ours (bond never pushes main; steward pushes admin-durability straight
  to its own main). Cargo-culting bond's pre-push would have broken the model steward ratified 2026-06-02.
  The "two models, no meld" move (extract the transferable invariant, leave the peer's *policy* at the
  boundary) is what made the adoption correct rather than a copy.
- **Verify-with-actual-tool, every branch.** Exercised the real `pre-push` binary (ff-allow · force-refuse ·
  delete-refuse · feature-allow) instead of eyeballing, re-ran it on `main` post-merge, and the live
  push-to-main was itself the end-to-end test of the "allow" branch. [[verify-with-actual-tool]].

## START *(commitment going forward)*

- **Set + verify tracked exec-mode (100755) at author time for any hook/launcher** — `git ls-files -s`, not
  just filesystem `chmod`. Under `core.fileMode=false`, `git add` records 100644 and a fresh clone/agy
  checks it out non-executable → git silently skips the hook. Now [[hooks-must-be-tracked-executable]].

## STOP *(Agent failure, named + corrected)*

- **I committed the dyad-rt hook + launcher tracked 100644** — a silent fail-open on any fresh clone / agy,
  the *exact class dyad-rt exists to prevent*. My PR's own falsifiable claim ("refused on ANY substrate")
  was **not established at commit time**; I caught it only during readiness, not at authoring. A
  [[claimed-not-established]] miss landed on my own guarantee. Corrected (100755 + memory), but the miss was
  authoring-time and should not have needed a second pass to find.

## SH *(Operator-provenance)*

- **Should Have:** *(none — no Operator claim cleared the materiality bar.* "i've merged PR #30" verified
  MERGED = true; nothing found-false-by-mechanical-check. A blank line is correct, not a gap.*)*
- **Should Hold:** *the Operator's decisive frame-simplification cuts Agent over-build — probe whether the
  standing posture / native substrate already answers it before building a mechanism.* Two instances this
  arc, both of which collapsed a thing I had designed:
  - verbatim: *"the default moving forward is always 'claude --dangerously-skip-permissions'"* — retired my
    per-launch-toggle framing (and `grant_push.py`) into a standing default.
  - verbatim: *"if you need mode detection, the claude-cli ui shows 'bypass permissions on' so it's likely a
    claude native setting"* — obviated my proposed `DYAD_RT_GATE` env-marker (a real over-build, removed).
