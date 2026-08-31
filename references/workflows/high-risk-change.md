# High-Risk Change Workflow Delta

Apply these additions when impact is high, reversibility is limited, authority is material, or failure would cross a security or compliance boundary:

- define the exact action, target, owner, and prohibited scope;
- require a verification plan and rollback or containment plan before execution;
- prefer dry runs, policy checks, and reversible staging;
- resolve the approval boundary and approval state explicitly;
- isolate writers and restrict tools to the minimum required;
- record externally visible side effects and post-action verification;
- stop when validation fails or authority is missing.

Do not report a requested approval as granted. Do not silently substitute a lower-quality route when the preferred route is unavailable.
