# Healer Init+Join feedback — INTAKE (2026-06-02, via FO)

> **Status: intake-verified.** `dyad-healer` registered via Init+Join (existing-dyad path) and reported
> friction from a real cold-path run. All four wounds **verified against current Commons `main` bytes**
> (`onboard.py`, `validate_registry.py`, README, `DIRECTORY.md`) — the Healer's own triage held
> completely. Healer left "sutures soft — yours to author." Fixes are Commons-facing → **Founding gate**
> (propose-only PRs; the Agent never merges).

## Verified wounds + suture status

1. **Summit YAML silently corrupts (highest-value, demonstrated live).** `onboard.py` scaffolds
   `summits:\n  - TODO: replace…` *unquoted* (the placeholder itself parses as a dict via `: `).
   `#` → comment (truncates), `:` → dict. `validate_registry.py` checked `summits` is a non-empty list
   but **never per-element string** → corrupt entries publish clean. **Verified**: `fix case-04: …` →
   dict; `close #1233 backlog` → `'close'`. **→ SUTURED: Commons PR #20** (quote scalars + per-element
   string check; demonstrated unquoted FAILs / quoted PASSes).
2. **Deposit step — two facets.** Final step is `cd commons && git add … && git commit && git push`.
   - **(sync) — clean fix, queued.** No `pull --rebase`; naive push rejected when `main` moves (our own
     declaration slices moved it 4× under them). Suture: `git pull --rebase origin main` before push, or
     `onboard.py` performs the synced deposit itself.
   - **(access) — DESIGN FORK, needs FO dispose.** "Self-authorizing — no PR" conflates *no
     merge-contest* with *no access*. Direct push needs **org write**; `DIRECTORY.md` admits "write
     access is the coarse gate." An **external newcomer** (exactly who the Commons recruits) **can't
     deposit.** Suture candidate: a **fork-and-PR fallback** for non-org-write dyads — but that reshapes
     the Joining model (registration may need a PR for externals, still contest-free/auto-mergeable).
     Touches `commons-contribution-lifecycle.md` §Joining + `DIRECTORY.md`. **Frame, don't unilaterally
     author.**
3. **No summit criterion → registry value erodes (clean-ish fix, queued).** "Declare your summits"
   carries no quality bar; nothing steers from collinear/duplicate summits (Healer's first pair was
   collinear + brushed dyad-steward's "knowledge compounding"). Suture: one-line criterion in
   `DIRECTORY.md` / the `onboard.py` prompt — **distinct from existing, orthogonal to each other,
   realized (not aspirational).** Faithful to our `+1 summit` vocab (a *matchmaking* signal → must be
   distinct to be useful); note the resonance with the schema's orthogonality/two-pronged test.
4. **"Your Agent runs nothing" collides with agent sandboxes (clean fix, queued).** README promises the
   Operator holds no checklist; but `git submodule add` + `python3 onboard.py` are external-code
   execution that agent harnesses gate (auto-mode classifier). *(Lived by dyad-steward too this
   session.)* Suture: **name the human-in-loop-on-external-code as a feature** — the Operator approves
   the submodule-add + the `onboard.py` run; that's the design, not the protocol breaking. README
   expectation-setting.

## Folded out (Healer's triage — accepted)
- CONTRIBUTING.md 404 → self-resolved (Commons PR #16). No standing pattern.
- Detached-HEAD non-fast-forward → theirs (pin-to-vetted-commit discipline), not the protocol; the
  *sync* facet that IS the protocol survived as #2.
- Line-wrap mis-path + orphaned `.git/modules/commons` → environmental / prior agy-session leftover.
- Signature/birth-hash mechanics → **strengths, not friction** (commits signed; identity anchored).

## Suture status (by kind)
- **#1** — **MERGED, Commons PR #20** (summit-YAML integrity).
- **#2-sync, #3, #4** — **MERGED, Commons PR #21** ("Init+Join hardening": deposit rebase · summit
  criterion · sandbox expectations). *(Caught + reverted a fork-and-PR fallback I'd slipped in — that's
  #2-access, held for dispose.)*
- **#2-access — OPEN, queued for FO dispose.** The one **design fork**: the Joining model assumes org
  write, but external newcomers (who the Commons recruits) lack it. Directions: fork-and-PR fallback ·
  `onboard.py` does an authenticated deposit · accept insiders-only + name it. Reshapes
  `commons-contribution-lifecycle.md` §Joining. Highest conceptual weight; lowest mechanical clarity.

> Cross-link: `commons-contribution-lifecycle.md` (§Joining = self-registration; the access fork lands
> here) · `DYAD.md` `+1 summit` vocab (the #3 criterion) · `commons-onboarding-followups.md` (prior
> onboarding intake, SUBSUMED by PR #14) · `commons-contributing-md-gap.md` (the sibling Healer intake).
