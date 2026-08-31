# High-Risk Change

## Task

> Plan a production permission change that is high impact and only partly reversible.

## Route

```yaml
quality_target: critical
capability_vector:
  reasoning_depth: high
  tool_use: required
eligibility_constraints:
  authority: explicit
  data_and_action_policy: required
topology: single-first
verification: required
rollback_or_containment: required
observability_level: L3
human_decision_required: true
```

Resolve the exact target, blast radius, approval boundary, dry-run or policy checks, rollback or containment path, and post-change verification before execution. Use a specialist or independent review only when it addresses remaining uncertainty. The route may prepare the decision packet, but it cannot grant authority. Approval requested remains different from approval granted.
