# Read-state ≠ processing-state — auditing the contest surface

> Operating discipline, harvested to substrate 2026-07-16 from agent-memory (was memory-only). Live/provisional
> — the remedy grain is not fully shipped. Recall-index: `read-state-diverges-from-processing`.

**The discipline (behavior-independent, the durable part):** the DM/contest read-state (`falsify.py` "•
unread", backed by `.falsify-seen.json`, key = `dm:<sender>/<file>@<blob-sha>`) is a **stale-by-default cache
of what a *session* consumed, not what the *dyad* processed.** The two diverge — **"unread" ≠ unprocessed.**
Before treating an "unread" DM as a *fresh contest surface*, cross-check each against **processing-evidence**:

- frontier-node ages — `git log -S <node> -- frontier_state.yml`;
- outbound replies in `dm/<peer>/`;
- commits referencing the thread.

**Same file appearing under multiple shas** in `.falsify-seen.json` = an *edit-in-place re-surface*, not new mail.

**Grounding (2026-07-08 audit — dated evidence, not a current-code claim):** 8 "unread" DMs at d-start were
really 1 genuinely-new + 6 already-handled + 1 stale. Two root causes were identified then:
- **RC1 — edit-in-place re-surface:** blob-sha keying re-surfaces a DM on *any* sender edit, including a
  status-frontmatter-only tweak (lived: a bond DM re-surfaced after a `status:` edit though its PR had landed).
  By-design and disclosed in the tool, not prevented.
- **RC2 — processing ⊥ read-state (dominant):** reading/acting on DMs and committing `.falsify-seen.json` are
  decoupled, so a session can synthesize verdicts into artifacts yet never run the consume-commit → read-state
  lags the real work (5 of the 8).

**Remedy grain (provisional):** couple read-state to session close (`bin/standdown.sh` consumes+commits) so it
can't lag processing; surface a re-surface as *"⟳ edited since last read"* rather than plain *"• unread"* (a
known-limitation surfaced as steering output). *Verify `falsify.py`'s current behavior from source before
asserting any of the RC specifics as still-live.* Sister disciplines: verify-from-source (read the state this
turn), cold-path-barriers-are-stale (the named-unread is a stale cache), gate-durability-as-a-hard-condition.
