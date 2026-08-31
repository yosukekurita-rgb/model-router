# Quality and Evaluation

Define success before selecting a model or topology.

## Task contract

Capture only what matters:

```yaml
success:
  required_outputs: []
  completion_criteria: []
  correctness: low|medium|high|critical
  completeness: low|medium|high|exhaustive
risk:
  impact: low|medium|high|critical
  reversibility: high|partial|low
verification:
  deterministic: []
  semantic: []
```

Infer reasonable defaults when safe. Ask only about ambiguity that would materially change the result or authority boundary.

## Verification order

Prefer, when applicable:

1. ground truth or an oracle;
2. unit, integration, or regression tests;
3. schema, type, lint, static-analysis, or policy checks;
4. reproducible scripts or queries;
5. rubric-based semantic evaluation;
6. accountable human judgment.

Evaluate observable outcomes and constraint compliance. Do not count a model's claim that it succeeded as evidence. For open-ended work, define a short rubric and preserve counterevidence and uncertainty.

Stop adding compute when the contract passes, evidence converges, marginal gain is small, a budget boundary is reached, or escalation is required.
