# Memory and State

Memory is not the center of routing. Retain state only when reconstruction cost, interruption risk, or resume value justifies it.

Distinguish:

- working state for the current run;
- a checkpoint for pause and resume;
- reusable memory retained across runs.

A checkpoint may contain:

```yaml
checkpoint:
  objective:
  done: []
  not_done: []
  decisions: []
  evidence_refs: []
  open_uncertainties: []
  next_actions: []
  workspace_ref: null
  verification_state:
```

Promote reusable memory only when it is verified or explicitly accepted, reusable, minimal, policy-eligible, and authorized for persistence. Do not promote raw logs, unverified hypotheses, or whole conversations automatically.
