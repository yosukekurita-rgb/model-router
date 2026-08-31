# Architecture Decision

## Task

> Compare three migration architectures with incomplete requirements and high switching cost.

## Route

```yaml
quality_target: high
deterministic_reduction: partial
capability_vector:
  reasoning_depth: high
  evidence_synthesis: required
topology: single-first
independent_review: conditional
verification: mixed
human_decision_required: likely
```

This is primarily depth: the alternatives share constraints and depend on one coherent tradeoff analysis. Start with one capable agent, improve the requirements and evidence, and use calculations or prototypes where possible. Add an independent review only if material semantic uncertainty remains. The accountable human selects the architecture because switching cost and incomplete requirements make the final choice consequential.
