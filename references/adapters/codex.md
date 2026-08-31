# Codex Adapter

This adapter maps the logical route to Codex controls. It does not redefine routing policy.

## Discover before resolution

Before resolution, discover and verify the current environment's:

- available models and reasoning controls;
- tool, skill, plugin, and connector access;
- local or cloud execution mode;
- sandbox, approval, and network boundaries;
- subagent and worktree support;
- runtime-native tracing and checkpoint behavior.

Do not resolve from an example registry before this discovery. Local and cloud Codex surfaces can expose different controls and permission boundaries.

## Logical mapping

Map to whatever the current Codex runtime exposes. The placeholders below are logical targets, not commands or flags.

| Logical route | Current-runtime mapping target |
| --- | --- |
| `compute_profile: light` | Lowest verified model/reasoning arrangement that still meets the quality target |
| `compute_profile: normal` | Current balanced/default arrangement, verified against task-relevant evals |
| `compute_profile: deep` | Higher supported reasoning or a more capable eligible model when measured benefit justifies it |
| `compute_profile: exhaustive` | Highest supported eligible compute only for a critical target with a stop condition and evidence of benefit |
| `topology: single` | One Codex task with no delegated workers |
| `topology: single-first` | Start with one task; add a specialist or reviewer only for a remaining, separable uncertainty |
| `topology: bounded-parallel` | A coordinator plus a bounded number of subagents for independent scopes, using read-only access or isolated worktrees |

For actual controls and syntax, verify against the current [Codex configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference), [subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents), and [worktree documentation](https://learn.chatgpt.com/docs/environments/git-worktrees). Do not invent a command when the active surface does not expose one.

## Known non-guarantees

The active Codex surface may not expose:

- a model override;
- a reasoning-effort override;
- subagents or isolated worktrees;
- cross-model review;
- the effective model, effort, or topology as observable telemetry.

Absence of a control changes resolution status; it does not justify silently lowering the quality target.

## Requested versus observed

Record logical intent separately from runtime evidence:

```yaml
requested:
  compute_profile: deep
  topology: bounded-parallel
  model: null
  reasoning_control: higher-supported
observed:
  model: null
  model_status: unverified
  reasoning_control: null
  reasoning_status: unverified
  topology: single
  topology_status: observed
```

Use `null` and `unverified` when the effective value is not exposed. Never infer an observed setting from a request.

## Worked boundaries

Positive: five independent repositories may be reviewed by a bounded set of read-only or worktree-isolated subagents, followed by coordinator synthesis and checklist verification.

Negative: one coupled architecture decision remains single-first. Do not create parallel workers that repeat the same unresolved tradeoff analysis.

Never infer permission from technical availability. Requested approval remains different from granted approval.
