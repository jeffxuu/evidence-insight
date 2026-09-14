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
| Local deterministic tests | VERIFIED | 16 unittest tests passed on 2026-09-13 UTC; raw output in verification-logs/engineering.txt |
| GitHub-hosted CI | VERIFIED | Both workflows and all job steps passed on candidate commit 1779c70; exact records below |
| Local CLI installation for Codex | VERIFIED | skills 1.5.26 discovered one skill and copied it into isolated `.agents/skills/evidence-insight/` |
| Remote candidate installation | VERIFIED | Fragment-ref command installed one skill; all 12 file hashes match current source |
| Default-branch installation | BLOCKED | Exact requested command ran with CLI 1.5.26: exit 1, No skills found; main still contains initialization only |
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

The retained preflight ran on **2026-09-13 at 15:11:45 UTC**, using the input bytes from
[R03: Different populations, different proposition](../evals/regression/R03.json).
The input SHA-256 was `7e07bdc9585269d799cb5f9744c07444ddbdf5dbd0db4597f73a3d58e0f2c882`,
matching [the actual attempt record](verification-logs/model-host-attempt.json).
It used a generic analysis-and-social request, read-only mode, no requested external research, the public runtime
and no evaluation answer files. It was an environment preflight, not an execution of the full R03 benchmark protocol.
No model output or tool action trace was produced. The earlier qualifier-preservation wording did not describe this retained attempt.
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

## Remote verification

Candidate commit: `1779c7078360f86f5ac66bd6a98ea691498e82a2`.
Its Git tree `e350740c6c8c0f596b26aaff7e0726143b2e480b` exactly matched the local staged tree before the branch update.

- [Validate skill run](https://github.com/jeffxuu/evidence-insight/actions/runs/34765071352): success, all job steps inspected.
- [Evaluation engineering smoke run](https://github.com/jeffxuu/evidence-insight/actions/runs/34765071351): success, all job steps inspected.
- [Workflow, job, step and check-run snapshot](verification-logs/remote-ci.json).
- [All remote installation attempts and file hashes](verification-logs/remote-installation.json).
- [Successful branch-install log](verification-logs/install-candidate-fixed.txt), [failed tree-URL log](verification-logs/install-candidate.txt), [default-main log](verification-logs/install-default.txt).

The legacy commit-status endpoint returns pending with zero statuses; GitHub Actions uses check runs,
and both check runs report completed/success. No failed CI job log exists for these successful runs.
The installation documentation now uses the CLI-supported fragment ref for the slash-containing branch.
This fixes an installation-command defect only; runtime files and migration mappings are unchanged.

## Continuation audit (2026-09-14 UTC)

This continuation read GitHub directly because the selected local execution environment was unavailable.
No terminal or model-execution capability was exposed. No local environment restoration, new host probe,
local test run or package rebuild was performed in this continuation.

| Recovery expectation | Actual observation | Impact |
| --- | --- | --- |
| Restore and inspect the local checkout and verification environment | Execution environment unavailable; no callable terminal | Local Git cleanliness and derivative-file existence cannot be rechecked |
| Read the complete migration manifest | GitHub blob retrieval succeeded for `52257860ddb60c57922b0c5a592c6e232e3531a1` | The earlier large-file reading gap is closed |
| Run a fresh independent model-host preflight | No model execution host is accessible in this session | Behavior remains BLOCKED; the 401/timeout is the retained 2026-09-13 observation, not a new run |

Remote static audit was executed against commit `4186dd0086ba66ca3e001c148a3bb913bac94dd5`.
All 16 distinct source/destination files were fetched. The audit compared every manifest source/destination
line to its actual file text, checked duplicate and missing source lines, required mapping fields and loading conditions
in the entrypoint, and checked the 33 recorded security-addition lines.

Result: **2,026 expected nonblank source lines; 2,026 unique mapped lines; zero discrepancies in those checks**.
All 42 changed source-text rows retain their recorded public-version or approved-conflict classifications.
This verifies static accounting only. It does not verify model reference loading, behavioral equivalence or injection resistance.

Only verification documentation and project state are updated. Runtime, adapter, historical originals,
manifest, fixtures, dependencies and workflows remain unchanged. Existing GitHub Actions can validate this documentation
commit independently; they cannot supply the missing model-host evidence.
