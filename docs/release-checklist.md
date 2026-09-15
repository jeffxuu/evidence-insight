# v1.0.0 release gates

This is a release candidate, not a tagged release. See [verification](verification.md) for actual evidence.

## P0

- [x] Agent Skills format and public version fields validated.
- [x] All runtime references remain inside the installable skill.
- [x] External Content Trust Boundary implemented and security fixtures supplied.
- [x] Apache-2.0 license text included at repository and installable-package levels.
- [x] No unauthorized media assets bundled; material inventory reviewed with provenance limits recorded.
- [x] Limited secret-pattern scan and source-file review performed.
- [ ] Real model injection behavior and required-reference loading verified.

## P1 / complete brief

- [x] English and Chinese README, installation, contribution and security guidance.
- [x] Public synthetic regression cases covering the specified failure types.
- [x] Anchored rubric, matching-configuration/blinding/reporting tools and deterministic CI definitions.
- [x] Local Codex file installation verified.
- [x] GitHub-hosted CI results verified on the initial candidate commit (see verification records).
- [x] Remote candidate file installation verified; model activation remains blocked.
- [ ] At least one completed model-host smoke run.
- [ ] Original-to-public behavioral migration regression completed before vanilla A/B.
- [ ] Three to five actual paired demos with reviewed provenance.
- [ ] Ten complete independently sealed holdout cases, not exposed blueprints.
- [ ] Default-branch command revalidated after owner-approved merge.

Full benchmark results may follow the initial release only if the remaining release requirements are consciously
resolved by the owner and documentation continues to state Results pending. Unverified behavior cannot be implied by badges.

Do not merge, tag or create a GitHub Release automatically. Current authorization ends at creating the PR.
