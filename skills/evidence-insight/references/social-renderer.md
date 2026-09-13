# Social Renderer

Required loading condition: Whenever Output B is requested or included by default; read before thesis selection, then apply composition and final-audit sections.

Section identifiers are stable rule identifiers, not release versions.

# 25A. RENDERER ROLE CONTRACT — Conversation vs Publishable Artifact

The two outputs are different object types, not merely different writing styles.

## Output A speaker role

**Assistant → User**

Output A is a research deliverable inside the conversation.

It may:
- explain;
- qualify;
- compare;
- point out uncertainty;
- discuss what still needs verification;
- mention methodological limitations.

It should still avoid unnecessary meta-process language.

## Output B speaker role

**Author / User → Public Audience**

Output B is a closed, publishable artifact.

It must read as if the user is posting it directly to:
-朋友圈;
- X;
- 小红书;
- or another public social platform.

The Assistant must not appear as a speaker inside Output B.

---

# 25B. ARTIFACT PURITY CONTRACT — Output B Is Closed Content

Output B may contain only publishable content belonging to the caption itself.

Allowed:
- evidence-backed statements;
- necessary image / source anchors;
- one clear thesis;
- necessary qualifiers;
- a supported consequence or hidden-line variable;
- natural rhetorical phrasing suitable for public posting.

Forbidden inside Output B:
- offers to help;
- service suggestions;
- automation proposals;
- reminder / monitoring offers;
- tool suggestions;
- questions about whether the user wants more work;
- implementation notes;
- version or Skill references;
- internal audit status;
- workflow explanations;
- assistant capability statements.

Examples that MUST NOT appear inside Output B:

- “如果你愿意，我可以继续帮你……”
- “我可以帮你设一个跟踪……”
- “需要的话我可以监控这些指标……”
- “要不要我继续查……”
- “我还能帮你整理……”
- “本次按项目规则执行……”
- “已通过语义审计……”
- “根据我的搜索……”

These are Assistant→User conversation acts, not social-caption content.

---

# 25C. CONTENT SO-WHAT vs ASSISTANT ACTION

Do not confuse a content consequence with an assistant action.

## Valid Content So-What

Examples:
- “接下来更值得观察的是家庭股票敞口和政府利息负担是否继续同步上升。”
- “如果这一趋势持续，下一轮衰退时家庭资产和财政缓冲可能同时承压。”

These statements belong to the topic.

## Invalid Assistant Action

Examples:
- “如果你愿意，我可以帮你持续跟踪这两个指标。”
- “数据更新后我可以提醒你。”
- “我可以给你设置一个自动监控。”

These statements describe what ChatGPT can do and must remain outside Output B.

A supported future variable may enter the caption.
An offer to monitor that variable may not.

---

# 25D. DELIVERABLE CLOSURE

Once Output B is complete, the Social Renderer is CLOSED.

After the final sentence of Output B:

- do not append an assistant offer;
- do not append a question;
- do not append a monitoring suggestion;
- do not append a reminder suggestion;
- do not append “如果你愿意……”;
- do not append a version note;
- do not append any conversational follow-up by default.

If the user later asks for:
- tracking;
- reminders;
- continued research;
- a different platform version;
- another rewrite,

handle that in the next conversational turn.

If a follow-up is exceptionally necessary in the same response, it must be clearly outside the Social artifact and must never be merged into 【配图文案】.

Default for Evidence Insight:
**finish the requested deliverables and stop.**

# 25E. AUTHORIAL STANCE CONTRACT — The Caption Must Belong to Someone

Output B should not read like a neutral third-party research note.

Its speaker role is:

**Author / User → Public Audience**

The caption should communicate an evidence-backed judgment the author is willing to stand behind.

Authorial stance does NOT require first person.

Strong stance can be written with or without “我”.

Examples:

Weak / neutral:
- “中国持有美债规模同比下降。”
- “外国官方机构持仓有所下降。”

Stronger authorial stance:
- “单看中国减持，已经不足以判断海外资金是否在撤离美债。”
- “比中国减持多少更重要的，是谁正在接替官方储备成为边际买家。”

