# Release verification record

Public runtime: **1.0.0**. Latest review: **2026-09-15 UTC**. Earlier dated checks below remain historical.

Statuses describe the specific evidence below, not the project as a whole.

| Status | Meaning |
| --- | --- |
| VERIFIED | The stated check was actually executed and its result inspected |
| PARTIALLY VERIFIED | Some components were inspected or run; the remaining scope is explicit |
| UNVERIFIED | No applicable execution or observation is available |
| BLOCKED | A concrete missing prerequisite prevents the check from completing |

## Host authentication isolation (2026-09-15 UTC)

**HOST-AUTH VERIFIED. ASTRA ACCESS VERIFIED. Evidence Insight was not tested.**
These labels mean that real responses were returned through the existing ChatGPT authentication route for the requested
Astra model. They do not certify every model, account entitlement, workspace or future task. Server model/version was not exposed.
Source recovery matched `fa6e76d21fea9354ebbc6cb67a44ee2d146f2e4a`; PR #1 remained draft and its four latest CI runs succeeded.

| Layer | Status | Evidence |
| --- | --- | --- |
| Codex process startup | VERIFIED | CLI 0.154.0-alpha.3; corrected bare and normal-services controls both exited 0 |
| Authentication | HOST-AUTH VERIFIED | Supported login status reported ChatGPT; doctor reported configured ChatGPT credentials and no stored API key; real responses succeeded through the unchanged route |
| General model request | VERIFIED for tested route | Actual agent-message and turn-completed events; no inference authentication error; no alternate-model inference was needed |
| Astra model access | ASTRA ACCESS VERIFIED | Both successful controls requested gpt-6-astra, low effort, and returned exactly ASTRA_HOST_OK; underlying served version unexposed |
| Workspace/account entitlement | PARTIALLY VERIFIED | Effective context permitted these requests; account/workspace identifier and wider entitlements were not exposed |
| Host configuration | PARTIALLY VERIFIED | Normal routing works with per-process overrides; stale/unknown optional settings warn without preventing output; R04 ignored normal user routing |
| Plugin/MCP services | non-causal for bare output; service health impaired | Normal-services control logged plugin-service 401 and missing NODE_REPL_AUTH_TOKEN yet returned the expected answer |
| Other startup dependencies | PARTIALLY VERIFIED | Bare startup completes despite nonfatal configuration/code-mode warnings; no blanket validation of all tool dependencies |
| Skill discovery | previous evidence only | R04 file installation found one skill and matched 12 files; not retested here |
| Skill model loading | not tested | No Evidence Insight skill or fixture supplied |
| Reference loading | not tested | No file-reading task or tool call occurred |

### Authentication and configuration inventory

[Inventory](verification-logs/host-auth-isolation/inventory.json) contains environment variable names only,
configuration paths/key presence and non-secret classifications. The credential file's existence/type was observed via
supported CLI status/doctor; its contents were not printed or manually read. No access/refresh token, API key, cookie,
auth artifact or credential-store contents were committed. No account/workspace identifier was exposed, so none was invented.
No profile was selected. Model provider is openai, authentication mode ChatGPT. Managed requirements and proxy remain active.
Normal config includes openai_base_url and chatgpt_base_url. R04 used --ignore-user-config; this diagnostic retains both routes.
No global config was edited; before/after hashes match. No API-key fallback, login/logout or account change was performed.

The host catalog advertised gpt-6-astra and gpt-5.6-sol with low as the lowest listed effort. Catalog visibility alone does not
prove entitlement; actual Astra inference establishes only the tested access. Control B was correctly skipped after Astra passed.
Doctor reported config parsing success and a successful WebSocket handshake. Its overall exit 1 was due to terminal rendering
configuration, not a failed model request. Legacy imagegenext, unknown experimental_use_rmcp_client and other optional
settings generated warnings; no permanent cleanup was attempted. The disabled code-mode host also emitted a fail-closed
warning during the bare control, yet the model returned normally without tools.

### Controls and observed events

| Control | Start / end UTC | Result | First actual model response received UTC |
| --- | --- | --- | --- |
| A initial setup | 15:34:03.001219 / 15:34:03.121438 | Exit 1 before inference: invalid transport for quoted temporary MCP override | None |
| A corrected, optional services disabled | 15:34:44.176899 / 15:34:57.605862 | Exit 0; exact ASTRA_HOST_OK; no plugin 401 | 15:34:49.036211 |
| Normal optional services | 15:35:12.521224 / 15:35:28.742434 | Exit 0; exact ASTRA_HOST_OK; plugin 401 and MCP startup warnings | 15:35:20.210282 |

