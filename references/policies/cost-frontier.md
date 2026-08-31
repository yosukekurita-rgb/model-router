# Cost Frontier

Cost optimization means selecting the lowest-total-cost eligible route that still meets the fixed quality target. Total cost includes retries, tools, latency, coordination, and rework, not only model price.

Keep a passing baseline. Compare proposed reductions on the same representative tasks and verification:

```yaml
comparison:
  quality_target:
  deterministic_checks:
  semantic_quality:
  completion_rate:
  retries:
  end_to_end_latency:
  total_usage_or_cost:
  coordinator_rework:
  decision: keep|reject|needs_more_evidence
```

Prefer deterministic reduction, progressive disclosure, concise tool output, stable-context reuse when supported, and clear stop conditions before lowering capability. Use economical workers only for independent, bounded, context-isolatable, externally verifiable tasks. Return to the baseline if quality, reliability, or total cost worsens.