The point is not to sound opinionated for its own sake.
The point is to make the selected interpretation explicit.

Do not force:
- “我认为”
- “我觉得”
- “我更关注”
- “我第一反应”
into every caption.

First person is optional.
Authorial ownership is required.

---

# 25F. OPENING THESIS RULE — Give the Reader a Reason to Continue

The first 1–2 sentences should reveal the main interpretive payoff as early as practical.

Useful openings usually do one of three things:

## Conclusion conflict
Correct a tempting but unsupported interpretation.

Example:
“China is cutting Treasury holdings, but that still does not show that foreign capital is broadly exiting U.S. debt.”

## Cognitive reframing
Shift attention to the more informative variable.

Example:
“More important than how much China cut is who is replacing official reserve buyers.”

## Structural tension
Put two simultaneously true facts next to each other.

Example:
“Foreign official holdings fell while foreign private holdings rose.”

Do not open with generic background merely because background is true.

Do not use clickbait phrases such as:
- “震惊的是”
- “真正的真相”
- “细思极恐”
- “最可怕的是”

The hook must come from the evidence-backed thesis itself.

---

# 25G. AUTHORIAL OWNERSHIP TEST — A Stance, Not a News Summary

After drafting, ask internally:

> “What does this author want the reader to believe, notice, or reconsider?”

If the answer is only:
- a number changed;
- a ranking moved;
- a chart went up or down;

the caption is still too neutral.

A good answer should name a judgment such as:
- what the common interpretation misses;
- which variable matters more;
- what relationship changes the reading;
- what uncertainty prevents a stronger conclusion;
- what structural consequence follows.

Do not mechanically remove all numbers to run this test.

Some strong theses are quantitative.

The test checks whether the caption has a point of view, not whether it can survive without evidence.

---

# 25H. EVIDENCE ARC — Support the Stance Without Rebuilding the Analysis

After the opening thesis, select the smallest set of evidence needed for the reader to follow the judgment.

The evidence arc should usually contain:
- 1–3 indispensable facts, comparisons or trends;
- the minimum necessary qualifier;
- only the mechanism directly relevant to the thesis.

Do not re-import:
- every important fact from Output A;
- all alternative explanations;
- all source caveats;
- every historical comparison.

Those belong in Analysis unless they are necessary to preserve the Social thesis.

Longer Social length exists to preserve one thesis more faithfully, not to create a second mini-report.

---

# 25I. IMPLICATION, NOT SUMMARY — End by Moving the Thought Forward

The ending should not merely repeat the opening.

Prefer a supported implication:

- what this changes in how the issue should be read;
- what variable becomes more important;
- what risk or constraint becomes visible;
- what next observation would meaningfully update the thesis.

Examples:
- “The question is shifting from how much foreign capital holds Treasuries to what kind of capital now absorbs new issuance.”
- “If the buyer mix keeps changing, future demand may become more sensitive to yields and market conditions.”

Do not add an implication merely to sound profound.

If the evidence supports no useful implication, end after the evidence arc.

Do not force:
- a metaphor;
- a prediction;
- a policy conclusion;
- a grand historical analogy;
- a moral.

The Social ending should advance the thesis, not restate it.

# 26. DUAL OUTPUT RENDERER — Analysis + Social Caption

After the research, counter-evidence, source filtering and evidence qualification are complete,
render two outputs from the SAME Qualified Evidence Pool using separate output-specific selection.

The research pipeline must run only once.

The social-media output must NOT trigger a second research process and must not introduce
facts, numbers, mechanisms or conclusions that are absent from the vetted evidence packet.

## Output B — Social-Media Caption

Purpose:
Create a **closed publishable artifact** that the user can copy from the first character to the last and post directly with the supplied evidence.

Speaker role:
**Author / User → Public Audience**

Editorial objective:
**do not merely summarize the evidence; form one evidence-backed judgment the author is willing to publish under their own name.**

This is NOT a summary of Output A.
This is NOT Assistant→User conversation.
This is NOT a neutral third-party research note.

Before drafting Output B, run the SOCIAL THESIS ENGINE.

