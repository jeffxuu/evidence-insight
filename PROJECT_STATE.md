# Evidence Insight project state

Updated: 2026-09-15 UTC. Public version: **1.0.0**.
This management document is not a runtime dependency.

## Current goal and phase

This implementation phase reached its authorized stop: [Draft PR #1](https://github.com/jeffxuu/evidence-insight/pull/1)
was created from **oss/v1.0.0 → main**. It is open and unmerged. No tag or Release was created.
The broader goal remains a portable, installable, maintainable skill with explicit evidence and safety limits.
Behavioral release gates remain open; this is not a benchmark-validated release.

## R04 stop gate (2026-09-15 UTC)

Current phase: clean-room recovery completed; **R04 execution preflight BLOCKED**. No behavioral migration,
security regression, vanilla A/B or holdout run followed it. The earlier recovery sections below are historical.

- **VERIFIED:** PR #1 and remote oss/v1.0.0 both matched the authorized head
  `5085a9504574933d00132cb87a8a4e04311bcee9`; four latest CI runs and all job steps were successful.
  A fresh remote clone checked out that exact head with a clean worktree. The old local checkout was retained.
- **VERIFIED:** A new isolated environment restored the pinned direct dependencies and validator commit.
  Official validation, repository validation and 16 engineering tests passed again, **0 failed**.
  Static migration coverage remains 2,026 nonblank source lines; this is not behavioral equivalence.
  CLI discovery found one skill, installed 12 files, and every installed SHA-256 matched source before and after R04.
- **PARTIALLY VERIFIED:** Repeatability beyond this restoration: direct dependencies are pinned but the repository
  has no complete transitive lock. Actual resolved versions are retained. Existing material/privacy limits remain.
- **UNVERIFIED:** Model-side skill discovery/loading, required-reference reads, effective model/version/effort,
  effective tool availability and trust-boundary behavior. Installation evidence cannot establish model loading.
- **BLOCKED:** R04 started a Codex process at 09:32:47 UTC and timed out at 09:33:47 UTC, normalized exit 124
  (process return code -15). Stdout is empty: zero model/tool/reference events and no final output.
  Stderr contains a new plugin-service 401 warning. Its causal relationship to the stalled model execution is undetermined.

R04 is a run identifier. It uses the existing R03 boundary-evidence fixture, unchanged; it is not a scored R03 run.
The fixture requires evidence-applicability.md; the dual-output task also activates the shared and renderer references.
No injected instruction was supplied; no security pass is claimed. No credentials were inspected or changed.
Runtime, references, adapter, manifest, fixtures, version and repository architecture remain frozen.
Only status documents and execution evidence are changed by this continuation; PR #1 stays draft and unmerged.

See the [R04 verification record](docs/verification.md#r04-clean-room-and-model-preflight-2026-09-15-utc),
[attempt](docs/verification-logs/R04/model/attempt.json) and [observations](docs/verification-logs/R04/observations.json).

## Earlier verified state

- Official Agent Skills validator, public version/adapter synchronization and internal reference integrity passed.
- Migration accounts for **2,026 nonblank source lines**, with unchanged owner-upload snapshots and explicit reference loading conditions.
- **20 synthetic regression fixtures** passed schema/hash checks; **16 engineering tests passed, 0 failed**.
- Source/installed hashes and bundle source hashes agree. Generators reproduce source bytes.
- Both GitHub Actions workflows and every job step succeeded on the initial candidate and documentation commits.
- Remote candidate file installation found one skill, exited 0 and installed 12 byte-identical files into the isolated Codex project.
- Default-main command was actually attempted: exit 1, **No skills found**. Default installation success remains BLOCKED.

These are engineering checks. They do not prove reference loading, migration behavior or injection resistance.
Raw commands, versions, outputs, SHA-256 inventories and limits are linked from [verification](docs/verification.md).

## Source of truth

- Canonical branch: **oss/v1.0.0**, with the current commit identified by Git and PR #1's head.
- Runtime/code commit: **1779c7078360f86f5ac66bd6a98ea691498e82a2**.
- Remote-validation/documentation commit: **6d105f7ba0d0b45722a714e5819183c22a3e2e54**.
- [Migration manifest](docs/migration/manifest.json) and four exact historical source files in docs/migration/internal/.
- Main remains the initialization baseline **451f2271ec3b3dfba9ab665d0de5eb99ca2ccb11**.
- Installed copies and generated bundles are derivatives; the source runtime and recorded hashes govern their identity.

CI evidence for the documentation commit: [validation](https://github.com/jeffxuu/evidence-insight/actions/runs/34765347267)
and [engineering smoke](https://github.com/jeffxuu/evidence-insight/actions/runs/34765347266).
The 2026-09-14 continuation changes only this management file and verification documentation; inspect PR checks for the current head result.

## Recovery changes completed

Restored the isolated verification environment without upgrading locked direct dependencies.
Rebuilt nine stale reference copies whose differences were trailing newlines; runtime rule text was not changed.
Fixed only the candidate installation command: CLI 1.5.26 needs the full slash-containing ref in a quoted fragment,
`'jeffxuu/evidence-insight#oss/v1.0.0'`. The failed tree-URL attempt and successful retry are both retained.

## Continuation recovery (2026-09-14 UTC)

GitHub branch and PR recovery succeeded at head 4186dd0086ba66ca3e001c148a3bb913bac94dd5.
The complete migration manifest was fetched through the GitHub blob API; all 2,026 source-line mappings and
their destination text/loading conditions were checked against 16 fetched files with zero discrepancies.
This closes the earlier manifest-reading gap without modifying the manifest or runtime.

The selected local execution environment remains unavailable and no terminal/model execution tool is exposed.
Local checkout cleanliness, installed copies and the ZIP entity cannot be inspected in this session.
No new environment restoration, model preflight, local test or bundle rebuild is claimed.
The earlier 45-second timeout and 401 remain historical evidence from 2026-09-13.

The verification document now identifies the retained host preflight as R03 by date and input hash.
The earlier qualifier-preservation description was corrected; benchmark status remains BLOCKED.

## In progress / blocked / not executed

| Status | Remaining scope |
| --- | --- |
| BLOCKED | Clean-room engineering recovery succeeded. New R04 model preflight timed out after 60 seconds, exit 124, zero model events; plugin-service 401 observed. Effective model/version remains unobserved. |
| BLOCKED | Internal-to-public migration behavioral comparison; vanilla A/B must follow it. Neither was executed. |
| BLOCKED | Actual paired model demos and evidence of runtime reference reads or injection behavior. |
| UNVERIFIED | Ten complete independently sealed holdout cases. Public blueprints are not unseen inputs. |
| UNVERIFIED | ChatGPT Project upload/retrieval, other hosts, multilingual quality, skills.sh indexing and Star History. |
| PARTIALLY VERIFIED | Material-rights provenance and secrets/privacy assurance beyond the inspected inventory and limited checks. |
| BLOCKED | Successful default-main installation until an owner-approved merge puts the skill on main. |

No benchmark performance number or measured improvement is claimed.

## Frozen decisions

Keep version 1.0.0 and the accepted repository structure. Preserve historical safeguards and all explicitly triggered references.
Do not redesign Research Engine, Qualified Evidence Pool, dual renderers or Social rules.
Only the documented approved conflict fixes and External Content Trust Boundary alter behavior.
Migration line coverage is not behavioral equivalence; engineering smoke is not a substitute for model tests.
Do not merge, tag or create a Release automatically. Keep any further release changes on oss/v1.0.0.

## Next exact action

Resolve the supported Codex host execution/authentication prerequisite without changing runtime or credentials through
this skill. The new plugin-service 401 is diagnostic evidence, not proof of the complete root cause.
After host recovery, obtain explicit authorization for another single traced preflight; do not retry R04 automatically.
Only a passing preflight and the owner's explicit “继续迁移行为回归” authorize the internal/public behavioral migration stage.
No merge, tag, Release, ready-for-review transition, benchmark or holdout execution is authorized by this checkpoint.
