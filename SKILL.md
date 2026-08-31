---
name: model-router
description: "Route an AI task when its execution arrangement must be selected or changed: runtime/provider/model capability, reasoning or compute intensity, tools, single-agent versus bounded multi-agent topology, verification, fallback, or human escalation. Use for explicit routing, high-risk execution design, or a route that cannot meet quality or policy constraints; do not use for ordinary work with a clear runtime and execution method."
license: MIT
metadata:
  version: "0.1.0"
---

# Model Router

Choose how a task should be executed before resolving which concrete model should run it. Select the simplest eligible route that can meet the quality target. Models, tools, compute, agents, reviewers, and escalation are means, not goals.

Host, runtime, organization, and repository rules remain authoritative. This skill supplies its own minimum routing, verification, and human-escalation contracts; a host may impose stricter requirements.

## Load references only when needed

- Define success and evaluation with [quality and evaluation](references/policies/quality-and-evaluation.md).
- Express requirements and compare candidates with [capability routing](references/policies/capability-routing.md).
- Check data, tool, and action eligibility with [tool permissions](references/policies/tool-permissions.md).
- Choose reasoning intensity or budget with [compute allocation](references/policies/compute-allocation.md) and, for optimization, [cost frontier](references/policies/cost-frontier.md).
- Consider delegation, review, or parallelism with [agent topology](references/policies/agent-topology.md). Load the [economical-worker profile](references/profiles/coordinator-with-economical-workers.md) only when that pattern is a real candidate.
- Manage context pressure with [context economy](references/policies/context-economy.md); load [memory and state](references/policies/memory-and-state.md) only for pause, resume, or checkpoint decisions.
- Retain run evidence with [observability](references/policies/observability.md). Use [run recording](references/run-recording.md) only when deterministic or runtime-native instrumentation is unavailable.
- Cross an authority, risk, or confidence boundary with [human escalation](references/policies/human-escalation.md).
- Handle an unavailable or failing route with [failure and degradation](references/policies/failure-and-degradation.md).
- Resolve a current model or tool only after discovering the host's available choices. Use [registry governance](references/registry/governance.md), and treat the [model](references/registry/model-capabilities.example.yaml) and [tool](references/registry/tool-capabilities.example.yaml) registries as examples, not runtime truth.
- Map the logical route to a host with the relevant [adapter](references/adapters/): [Codex](references/adapters/codex.md) or [Claude Code](references/adapters/claude-code.md).
- Apply only the relevant workflow delta: [implementation](references/workflows/implementation.md), [investigation](references/workflows/investigation.md), or [high-risk change](references/workflows/high-risk-change.md).

Do not load every reference. Do not load examples or evals during ordinary routing unless evaluating this skill.

## Routing flow

1. Define the required output, success criteria, quality target, and verification plan.
2. Assess impact, reversibility, uncertainty, data eligibility, and action authority.
3. Reduce deterministic work first with parsers, search, queries, scripts, computation, schemas, static analysis, or tests.
4. Express the remaining need as provider-neutral capabilities and eligibility constraints.
5. Identify the limiting shape: depth, breadth, context, risk, or an external dependency.
6. Prefer one capable agent and the lightest compute profile expected to meet the target.
7. For depth, improve evidence, context, reasoning intensity, or single-agent capability before adding agents.
8. For breadth, use only bounded parallel work with independent scopes and a coordinator. Keep one writer per mutable workspace unless writers are isolated.
9. Discover currently installed, authenticated, invocable, and policy-eligible runtimes, models, and tools. Then resolve the logical route to concrete controls.
10. Execute and verify with ground truth or reproducible checks where possible. An AI's success report is not verification.
11. If material uncertainty remains, add stronger reasoning, a specialist, independent review, cross-model review, bounded parallelism, or human escalation only when it addresses that uncertainty.
12. Stop when the target is met, evidence converges, marginal gain is small, the budget is reached, or policy requires escalation.

Ask for missing information only when it cannot be discovered and would materially change the route.

## Route outcome

Return enough information to reconstruct the decision. The following block is the canonical route-outcome contract. Use every field when emitting YAML; prose may be used instead when it preserves the same information more clearly.

```yaml
quality_target: low|medium|high|critical
capability_vector:
  reasoning_depth: low|medium|high|frontier
  coding: none|preferred|required
  context_size: low|medium|high
  multimodal: none|preferred|required
  tool_use: none|preferred|required
  long_horizon: false|true
eligibility_constraints: []
deterministic_first: true|partial|false
limiting_shape: depth|breadth|context|risk|external_dependency
topology: single|single-first|bounded-parallel
compute_profile: light|normal|deep|exhaustive
runtime_resolution:
  status: unresolved|resolved|degraded|blocked
  notes: string
verification: deterministic|mixed|semantic|unavailable
independent_review: false|conditional|true
observability_level: L0|L1|L2|L3
human_escalation: false|conditional|required
assumptions: []
residual_uncertainty: []
human_decision_required: null|string
```

`runtime_resolution.notes` records concrete resolution or verification detail without adding vendor-specific fields to the stable contract. `human_decision_required` is either a short decision statement or `null`; it is not a second escalation enum.

If a human decision is required, use the minimum decision information in [human escalation](references/policies/human-escalation.md). Never report requested approval as granted approval.

## Guardrails

- Do not hard-code concrete models, prices, context limits, or provider controls in stable policy.
- Do not mistake technical availability for permission or policy eligibility.
- Do not send deterministic core processing to an LLM without a reason.
- Do not replace deterministic verification with an LLM reviewer.
- Do not parallelize one coupled bottleneck or add agents merely because they are available.
- Do not silently lower the quality target when a runtime or tool fails.
- Do not persist logs or task state without authority.
- Do not continue adding compute after the stop condition is met.
