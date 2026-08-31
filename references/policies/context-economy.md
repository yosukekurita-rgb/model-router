# Context Economy

Keep the current objective, constraints, relevant evidence, state, and next action in active context. Do not use the context window as an archive.

Reduce large inputs with search, queries, parsing, aggregation, schemas, or scripts before model reasoning. Load references and tools only when the active decision needs them.

Use an isolated worker as a context compressor only when the scope is independent. A useful handoff is compact and evidence-bearing:

```yaml
conclusion:
evidence: []
affected_items: []
uncertainties: []
confidence:
artifact_ref: null
```

Consider semantic compaction when context pressure, interruption risk, or handoff value is material. Preserve the objective, constraints, decisions, unresolved uncertainty, artifact references, verification state, and next actions. Never compact an unverified claim into a verified one.