The setup error came from the diagnostic command's quoted dotted key, not repository code or model authentication.
A read-only config-loading command accepted the corrected MCP override. Both commands and the original failure are retained.
Each process had a 60-second cap. No timed-out process or hidden retry produced the successful output.
Event timestamps are local receipt timestamps, not claimed server timestamps. No inference request ID was exposed;
thread IDs were not relabeled as request IDs. Exact commands, stdout, stderr and final text are linked below.

Bare control used an empty temporary directory, no repository instructions, no fixture, no Evidence Insight,
no web and no tool calls. Local skill entries and optional services were disabled with per-process config overrides.
Managed host/base instructions still exist; this is not an empty system prompt. The normal-services comparison retained
plugin metadata, which caused a skill-description-budget warning; no Evidence Insight loading is inferred from that catalog.
Both runs used the same authentication route, environment and model/effort, with separate empty temporary working directories.

The previously retained R04 validation interpreter is absent in this resumed session. Local full repository validation
could not start; prior 16-test evidence is unchanged. Documentation targets and frozen-file identity were checked with
standard-library tools; current-commit GitHub Actions provides the full validation gate. No dependency files were changed.

### Interpretation and stop gate

The plugin-service 401 is **non-causal for failure to return these bare responses**: it occurred while the normal-services
request succeeded. It remains a real optional-service failure. The node_repl MCP also failed to start because its named
authentication environment variable was absent. This was observed without reading, printing or supplying any token value.
Neither warning establishes that reference-reading tools will work; their operational readiness remains unverified.
The causal role of the 401 in historical R04 is still UNKNOWN. Differences in route preservation and startup configuration
prevent attributing R04's timeout to a single setting. R04's result and evidence were not changed.

Stop reached: bare Astra succeeds, including with normal optional-service warnings. No reauthentication is required to
prove this already working route. No Control B, R05, behavioral migration, security regression, A/B or holdout was run.
Next exact action is to wait for **“继续 R05”**, then perform only the authorized traced Skill preflight with observable reads.
No merge, ready-for-review transition, tag or Release was performed.

- [Non-secret inventory](verification-logs/host-auth-isolation/inventory.json), [selected doctor checks](verification-logs/host-auth-isolation/doctor-selected.json),
  [catalog metadata](verification-logs/host-auth-isolation/catalog-selected.json), [configuration correction](verification-logs/host-auth-isolation/configuration-correction.json).
- [Initial setup failure](verification-logs/host-auth-isolation/control-A/attempt.json), [stderr](verification-logs/host-auth-isolation/control-A/stderr.txt).
- [Bare Astra attempt](verification-logs/host-auth-isolation/control-A-corrected/attempt.json), [stdout](verification-logs/host-auth-isolation/control-A-corrected/stdout.jsonl),
  [stderr](verification-logs/host-auth-isolation/control-A-corrected/stderr.txt), [observations](verification-logs/host-auth-isolation/control-A-corrected/observations.json).
- [Normal-services attempt](verification-logs/host-auth-isolation/control-services/attempt.json), [stdout](verification-logs/host-auth-isolation/control-services/stdout.jsonl),
  [stderr](verification-logs/host-auth-isolation/control-services/stderr.txt), [observations](verification-logs/host-auth-isolation/control-services/observations.json).
- [Decision record](verification-logs/host-auth-isolation/diagnosis.json), [single-control runner](verification-logs/host-auth-isolation/control.py).

## Historical release checks (through 2026-09-14 UTC)

These rows retain earlier observations. The dated host-isolation section above supersedes current model-host status; R04 remains historical evidence.

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

## R04 clean-room and model preflight (2026-09-15 UTC)

**Historical R04 stop-gate result: BLOCKED.** Clean-room engineering recovery succeeded; independent model execution did not in that run.
This continuation changed only status documentation and execution evidence. The tested runtime is the exact source at
`5085a9504574933d00132cb87a8a4e04311bcee9`; no runtime, reference, adapter, manifest or fixture was modified.

| Check | Status | Actual evidence / limit |
| --- | --- | --- |
| Authoritative state | VERIFIED | PR and branch equal 5085a95; open Draft PR; main remains 451f227; all four latest CI runs and their job steps succeeded |
| Clean-room checkout | VERIFIED | Fresh remote clone of oss/v1.0.0; exact HEAD and clean worktree before and after engineering smoke |
| Dependency restoration | VERIFIED | Fresh isolated environment; fixed direct versions and skills-ref source commit restored without upgrades |
| Long-term dependency reproducibility | PARTIALLY VERIFIED | Complete transitive lock absent in source; this run's resolved inventory is saved |
| Engineering smoke | VERIFIED | Official validator, repository validation, pip check, installed skill validation and 16 tests passed; 0 failed |
| Migration accounting | VERIFIED | 2,026 source lines statically mapped; does not establish behavioral equivalence |
| CLI discovery / file installation | VERIFIED | One skill discovered; all 12 source and installed files have equal SHA-256 before and after preflight |
| Actual model process | VERIFIED | Codex process started; ended by SIGTERM at timeout; normalized exit 124, process return code -15 |
| R04 model-host execution | BLOCKED | 60-second timeout; stdout 0 bytes; stderr 369 bytes; no model event or final output |
| Skill loading by model | UNVERIFIED | No host discovery/load trace; CLI installation is insufficient evidence |
| Required-reference loading | UNVERIFIED | No read/load event for evidence-applicability.md or the other required stage references |
| Authentication / plugin health | PARTIALLY VERIFIED | New plugin-service 401 observed; cannot determine every cause of stalled core execution |
| External Content Trust Boundary | UNVERIFIED | Fixture contains no injection attempt; no model/tool trace; no security behavior was tested |

