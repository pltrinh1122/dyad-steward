# Reflection (D3 · CSS+SH) — permissioning: verify-the-honoring, then park for bond

*CSS = Agent (Continue/Start/Stop); SH = Operator-provenance (Should-Have carries the materiality bar —
a miss producing a claim found-false-by-mechanical-check; Should-Hold = standing credit; both descriptive,
verbatim-quoted). Grounded on bond's live `kb/reflection-discipline.md §D3` (fresh-fetched this session).
Landed by being committed; no CTA.*

**Scope:** `d-start` to ensure dyad-permissioning operates per intent → verified the project-level
`autoMode.allow` push-to-main exception is **inert** → added d-start ritual allows on Operator grant →
surfaced the strip-vs-global fork → Operator **parked** it pending dyad-bond's holistic approach.

## CONTINUE

- **Verify the *honoring*, not just the config text — with the actual tool.** `apply_automode_allow.py`'s
  docstring *asserts* "autoMode is honored only from user settings." I did not trust the assertion; I ran
  `claude auto-mode config` and confirmed our project-level rule is **absent** from the effective config
  while the built-in BLOCK rule is **live**. Turned a docstring claim into an established fact
  ([[verify-with-actual-tool]], [[claimed-not-established]]). The general grain: a settings *file* containing
  a rule ≠ that rule being *in force* — check the effective/resolved config.
- **Couple the state-change to a remote read-back.** The commit ended by `git cat-file`-ing
  `origin/main:.claude/settings.json` and asserting `local==origin` — "done" reached only through the
  read-back, not the push's own success signal (DYAD §NON-NEGOTIABLE, [[gate-durability-as-hard-condition]]).
- **Act on the granted autonomy; surface only the genuinely-Operator-owned fork.** Added the d-start allows
  without a CTA (grant given); reserved the single PFP surfacing for the strip-vs-global decision, which
  crosses into global user-settings (outward) and a real pollution-vs-autonomy value tradeoff.

## START

- **Default to python for any multi-step shell.** The moment an inspection grows a pipe chain / `sed` /
  here-string parsing, write `python3 - <<'PY'` instead. New standing behavior ([[python-for-complex-commands]]).

## STOP

- **Reaching for a complex bash pipeline when python was the right tool.** My config-honoring check was a
  chained `grep … | sed … | tail` block; the Operator corrected it mid-session. The command *worked* (no
  false result — hence not a Should-Have), but it was fragile and less readable than the python I switched to.

## SH — Operator provenance

- **Should Hold** *(standing pattern, credit):* **portfolio-level parking over local optimization.** Rather
  than let me finish a steward-local permissioning fix, the Operator lifted to the portfolio view and parked
  it for a sibling dyad's holistic solution. Verbatim: *"dyad-bond has a more holistic and strategic approach
  to dyad-permissioning so we'll wait for that outcome before continuing on this work."* This is the N\*/
  `1+1=3` discipline in action — don't spend force local-optimizing what a peer is solving holistically
  ([[steward-operates-platform-delegates]], [[fo-motivation-prioritization-key]]). Also the d-start grant —
  *"when executing d-start, agent has full permission to tools so CTA are unnecessary"* — a standing
  authorization to cut ritual friction ([[dstart-full-permission-no-cta]]).
- **Should Have** — **none meeting the materiality bar.** The complex-bash miss produced a correct result
  (the read-back and the finding both held), so no claim was found false by mechanical check; it is a STOP
  (Agent behavior), not a Should-Have. Naming one would be manufactured balance.

## Coverage

Intra-dyad, same-agent — the form's `L2b` cross-dyad/cross-human gap persists. But the *session* had a
cross-dyad axis: the reflection form was re-grounded on bond's remote §D3, and the work itself was parked
*for* bond — a datum that the portfolio treats permissioning as a shared, not per-dyad, concern.
