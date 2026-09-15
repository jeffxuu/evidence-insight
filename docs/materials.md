# License and material review

Review date: 2026-09-12 UTC. Status: **PARTIALLY VERIFIED** for rights provenance;
file inventory and limited secret-pattern checks are engineering-verifiable.

The repository was empty before the authorized baseline initialization. There was no existing third-party code,
asset or alternative repository license to migrate.
The owner supplied four text files and authorized their public Apache-2.0 release preparation.
Their authorship history cannot be independently established by a file scan.

| Material | Origin / reuse basis | Handling |
| --- | --- | --- |
| Historical runtime, adapter and two notes | Owner-supplied source files; release authorized by owner | Exact snapshots confined to historical migration directory |
| Public runtime and adapter | Migrations of those supplied files | Apache-2.0; all changed source lines recorded |
| Engineering scripts and public fixtures | Original implementation and synthetic examples created for this project | Apache-2.0; no third-party statistical observations asserted |
| LICENSE | Official Apache License 2.0 text | Unmodified license text, duplicated inside installable skill |
| Agent Skills validator | Official agentskills repository at pinned commit | Installed as a development dependency; its code is not copied into runtime |
| skills CLI | Published `skills@1.5.26` used for installation verification | External development/installation tool, not vendored |
| GitHub Actions | Official checkout/setup-python actions pinned to verified commit SHAs | External CI dependencies, not relicensed copies |

No full media chart, paywalled image, social screenshot or scraped article is bundled.
Textual fixture attacks use dummy canaries and `.invalid` destinations. I03.zip contains only inert text and CSV.
No third-party attribution requirement was identified for bundled implementation files; no invented NOTICE is added.
New contributors must disclose separate third-party licensing and retain required notices.

References: [Apache license](https://www.apache.org/licenses/LICENSE-2.0),
[Agent Skills specification](https://agentskills.io/specification),
[CLI source](https://github.com/vercel-labs/skills).

The limited scan checks common private-key and API/GitHub-token shapes. It cannot prove absence of all secrets,
personal information or copyright restrictions. Review the complete diff before public submission.