It should select the single most interesting, defensible insight from the Qualified Evidence Pool
and express it naturally for a general reader.

Length policy:
- Use the adaptive semantic-load policy in §32.
- User-specified length overrides all defaults.
- Never distort the thesis or drop mandatory qualifiers merely to fit a range.

### Evidence Boundary

Output B may only use:
- facts present in the supplied evidence;
- facts already verified during the 1.0.0 research pipeline;
- interpretations that survived the counter-evidence, applicability, coverage and editorial gates.

Output B must not:
- add a new statistic;
- add a new historical claim;
- add a new causal explanation;
- strengthen uncertainty;
- turn correlation into causation;
- introduce an unsupported “deep meaning”.

If Output A says “可能”, Output B cannot silently change it into certainty.

### Artifact Boundary

Output B must contain only content suitable for direct publication.

Do not include:
- “如果你愿意，我可以……”
- monitoring / reminder offers;
- tool or workflow offers;
- follow-up questions to the user;
- capability statements;
- version / Skill / Project metadata.

A topic-level “what to watch next” may be part of the caption.
An Assistant-level offer to watch it for the user may not.


### Evidence / Source Linkage

The caption must depend on the supplied evidence; when an image is supplied, preserve its specific visual linkage.

Prefer one or two natural visual anchors:
- ranking reversal;
- turning point;
- slope difference;
- historical change;
- contrast between panels;
- a distinctive number when necessary.

Do not mechanically describe the chart.

Do not write generic philosophy that could accompany unrelated images.

Run the test:

“If the supplied evidence were replaced with a random chart, would this paragraph still work?”

If yes, rewrite.

### Social Writing Style

Write like someone who has read the chart, checked the evidence,
and is sharing one observation worth discussing.

Prefer:
- concrete relationships;
- natural sentence rhythm;
- one central thought;
- a little unresolved tension.

Avoid:
- research-report tone;
- teaching tone;
- source-verification language;
- explanatory completeness;
- excessive qualifications;
- methodology details unless indispensable.

Do not write:
- 经核实
- 数据显示
- 根据研究
- 从图中可以发现
- 这张图告诉我们
- 真正值得关注的是
- 本质上
- 不是……而是……
- 这揭示了
- 这提醒我们
- 值得深思

unless genuinely unavoidable.

### Information Budget for Output B

Use only the material required by the selected thesis.

Do not allocate space by fixed percentages.

A longer caption may keep more evidence or qualification, but it must still revolve around one thesis rather than recreating the entire analysis.

### Citations

By default, do not place formal inline citations inside Output B,
because it should be ready for direct social posting.

All factual content must still come from the vetted evidence packet.

If the user explicitly asks for:
- 带来源
- 适合X并附来源
- 文末加出处

then add a concise source reference after the paragraph.

### Final Social Caption Audit

Before returning Output B, check:

1. Does it clearly belong with this exact supplied evidence?
2. Does it contain only vetted claims?
3. Is there only one main idea?
4. Did it avoid turning caveats into certainty?
5. Does it sound like natural social writing rather than an AI summary?
6. Is every sentence part of the publishable artifact itself?
7. Did any Assistant→User service language leak into the caption?
8. Is there any “如果你愿意，我可以…… / 要不要我…… / 我可以帮你跟踪……” language?
9. Could any sentence be removed without losing the central thought?
   If yes, remove it.

If items 6–8 fail:
remove the leaked conversational content completely.
Do not move it to another sentence inside Output B.

### User Overrides

“只要分析”
→ return Output A only.

“只要配图文案”
→ still run the full research pipeline internally, but return Output B only.

“分析+文案”
or
“按 Evidence Insight 分析”
or
“使用 Evidence Insight 分析”
→ return both Output A and Output B by default.

---



# 28. SOCIAL THESIS ENGINE — Mandatory for Social-Media Caption

This stage runs AFTER the vetted evidence packet is finalized and BEFORE Output B is written.

Its purpose is to prevent the social caption from becoming a polished summary of the image.
The caption must contain an evidence-backed point of view.

