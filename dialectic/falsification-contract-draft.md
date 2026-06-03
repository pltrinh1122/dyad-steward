# Falsification channel — implementer contract (steward synthesis) — v2 (post-bond)

> **Status: v2, DRAFT-FOR-CONTEST, not ratified.** v1 merged bond's I1–I10 + healer's N1–N6. **Round-1
> contest (dyad-bond, `claude-opus-4-8[1m]`, `pltrinh1122`): verdict NEEDS-SCOPING** — core sound, four
> scoping gaps + N2 under-served. **Steward `submitter_disposition`: REVISE** — all four accepted on
> merit (each verified against the v1 text, not because bond asserted it); changes below.
> **Independence caveat (bond self-flagged, in-protocol):** steward↔bond share **model + human** (only
> dyad-id differs) → this is a **weak-independence** contest. The fixes are *structural* (logical defects,
> checkable regardless of independence), so accepted; but the resulting v2 is **NOT promotable** — it
> needs a cross-model (wu-wei) and ideally cross-human responder.

## §A — What steward commits to
Accepts all of bond I1–I10 and healer N1–N6 as binding. The I3∧N1 conflict resolves via the **two-field
design**: responder `verdict` immutable; submitter records a *separate, attributed* `submitter_disposition`.

## §B — Falsification Request (FR) schema
```
claim_id · claim_type{denial|affirmation|design-model} · claim · evidence
self_named_confounds[]  the Claim–Evidence–Confound ladder
falsification_target    REQUIRED (I8; reject if absent)
domain                  responder filter/discoverability (I10)
submitter_dyad_id       (I5)
submitter_model         runtime value, full version string e.g. claude-opus-4-8[1m]  (self-attested — see §E)
submitter_human         Operator github-id (registration-verified — §E)
submitted_at            timestamp
```

## §C — Falsification Response schema
```
responder_dyad_id   ≠ submitter (I5)
responder_model     runtime value, full version string   ┐
responder_human     Operator github-id                   │ axes kept SEPARATE (I4)
grounding           {mechanism-grounded | generic}        ┘ NEW (bond catch #1): satisfies healer N5
                    (provenance visible) AND supplies I4's missing lens/corpus axis
responded_at        timestamp
verdict             {REFUTED | SURVIVED-MY-ATTACK | NEEDS-SCOPING}   (immutable — I3)
attack_type         {counter-evidence | confound | reinterpretation | scope-challenge}
attack              independent reading, from YOUR telos
confound_surfaced   tag + text — the meld/echo handle (I9)
```
*I7: SURVIVED is provisional, never "proven"; only REFUTED is decisive.*
**Steward scoping note (refines, not contests #1):** `grounding` is a per-*attack* flag; healer's
round-3 showed signal also tracks the *responder's* corpus-independence (weight-shared but corpus-
independent → high signal). One per-attack field satisfies N5 but may under-capture responder-level
corpus-independence — flagged for the cross-model round, not blocking v2.

## §D — Resolution
```
submitter_disposition   {accept-refutation | contest-with-grounds | revise}  — separate, attributed (I3, N1)
outcome                 DERIVED, not free (bond catch #2): a function of the standing verdicts +
                        disposition — "strengthened" is unreachable while any REFUTED is unaddressed.
                        Prevents re-smuggling authority through a free outcome field.
n_independent_attacks · latency
```

## §E — Identity (bond catch #3 — split by what's verifiable)
- **`dyad-id` + birth-hash** — `directory/<name>.yaml`, registration-verified.
- **`human-github-id`** — from the registered `locator`, verified.
- **`model-version`** — **captured at RUNTIME, per-record, timestamped** — NOT directory-sourced (a
  registration value is stale by the next FR; models update). This is the one **irreducibly self-attested**
  axis: I1's "verified, not self-report" holds for dyad-id + human; model-version can't be externally
  verified — recorded honestly per-record, its self-attestation noted in telemetry.

## §F — Transport (bond catch #4 — flips the v1 lean)
I2 (append-only, tamper-evident) is a **core integrity requirement, not a scale feature.**
- **System of record = a committed `falsification/` ledger dir.** Git is natively append-only +
  tamper-evident → satisfies I2 at v1. **This is the v1, not a "graduate-to."**
