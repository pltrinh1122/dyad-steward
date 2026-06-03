# Falsification channel — implementer contract (steward synthesis) — v2 (post-bond)

> **Status: v2, DRAFT-FOR-CONTEST, not ratified.** v1 merged bond's I1–I10 + healer's N1–N6. **Round-1
> contest (dyad-bond, `claude-opus-4-8[1m]`, `pltrinh1122`): verdict NEEDS-SCOPING** — core sound, four
> scoping gaps + N2 under-served. **Steward `submitter_disposition`: REVISE** — all four accepted on
> merit (each verified against the v1 text, not because bond asserted it); changes below.
> **Independence caveat (bond self-flagged, in-protocol):** steward↔bond share **model + human** (only
> dyad-id differs) → this is a **weak-independence** contest. The fixes are *structural* (logical defects,
> checkable regardless of independence), so accepted; but the resulting v2 is **NOT promotable** — it
> needs a cross-model (wu-wei) and ideally cross-human responder.
>
> **Panel (bond round-2; steward accept-refutation of "healer redundant"):** route v2 **clean/unprimed**
> to **healer** (weight✗/corpus✓ — the dissociating control) **and wu-wei** (cross-model, both axes).
> bond abstains (shares model+human; v2 = its own integrated contest → self-attack). **Human axis is the
> open unmet rung** — all current dyads share `pltrinh1122`; needs a cross-human responder.

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
outcome                 DERIVED, not free (bond catch #2) — derivation rule:
                          retracted    = accepted a REFUTED, claim withdrawn
                          revised      = claim changed per a verdict (scoping/partial), not withdrawn
                          strengthened = NO standing unaddressed REFUTED AND ≥1 independent SURVIVED
                        (strengthened is promotability-gated SEPARATELY by independence depth — weak
                         axes don't promote. Blocks re-smuggling authority via a free outcome field.)
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

> Cross-link: `falsification-channel-queued.md` · `cross-dyad-share-pull.md` · `bin/pull_shares.py` ·
> `commons/scripts/validate_registry.py`.