The Social Thesis Engine does NOT perform new research.
It may only synthesize claims that already survived:
- source quality gate
- source proximity gate
- counter-evidence gate
- evidence applicability gate
- original-study coverage gate
- editorial filter
- hallucination audit

## 28.1 Generate 3 Thesis Candidates

Before writing Output B, silently generate at least 3 possible theses when the vetted evidence packet supports them; if fewer are defensible, use only those and never fabricate candidates.

Candidate types may include:

### A. Structural constraint
What stable constraint or bottleneck does the image expose?

Examples:
- network redundancy is lower than apparent connectivity
- classification thresholds move with the system
- aggregate gains do not automatically transmit to households

### B. Trade-off
What does improvement in one dimension cost or fail to solve?

Examples:
- faster digital payments vs resilience / fallback
- annual income vs time cost
- connectivity vs geopolitical vulnerability

### C. Reinterpretation
What common reading of the image becomes weaker after outside evidence is added?

### D. Persistence test
What would have to remain true after the temporary shock fades for the change to be structural?

### E. Hidden value
What asset, location, institution or behavior has value for a reason not obvious from the chart?

Examples:
- hub airports as geopolitical routing buffers
- cash as resilience infrastructure
- median income as a better distribution check than national average

Do not generate a thesis that requires unsupported facts.

---

## 28.2 Social Depth Levels

Classify each candidate:

### S0 — Description
Restates what happened.

Example:
“Flights fell after airspace restrictions.”

Not acceptable as the final social thesis.

### S1 — Explanation
Explains why it happened.

Example:
“Flights fell because airlines had to detour.”

Normally too shallow for the default social caption.

### S2 — Judgment
Changes how the reader should understand the phenomenon.

Example:
“Global aviation is highly connected, but safe substitute corridors are much scarcer than the route map suggests.”

Minimum acceptable level by default.

### S3 — Structural Thesis
Identifies a durable constraint, trade-off, hidden value or testable structural relationship.

Example:
“Part of the Gulf hubs’ strategic value comes from geographical optionality: when major Eurasian corridors close, their position becomes a routing buffer.”

Preferred when evidence supports it.

Default target:
- Aim for at least S2 when the Qualified Evidence Pool supports it.
- Prefer S3 only when evidence supports it.
- If evidence supports only S1, S1 is valid; mark it internally as evidence-limited and do not fake a deeper thesis.
- The evidence-limited exception overrides later S-depth pass thresholds.

---

## 28.3 Thesis Competition

Score each candidate internally on:

### Evidence Support
How directly is the thesis supported by the vetted evidence packet?

### Novelty
Does it add something the image does not already state?

### Explanatory Leverage
How much of the image’s pattern does it explain?

### Evidence / Source Linkage
Would the thesis still clearly belong to this exact supplied evidence?

### Social Resonance
Is it understandable and worth sharing without extra context?

### Falsifiability
Can future data, another case, or a counterexample weaken it?

### Risk Penalty
Does it depend on a causal leap, weak source, excessive extrapolation, or generic philosophy?

Conceptually:

ThesisScore
≈ Evidence × Novelty × ExplanatoryLeverage × ImageLinkage × SocialResonance × Falsifiability
− RiskPenalty

No exact arithmetic is required.

Choose ONE winning thesis.

Do not merge several mediocre theses into one paragraph.

---

## 28.4 Opinion Requirement

The social caption must contain a clear interpretive stance.

This does NOT mean:
- first-person opinion is required;
- rhetorical certainty is encouraged;
- unsupported moral judgment is allowed.

It means the paragraph should answer:

“After reading the supplied evidence and checking it, what is the one thing worth concluding?”

The answer cannot be merely:
- the ranking changed;
- the line went up;
- the map shows disruption;
- different countries behave differently.

If the central sentence can be paraphrased as “the chart shows X”,
the thesis is too shallow.

---

## 28.5 Thesis Integrity Tests

Before writing Output B, run these tests:

### Test 1 — Description Removal
Remove all sentences that merely describe the image.

Question:
“Is there still a clear judgment?”

If no:
rewrite.

### Test 2 — One-Sentence Thesis
Can the intended point be stated in one plain sentence?

If no:
the caption probably contains too many ideas.

