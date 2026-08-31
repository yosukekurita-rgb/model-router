# Deterministic Data Processing

## Task

> Deduplicate 100,000 CSV rows and count records by category.

## Route

```yaml
quality_target: high
capability_vector:
  reasoning_depth: low
  coding: preferred
  context_size: low
  multimodal: none
  tool_use: required
  long_horizon: false
eligibility_constraints:
  - The input data is authorized for the selected local tool or runtime.
deterministic_first: true
limiting_shape: context
topology: single
compute_profile: light
runtime_resolution:
  status: resolved
  notes: Use a parser, query engine, or database for the core row processing.
verification: deterministic
independent_review: false
observability_level: L1
human_escalation: false
assumptions:
  - A deterministic deduplication key can be defined.
residual_uncertainty: []
human_decision_required: null
```

Parse the CSV with a script, query engine, or database; define the deduplication key; compute counts; and verify row totals, uniqueness, and a reproducible sample. Use an LLM only if a semantic decision such as ambiguous category mapping remains. A high-end model is not the default execution engine for the rows.
