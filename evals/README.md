# Evaluation

Rubric and protocol version: **1.0.0**.

Benchmark methodology available. Results pending.

This repository contains deterministic engineering tests and public synthetic regression fixtures.
No model failure rate, improvement percentage or social preference has been measured here yet.
Case files marked `not_run` describe tests, not successful executions.

- [Rubric](rubric.md): eight hard failures and seven anchored quality dimensions.
- [Protocol](protocol.md): migration comparison first, then vanilla A/B; same settings, three runs and blind judging.
- [Schema](schema.json): separate case, actual run and judgment contracts.
- [Regression](regression/): 15 reconstructed historical failure types and five security/metadata cases.
- [Holdout](holdout/README.md): prospective custody and contamination policy.
- [Results](results/README.md): no benchmark observations are currently published.

## Reproduce engineering checks

From the repository root, in a Python 3.12 virtual environment:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests -v
```

These checks validate file/accounting invariants, data arithmetic, packaging, blinded-pair construction
and scoring mechanics. They do not execute an LLM or prove that injection defenses work.

## Produce actual evaluation records

Use a clean host session per case/arm/run. Follow the protocol's isolation instructions.
The generator gets only the user prompt and the files listed under `inputs`; the case JSON,
expected boundaries, rubric, other runs and judge instructions are kept out of its workspace.
Copy each input byte-for-byte, verify its SHA-256, and capture actual output and tool events.
The `actual` field is an attestation by the recorder, not cryptographic proof of execution.
Attach auditable execution evidence; schema validity alone cannot establish provenance.

Store run JSONL outside the checked-in result directory until privacy and provenance review.
The run schema requires model, version if exposed, reasoning effort, date, host, tools, budget,
input/runtime hashes, run count, rubric and completion status. Preserve errors and timeouts.
Keep optional model API credentials in the host's secret facility, never in fixtures or results.

For a complete paired run file, create blind packets and put the mapping in a separate private directory:

```bash
python scripts/prepare_blind_eval.py --runs actual-runs.jsonl --packets judge/packets.jsonl --mapping private/mapping.private.json
python scripts/score_eval.py --runs actual-runs.jsonl --judgments adjudicated.jsonl
python scripts/build_report.py --runs actual-runs.jsonl --judgments adjudicated.jsonl
```

The filenames in these commands are operator-created execution records, not bundled example results.
`score_eval.py` aggregates judgments; it does not decide whether a claim is true.
`build_report.py` emits Markdown to stdout; save it only after reviewing the underlying actual records.
After preferences are locked, both tools accept `--preferences preferences.jsonl --mapping private/mapping.private.json`.
The optional preference schema records A/B/Tie/Neither; the custodian resolves randomized labels to actual arms only after judging.
Before publication, verify all declared runs exist, both arms have matching settings and counts,
the required migration comparison preceded A/B, and holdout custody was preserved.

Unit-test doubles exist only inside `tests/` and are never benchmark observations.
