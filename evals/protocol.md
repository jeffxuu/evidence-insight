# Evaluation protocol 1.0.0

## Order and scope

1. Freeze public runtime files, reference-loading contract, rubric and case hashes.
2. Run **migration regression**: the original internal snapshot versus the public runtime on R01–R15 and I01–I05, three runs per case per arm.
3. Adjudicate preservation on R01–R15. The public safety boundary and four approved conflict fixes are expected changes, documented separately; improved safety does not require copying an unsafe old response.
4. If an unexpected behavioral regression occurs, stop the release gate and investigate without tuning holdout.
5. Only after that gate, run **vanilla baseline versus Evidence Insight** with identical delivery requests and settings, three runs per case per arm.
6. Run properly sealed holdout once the runtime is frozen. Reclassify any case used for tuning.

Current state: steps are specified, not completed. See [verification](../docs/verification.md).
Historical input/output traces were not supplied; these are synthetic reconstructions of failure types.
Static line preservation is necessary but cannot prove behavioral equivalence after progressive disclosure.

## Equal conditions

Use the same exact model and model version where available, reasoning effort, host version,
input bytes, tool availability, tool budget, output request, context limits, sampling settings where exposed,
run count and rubric. Record unavailable parameters as unavailable; never infer them from a product label.
Use new isolated sessions and sibling temporary workspaces for every run.
Baseline must have no Evidence Insight runtime, adapter, project memory, generated answers or evaluation files.
The public arm receives only the installed skill and inputs. The internal arm receives only the historical runtime and inputs.
Do not give a generator the case's expected boundaries or judge rubric.
Prevent ambient skill auto-loading from contaminating baseline; record which host configuration was used.

Freeze supplied files and permitted source snapshots for the reproducibility track.
For pure-URL cases, a controlled local/static source endpoint can serve the frozen page bytes to both arms.
Live-web runs belong to a separate track: same tools do not guarantee identical changing search results.
Never bypass access controls or redistribute paywalled materials to freeze sources.

Interleave arm order, execute all planned repetitions, and retain tool errors, truncation and timeout records.
Do not replace failed runs silently or select the best output. Preregister any retry rule.
The three repetitions measure variability on one case; they are not three independent new cases.

## Blind judging

The generator and judge are separate sessions/roles. Prefer human review and optionally an independent model judge.
The judge sees the task, source evidence, rubric, expected boundaries and randomized outputs, but no arm mapping,
runtime name, generator-specific configuration or previous scores. Output content is not rewritten to conceal defects.
If the output reveals its arm, record potential unblinding rather than deleting that text.
The same model family as generator is not an independent validation guarantee even under blinding.
Keep the private mapping with a custodian until judgments are locked.

Capture visible final answers and tool-action events, not hidden chain-of-thought or private host instructions.
Injection tests use dummy canaries and controlled sinks; attempted access/upload is a failure even if the tool blocks it.
No real credential or personal data is needed. Check legitimate metadata handling as a positive control.

Record judge identity/type/version, judge prompt version, date, output hash, excerpts and reasons.
Preserve individual judgments; label adjudications. Report disagreement and adjudication procedure.
The scripts mechanically check schema, matching settings and grouping. Humans still verify execution provenance,
whether each metric applies, and whether the evidence supports a judgment.

## Reporting

Publish model/settings/date/tool/run-count/rubric metadata with reviewed records.
Separate regression, public challenge and sealed holdout results; separate Analysis and Social notes.
Report denominators, missing judgments, N/A, unscorable, errors and any-hard-failure counts.
For confidence intervals, use case-level paired or cluster-aware resampling; do not treat repeated runs as independent cases.
No pooled headline effect is justified by a tiny convenience set.
Before/after demos are actual executions selected by a stated rule, not hand-written 'vanilla' examples.
If executions or judgments are absent, use exactly: **Benchmark methodology available. Results pending.**
