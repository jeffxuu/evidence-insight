# Installation and verification

Checked against the official Agent Skills specification and skills CLI source on 2026-09-13 UTC.
Verification CLI: **skills 1.5.26**. Installed skill version: **1.0.0**.

## Default command

**BLOCKED — tested before merge: exit 1, no skills found.** The current main branch contains only the repository initialization baseline.
Do not interpret this target command as a verified main-branch installation:

```bash
npx skills add jeffxuu/evidence-insight --skill evidence-insight
```

The CLI may prompt for agent, scope and installation method. A single command is not a promise of zero prompts.
Node.js/npm, repository network access and a compatible host are prerequisites.

## Release-candidate branch

**VERIFIED for file installation with skills 1.5.26.** The remote candidate was installed in an isolated Codex project; exactly one skill was discovered and all 12 files matched the source SHA-256 inventory. Model execution remains BLOCKED.

```bash
npx --yes skills@1.5.26 add 'jeffxuu/evidence-insight#oss/v1.0.0' --skill evidence-insight -a codex --copy -y
```

The quoted fragment specifies the complete branch name. In skills 1.5.26, the GitHub `/tree/oss/v1.0.0/...` URL is parsed as ref `oss` and fails; that failed attempt is retained in the logs.

Run in the intended project directory. `--copy` requests a concrete copy for inspection;
`-a codex` selects Codex, and `-y` accepts CLI prompts. Review the skill before installing.

## Verified local installation

In an isolated project directory, the following was executed against a local checkout:

```bash
DISABLE_TELEMETRY=1 npx --yes skills@1.5.26 add /path/to/evidence-insight --skill evidence-insight -a codex --copy -y
```

Replace `/path/to/evidence-insight` with the actual checkout path. This is a command parameter, not an included directory.
The CLI discovered exactly one skill and copied it to `.agents/skills/evidence-insight/`.
The entrypoint, ten references and bundled LICENSE were inspected as a standalone installation.
No global skill directory was changed. The exact local absolute path is not required to reproduce the behavior.

| Scope / mode | Path |
| --- | --- |
| Codex project copy, tested | `.agents/skills/evidence-insight/` |
| Codex global copy, untested | `~/.codex/skills/evidence-insight/` |
| Symlink mode, untested here | CLI canonical copy and agent-specific links; inspect actual CLI output |

File installation is not proof of host activation, reference loading or research quality.
The host probe used Codex CLI `0.154.0-alpha.3`, a fresh input directory and read-only mode.
It timed out without a model output; stderr included a plugin-service 401 authentication warning.
This establishes a blocked initialization attempt, not a measured skill failure or a complete diagnosis of the host.

## ChatGPT Projects

The adapter is optional and does not affect other hosts.

```bash
python scripts/build_chatgpt_bundle.py
```

This generates `dist/evidence-insight-chatgpt-1.0.0.zip` from the canonical public files.
Extract it, paste `chatgpt-project-instructions.txt` into Project Instructions,
and upload `evidence-insight-runtime-1.0.0.md` as a Project file. Keep both at version 1.0.0.
The runtime document includes the entrypoint and all ten references with in-document navigation.
Do not upload the historical snapshots as active instructions.
Bundle coverage is deterministically checked; actual Project upload, retrieval and behavior are **UNVERIFIED**.

## Revalidation after merge

Re-run the default command from an empty project, inspect files and run a real task in the target host.
Record CLI/host/model versions, settings, date, output and required-reference reads.
Do not mark global installation or another host verified based on the project-copy test.

## Directory and telemetry

The skills.sh documentation describes automatic listing/ranking through install telemetry.
This project's listing has not been verified. The local test disabled telemetry and does not establish directory indexing.
`DISABLE_TELEMETRY=1` or `DO_NOT_TRACK=1` are the CLI's documented opt-outs.

Sources: [Agent Skills specification](https://agentskills.io/specification),
[CLI documentation](https://github.com/vercel-labs/skills),
[discovery implementation](https://github.com/vercel-labs/skills/blob/main/src/skills.ts),
[installation implementation](https://github.com/vercel-labs/skills/blob/main/src/installer.ts),
[skills.sh FAQ](https://www.skills.sh/docs/faq).

## Actual remote-install records

[Commands, exit statuses and installed file hashes](verification-logs/remote-installation.json)
record the failed tree-URL attempt, the default-main no-skill result, and the successful fragment-ref installation.
The successful candidate run used commit `1779c7078360f86f5ac66bd6a98ea691498e82a2`.
Default-main success must be checked again after owner-approved merge; it is not established by candidate success.
