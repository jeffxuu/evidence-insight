# Migration audit

Public version: **1.0.0**. Historical source: **Image Insight V7.6.3**.

The four exact supplied files are preserved in [internal](internal/). They are historical inputs,
not discoverable runtime skills. The original filename is retained deliberately; no extra `SKILL.md` exists there.

[manifest.json](manifest.json) accounts for every nonblank input line, including list items, exceptions,
examples and headings. This is a conservative superset of normative-rule coverage.
Each row records source location/text, destination location/text, original trigger,
new loading condition, change type and regression case IDs. It is not a behavioral pass certificate.
Context and local conditional wording remain available in the original and destination sections.

The original runtime SHA-256 is:

`4bc44e13856549d1a14fafce8282960ca666821a591b75c9f7648d988e929071`

## Loading and preservation

The entrypoint links every reference directly and states when to read it. Core source intake,
research, pool and semantic safeguards still apply to Social-only tasks.
Analysis-only requests do not need the full Social renderer; Social-only requests do not load the Analysis renderer.
Applicability checks load when evidence is used for support, contradiction, boundary, method caveat or context.
Style guidance loads at final editing, not before evidence intake. Format-specific intake clauses retain their local conditions.
The security boundary applies before reading any external material.

Much of the detailed instruction text remains deliberately verbatim. Repeated checks at different stages remain.
No token reduction or behavioral equivalence is inferred from the shorter entrypoint.
The source-line validator catches a missing or edited destination line, but a real host trace is still needed
to establish that a required reference is actually loaded during use.

## Approved changes only

| Change | Failure addressed | Preserved guard | Regression |
| --- | --- | --- | --- |
| Public metadata, names, triggers, adapter packaging | Nonstandard version field and internal-version dependence | Version synchronization and silent metadata | R15 |
| Include read attachments / reproducible calculations in factual provenance | Dataset/document evidence excluded by old image-only wording | Provenance, reliability and derived/direct distinction | R11, R15, I05 |
| Bind no-image tasks to actual supplied evidence | Impossible dependence on an absent image | Specific linkage remains mandatory | R15 |
| Make old Social ordering optional under later priorities | Anchor-first template competing with stance-first and free order | Evidence arc, one thesis and ownership | R09 |
| Do not fabricate three candidates under weak evidence | Candidate count pushing beyond available facts | Comparison when possible, evidence-limited downgrade | R14 |
| External Content Trust Boundary | Material instructions acting as runtime authority | Legitimate methodology use and authorized tools | I01–I05 |

No change was made to the known-information percentage heuristic, source tiers, default Chinese length bands,
style diagnostics, one-thesis contract or evidence pool. Their possible tensions remain subjects for recorded tests,
not justification for unapproved redesign.

## Repeat the accounting

```bash
python scripts/migrate_internal.py
python scripts/validate.py
git diff --exit-code
```

Run these from the repository root after installing development dependencies.
The generator is a migration utility, not part of runtime. It refuses a changed original runtime fingerprint.
For future behavior changes, propose and document a new migration/release rather than editing the sealed original snapshot.

## Migration regression status

Static source coverage: verified by the deterministic validator.
Original-versus-public model equivalence: **BLOCKED / UNVERIFIED** pending an authenticated independent host execution.
Vanilla A/B must follow that comparison; no self-scored or hand-written replacement results are supplied.
