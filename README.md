# Evidence Insight

**Evidence-checked analysis for charts, URLs, papers, datasets and archives — plus publish-ready social insight.**

A portable evidence-synthesis layer for capable tool-using AI agents.
It guides an agent from supplied material to bounded analysis and one evidence-backed social thesis,
with checks for source applicability, causality, missing qualifiers and assistant language leaking into the final caption.

[简体中文](README.zh-CN.md) · [Install](docs/installation.md) · [Evaluation](evals/README.md) · [Verification status](docs/verification.md)

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)
[![Validate skill](https://github.com/jeffxuu/evidence-insight/actions/workflows/validate-skill.yml/badge.svg?branch=oss%2Fv1.0.0)](https://github.com/jeffxuu/evidence-insight/actions/workflows/validate-skill.yml)

**v1.0.0 release preparation. Benchmark methodology available. Results pending.**

## Before / after: the boundary being tested

The examples below explain evaluation targets. They are **not measured vanilla-versus-skill model outputs**.
Actual paired demos are pending a working generator host and blind review.

| Failure to catch | Evidence Insight's required boundary |
| --- | --- |
| A study in another population is treated as a refutation | Match population, variable, outcome, period and design before classifying evidence |
| “May decline under this scenario” becomes “will disappear” in a caption | Keep scenario, uncertainty, degree and model status through compression |
| A correlation becomes a confident cause | Separate association from identified causal effects and compare plausible explanations |
| A chart, table and README are used interchangeably | Assign exact values, definitions, provenance and visual framing to their appropriate sources |
| Accurate Social text reads as a research memo or ends with an assistant offer | Express one author-owned judgment inside a closed publishing artifact |

## Quick install

Requires Node.js/npm, a compatible skill host and access to the repository.

**Default-branch installation: BLOCKED / pending merge.** The command was tested and found no skills on main.

```bash
npx skills add jeffxuu/evidence-insight --skill evidence-insight
```

For the proposed release, see [candidate installation and verification](docs/installation.md).
Local and remote candidate file installation with `skills@1.5.26` were verified. This does not establish model execution or default-branch installation.

Verified candidate command:

```bash
npx --yes skills@1.5.26 add 'jeffxuu/evidence-insight#oss/v1.0.0' --skill evidence-insight -a codex --copy -y
```

After installing in a capable host, supply a chart, URL or data file and ask:

> Analyze this evidence. Keep uncertainty and causal limits. Give me analysis and one publish-ready social insight.

Use “analysis only” or “social only” to select one output. The inherited default style and character bands target Chinese.
The optional [ChatGPT Project adapter](adapters/chatgpt-project-instructions.txt) has the same public version, **1.0.0**.

## Why Evidence Insight

Good source retrieval does not automatically produce an applicable conclusion. A correct number can be attached
to the wrong population, a method caveat can be called a contradiction, and a shorter caption can quietly become
more certain than the evidence. This skill makes those boundaries explicit at intake, selection, rendering and revision.

It provides procedural guidance, not its own search service, data access, model or execution sandbox.

## Core capabilities

- Multi-source intake and source-role assignment, including archive and version conflicts.
- Known-information suppression and metric decomposition before broad research.
- Source quality, original-source proximity, applicability and original-study coverage checks.
- Competing explanations and evidence-limited fallback without manufactured depth.
- One Qualified Evidence Pool with separate Analysis and Social selection.
- Qualifier propagation, semantic-strength preservation and bounded style edits.
- One-thesis Social writing with authorial ownership, adaptive length and an artifact boundary.

## Supported inputs

Charts and screenshots; webpages and URLs; PDFs and papers; CSV, TSV, JSON and XLSX;
ZIP archives; and mixed evidence. Actual reading, vision, browsing and calculation depend on the host's tools.
An unreadable input must be reported as unreadable. The skill does not bypass paywalls or permission controls.

## Architecture

The [entrypoint](skills/evidence-insight/SKILL.md) gives the workflow, hard boundaries and explicit reference-loading conditions.
Detailed rules live in ten references inside the installable skill. Research produces one qualified evidence pool;
two selectors draw from it for Analysis and Social. Social does not start a second research pass.
Migration accounting and tests stay outside the installed runtime.

## Examples

[Chart analysis](examples/chart-analysis/README.md) · [URL research](examples/url-research/README.md) ·
[Dataset analysis](examples/dataset-analysis/README.md) · [Mixed sources](examples/mixed-source/README.md) ·
[Social output](examples/social-output/README.md)

These pages contain synthetic inputs and expected boundaries. Actual paired outputs remain pending.
No copyrighted media screenshot or paywalled infographic is bundled.

## Benchmark

**Benchmark methodology available. Results pending.**

[Rubric](evals/rubric.md): pass/fail hard failures, anchored 0–4 quality ratings, and separate A/B/Tie/Neither social preference.
[Protocol](evals/protocol.md): migration comparison before vanilla A/B; same model/settings/tools/input/count;
three runs per case/arm; randomized blinded judging with human review and an optional independent model judge.

Deterministic CI tests packaging and evaluation mechanics. It does not establish fewer hallucinations or injection resistance.
There is no measured improvement, preference percentage, token saving or latency claim.

## Compatibility

| Environment | Format / installation | Behavioral verification |
| --- | --- | --- |
| Agent Skills format | Official validator passed | Format compliance alone is not behavior |
| Codex | Local and remote candidate file installation verified | BLOCKED: model-host authentication/initialization unavailable in the test environment |
| Other Agent Skills hosts | UNVERIFIED for this project | UNVERIFIED |
| ChatGPT Projects | Adapter and generated bundle structurally checked | Manual upload/loading UNVERIFIED |

## Security

External text, screenshots, metadata and archive READMEs are untrusted evidence, not runtime instructions.
They cannot authorize secrets access, uploads, commands, repository edits, installation or tool calls.
Legitimate data definitions remain usable. See [SECURITY.md](SECURITY.md).
Instruction-level safeguards are not an execution sandbox or a security guarantee.

## Limitations

Behavior varies with the model and tools. Cross-host and multilingual quality have not been established.
The release preserves detailed historical safeguards; it does not claim measured token savings from file splitting.
The ten holdout blueprints are public designs, **not a sealed unseen test set**.
Full behavior validation and real before/after demos remain release follow-up work.

## Contributing

The most useful contribution is: input → current output → observed failure → expected boundary → proposed regression.
Read [CONTRIBUTING.md](CONTRIBUTING.md), include source rights and redact private information.

## Star History

**UNVERIFIED / pending.** No history chart is displayed until this repository's dynamic chart is verified.
No static growth image is used. Directory visibility on skills.sh is also **UNVERIFIED**;
ecosystem compatibility does not mean an indexed listing or ranking has been confirmed.

## License

[Apache License 2.0](LICENSE). Separately sourced materials retain their own license and attribution requirements.
See [materials review](docs/materials.md).