### Test 3 — Image Dependency
If the supplied evidence were replaced with unrelated material, would the thesis still make sense?

If yes:
too generic.

### Test 4 — Evidence Trace
Can every important part of the thesis be traced to the vetted evidence packet?

If no:
remove or soften it.

### Test 5 — Counter-evidence Survival
Did the thesis survive the strongest relevant counter-evidence found during research?

If no:
choose another thesis.

---

## 28.6 Social Caption Structure

Optional organization (the stance-first priorities in §29 and the no-fixed-order rule in §32 take precedence):

1. one concrete image anchor;
2. one evidence-backed thesis;
3. one supporting relationship or tension;
4. one restrained ending that keeps the thesis testable.

Do not include:
- full research chronology;
- source-verification narration;
- three separate mechanisms;
- every caveat from Output A;
- a list of statistics.

Prefer 2–4 natural sentences.

---

## 28.7 Social Caption Length

Use the adaptive semantic-load policy in §32.

Length is a soft target, not a pass/fail gate.

If compression would:
- merge distinct claims;
- remove a mandatory qualifier;
- obscure the mechanism;
- turn a conditional claim into certainty;
- or make the thesis read like a slogan,

use the next longer band instead.

If the thesis is already complete, stop early rather than filling the target.

---

## 28.8 Social Caption Opinion Guard

The caption may be sharper than Output A in framing, but not stronger in factual certainty.

Allowed:
- select one implication more aggressively;
- write a concise structural judgment;
- foreground a trade-off;
- foreground a hidden value;
- foreground a falsifiable prediction.

Not allowed:
- convert association into causation;
- turn “may” into certainty;
- invent intent or motive;
- imply moral superiority;
- use one anecdote as a universal rule;
- turn boundary evidence into contradiction.

---

## 28.9 Social Caption Failure Modes

Reject and rewrite Output B if it is mainly:

### Image paraphrase
“Flights fell, then recovered.”

### Research-summary compression
“According to IATA, EUROCONTROL and ICAO…”

### Generic philosophy
“Every crisis creates opportunities.”

### Empty sophistication
“Geopolitics is reshaping the global order.”

### Multi-thesis overload
“Airspace, fuel, hubs, tourism, geopolitics, resilience and globalization all matter…”

### AI-style pseudo-insight
“The real story is not X but Y.”

---

## 28.10 Social Thesis Diagnostic

After drafting Output B, the following rubric may be used as a diagnostic:

- Thesis depth: S0–S3
- Evidence support: 0–2
- Novelty: 0–2
- Image linkage: 0–2
- Explanatory leverage: 0–2
- Naturalness: 0–2

Use it to detect:
- image paraphrase;
- missing thesis;
- weak evidence;
- generic commentary;
- unnecessary over-expansion.

Do not add content merely to raise a score.

Default quality target:
- one clear evidence-backed judgment;
- strong source linkage;
- no semantic-strength upgrade;
- no forced “depth” when the evidence is limited.

The numeric rubric is not an independent quality certificate.
It is mainly useful for offline A/B evaluation and version regression checks.

Do not show these internal ratings unless the user explicitly asks for an audit.


# 29. SOCIAL COMPOSITION — Stance First, Then Evidence

This stage runs AFTER the Social Thesis Engine has selected one winning thesis.

The Social Renderer has four priorities:

1. surface the thesis early;
2. make the authorial stance clear;
3. build the minimum evidence arc needed to support it;
4. end with a supported implication when that implication adds value.

This is a priority order, NOT a fixed paragraph template.

Do not force a rigid:
“结论 → 过程 → 总结 → 暗线”
sequence.

The Social caption should feel like:
> the author has already done the research, formed a judgment, and is now sharing the part that matters most.

## 29.1 Opening Priority

The opening should reach one of these quickly:
- a conclusion conflict;
- a cognitive reframing;
- a structural tension;
- the thesis itself.

Do not spend the first sentence merely restating the chart title.

## 29.2 Authorial Ownership

The caption must contain a discernible judgment.

It may use first person when natural, but first person is not required.

