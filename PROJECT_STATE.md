# Evidence Insight project state

Updated: 2026-09-13 UTC. Public version: **1.0.0**.
This management document is not a runtime dependency.

## Current goal and phase

This implementation phase reached its authorized stop: [Draft PR #1](https://github.com/jeffxuu/evidence-insight/pull/1)
was created from **oss/v1.0.0 → main**. It is open and unmerged. No tag or Release was created.
The broader goal remains a portable, installable, maintainable skill with explicit evidence and safety limits.
Behavioral release gates remain open; this is not a benchmark-validated release.

## Last verified state

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
This post-PR state update changes only this management file; inspect PR checks for its own head result.

## Recovery changes completed

Restored the isolated verification environment without upgrading locked direct dependencies.
Rebuilt nine stale reference copies whose differences were trailing newlines; runtime rule text was not changed.
Fixed only the candidate installation command: CLI 1.5.26 needs the full slash-containing ref in a quoted fragment,
`'jeffxuu/evidence-insight#oss/v1.0.0'`. The failed tree-URL attempt and successful retry are both retained.

## In progress / blocked / not executed

| Status | Remaining scope |
| --- | --- |
| BLOCKED | Model-host preflight: timeout after 45 seconds, exit 124, zero model events, plugin-service 401. Effective model/version is unobserved. |
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

Review Draft PR #1 and resolve a working independent model host before running the protocol's internal/public
migration regression. Retain the frozen runtime and original cases; only after that gate may vanilla A/B proceed.
Independent holdout custody and real paired demos remain separate required work.
