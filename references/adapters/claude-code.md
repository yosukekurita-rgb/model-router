# Claude Code Adapter

This adapter maps the logical route to Claude Code controls. It does not redefine routing policy.

Before resolution, discover and verify the current environment's:

- available models and reasoning controls;
- tool and permission configuration;
- skill, plugin, and connector access;
- non-interactive execution controls;
- subagent, isolation, and workspace behavior;
- runtime-native tracing and checkpoint behavior.

Map logical compute profiles to controls actually exposed by the current Claude Code version. Do not assume that model overrides, reasoning overrides, subagents, or cross-model review are available on every surface.

For delegated or advisory work, pass a bounded scope and relevant evidence, use read-only access when possible, and return findings to the coordinator for disposition. Treat requested settings separately from observed execution.

For current product details, consult [Anthropic's Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code/overview) before relying on commands or controls.
