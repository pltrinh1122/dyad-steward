# `falsification/` ledger format (staged for Commons)

The committed, append-only system of record (v3 contract §F). Git supplies append-only + tamper-evidence.

```
falsification/
  <claim_id>/
    fr.yaml                       # the Falsification Request (§B). Written once.
    responses/
      <responder_dyad_id>.yaml    # one per responder (§C). APPEND-ONLY — verdict immutable;
                                  #   a changed verdict = a new file, never an edit (§A/I2/I3).
    disposition.yaml              # the submitter's disposition (§D). Optional until disposed.
```

- **Discovery (I10):** an *open* FR = a `<claim_id>/` with `fr.yaml` and no `disposition.yaml`; browse
  `falsification/` or filter by `fr.domain`. (A `bin/` surfacer — pull_shares-style — is the next slice.)
- **Validation:** `validate_falsification.py <ledger-dir>` enforces the schema (this dir's `example/`
  is the dogfood). Honesty (non-eristic attack) is a user discipline, not enforced — echo is made
  *detectable* via `divergent_axes` + `confound_surfaced` (§J), not policed.
- **Field meanings:** see `dialectic/falsification-contract.md` (v3). `divergent_axes ⊆ {model, human,
  corpus}` is the §J weighting key (dyad-id is trivially always divergent, so it carries no signal).
