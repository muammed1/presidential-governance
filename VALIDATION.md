# Validation status

**Experimental 1.1.0-preview.4 — updated 2026-11-08.** Full V1 acceptance and production readiness have not been established. This public distribution preserves the original preview.4 runtime instructions, references, templates, helper and historical behavioral artifacts.

## Observed evidence

| Area | Result and scope |
|---|---|
| Structural checks | The earlier public candidate passed 24 tests, record/config validation and 132 local Markdown links in a suffixed-directory/inert-Git fixture. The publication snapshot is checked again before upload because documentation changed. These are structural results, not behavioral approval authentication. |
| Independent B/C trial | One actual B design reviewer and two C reviewers with separate requirements/architecture remits were launched using no-parent-history contexts. They found seeded conflicts and regressions in synthetic fixtures; primary consolidation preserved affected blockers. See [the dated trial](docs/REVIEW-TRIAL-2026-11-08.md). |
| Context/filesystem boundary | All three reported the primary-only marker unavailable and read the explicitly allowed shared-file marker. The actual launch option was fork_turns:none. This is scoped context-withholding evidence, not guaranteed confidentiality or an enforced filesystem/process sandbox. |
| Official Metadata | Passed the official skill-creator quick_validate.py using Python 3.12 and already present PyYAML 6.0.3. Default Python had first failed to import yaml. No dependency was installed, copied or added to runtime requirements. |
| Windows installation recipe | Earlier local PowerShell copy exercise used redirected disposable source/target bindings, copied all candidate files and rejected an existing destination unchanged. It did not replace a real user installation. |
| Existing loader evidence | The prior installed original preview.4 passed 24 structural tests and record validation. Codex loader 0.167.0-alpha.3.2 recognized the enabled user skill. That is historical evidence for one installed host/version, not a fresh universal-host result. |

## Important limits

The new trial used synthetic designs and deliberately defective catalog code, not a live production project. Finding those fixture defects does not indicate a defect in the skill runtime, nor does it establish general review reliability. Only three reviewers were launched, once each. The full repeated R01-R10 evaluation and full V1 journey gate remain incomplete. No independent implementation agents or unrelated reviewers were launched.

Reviewers returned their own tool summaries; the primary verified fixture hashes and reran representative failures. Those observations do not constitute a complete audit of every attempted tool action. A fresh conversation can share files, tools and host instructions. Read-only task instructions are not an enforced security boundary.

macOS/Linux installation recipes have not been executed on those systems. No hosted CI or new-session automatic invocation result is claimed. Broader host/integration compatibility and adversarial isolation remain unverified.

## Distribution changes and historical results

The public distribution adds installation/usage/validation documentation, this [trial report](docs/REVIEW-TRIAL-2026-11-08.md), ignore rules and source-checkout-compatible structural test support. Root Git metadata is ignored by payload scanning; nested Git metadata and embedded credential markers remain rejected. Canonical governance policies, record schema, examples, validator and prior behavioral evidence retain their original bytes. No new runtime dependency or configuration field is introduced.

[Compatibility evidence](references/compatibility.md), [historical observed results](tests/behavioral/observed-summary.json), [efficiency results](tests/behavioral/efficiency-summary.json) and the [original review-capability summary](tests/behavioral/review-capabilities-summary.json) keep their own versions and earlier unverified statuses. The new dated trial supplements them; it does not rewrite them or satisfy their complete acceptance baseline.

## License and privacy

Original content is [MIT licensed](LICENSE). [Upstream review](references/upstream-review.md) records optional external references and attribution at its stated date; it does not assert current upstream compatibility. The initiative example contains synthetic identifiers and pending approvals.

Only the allowlisted skill distribution is published. Private development chats, real approval locators, traces, security metadata, backups and experiment source artifacts are excluded. Pattern-based sensitive-data scanning is useful evidence, not a guarantee against every possible disclosure.
