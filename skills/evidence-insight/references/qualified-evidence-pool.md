# Qualified Evidence Pool

Required loading condition: Before either renderer selects evidence, including when only one output is requested.

Section identifiers are stable rule identifiers, not release versions.

# 6. Claim Ledger — Confidence + Novelty

Create an internal ledger of 3–8 important claims.

Each claim gets:

## Confidence
- HIGH
- MEDIUM
- LOW

## Novelty
- HIGH
- MEDIUM
- LOW

## Source Type
- IMAGE
- PRIMARY_SOURCE
- OFFICIAL_DATA
- RESEARCH_SOURCE
- HIGH_QUALITY_SECONDARY
- LOW_QUALITY_SECONDARY
- UNVERIFIED

Final-output priority:
HIGH CONFIDENCE + HIGH NOVELTY.

Do not spend valuable writing space on:
HIGH CONFIDENCE + LOW NOVELTY
unless it is the necessary opening anchor.

---

# 17. EDITORIAL FILTER — Only Keep What Explains the Image

Research may produce many useful facts.
The final answer must not include all of them.

Score each candidate fact internally on:

## Confidence
How reliable is it?

## Novelty
Does the image already tell the user this?

## Relevance
Does it directly bear on the question?

## Explanatory Power
How much does it explain the pattern in the image?

Conceptually:

Final Value
≈ Confidence × Novelty × Relevance × Explanatory Power

No exact arithmetic is required.

## Editorial priority

Keep:
- one image anchor
- one or two external facts with high explanatory power
- one structural comparison
- one main interpretation
- one testable judgment

Cut:
- facts that are merely interesting
- extra country examples
- methodological history that does not change interpretation
- side issues that do not explain the image

Research broadly.
Write narrowly.

## 17.0 Multi-Source Evidence Roles

Claims entering the Qualified Evidence Pool should preserve provenance at source-role level.

Examples:
- IMAGE_OBSERVED
- DATA_DIRECT
- DATA_DERIVED
- METADATA_DEFINITION
- PRIMARY_RESEARCH
- OFFICIAL_CONTEXT
- HIGH_QUALITY_SECONDARY

A derived calculation from an attached dataset should not be mislabeled as a direct source value.

A chart observation should not be promoted into a precise numeric claim when the underlying data disagree.

A methodology note may define a variable without independently supporting the empirical result.

The purpose is claim/source alignment, not building a visible schema.

## 17.1 QUALIFIED EVIDENCE POOL — Shared Evidence, Separate Selection

The research pipeline produces one internal **Qualified Evidence Pool**.

A claim may enter this pool only after it passes the applicable:
- source-quality / source-proximity checks;
- evidence-applicability checks;
- causal-boundary checks;
- counterevidence / original-study coverage checks when relevant.

The pool is broader than either final output.

**Important distinction:**
- “Qualified for use” is not the same as “selected for Output A”.
- A qualified claim that is not used in the analytical paragraph remains available to Output B.
- Output B therefore does not need to copy Output A’s evidence selection.
- Output B still may not introduce any fact, mechanism or inference that is outside the Qualified Evidence Pool.

For each key claim retained in the pool, preserve the minimum semantic payload:
- Claim — what can be said;
- Source / provenance — what supports it;
- Scope — population, geography, period, denominator or metric;
- Status — observed fact, estimate, model, association, causal result, or inference;
- Mandatory qualifier — wording that cannot be dropped without changing meaning;
- Applicability — what proposition this evidence can and cannot support.

Do not turn this into a visible table unless the user asks.
Do not add numeric scores or a new database schema.

## 17.2 OUTPUT-SPECIFIC SELECTION

After the Qualified Evidence Pool is established:

- **Analysis Selector** chooses the evidence needed to explain the result rigorously.
- **Social Selector** chooses the evidence needed to support one worthwhile, image-linked judgment.

The two selectors may choose:
- the same central claim;
- overlapping evidence;
- or different qualified supporting facts.

They are not required to produce different “discoveries”.

The Editorial Filter applies to each output's final selection.
It must not delete otherwise-qualified evidence from the shared pool merely because Output A did not use it.

---