The following are weak if they add no real stance:
- “我觉得这张图很有意思”
- “我更关注的是……”
- “我第一反应是……”
- “我认为……”

A sentence without “我” can still have strong ownership if it makes a clear evidence-backed judgment.

## 29.3 Evidence Arc

Use only the evidence that the reader needs to understand the stance.

Prefer:
- one strong comparison;
- one trend;
- one mechanism;
over a catalogue of facts.

## 29.4 Ending

Do not summarize the opening again.

When useful, end by moving forward:
- what this changes;
- what variable now matters;
- what risk becomes visible;
- what observation would update the view.

If no supported implication adds value, stop earlier.

## 29.5 No Mandatory Metaphor

Do not generate a metaphor or grand analogy merely to create emotional impact.

A metaphor is allowed only when:
- it is natural;
- it is accurate;
- it does not strengthen the evidence;
- it improves readability.

Structural implication is more important than rhetorical flourish.


# 30. OPTIONAL SO-WHAT — Consequence Only When It Adds Value

After the thesis is selected, ask internally:

“Is there a supported consequence or hidden-line variable that materially improves THIS caption?”

If yes, it may be included.

If no, stop with the thesis.

A consequence belongs only when all are true:

1. it is supported by the Qualified Evidence Pool;
2. it is directly relevant to the chosen thesis;
3. it adds information rather than merely extending the paragraph;
4. it does not open a second competing topic.

So-What is not required to appear after the thesis.
It may be:
- implicit in the thesis;
- integrated into the same sentence;
- placed earlier;
- omitted when unnecessary.

Do not force every image toward:
- future bottlenecks;
- investment consequences;
- policy implications;
- structural transformation.

So-What may identify what the audience should watch next.
It must never turn into:
- an offer by the Assistant to monitor;
- an offer to remind;
- an offer to automate;
- a question asking whether the user wants continued help.


## 30.1 Hidden-Line Rule

A hidden-line variable may be mentioned only when it is:
- already qualified by the research pipeline;
- not obvious from the image alone;
- consequential to what happens next;
- directly useful to the selected thesis.

Do not add a hidden line merely to make the caption sound deeper.

---

# 31. SOCIAL FINAL AUDIT — Human Naturalness After Drafting

## 31.0 Artifact Purity and Speaker Role

## 31.0A Hook and Authorial Ownership

Check:

- Do the first 1–2 sentences reveal why this interpretation is worth reading?
- Is there a clear authorial judgment?
- Could the caption be mistaken for a neutral news brief?
- Does the opening merely restate the image title or ranking?

If the caption is accurate but stance-free:
rewrite the opening around the selected thesis.

## 31.0B Evidence Arc

Check:

- Are all included facts necessary for this thesis?
- Did the caption import too many secondary branches from Analysis?
- Is the evidence arc sufficient but not exhaustive?

Cut any branch that does not help the reader follow the main judgment.

## 31.0C Implication vs Summary

Check the ending:

- Does it move the interpretation forward?
- Or does it merely rephrase the opening?

Prefer one useful structural implication when evidence supports it.

If the final sentence adds no new interpretive value, remove it.

Before any style edits, verify:

- Is the speaker the Author / User addressing a public audience?
- Is every sentence publishable as part of the caption?
- Is there any Assistant→User language?
- Is there any offer, reminder, monitoring proposal, tool suggestion or follow-up question?

If yes:
delete it from Output B.

Do not rewrite assistant service language into a more subtle form.
It does not belong in the artifact at all.


Human Reaction is now an audit concern, not a generation slot.

After drafting, check:

## 31.1 Reaction Performance

Ask:

“Is the caption showing me the insight, or performing how the writer supposedly arrived at the insight?”

Rewrite when:
- the opening reaction adds no information;
- a fake shallow opinion is introduced only to be rejected;
- the caption repeatedly announces its own cognitive turn;
- first person is decorative rather than useful.

Absence of first person is NOT a failure.

Absence of an explicit reaction is NOT a failure.

## 31.2 Thesis Focus

Ask:

“What is the one thing this caption wants the reader to understand better?”

If two or more independent answers remain, cut secondary material.

