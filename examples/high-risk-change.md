# High-Risk Change

## Task

> Plan a production permission change that is high impact and only partly reversible.

## Route

```yaml
quality_target: critical
capability_vector:
  reasoning_depth: high
  coding: preferred
  context_size: medium
  multimodal: none
  tool_use: required
  long_horizon: true
eligibility_constraints:
  - Explicit authority is required before execution.
  - The target must satisfy data and action policy.
deterministic_first: true
limiting_shape: risk
topology: single-first
compute_profile: deep
runtime_resolution:
  status: unresolved
  notes: Resolve the runtime only after approval, sandbox, rollback, and target checks.
verification: mixed
independent_review: conditional
observability_level: L3
human_escalation: required
assumptions:
  - A rollback or containment path can be prepared before execution.
residual_uncertainty:
  - Production impact is high and reversibility is partial.
human_decision_required: Approve or reject the exact production permission change.
```

Resolve the exact target, blast radius, approval boundary, dry-run or policy checks, rollback or containment path, and post-change verification before execution. Use a specialist or independent review only when it addresses remaining uncertainty. The route may prepare the decision packet, but it cannot grant authority. Approval requested remains different from approval granted.
