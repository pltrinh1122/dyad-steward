# Dual-generation decorrelation — a Steward theory (LIVE, continuously tested)

> **Status: live theory** in knowledge-unit shape (claim · refutation · ledger). Opened 2026-06-02 (FO
> `[NOTE]`: falsify the claim, capture the survivor as a usable, continuously-tested theory). **Home:
> Steward repo** — a theory about *how we generate+validate* (verb-adjacent epistemics). Underpins
> `steward-validation-infra.md`. "Continuously tested" = the ledger accrues every code+test generation.

## The proposed claim (FO `[NOTE]`)
Generating the script and its test-script **independently** reduces error rate tremendously:
`P(error_in_code) × P(error_in_test)` is low — an undetected bug needs **both** wrong.

## Falsification (the claim does NOT survive as stated)
`P(A ∩ B) = P(A) × P(B)` holds **only under independence.** Same generator (one Agent/model), same
session, same spec-reading → the two error events share a **common cause**: the generator's
understanding. A misread spec is encoded into **both** the code *and* the test — the test asserts the
buggy behavior as *correct* — so they **agree** and the bug passes. That is exactly **1+1=1
mutual-confirmation**, the failure the NON-NEGOTIABLE guards. Empirically: N-version programming
(Knight & Leveson, 1986) found independently-developed versions fail in **correlated** ways — generators
make the same mistakes on the hard parts. **Naive "generate both" does not deliver the product;
correlation collapses it back toward `P(single error)`.**

## Survivor (refined theory — usable, falsifiable)
**Independent dual-generation reduces the undetected-error rate by a factor that grows with the
DECORRELATION between code-gen and test-gen. `P(code) × P(test)` is the *idealized upper bound* (full
independence), never the realized rate; the residual is the common-cause (shared spec-reading) errors
the product ignores. Correlation is the failure mode (→ 1+1=1).**
This is **1+1=3 at the code level**: two independent halves contest; the `+1` is the caught error;
mutual confirmation is the `1+1=1` collapse.

## Usable corollary — engineer the decorrelation (the lever, weak → strong)
The benefit is *bought* by mechanisms that force independence:
- generate the test from the **spec/intent, not from the code** (so it doesn't inherit the code's reading);
- different **session / context / framing** (reset the generator's state);
- **property/invariant-based** tests (assert the contract, don't mirror the impl);
- **attack-posture** — the test tries to *refute* (the verify discipline);
- **a different dyad entirely (dyad-bond) = maximal decorrelation** — a genuinely independent generator.
  ← *why Tier 3 is the strong form; Steward-self-test is the weak-but-positive form.*
- **Irreducible residual:** a spec-level misunderstanding both halves share → only a human/contest (the
  FO/substance gate) catches it. Hence **CI=form / FO=substance**: independent test-gen cannot certify
  substance.

## Refutation conditions (how this theory dies)
- Decorrelated dual-gen shows **no** error-rate drop vs single-gen → the independence benefit is fiction.
- Errors turn out **uncorrelated by default** (the product holds with no engineered decorrelation) → the
  correlation caveat is wrong (N-version evidence argues against this).
- The common-cause residual **dominates** such that decorrelation doesn't move the rate → wrong lever.

## Evidence — software-engineering practice (FO `[NOTE]` 2026-06-02)
*Added per FO; with the theory's own discipline — include the nuancing/cutting evidence, not only the
confirming (cherry-picking would be the mutual-confirmation failure this theory warns against).*

**Supports the refined (decorrelation) theory — crucially, NOT the naive product:**
- **TDD / test-first effectiveness.** Nagappan, Maximilien, Bhat & Williams (2008, *Empirical SE*):
  test-driven teams at Microsoft/IBM cut defect density **40–90%** (for ~15–35% more dev time). The
  benefit attaches to writing the test **from the spec/intent *before* the code** — i.e. it *is* a
  decorrelation mechanism. Strong support for the **lever**, not the bare product.
- **Independent V&V / code inspection.** NASA IV&V and Fagan inspections (1976): an **independent**
  party catches defects the author's own checking misses. Direct support for the **"different generator
  catches common-cause"** corollary → the rigorous case for **Tier 3 (dyad-bond)**.

**Nuances / cuts (the honest other half):**
- **Coverage ≠ effectiveness.** Inozemtseva & Holmes (2014, ICSE): test-suite coverage is **not**
  strongly correlated with fault-detection once size is controlled. Tests that **mirror the
  implementation** (high coverage, low independence) underperform — i.e. **correlated tests are weak**,
  exactly the failure mode. Supports the theory *by cutting against naive "just add tests."*
- **Author-written-after-code tests** encode the author's blind spots (confirmation-oriented) — the
  **weak/correlated** form; effectiveness comes from independence, not test-count.

**The load-bearing caveat (don't over-claim):** this evidence is **human-written** tests in industrial
settings. An LLM generating *both* code and test from one context/weights is plausibly **more
correlated** than two human developers — so the SE evidence transfers **by analogy, not directly**, and
the likely implication is that **decorrelation matters *more* for Agent self-generation, not less**.
That is itself a refutation-condition to watch (if Agent self-tests catch at human-independent rates,
the higher-correlation conjecture is wrong).

## Ledger (continuously tested — append each code+test generation)
*Record: did the independent test catch a real bug? if one escaped, was it common-cause (correlated) or
genuinely independent? did a decorrelation mechanism move the catch?*
- **2026-06-02 (seed, supportive, n=1):** summit-YAML fix (Commons PR #20). I generated the validator
  hardening **and** an independent `yaml.safe_load` check derived from the **spec** (the Healer's
  reported `#`/`:` corruption cases) — *not* from my validator code — which caught/confirmed the
  corruption. **Weak decorrelation** (same Agent, but test-from-reported-symptom, not from-my-code).
  Supportive, not strong (the decorrelation was mild).

## Connection
Underpins `steward-validation-infra.md` (T1 self-test = weak/correlated; **T3 dyad-bond = strong/
independent**; the residual = the FO substance gate). **Library-`discipline` candidate** (every dyad,
proportioned to its grain) — and the rigorous case *for* dyad-bond's independent-validator frontier.
