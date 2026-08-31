# Architecture Decision

## Task

> Compare three migration architectures with incomplete requirements and high switching cost.

## Route

```yaml
quality_target: high
capability_vector:
  reasoning_depth: high
  coding: preferred
  context_size: high
  multimodal: none
  tool_use: required
  long_horizon: true
eligibility_constraints:
  - Architecture evidence must be accessible and releasable to the selected runtime.
deterministic_first: partial
limiting_shape: depth
topology: single-first
compute_profile: deep
runtime_resolution:
  status: unresolved
  notes: Discover the current host controls only after the logical route is accepted.
verification: mixed
independent_review: conditional
observability_level: L2
human_escalation: required
assumptions:
  - The alternatives share constraints and require one coherent tradeoff analysis.
residual_uncertainty:
  - Requirements remain incomplete and switching cost is high.
human_decision_required: Choose the architecture and accept its switching cost.
```

This is primarily depth: the alternatives share constraints and depend on one coherent tradeoff analysis. Start with one capable agent, improve the requirements and evidence, and use calculations or prototypes where possible. Add an independent review only if material semantic uncertainty remains. The accountable human selects the architecture because switching cost and incomplete requirements make the final choice consequential.
