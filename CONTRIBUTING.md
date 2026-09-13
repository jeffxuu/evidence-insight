# Contributing

The best contribution is a reproducible failure case:

**Input → Current output → Observed failure → Expected boundary → Proposed regression test.**

Use the failure-case issue form. Include the model/version where exposed, reasoning effort, host,
date, available tools, exact user request, runtime version and whether the failure reproduced.
For source applicability, name the proposition and explain the population/outcome/period mismatch.
For semantic strength, show the original qualified statement and the stronger rewritten statement.
For Social, identify whether the failure concerns authorial stance, multiple theses or artifact leakage.
For injection, include an inert reproduction without real credentials or an active exfiltration destination.

Only submit material you have permission to redistribute. Prefer original synthetic fixtures,
public-domain data or permissively licensed datasets. Include provenance and license information.
Redact names, contact details, tokens and private files. Never upload a full paywalled infographic by default.

## Changing rules

Explain which failure a rule prevents before proposing its removal, merge or rewrite.
State the failure that could return, any actually redundant mechanism and the supporting regression.
Shorter text or a prettier directory is not sufficient justification.
Keep the source-line migration record current; preserve exceptions as well as prohibitions.
Moving a rule without a working loading condition is a regression.
New architectural changes require a separate proposal; the first public release permits only its recorded minimal repairs and safety boundary.

## Local checks

```bash
python -m venv .venv
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests -v
```

Activate the virtual environment using your shell's usual method before running the pip/python commands.
These are engineering checks. Add a separately recorded model evaluation when behavior is affected.
Never label unit-test doubles or a judge's guess as a measured benchmark.

Keep `metadata.version`, the public runtime contract, adapter and generated upload package synchronized.
Do not tune on sealed holdout. Retire exposed/tuned holdout cases into public regression.
Submit changes through a branch and PR; retain actual run records and unresolved limitations.

Contributions intentionally submitted for inclusion follow the project's Apache-2.0 license,
subject to any separately identified third-party material. See [LICENSE](LICENSE).
