# Compute Allocation

Use the least compute reasonably expected to meet the quality target.

Treat compute as several dimensions:

- depth: reasoning intensity or stronger single-agent capability;
- breadth: independent bounded work;
- risk: stronger verification, rollback, or approval;
- context: retrieval, reduction, isolation, or checkpointing.

Use logical profiles such as `light`, `normal`, `deep`, and `exhaustive`. Map them to current host controls only at runtime. Do not place provider-specific effort values in stable policy.

For a depth problem, improve evidence and context, then consider more reasoning or a stronger single agent. For a breadth problem, consider bounded parallelism only when scopes are independent, outputs are individually useful, and synthesis is defined.

Do not default to exhaustive compute. Stop on quality pass, evidence convergence, low marginal gain, budget boundary, or escalation boundary.
