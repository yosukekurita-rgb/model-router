# Codex Adapter

This adapter maps the logical route to Codex controls. It does not redefine routing policy.

Before resolution, discover and verify the current environment's:

- available models and reasoning controls;
- tool, skill, plugin, and connector access;
- local or cloud execution mode;
- sandbox, approval, and network boundaries;
- subagent and worktree support;
- runtime-native tracing and checkpoint behavior.

Map logical compute profiles to controls exposed by the current Codex runtime. Do not assume that every surface supports model overrides, reasoning overrides, subagents, or cross-model review.

Distinguish requested settings from runtime-observed settings. If the effective model, effort, or topology is not exposed, report it as unverified. Never infer permission from technical availability.

For current product details, consult [OpenAI's Codex documentation](https://learn.chatgpt.com/docs) before relying on commands or controls.