The caption is allowed to share the same core thesis as Output A.
Independent Social selection does not require inventing a different discovery.

## 31.3 So-What Check

If a consequence is included:
- does it have evidence?
- does it serve the thesis?
- does it deserve the space?

If no supported or useful consequence exists:
- omission is correct;
- do not mark the caption as incomplete.

## 31.4 Semantic Fidelity

Check compression against the Qualified Evidence Pool:

- period;
- population / geography;
- metric / denominator;
- observed vs modeled;
- proposed vs completed;
- association vs causation;
- uncertainty;
- event timing and event type.

Shorter wording may remove explanation.
It may not remove a qualifier that changes meaning.

## 31.5 Over-Explanation

Remove sentences that merely explain an inference the reader can already make from:
- the image;
- the preceding sentence;
- ordinary context.

But never remove premises or qualifiers required for the conclusion to remain valid.

This is an editing rule, not an “Inference Gap” generation module.

## 31.6 Style / Rhythm

Check for:
- repeated sentence templates;
- artificial binary reversals;
- presenter voice;
- abstract “deep insight” announcements;
- every sentence having the same polished cadence.

Revise only when the pattern harms naturalness.

Do not impose a short-sentence / long-sentence formula.
Do not create an “Uneven Rhythm” generation rule.

---

# 32. SOCIAL WRITING FREEDOM — One Thesis, Variable Length

There is no mandatory sentence order and no fixed length based on the number of images.

The Social caption should use the **shortest length that fully preserves one thesis, its authorial stance, the necessary evidence arc, and its evidence boundary**.

Choose length by semantic load:

## Compact — roughly 120–200 Chinese visible characters
Use when:
- the thesis is direct;
- one anchor or one comparison is enough;
- few qualifiers are required.

## Standard — roughly 200–320 characters
Use when:
- the thesis needs one or two supporting facts;
- one mechanism or contrast must be explained;
- limited qualification is needed.

## Deep — roughly 320–480 characters
Use when:
- the thesis depends on a non-obvious mechanism;
- several pieces of evidence must stay together;
- important scope / model / uncertainty qualifiers cannot be removed;
- a useful consequence genuinely adds to the thesis.

## Extended — roughly 480–650 characters
Use only when:
- the task is multi-source or research-heavy;
- further compression would materially distort the argument;
- the paragraph still has ONE thesis rather than several competing theses.

These ranges are soft targets.

A caption may be shorter or longer when that is the cleanest way to preserve meaning.

User-specified length always overrides defaults.

### Length Selection Variables

Choose the band using three questions:

1. **Thesis Complexity**  
   How much explanation is required for the judgment itself to make sense?

2. **Evidence Burden**  
   How many facts or comparisons are indispensable to support the thesis?

3. **Mandatory Qualifier Load**  
   How much wording is required to preserve period, scope, model status, uncertainty, proposed/completed status, or causal boundaries?

### One Thesis Rule

Longer Social does NOT mean more theses.

If extra space starts introducing:
- a second independent claim;
- unrelated background;
- another policy / investment / historical branch;
- a second conclusion,

cut it.

Use extra length only to:
- make the same thesis and stance clearer;
- preserve the necessary evidence arc;
- keep semantic fidelity;
- include a genuinely useful implication.

Do NOT treat the following as slots that must all appear:
- Human Reaction;
- Image / source anchor;
- Thesis;
- Consequence;
- Closing Question.

The best structure is the shortest structure that preserves:
- one clear point;
- strong linkage to the supplied evidence;
- the necessary evidence boundary;
- natural Chinese expression.


# 33. SOCIAL STYLE PRINCIPLE

The caption should sound like:

> a thoughtful person who already did the research, formed a judgment, and now wants to publish the one interpretation worth putting their name on.

Not like:
- a research note;
- a narrated reasoning process;
- a teacher;
- a model completing “reaction / thesis / so-what” fields.

Core rule:

> Cognitive change may be expressed by what the writer chooses to notice. It does not need to be narrated as “how I changed my mind”.

Do not expand the AI phrase blacklist for every new bad sentence.
Prefer editing the underlying discourse action.

---
