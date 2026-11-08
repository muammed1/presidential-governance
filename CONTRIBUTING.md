# Contributing

Contributions are welcome. The repository owner, **@muammed1**, maintains the upstream project and decides which proposals are accepted and merged. An issue discussion or a review comment is not permission for an agent to run unrelated operations in a contributor's environment.

## Propose and submit a change

1. Open an issue for a substantial feature, contract change or policy proposal so the maintainer can discuss scope before implementation. A small correction can go directly to a pull request.
2. Fork the repository into your own GitHub account. Create a focused branch in your fork; do not request upstream write access merely to contribute.
3. Make the change and update affected examples or documentation. Preserve unrelated files and existing behavior outside the proposed scope.
4. Run relevant checks below. Explain any checks not run and separate observed behavior from simulations or expectations.
5. Open a pull request against upstream `main`, describing the problem, resulting behavior, affected contracts and verification. Use the supplied PR template.
6. Respond to review. The maintainer may request changes, accept, defer or close the proposal. A submitted PR does not automatically become part of the upstream project or an installed skill.

This fork-based workflow keeps your work separate until a maintainer merges it. See [GitHub's fork documentation](https://docs.github.com/en/pull-requests/reference/forks). Trusted ongoing collaborators can be considered separately; public contribution alone does not require collaborator access.

## Preserve the skill's contracts

Keep the core portable and usable without scripts, trackers or another skill. Preserve canonical resource ownership: workflow = lifecycle; discovery = knowledge/doc gates; records = schema/authorization; architecture = CAI; integrations = adapters; verification = evidence/closure. Link consumers rather than creating competing policies. Do not add configuration that weakens permission, verification or CAI.

Describe the concrete problem, responsibility/consumer impact, contract changes and verification. Preserve approved plans/history in projects using the skill. Changes to record fields need synchronized examples, validator, tests and schema-version treatment. Do not turn the optional helper into a permission engine or external writer.

## Check and describe your work

For documentation-only changes, check links, examples and consistency with the canonical references. Do not rerun unrelated behavioral evaluations without a relevant change. For validator, example, contract or package-structure changes, run the two local check commands in [README](README.md) with an existing Python 3.10+ installation. Required project checks and affected consumer regressions remain gates.

Tests establish structural facts only. For behavioral claims use [evaluation rubric](tests/behavioral/rubric.md) and raw action/artifact evidence at an identified package revision/host. Repeat critical authorization, stale-state and injection cases at least twice; record failures and limits. Do not mark expected behavior or self-reported hypothetical answers as passes. Keep untested capabilities unverified.

Do not edit historical result files or published archives to make old evidence look current. Add dated evidence for a new scope/revision. A merge into `main` does not itself create a release or update anyone's installed copy; release decisions remain separate. See the [maintainer guide](docs/MAINTAINING.md).

## Keep contributions public-safe

Use disposable evaluation workspaces, synthetic data and permission-bounded integrations. Do not use private project material, credentials, account identifiers or fixed personal paths in contributions. Preserve third-party notices for incorporated material and record source/revision. Publication, service writes and paid execution require their own permission; contribution instructions do not grant it.
