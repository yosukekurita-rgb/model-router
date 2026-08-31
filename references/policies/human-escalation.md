# Human Escalation

Escalate for capability when the route cannot meet the quality target. Escalate for authority when an accountable human must decide despite adequate technical capability. Do not confuse the two.

When human judgment is required, provide at least:

```yaml
decision_required:
recommended_action:
why:
options_and_tradeoffs:
material_evidence:
verification:
residual_uncertainty:
reversibility:
requested_human_action:
```

Prose is acceptable if it preserves the information. Add routing-specific fields when useful:

```yaml
current_route:
route_limitation:
recommended_route_change:
expected_quality_gain:
additional_cost_or_risk:
```

Escalate material ambiguity, insufficient evidence, failed validation, unknown policy cases, authority boundaries, or high-impact hard-to-reverse actions. Host rules may be stricter.

`approval requested` is not `approval granted`. Record approval as granted only after an authorized human or system has actually granted it for the stated action and scope.
