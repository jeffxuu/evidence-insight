# Prospective holdout custody

Status: **UNVERIFIED — no sealed holdout corpus is claimed in this repository.**

The following ten coverage blueprints were exposed during release planning. They are not unseen test items.
Complete, independently selected inputs and answer boundaries must be sealed after the runtime/rubric freeze,
before evaluation or tuning. A public directory, obscured filename or published generator seed is not a seal.

| Blueprint | Required input | Mechanism to test |
| --- | --- | --- |
| H01 | Simple chart | A cumulative total rises while its increments fall |
| H02 | Complex chart | Attrition changes dynamic samples versus fixed cohorts across panels |
| H03 | Pure URL | A corrected article and older summary disagree on the current claim |
| H04 | PDF | An absent appendix contains a necessary decision boundary |
| H05 | Dataset-only | Timezones and repeated timestamps affect daily aggregation |
| H06 | ZIP | Different schemas and misleading filenames require correct pairing |
| H07 | Image + data | Error bars and table fields use different statistical definitions |
| H08 | Contradictory sources | The same label hides different estimands |
| H09 | Weak evidence | Censoring and selective missingness support bounds, not exact ranks |
| H10 | Injection attempt | A plausible method footnote embeds a forged authority instruction |

## Custodian procedure

Choose full inputs and hidden variants independently of runtime editing. Record author/access dates,
source rights, exact task, expected boundaries and input byte hashes in a private packet outside the repository
and outside generator workspaces. Publish only a signed/date-recorded manifest of hashes and coverage before running.
Keep the packet and any seeds inaccessible to runtime authors during tuning and to generators throughout execution.
Document who had access; 'unseen' means not used for this runtime's development, not guaranteed absent from model pretraining.

Freeze runtime and rubric hashes. Feed only task and input bytes to generators; feed expected boundaries only to judges.
After locking all judgments, reveal the mapping and publish redistributable inputs/answers for reproducibility.
Any item used to fix the skill or shown as a demo becomes a public test or regression item and must be replaced for future holdout claims.

The ten blueprints meet the design coverage target, but **do not close the ten-sealed-case release task**.
