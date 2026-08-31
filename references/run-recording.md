# Run Recording Fallback

Prefer runtime-native tracing, hooks, scripts, or deterministic artifact writers. Use this fallback only when those mechanisms cannot capture material routing and verification evidence.

Record a compact event when a material route, retry, escalation, verification, or stop decision occurs:

```yaml
event:
  type: route|retry|escalate|verify|stop
  reason:
  evidence_refs: []
  verification_state:
  residual_uncertainty: []
  approval_state: not_required|requested|granted|denied|unknown
```

Use observed values. Keep unavailable telemetry as `null` or unknown. Do not ask an LLM to fabricate exact token, model, effort, timing, or approval data.

Store compact artifacts only when authorized and justified by reconstruction or audit value. Do not make a recorder agent, full transcript archive, or persistent memory a default requirement.
