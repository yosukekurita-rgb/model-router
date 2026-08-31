# Deterministic Data Processing

## Task

> Deduplicate 100,000 CSV rows and count records by category.

## Route

```yaml
quality_target: high
llm_required_for_core_processing: false
deterministic_first: true
capability_vector:
  data_processing: required
  reasoning_depth: low
topology: single
runtime_resolution: script-or-query-tool
verification: deterministic
human_decision_required: null
```

Parse the CSV with a script, query engine, or database; define the deduplication key; compute counts; and verify row totals, uniqueness, and a reproducible sample. Use an LLM only if a semantic decision such as ambiguous category mapping remains. A high-end model is not the default execution engine for the rows.
