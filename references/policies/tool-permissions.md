# Tool Permissions and Information Boundaries

Two questions are independent:

- May this agent perform this action?
- May this data be processed by this provider, runtime, or tool?

Technical availability answers neither question.

An eligible route should be reachable, authenticated, invocable, provider-allowed, data-allowed, tool-allowed, and action-allowed. Apply the least privilege needed for each coordinator, worker, or reviewer. Default reviewers to read-only when possible.

Before a cross-provider handoff, recheck data eligibility, redact or minimize the payload, and send only the relevant evidence and task contract. Do not transfer an entire conversation by default.

Host, organization, repository, and user authority rules take precedence. High-impact, destructive, externally visible, privileged, or hard-to-reverse actions may require explicit approval. Availability never implies approval.
