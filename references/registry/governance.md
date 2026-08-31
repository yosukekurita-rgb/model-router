# Registry Governance

Stable policy and volatile environment information are different artifacts. A registry records the latter and must be refreshed.

## Entry contract

```yaml
id:
provider:
status:
last_verified:
official_sources: []
declared:
evaluated:
```

- `declared` contains facts or positioning supported by primary vendor documentation.
- `evaluated` contains results observed on a stated task set and environment.

Do not convert a vendor claim into an evaluated score. Do not treat a published benchmark as a universal ranking.

## Resolution order

1. Discover choices currently available in the host or runtime.
2. Check authentication, policy, data, tool, and action eligibility.
3. Compare required capabilities with current evidence.
4. Consult a repository-local registry when it adds verified information.

Registry presence does not prove current availability or permission. Refresh entries after releases, alias changes, pricing or limit changes, deprecations, capability changes, or contradictory evaluation evidence.
