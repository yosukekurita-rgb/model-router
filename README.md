# Model Router

Capability-based execution policy routing for AI agent workflows.

Model Router is a capability-based execution policy router for AI agent workflows. It decides how a task should be executed before resolving which concrete model should run it.

Do not start by asking which model should do the task. First decide how the task should be executed.

## Why this exists

Many model routers focus primarily on selecting a model:

```text
task
→ pick a model
```

This project deliberately treats model selection as one step in a broader execution decision:

```text
task
→ success criteria and quality target
→ deterministic or probabilistic execution
→ capability requirements
→ depth or breadth
→ single-agent or bounded parallel topology
→ runtime, provider, model, and tools
→ verification
→ residual uncertainty
→ escalation when justified
```

The result is an Agent Skills-compatible bundle that keeps stable policy separate from volatile model and runtime information.

## What it routes

- deterministic processing versus LLM reasoning;
- required capabilities and eligibility constraints;
- compute and reasoning depth;
- single-agent versus bounded multi-agent topology;
- runtime, provider, model, and tools;
- verification strategy;
- fallback and degraded execution;
- checkpointing and observability when justified;
- human escalation.

## What it does not do

This project is not:

- a universal model benchmark;
- a static model ranking;
- a cheapest-model selector;
- an automatic permission or approval system;
- a replacement for deterministic tests;
- a reason to use multi-agent execution by default;
- a guarantee that every host exposes the requested controls.

## Core routing flow

1. Define required output, success criteria, quality, and verification.
2. Reduce deterministic work before using model reasoning.
3. Express the remaining need as provider-neutral capabilities.
4. Distinguish depth from breadth.
5. Start with one capable agent.
6. Use bounded parallelism only for independent breadth.
7. Discover current eligible runtimes, models, and tools.
8. Execute and verify with observable evidence.
9. Address material residual uncertainty with targeted additional compute, review, or escalation.
10. Stop when the target is met or a policy boundary requires escalation.

See [SKILL.md](SKILL.md) for the executable instructions and [the glossary](references/GLOSSARY.md) for terminology.

## Examples

- [Deterministic data processing](examples/deterministic-data-processing.md): reduce and verify 100,000 CSV rows without using an LLM for core processing.
- [Architecture decision](examples/architecture-decision.md): treat a coupled, high-switching-cost decision as depth and start single-agent.
- [Multi-repository review](examples/multi-repository-review.md): use bounded parallelism for five independent repositories.
- [High-risk change](examples/high-risk-change.md): route a partly reversible permission change through verification, rollback, and authority checks.

## Installation and usage

Use the repository root as the skill directory. Install or link it as `model-router` in a location supported by your Agent Skills-compatible host. For Codex repository-local use, one supported layout is:

```text
.agents/skills/model-router/
└── SKILL.md
```

Keep the complete repository contents together so relative references resolve. Invoke it explicitly when needed:

```text
$model-router choose an execution strategy for reviewing five independent repositories.
```

Compatible hosts may also invoke the skill implicitly from its description. Ordinary work with an already-clear runtime and topology should not trigger it. See [OpenAI's current skills documentation](https://learn.chatgpt.com/docs/build-skills) or your host's documentation for current discovery locations and invocation syntax.

## Repository structure

```text
model-router/
├── README.md
├── SKILL.md
├── LICENSE
├── agents/
│   └── openai.yaml
├── assets/
│   └── ai-environment.example.yaml
├── references/
│   ├── GLOSSARY.md
│   ├── SOURCES.md
│   ├── policies/
│   ├── registry/
│   ├── adapters/
│   ├── workflows/
│   ├── profiles/
│   └── run-recording.md
├── examples/
└── evals/
    ├── routing-cases.yaml
    └── trigger-cases.md
```

## Evaluation

[`evals/routing-cases.yaml`](evals/routing-cases.yaml) contains 20 routing cases covering deterministic reduction, depth, breadth, fallback, data eligibility, verification, and escalation. [`evals/trigger-cases.md`](evals/trigger-cases.md) covers expected invocation, expected non-invocation, and prohibited routing behavior.

The eval files are specifications for behavioral testing. Static validation confirms packaging and links; it does not prove that a host discovered the skill or followed the intended route.

## Design principles

- quality target first;
- deterministic reduction first;
- capability-based, provider-neutral requirements;
- depth and breadth are different problems;
- single-agent first;
- bounded parallelism for independent work only;
- deterministic verification before semantic review when available;
- explicit residual uncertainty and escalation;
- stable policy separated from volatile registries and adapters;
- stop when additional compute no longer improves the decision.

## Limitations

- Concrete model, pricing, context, effort, and availability data change and must be discovered or refreshed at runtime.
- Example registries are documentation, not recommendations or runtime truth.
- Host support for model overrides, reasoning controls, subagents, tool restrictions, tracing, and cross-model review varies.
- Logical routing cannot grant permission or approval.
- Semantic work may retain uncertainty even after the best available verification.

## License

This project is licensed under the [MIT License](LICENSE).
