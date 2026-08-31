# Capability Routing

Stable policy describes requirements, not model names.

## Capability vector

Use dimensions relevant to the task:

```yaml
required_capabilities:
  reasoning_depth: low|medium|high|frontier
  coding: none|preferred|required
  context_size: low|medium|high
  multimodal: none|preferred|required
  tool_use: none|preferred|required
  long_horizon: false|true
constraints:
  latency_priority: low|medium|high
  cost_priority: low|medium|high
  data_classification: public|restricted|sensitive
  reversibility: high|partial|low
```

## Resolution

1. Discover current host choices.
2. Exclude candidates that are unavailable, unauthenticated, unauthorized, data-ineligible, or action-ineligible.
3. Exclude candidates that do not meet required capabilities.
4. Prefer candidates supported by task-relevant evaluation.
5. Among routes expected to meet the same target, prefer lower total cost, latency, and coordination burden.

Keep vendor declarations separate from observed evaluation. An example registry is not proof of current availability or suitability.
