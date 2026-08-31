# Multi-Repository Review

## Task

> Review five independent repositories against the same security checklist.

## Route

```yaml
quality_target: high
capability_vector:
  reasoning_depth: medium
  coding: required
  context_size: high
  multimodal: none
  tool_use: required
  long_horizon: true
eligibility_constraints:
  - Repository access is authorized.
  - Each repository is an independent read-only or isolated scope.
deterministic_first: partial
limiting_shape: breadth
topology: bounded-parallel
compute_profile: normal
runtime_resolution:
  status: unresolved
  notes: Map bounded parallelism to current host controls only if isolation is available.
verification: mixed
independent_review: false
observability_level: L2
human_escalation: conditional
assumptions:
  - The five repositories do not share a coupled analysis bottleneck.
residual_uncertainty:
  - Cross-repository synthesis remains a coordinator responsibility.
human_decision_required: null
```

Each repository is an independent scope, so bounded parallel review can reduce elapsed time. Give each worker the same checklist and evidence contract. Keep workers read-only or isolate their workspaces. One coordinator reconciles findings, checks coverage, removes duplicates, and produces the final report. Do not increase fan-out beyond the independent scopes.
