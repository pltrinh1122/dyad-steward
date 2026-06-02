# wu-wei Init+Join — the birth-certificate invariant stress test (PREDICTIVE, pre-onboard)

> **Status: LIVE, predictive. Not yet falsified by the real run.** Grounded 2026-06-02 (Steward
> Operator) from wu-wei's *actual remote bytes*, before its Operator runs `onboard.py`. The real
> falsification is **wu-wei's own cold-path onboard run** (sovereignty — not the Steward's to run).
> This file records what we predict, so the actual run *tests* it instead of us theorizing post-hoc.

> **Tended-first:** the consumer here is **wu-wei** (a sibling Dyad joining the Commons). The grain is
> *"what happens when wu-wei runs `onboard.py` against its real history"* — not our maintainer view of
> the tool. `enablement` = lower **wu-wei's** barrier to a clean, verifiable join.

## Why wu-wei is the stress test
wu-wei (`pltrinh1122/dyad-wu-wei`; `dz-cil` redirects to it — rename real) was **created 2026-05-16**,
**13 days before** dyad-steward's birth (2026-05-29). It is a **prototype spawned without prior
patterns** — the birth-cert invariant was designed *around* pattern-native dyads (steward), so wu-wei
inverts the invariant's hidden assumptions. Grounded shape (from `gh api`, the remote bytes):

- **Genesis commit (2026-05-16):** `kb/`, `artifacts/`, `kernel/` — **no shim, no anchor at all.**
- **`AGENT.md`** first appears **2026-05-16** (genesis day) — but it is the universal layer, **not a
  recognized birth shim** (`onboard.py SHIMS = ("CLAUDE.md","GEMINI.md")` only).
- **`GEMINI.md`** first appears **2026-05-17** via a commit titled *"chore: migrate to GEMINI.md
  hook"* — a **retrofit/migration**, ~a day after genesis.
- **No `CLAUDE.md`** ever. **~844 commits** in two weeks — a high-velocity, auto-PR-driven SPAO swarm.

## The invariant's hidden premise (where it strains)
`birth_hash = sha256( shim_content_at_add_commit ‖ committer_date %cI )`, keyed to the **earliest
add-commit of a recognized shim**. It silently assumes **genesis ≡ anchor-add ≡ a never-rewritten
commit**. For steward those are one act (`CLAUDE.md@2a9dc10`, clean linear history, reproducible by
anyone who clones). For wu-wei all three diverge → **two failure legs:**

### Leg 1 — birth_hash records a migration artifact, fragile under churn
- **Anchor ≠ genesis.** The shim was **migrated in a day late**, so the recorded "birth" is a
  *migration commit* (`GEMINI.md @ 2026-05-17`), not wu-wei's actual birth (repo-create 2026-05-16).
- **Date fragility.** That add-commit sits inside **~844 auto-churned commits**; any squash / rebase /
  amend that ever touches it **silently changes `%cI` → silently changes identity**. Pattern-native
  dyads never rebase their first commit; a prototype swarm very plausibly has.
- **Not Commons-verifiable.** From outside, the true `--diff-filter=A` add-commit is **masked** under
  heavy churn (API/path-history caps); only wu-wei's *local* git can name it. The hash becomes
  **trust-me, not verify-me** — denting the *consumer-side* of our verify NON-NEGOTIABLE.
- It will **not** mis-fire as NEW (GEMINI.md exists → detected EXISTING, no re-birth). It will quietly
  register a **semantically-wrong, mechanically-fragile** birth_hash and *look* fine.

### Leg 2 — `name = basename(cwd)` collides with wu-wei's multi-agent reality
`onboard.py` derives the registry name as `name = os.path.basename(os.getcwd())` (→
`directory/<name>.yaml`). wu-wei's own **`WHAT/WHY-0064: Dynamic Agent Identity`** is *literally a
writeup of why basename/workspace-derived identity is brittle in a multi-agent swarm*: its SPAO workers
run from worktrees like `/mnt/shared_data/git_repos/agent-SG2-auto`, and it deliberately **strips
`-auto`, lowercases, and resolves a *worker* id** (`agent-sg2`), explicitly **decoupling identity from
the git-tracked config** to avoid `main` merge conflicts.
- So if onboard runs from a **worker worktree**, `basename(cwd)` = `agent-SG2-auto`, → it registers
  **`directory/agent-SG2-auto.yaml`**, not `dyad-wu-wei.yaml`. The Commons' *dyad*-granularity name
  derivation collides head-on with wu-wei's *ephemeral-worker*-granularity filesystem reality.
- Run it from the **canonical repo root** and it's fine — but nothing in the tool *guarantees* that,
  and wu-wei's whole architecture normalizes running from worktrees.

## Honest correction of an earlier (Steward) overclaim
First pass flagged `WHAT/WHY-0064 "dynamic-agent-identity"` as a **philosophical contest: dynamic
vs. frozen *dyad* identity.** Reading the files refutes that literal framing: 0064 is **intra-dyad
*runtime-worker* identity** (which SPAO agent is executing), a *different level* from the Commons'
*dyad* identity. *(Sycophancy guard applied to our own prior claim — retracted, not doubled-down.)*
What survives is **sharper**: a **cultural inversion** (wu-wei's instinct = *identity should NOT be
git-tracked, resolve it dynamically to avoid `main` conflicts*; the Commons invariant = *identity IS a
git-history-frozen content+date hash*) **and** the concrete **Leg-2 basename-granularity collision** —
the same brittleness wu-wei already learned internally, which the Commons onboarding has not.

## Falsifiable claim
**The birth-cert invariant, as coded, cannot give a prototype like wu-wei a *meaningful + independently
reproducible* birth identity.** *Test (the real run):* when wu-wei's Operator runs `onboard.py`,
capture **(a)** the `birth_hash` it emits, **(b)** the `<name>.yaml` it targets, and **(c)** whether a
**fresh independent clone recomputes the same hash**. **Refuted if** the hash is reproducible *and* the
recorded birth is semantically wu-wei's genesis *and* the name lands as `dyad-wu-wei` — i.e. the
invariant is robust to pattern-foreign repos after all.

## `[IDEATE]` — candidate hardenings (Commons-facing → **Founding gate**; NOT disposed here)
Any change to `onboard.py`/the invariant is a tended-Commons change — Steward *proposes*, FO *gates*.
- **(a)** Prefer an explicit `birth:`-tagged commit / `BIRTH` marker over "earliest recognized-shim add."
- **(b)** Accept **`AGENT.md`** as a birth anchor (wu-wei had it at genesis; it is the universal layer).
- **(c)** Retrofitted prototypes get a **declared** birth, not a *derived* one — make the invariant
  honest that some dyads predate the pattern.
- **(d)** Derive the registry `name` from the **dyad's own anchor / declared identity**, not
  `basename(cwd)` — closing the Leg-2 worktree collision.

## Cross-references
- `../CLAUDE.md` §IDENTITY CAVEAT (the frozen-at-birth rule) · `commons/scripts/onboard.py` (the logic).
- `self-registration-remedy.md` (our own birth_hash correction — the *pattern-native* baseline).
- `commons-onboarding-followups.md` (prior onboard items, subsumed by PR #14).
- `AGENT.md` §Cross-references (sibling dyads; the `dz-cil`→wu-wei rename).
- **OPEN (carried):** wu-wei is one of the two remaining dyads in the intake→verify→suture loop.
