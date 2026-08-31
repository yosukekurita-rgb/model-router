# Coordinator with Economical Workers

This is an optional profile, not a default topology or model recommendation.

Use it only when worker tasks are independent, bounded, context-isolatable, and externally verifiable. Keep cross-cutting judgment, synthesis, and completion ownership with one capable coordinator.

```yaml
coordinator:
  responsibilities:
    - decomposition
    - eligibility checks
    - synthesis
    - final verification
workers:
  initial_fan_out: bounded
  task_requirements:
    - independent
    - bounded
    - context-isolatable
    - externally-verifiable
  write_permission: read-only-or-isolated
fallback:
  - return cross-cutting judgment to the coordinator
  - use a stronger eligible route when retries erase the expected saving
```

Compare this profile against a passing single-agent baseline. Account for retries, handoff loss, coordination, and coordinator rework. Remove the profile when it does not preserve quality or reduce total cost.
