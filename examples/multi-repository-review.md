# Multi-Repository Review

## Task

> Review five independent repositories against the same security checklist.

## Route

```yaml
quality_target: high
breadth: high
parallelism: justified
topology: bounded-parallel
fan_out: small-and-bounded
writers: read-only-or-isolated
final_synthesis: coordinator
verification: checklist-plus-reproducible-evidence
```

Each repository is an independent scope, so bounded parallel review can reduce elapsed time. Give each worker the same checklist and evidence contract. Keep workers read-only or isolate their workspaces. One coordinator reconciles findings, checks coverage, removes duplicates, and produces the final report. Do not increase fan-out beyond the independent scopes.
