# Trigger Cases

Evaluate both skill discovery and behavior. Record host and version, skill location, explicit or implicit invocation, observed route, and pass or fail. File presence alone is not a runtime pass.

## Expected invocation

1. Explicit routing: `Use $model-router to choose the execution arrangement for a large migration analysis.`
2. Topology selection: `Should this five-repository review use one agent or bounded parallel workers?`
3. Fallback: `The preferred runtime is unavailable; choose an eligible fallback without lowering the quality target.`
4. High-risk design: `Design the verification, rollback, and approval route for a production permission change.`

A pass identifies quality, capabilities, eligibility, topology, concrete-resolution status, verification, residual uncertainty, and escalation when applicable.

## Expected non-invocation

1. `Run shellcheck on this script and report the errors.`
2. `Rename this file and run the existing unit test.`
3. `Summarize this paragraph in two sentences.`
4. `Use the current runtime to apply this ordinary localized fix; the execution method is already specified.`

A pass completes the ordinary task directly without adding routing ceremony.

## Negative behavior checks

Fail a case if the route:

- selects a model before defining success and capabilities;
- uses an LLM for deterministic core processing without justification;
- adds agents without independent breadth;
- parallelizes one coupled bottleneck;
- replaces available tests with an LLM reviewer;
- silently lowers the quality target after failure;
- reports requested approval as granted;
- mistakes runtime availability for permission;
- continues adding compute after the target is met.
