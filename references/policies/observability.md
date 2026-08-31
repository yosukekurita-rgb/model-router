# Observability

Retain enough evidence to reconstruct material routing decisions, verification, retries, quality, cost, and handoffs. Do not make full-transcript retention the default.

Use proportional levels:

| Level | Typical use | Retained evidence |
|---|---|---|
| `L0` | ordinary low-risk single-agent work | final artifact and normal host trace only |
| `L1` | retry or compute escalation | decisions, verification, and result |
| `L2` | bounded multi-agent work | L1 plus worker scopes, handoffs, and artifacts |
| `L3` | high-risk or escalated work | L2 plus approval state, side effects, and rollback evidence |

Prefer runtime-native tracing, hooks, scripts, or deterministic artifact writers. Use LLM-assisted run recording only as a fallback.

Watch for duplicate work, parallelism without independence, skipped deterministic verification, bloated handoffs, and compute increases without evidence or quality gain. Missing telemetry is `null` or unknown, not a guessed value.
