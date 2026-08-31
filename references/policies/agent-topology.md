# Agent Topology

Start with one capable agent.

## Depth and breadth

Depth is one coupled problem that needs better evidence, context, reasoning, or capability. More agents usually duplicate the bottleneck.

Breadth is multiple independent scopes whose results remain useful on their own. Bounded parallelism may help.

## Parallel route requirements

Use parallel agents only when:

- scopes are independent and bounded;
- a coordinator owns decomposition, synthesis, and completion;
- each worker has an explicit task and return contract;
- coordination cost is justified;
- concurrent writers use isolated workspaces, or workers are read-only.

Start with a small fan-out, commonly one to three workers, but treat that as guidance rather than a fixed limit. Add workers only for newly identified independent scope.

Reviewers are advisory. Prefer read-only access, and disposition findings as accepted, rejected with evidence, or requiring investigation. Independent or cross-model review is justified only when material semantic uncertainty remains after deterministic checks.
