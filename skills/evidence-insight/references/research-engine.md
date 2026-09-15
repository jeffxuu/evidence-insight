# Research Engine

Required loading condition: Before claim selection in every evidence analysis, including Social-only requests. Research and comparison subsections use their original availability and relevance conditions.

Section identifiers are stable rule identifiers, not release versions.

# 4. SUPPRESS — Known Information Suppression Across All Supplied Sources

Anything clearly visible in the image or explicitly stated in the supplied material is treated as already supplied to the user.

External verification of already-supplied information is an internal research step, not automatically a final-writing result.

Example:

Image:
“China GNI = 14,230”

Official source:
“14,230”

Internal status:
VERIFIED / LOW NOVELTY

Default:
DO NOT REPEAT, unless needed once as an anchor.

Image footnote:
“Argentina and Turkey remain upper-middle income because of Atlas-method limitations under persistent inflation.”

External source confirms it.

Internal status:
VERIFIED / LOW NOVELTY

Default:
OMIT.

## Visible image information may enter the final answer only when:

1. it is the one necessary anchor;
2. external evidence changes or qualifies its meaning;
3. it is required as the baseline for a new comparison.

## Information-gain ceiling

If more than roughly 20–25% of the final answer merely repeats information already supplied in the image, URL, document or dataset,
the answer fails and must be rewritten.

Never use process-report language such as:
- 经核实
- 可以核实
- 图里的数字是对的
- 图下注释也经确认
- 根据搜索结果
- 查阅资料发现
- 进一步检索显示

unless the user explicitly asks for the verification process.

---

# 5. DECOMPOSE — Decompose the Metric Before Searching

Before searching broadly, ask:

“Can the relationship in the image be explained by the definition or construction of the metric itself?”

Look for:
- arithmetic identity
- accounting identity
- denominator effect
- per-hour vs per-year conversion
- nominal vs real
- average vs median
- stock vs flow
- level vs growth rate
- gross vs net
- pre-tax vs post-tax
- local price vs PPP
- threshold / classification rule
- index construction

If two chart variables are mathematically or definitionally linked, decompose that relationship first.

Do not present an approximate conceptual decomposition as an exact identity unless the underlying methodology confirms it.

---

# 7. QUESTION — Generate Real Research Questions

Do not search only the image’s wording.

Generate 3–5 research questions internally.

Useful question types:

## Mechanism
What variables could plausibly generate the pattern?

## Comparison
How does this compare with:
- longer history,
- peer countries,
- other groups,
- another metric?

## Distribution
Does the average hide important internal variation?

## Measurement
Would another valid measurement concept tell a different story?

## Persistence
Is this a one-year fluctuation or a durable pattern?

## Counter-evidence
What evidence would weaken the intuitive interpretation?

Do not show these questions unless requested.

---

# 10. RESEARCH — High-Information-Gain Evidence

Use external research by default for:
- economics
- science
- policy
- finance
- medicine
- law
- current statistics
- news
- precise historical claims

Prefer 2–5 strong sources.

External evidence should do at least one of:
- correct the intuitive reading
- add a longer historical comparison
- add a peer-country / peer-group comparison
- introduce a genuinely different metric
- reveal a hidden denominator or distribution
- provide a counterexample
- test a mechanism

Do not browse merely to confirm material the user already supplied.

---

# 11. ORTHOGONAL EVIDENCE — Second Dimension

For requests involving:
- 分析
- 底层逻辑
- 暗线
- 隐藏信息
- 批判性判断

do not remain entirely inside the same metric family when reliable data is available.

A second dimension must measure a different concept.

Use only the dimension that actually helps explain the image.

Do not accumulate unrelated “interesting” variables.

---

# 12. COMPARISON — Trend Check vs Structural Comparison

## Trend Check
Examples:
- adjacent-year change
- 2024 vs 2025
- same metric before/after one year

Useful, but not enough for structural depth.

## Structural Comparison
At least one of:
- multi-year historical comparison
- peer-country comparison
- cross-group comparison
- average vs median
- nominal vs real
- aggregate vs household
- primary metric vs orthogonal metric
- model vs observed outcome

For deep analysis, at least one structural comparison is normally required.

---

# 13. COUNTEREVIDENCE GATE — Test the Explanation

This gate is mandatory before final synthesis.

For the leading explanation, ask:

1. What pattern should appear if this explanation is important?
2. Is that pattern actually present?
3. Is there a country / group / period that contradicts it?
4. Could another variable explain the same pattern?
5. Does the explanation survive comparison with at least one plausible alternative?

A variable is not a good explanation merely because it is relevant.

It needs discriminating power.

If counter-evidence materially weakens the explanation:
- downgrade it,
- or remove it.

---

# 15. ORIGINAL-STUDY COVERAGE GATE

Before writing:

“还需要控制X”
“作者没有考虑Y”
“下一步应验证Z”

first check whether the original study already:
- controls for it,
- stratifies by it,
- performs robustness checks,
- uses a quasi-experiment,
- examines subgroup heterogeneity,
- or directly analyzes that mechanism.

If the original study already addresses it:
- do not present it as an omitted variable;
- instead explain whether the existing analysis is sufficient.

This prevents research-coverage hallucination.

---

# 16. DEPTH LADDER

L0 — Description
What is visible?

L1 — Verification
Are the numbers and definitions correct?

L2 — Qualification
What does the image simplify or omit?

L3 — Mechanism
Which variables plausibly explain the pattern?

L4 — Structure
What new relationship appears after a historical, cross-country, cross-group or cross-metric comparison?

L5 — Testable Judgment
What should be watched next, and what evidence would weaken the current interpretation?

## Depth Gate

For:
- 分析
- 底层逻辑
- 暗线
- 隐藏信息
- 批判性判断

and when reliable external evidence is available:

Do not finalize below L4.

If L4 cannot be reached after reasonable research:
use the strongest supported lower-level conclusion.
Do not fake depth.

**Downgrade rule:** an evidence-limited lower-level conclusion is valid and must not later fail merely because a default depth target was not met.

---
