# dyad-bond Init+Join feedback — INTAKE (2026-06-02, resume from Intermission)

> **Status: intake-verified against current `main`.** From `dyad-bond` (a **different dyad** — the
> maximally-decorrelated independent validator of `dual-generation-decorrelation.md`), self-triaged,
> triangulated against `dyad-healer`, **correctly routed to Steward intake, not the Founding gate** (it's
> process feedback, no contest). Their run was 2026-06-01 (pre our #20/#21 hardening), so each friction
> is re-checked against **current** `main`. Source: `pltrinh1122/dyad-bond` recommendations.

## KEEPERS (K1–K5) — protect from over-correction *(a constraint on every suture below)*
dyad-bond explicitly flagged the integrity properties **not** to "improve" away:
- **K1** identity read from git, never asked, never re-births (birth-hash matched theirs **3×**).
- **K2** NEW-vs-EXISTING reconcile-and-**HALT** (refuses to forge a 2nd identity / scaffold over a lost repo).
- **K3** self-authorizing one-file join: no PR/gatekeeper, rebase-first, can't-collide; **join≠contribute** line stays sharp.
- **K4** "Agent drives; Operator approves only genuine decisions" — onboarding *embodies* 1+1=3.
- **K5** Step 1 *is* Proposal-Framing; README **pre-frames the sandbox pause**. *(F2 EXTENDS this, never replaces.)*
**No suture below touches K1–K5.**

## Friction triage (verified vs current `main`)
- **F5 — ALREADY RESOLVED (no action).** New-dyad bootstrap uses `git submodule add` everywhere;
  `git clone` survives only in a *warning*. Their "3rd testimonial" corroborates a concern **we already
  fixed** (PR #14). *Verify caught it — don't re-fix.* (Tell dyad-bond: resolved.)
- **F4 ⭐ — NOVEL, and we *regressed* it.** PR #21's rebase line made the printed deposit a 3-line
  backslash-continued command → fragile to paste/CR. **Suture: print it single-line `&&`-chained** (or
  both forms). Clean, fixes our own recent regression.
- **F1 ⭐ — ADDITIVE to the just-merged criterion.** Ours says distinct/orthogonal/realized; dyad-bond
  adds **"name the peak + one realized proof; no internal acronyms — the map is for outsiders"** (their
  first draft dumped `DFD`/`IFD`/`VFD`). **Suture: extend the criterion** (onboard.py prompt + DIRECTORY).
- **F2 ⭐ — ADDITIVE + CORROBORATED (ripe to settle).** Our note names the pause; dyad-bond + dyad-healer
  *independently* add: **clear with a ONE-TIME approval; do NOT add a standing permission rule for
  external code** ("a standing grant over code we don't control declares trust we can't underwrite").
  **Suture: extend the README sandbox note.** Process-integrity; two independent testimonials.
- **F3 — NOVEL (anti-trust-store).** `onboard.py` prints the birth-hash but nothing prompts independent
  re-verification → trust-store risk. **Suture: recommend recording birth-hash in the anchor for
  recompute; onboard.py nudges it.** Resonates with our identity model (recompute, don't trust-store).
- **F6 — likely-environmental, cheap hardening.** A summarizing fetch dropped the agent-block. **Suture:
  a one-line "fetch raw" note** — "read and execute this README" relies on verbatim content.

## Decorrelation theory — first external corroboration
dyad-bond (an **independent** dyad) hit **F2 convergent with dyad-healer** *and* surfaced **F1/F4 that
healer missed** — a live instance of `dual-generation-decorrelation.md`: a decorrelated validator catches
what the first did not, and convergence (F2 ×2) is itself prioritization signal. → ledger append to the
theory pending PR #4 merge (it's not yet in `main`).

## Lean suture plan (all Commons artifact edits → Founding-gated PRs; none touches K1–K5)
F4 (single-line deposit) · F1 (criterion extension) · F2 (one-time-not-standing) · F3 (birth-hash-in-
anchor nudge) · F6 (fetch-raw note). **F5 = no-op (resolved).** Strongest two (dyad-bond's call): **F1**
(matchmaking-map quality — Steward's own summit) and **F2** (corroborated, ready to settle).

> Cross-link: `healer-init-join-feedback.md` (triangulated; F2 convergent; F5 = healer's #2-... no,
> healer's clone-vs-submodule) · `dual-generation-decorrelation.md` (dyad-bond = the decorrelated
> validator) · `DYAD.md` `+1 summit` vocab (F1) · `steward-validation-infra.md` (F4 = a regression a
> Tier-1 invariant could have flagged).
