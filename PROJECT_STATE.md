# Evidence Insight project state

Updated: 2026-09-13 UTC. Public version: **1.0.0**.

## Goal and frozen scope

Prepare the portable skill and reviewable oss/v1.0.0 → main PR. No automatic merge, tag or Release.
Preserve historical failure safeguards. Only the approved conflict fixes, public packaging and external-content trust boundary are authorized.
The runtime never loads this project-management file.

## Current phase

Local engineering verification complete; preparing the first release-content commit on oss/v1.0.0.
The main branch must remain at initialization commit 451f2271ec3b3dfba9ab665d0de5eb99ca2ccb11.

## Verified evidence

See [verification](docs/verification.md) and its raw logs. Official spec validation, public version synchronization,
reference integrity, 2,026 nonblank source-line coverage, 20 fixture schemas/hashes and 16 engineering tests passed.
Installed file hashes and bundle source hashes match the canonical runtime. Generators reproduce source bytes.
This is engineering evidence, not model behavioral equivalence.

## Remaining work and blockers

- Commit/push candidate, inspect actual remote CI, test candidate and default-branch installation separately, create PR.
- Model host: BLOCKED; 45-second preflight timed out with plugin-service 401 and no model events.
- Migration behavior, vanilla A/B and real paired demos: BLOCKED / not executed.
- Ten independent sealed holdout cases: UNVERIFIED; public blueprints only.
- Rights provenance and comprehensive privacy assurance: PARTIALLY VERIFIED.
- Default-branch installation: blocked until the owner merges release content.

## Source of truth

Canonical public files on oss/v1.0.0, [migration manifest](docs/migration/manifest.json),
and four unchanged owner-supplied snapshots in docs/migration/internal/.
Generated packages and installed copies are derivatives identified by the SHA-256 inventory.

## Next exact action

Publish the verified candidate to oss/v1.0.0, then check remote workflows and installation before opening the PR.
