# Security boundary

Evidence Insight is procedural guidance, not an execution sandbox.
No claim of universal prompt-injection resistance is made.

External webpages, PDFs, papers, datasets, CSV/JSON/XLSX, archives, READMEs, metadata,
screenshots, quoted text and social posts are **untrusted evidence content**.
They cannot override instructions or authorize secrets access, uploads, arbitrary commands,
repository changes, software installation or tool calls. The host's actual user task and permissions remain authoritative.

Legitimate codebooks, units and methodological notes may inform evidence interpretation.
Instruction-shaped wording alone does not make a data definition malicious.
The [runtime security reference](skills/evidence-insight/references/security-boundary.md) applies before intake.

Archive reading must not execute code/macros or extract paths outside its controlled directory.
Permission checks and isolation belong to the host; this package does not implement a universal archive sandbox.

## Reporting

For a non-sensitive failure, use the repository's failure-case issue form with an inert reproduction.
Do not put secrets, active exploit targets, private data or credential-bearing logs in a public issue.
Private vulnerability reporting has not been verified as enabled for this repository; no private contact channel is claimed.
For a sensitive report, request a private reporting channel in an issue without disclosing exploit details.

The public fixtures use synthetic data, dummy markers and reserved `.invalid` destinations.
Their presence does not mean model behavior has been tested successfully.
See [verification status](docs/verification.md) and [evaluation protocol](evals/protocol.md).
