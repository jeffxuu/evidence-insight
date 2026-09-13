# Release verification record

Public runtime: **1.0.0**. Review date: **2026-09-13 UTC**.

Statuses describe the specific evidence below, not the project as a whole.

| Status | Meaning |
| --- | --- |
| VERIFIED | The stated check was actually executed and its result inspected |
| PARTIALLY VERIFIED | Some components were inspected or run; the remaining scope is explicit |
| UNVERIFIED | No applicable execution or observation is available |
| BLOCKED | A concrete missing prerequisite prevents the check from completing |

| Check | Status | Evidence / remaining limit |
| --- | --- | --- |
| main baseline and feature branch | VERIFIED | Authorized initial commit `451f2271ec3b3dfba9ab665d0de5eb99ca2ccb11`; only empty `.gitkeep`; release files on `oss/v1.0.0` |
| Agent Skills validation | VERIFIED | Official skills-ref from commit `69ef37e9424c0a7ea9dd2293b559e43ec8176379`, `skills-ref validate skills/evidence-insight` succeeded |
| Public metadata and adapter version | VERIFIED | String metadata.version 1.0.0 and exact adapter version checked |
| Entrypoint/reference paths | VERIFIED | 308-line entrypoint; ten direct references; independent directory validation |
| Migration source accounting | VERIFIED | 2,026 nonblank lines across four supplied files mapped and text-checked |
| Actual reference loading by a model | UNVERIFIED | Explicit conditions are present; no completed host trace exists |
| Local deterministic tests | VERIFIED | 16 unittest tests passed again in this session; raw output in verification-logs/engineering.txt |
| GitHub-hosted CI | UNVERIFIED | Workflows implemented; remote result will be recorded after branch push |
| Local CLI installation for Codex | VERIFIED | skills 1.5.26 discovered one skill and copied it into isolated `.agents/skills/evidence-insight/` |
| Remote candidate installation | UNVERIFIED | Pending branch push and direct GitHub-source installation |
| Default-branch installation | BLOCKED | main intentionally lacks release files until owner reviews and merges PR |
| Global / other-host installation | UNVERIFIED | No such installation was executed |
| Codex model-host smoke | BLOCKED | CLI 0.154.0-alpha.3 initialized without producing model events/output before a 45-second timeout; plugin-service request returned 401 |
| Original-to-public model equivalence | BLOCKED | No authenticated independent generator execution; only static preservation checked |
| Vanilla A/B | BLOCKED | Must follow model migration comparison; no executions/judgments claimed |
| Actual before/after demos | BLOCKED | Five example guides contain inputs and expected boundaries, not model outputs |
| Sealed holdout | UNVERIFIED | Ten exposed blueprints; no independent custody or sealed full inputs claimed |
| ChatGPT upload bundle | PARTIALLY VERIFIED | Regenerated; source hashes, merged reference text, adapter and license checked; actual Project upload/retrieval not run |
| License/material hygiene | PARTIALLY VERIFIED | Owner-authorized text, original synthetic fixtures and official license text reviewed; authorship provenance not independently certifiable |
| Secrets | PARTIALLY VERIFIED | Limited patterns found no key/token matches; manual review required; not a universal absence guarantee |
| skills.sh indexing | UNVERIFIED | No listing confirmed; test installs disable telemetry |
| Star History | UNVERIFIED | No chart displayed; target endpoint not confirmed usable |

## Executed local commands

```bash
skills-ref validate skills/evidence-insight
python scripts/validate.py
python -m unittest discover -s tests -v
python scripts/build_chatgpt_bundle.py
```

Development environment: Python 3.12; dependencies pinned in `requirements-dev.txt`.
The official validator package reports 0.1.0 at the pinned source commit; the commit identifies the validation code precisely.
The tests reject missing references, uncovered source lines, duplicate YAML keys, duplicate/forged records,
output tampering, mismatched A/B settings, double adjudication and injection passes without tool traces.
They check empty-result reports, unit conversion and inert archive contents. No model quality metric was measured.

## Host probe boundary

The model attempt used a synthetic qualifier-preservation input, read-only mode, no requested external research,
an isolated installed skill and no evaluation answer files. No model output or tool action trace was produced.
The 401 warning concerned plugin initialization; it is not enough to identify every cause of the stalled model host.
No credentials were read, printed or changed to work around the problem. No retry loop or hidden fallback generated substitute results.

This PR must not be presented as a benchmark-validated release. See [remaining gates](release-checklist.md).

## Resumed verification evidence (2026-09-13 UTC)

The original isolated environment was restored at the same path with Python 3.12.14. No locked direct dependency was upgraded.
Node v24.19.0, npm 11.9.0, skills CLI 1.5.26 and Codex CLI 0.154.0-alpha.3 were actually observed.
The nine stale reference copies differed only in trailing newlines. Regeneration resolved their hashes without editing runtime rules.
All 12 installed files now match the source skill byte for byte. The ChatGPT bundle records the same source hashes.

- [Environment restoration](verification-logs/environment.txt) and [actual versions](verification-logs/versions.txt).
- [Regeneration commands and exit statuses](verification-logs/regeneration.txt).
- [Source / installed / bundle SHA-256 inventory](verification-logs/package-consistency.json).
- [Official validation and 16 passing engineering tests](verification-logs/engineering.txt).
- [Generator reproducibility](verification-logs/reproducibility.txt).
- [Migration and material/privacy audit](verification-logs/migration-audit.txt).
- [Model-host preflight metadata](verification-logs/model-host-attempt.json), [stderr](verification-logs/model-host-stderr.txt) and [stdout](verification-logs/model-host-stdout.txt).

The model-host preflight requested gpt-6-astra with high reasoning effort but never returned model events.
Actual model/version and effective reasoning settings therefore remain unobserved. Exit status was 124 after 45 seconds;
the 401 concerned plugin-service initialization. The internal/public comparison and vanilla A/B were not executed.
No completed model execution, security pass, reference-loading trace or paired demo is inferred from engineering checks.

The current [official specification](https://agentskills.io/specification) and [skills.sh FAQ](https://www.skills.sh/docs/faq)
were rechecked on 2026-09-13 UTC. Directory indexing remains unverified.