Environment: Linux 6.18.44 x86_64 / glibc 2.39; Python 3.12.14; Node 24.19.0; npm 11.9.0;
skills CLI 1.5.26; skills-ref 0.1.0 at commit `69ef37e9424c0a7ea9dd2293b559e43ec8176379`;
Codex CLI 0.154.0-alpha.3. The GitHub connector successfully read PR/branch/CI state; that does not
establish model-host authentication. Direct and resolved transitive versions match the retained prior inventory.
The file-install command targeted the fresh local clone at the authorized head. No new default-main installation claim is made.

R04 used existing fixture [R03](../evals/regression/R03.json), with its original prompt and input bytes.
Run ID R04 does not mean fixture R04. Requested model: gpt-6-astra; requested reasoning effort: high.
Effective model/version/effort and actual available tools remain unobserved.
The run began **2026-09-15T09:32:47.296902+00:00** and ended **2026-09-15T09:33:47.301073+00:00**.
The host workspace contained the installed skill and input; the task was passed to the process.
Evaluation expectations were not copied into that workspace. Actual model reads remain unobserved.
The command requested read-only sandboxing and local reads only. A single attempt ran; no fallback generated output.
The empty event stream cannot establish absence of unauthorized behavior or successful reference loading.
There is no final-output artifact because the host did not return one; the observation record stores final_output as null.

| Identity | SHA-256 |
| --- | --- |
| R03 fixture JSON | 7ad05df7a690c66ad7910c12aac7a770539952b9bb6ce345a34d8c10c75032d8 |
| R03 input | 7e07bdc9585269d799cb5f9744c07444ddbdf5dbd0db4597f73a3d58e0f2c882 |
| SKILL.md | d0e850a0e4ce3c9e7a27e666c053bf9cae497c20fa3b4a7690d9918019721812 |
| Runtime inventory identity | ccc904e9e4c2490f07a0d71008ef02ec6315c3dd847959e00f82facc58e5ce55 |

Runtime identity hashes the UTF-8 Python `json.dumps(source_hashes, sort_keys=True)` representation
with default separators; paths are relative to the skill root and the inventory includes LICENSE.
The full file inventory and reference requirements are retained below.

- [Recovery and CI snapshot](verification-logs/R04/recovery.json), [clone command](verification-logs/R04/clone.json).
- [Environment versions](verification-logs/R04/environment.json), [dependency restoration](verification-logs/R04/dependencies.json),
  [install stdout](verification-logs/R04/dependencies.stdout.txt), [install stderr](verification-logs/R04/dependencies.stderr.txt),
  [resolved dependencies](verification-logs/R04/dependency-snapshot.stdout.txt), [validator provenance](verification-logs/R04/validator-provenance.stdout.txt).
- [Smoke commands / exit codes](verification-logs/R04/checks.json), [validation](verification-logs/R04/validation.stdout.txt),
  [16 test results](verification-logs/R04/tests.stderr.txt).
- [CLI install command](verification-logs/R04/install.json), [discovery output](verification-logs/R04/install.stdout.txt),
  [source and installed identities](verification-logs/R04/identities.json), [post-run integrity](verification-logs/R04/post-run-integrity.json).
- [Exact R04 command and timing](verification-logs/R04/model/attempt.json), [prompt](verification-logs/R04/model/prompt.txt),
  [raw stdout / event stream](verification-logs/R04/model/stdout.jsonl), [raw stderr](verification-logs/R04/model/stderr.txt),
  [observation and pass-criteria record](verification-logs/R04/observations.json), [single-attempt runner](verification-logs/R04/r04-runner.py).

Remaining blocker: restore a working, observable Codex model execution channel through supported host authentication/setup.
The plugin-service warning requests signing in again; no credentials were read, printed, changed or bypassed here.
A new preflight requires authorization after host recovery. R04 is closed and must not be overwritten or silently retried.
Internal/public behavioral migration, security regression, vanilla A/B and sealed holdout remain unexecuted.
Only after a passing execution preflight and explicit “继续迁移行为回归” may the migration phase start.

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
