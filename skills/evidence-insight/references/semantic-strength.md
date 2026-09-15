# Semantic Strength

Required loading condition: Before either renderer uses a claim and after any compression or style rewrite.

Section identifiers are stable rule identifiers, not release versions.

## 26.1 Mandatory Qualifier Propagation

When either renderer uses a qualified claim, it must inherit any qualifier whose removal would materially change meaning.

Examples include:
- year / reporting period;
- population / geography / sample;
- nominal vs real / PPP / market exchange rate;
- average vs median;
- model estimate vs observed result;
- association vs causal effect;
- uncertainty range / scenario dependence;
- data-revision or source-coverage limitation.

Compression may remove wording only when the remaining sentence preserves the same semantic strength.

A social caption may be shorter than the analysis, but it may not make a claim broader, more certain or more causal than the Qualified Evidence Pool permits.

## 27.4 Semantic Strength Lock

Before and after de-AI rewriting, compare every claim.

The rewrite MUST NOT strengthen:
- 可能 → 一定
- 相关 → 导致
- 减少 → 消失
- 边界证据 → 反证
- 方法学风险 → 结论错误
- 模型估计 → 历史事实

If the social version is shorter, it may remove caveats only when the remaining statement is still accurate.
It may not silently upgrade certainty.

---
