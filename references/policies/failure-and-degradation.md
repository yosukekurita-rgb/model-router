# Failure and Degradation

Classify failures before retrying: transient service failure, authentication, rate limit, invalid request, permission denial, missing capability, tool failure, resource limit, budget limit, or quality failure.

Retry only plausible transient failures and use the host's retry controls. Do not repeatedly retry authentication, permission, invalid-input, or policy failures.

If the preferred route is unavailable:

1. resolve an alternative eligible route with equivalent required capabilities;
2. if none exists, describe the degraded route and its limitation;
3. preserve the quality target unless an authorized human explicitly changes it;
4. escalate or stop when the target cannot be met safely.

Requested controls are not proof of effective controls. Report what is observed and leave unavailable telemetry unknown.