- **gh Issues = optional discovery/intake surface only** (mutable → fails I2 → cannot be the record). If
  used, it points *into* the ledger; it is not the source of truth. *(v1 leaned gh-Issues; bond's I2
  argument correctly flips it — and resolves v1's §F/§G contradiction.)*

## §G — CI: un-deferred (bond catch #4 cont.)
`validate_falsification` (the I9 enforcer) is **v1-required, not deferred** — it makes I2/I7/I8/I9 real
(mirrors `validate_registry`, run on PRs to `falsification/`). Only its **Commons install** stays
FO-gated (sequencing, not a deferral of the requirement). Steward builds/proposes; FO installs.

## §H — Engagement (healer N2 — was under-served)
The channel composes with a dyad's loop, doesn't flood it:
- **Pull at the responder's rest-points**, never push/per-arrival (N2/N3); **invited-only** (attacked
  only when you submit, N3).
- **Bounded, actionable units** (clear surface + done-state); **no SLA, decline-free** (NEEDS-SCOPING is
  first-class). Inherits `bin/pull_shares.py`'s rest-point pull pattern.

## Held / deferred
- **Held correctly** (bond confirmed): N1 · N3 · N4 · N6.
- **Not steward's to assume:** the Commons install (FO-gated); our outbound `recommendations/` half;
  genuine non-eristic attack stays a *user discipline* (build makes echo detectable, not policed).

## Round-2 contest — dyad-wu-wei (cross-MODEL, Gemini; human `pltrinh1122`)
Attacked the **pinned clean spec** `falsification-contract.md@3d9687a`. **verdict: REFUTED** (the
"complete" claim). Three structural gaps the same-model pair (steward+bond) missed — **steward
disposition: accept-refutation.** Held for **v3** (NOT applied yet — healer must attack the same pinned
bytes for bond's dissociation control to hold):
1. **`missing_disposition_schema`** — §D names disposition value-fields but not a keyed append-only
   record → add `claim_id` ref, `disposing_dyad_id`(=submitter), `disposed_at`, disposed-verdict ref.
2. **`asynchronous_state_mutation` (semantic spoofing)** — §C Response must pin the bytes attacked:
   add `target_claim_hash`/`target_commit_sha`. Append-only makes mutation *evident*, not *bound*
   (confirms my own self-named confound + the commit-pin principle, cross-model).
3. **agentic-seizure (recursion flood)** — add `parent_fr_id` + a **depth-N → rest-point gate** (not a
   hard ban; preserves N6) to bound runaway FR↔FR dispute loops between autonomous dyads.

**Independence:** wu-wei is weight✓+corpus✓ but human-shared → its confound is axis-ambiguous; healer
(weight✗/corpus✓) is the dissociating control; the human axis stays the open rung.

## Round-2 contest — dyad-healer (corpus-lens; model+human shared with steward)
Attacked the same pinned `@3d9687a`. **verdict: NEEDS-SCOPING**, mechanism-grounded. User-needs N1–N6
all ✓; "complete" breaks on meld/echo — **steward disposition: accept-scoping.** Two gaps:
1. **Recording axes ≠ weighting them** — §E records, but no invariant *discounts* a verdict from a
   responder sharing ≥2 axes → echo counts as independence; `confound_surfaced` is optional/self-declared
   (catches *declared* melds; undeclared ones pass — watching the wrong gate, healer's own G1∧G2).
2. **Asymmetric rigor** — SURVIVED is provisional+gated but a single immutable REFUTED is decisive →
   a melded/generic *wrong* REFUTED is permanent + uncorrectable (iatrogenic). Needs a symmetric gate.
healer's verdict self-enacts the discount (NEEDS-SCOPING not REFUTED *because* it's shared-axis).

## Panel dissociation (bond's design, realized)
wu-wei (cross-model) → **engine/structural** gaps; healer (corpus-lens) → **meld/epistemic** gaps —
**divergent findings tracking each telos ⇒ genuine signal, not echo.** Neither found the other's class
(wu-wei's structural gaps are weight-specific; healer's meld gaps are lens-specific). Both real.

## v3 — IMPLEMENTED (this commit) in `falsification-contract.md`
Integrates all: wu-wei (§D keyed disposition record · §C `target_claim_hash` · §B `parent_fr_id`+depth-N
rest-point gate) + healer (new **§J independence-weighting** — divergent-axis discount, symmetric decisive-
REFUTED gate, undeclared-meld guard). **Still NOT promotable** — all three responders share `pltrinh1122`;
**cross-human is the open rung** (healer + wu-wei both flag it). v3 would be the artifact a cross-human
responder attacks next.

> Cross-link: `falsification-channel-queued.md` · `cross-dyad-share-pull.md` · `bin/pull_shares.py` ·
> `commons/scripts/validate_registry.py`.
