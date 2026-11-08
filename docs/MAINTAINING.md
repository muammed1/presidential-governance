# Maintaining this project

The owner **@muammed1** maintains the upstream repository. The default collaboration path is:

**Issue when needed → contributor fork/branch → pull request → owner review → merge → separate release decision.**

## Review a contribution

Read the PR description and the **Files changed** tab. Check that it solves the stated problem, preserves applicable contracts and safeguards, and supplies appropriate verification. Use review comments to request specific changes. Accept, defer or close a proposal on its merits; a contributor has no automatic entitlement to a merge.

Merge only the reviewed revision after resolving blocking concerns. A documentation correction may need link/consistency checks; a policy, schema or helper change needs affected behavioral/consumer evidence. A passing structural test does not establish authorization correctness or reviewer isolation. Preserve historical evidence with its tested revision.

Use issues to agree on substantial scope before someone spends time implementing it. Keep PRs focused so the owner can understand and review them. Other people can help with reviews while the owner retains the upstream merge decision under this project's workflow.

## Access and enforcement

Outside contributors can use forks and PRs without upstream write access. Grant collaborator access only when direct ongoing access is needed and trusted. In a personal-account repository, collaborators can write; ownership remains with the account owner. An organization is an option later if finer roles are needed. [GitHub personal-repository permissions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/permission-levels-for-a-personal-account-repository).

[CODEOWNERS](../.github/CODEOWNERS) identifies `@muammed1` for all files, including ownership rules themselves. It routes review requests for eligible PRs; it **does not by itself prevent direct pushes or require approval**. Enforcement needs a separate repository setting. [GitHub CODEOWNERS documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).

Before granting upstream write access, configure protection for `main`: require PRs and appropriate code-owner review, dismiss approvals invalidated by relevant updates, and disallow force-push/deletion. Check how administrator exceptions and owner-authored PRs will work; do not create a requirement that only the PR author could satisfy. Require named automated checks only once real checks exist and have run. [GitHub protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

This guide and CODEOWNERS do not activate protection, invite collaborators or configure CI. Confirm actual settings on GitHub. When adding more code owners, note that approval by any matching owner may satisfy a required-owner review; adding names is not a way to require every listed person's approval.

## Merge and release separately

A reviewed merge updates `main`. Users of an older release or installed skill do not update automatically. For a release, review the exact files and validation limits, choose an appropriate version/tag, publish release notes and checksums, and verify the downloadable archive. Keep an experimental label until the claimed acceptance criteria are actually met.

Do not replace an existing tagged archive merely to add documentation. Publish a new release when warranted; in the meantime link the latest guides from `main`. Preserve the project's MIT notice and applicable third-party attribution.
