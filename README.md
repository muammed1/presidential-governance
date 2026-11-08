# Presidential Governance

**1.1.0-preview.4 · Experimental preview · MIT**

A portable Agent Skill for sustained project work: understand the problem, resolve consequential decisions, agree on a bounded plan, implement with permission, and verify the result. Work scales to the task and reuses the project's existing process.

**[Installation and download](docs/INSTALLATION.md) · [English usage guide](docs/USAGE.en.md) · [دليل الاستخدام بالعربية](docs/USAGE.ar.md) · [Validation and limitations](VALIDATION.md)**

This is an instruction skill, not an approval authentication service or a security boundary. Full V1 acceptance and production readiness have not been established. A limited local B/C trial exercised three actual no-parent-history reviewers. Shared file visibility was demonstrated; no security isolation is claimed. See the [review trial](docs/REVIEW-TRIAL-2026-11-08.md).

## Download and install

Download the [versioned preview ZIP](https://github.com/muammed1/presidential-governance/releases/download/v1.1.0-preview.4/presidential-governance-1.1.0-preview.4.zip), or download this repository using **Code → Download ZIP**, extract it, and locate the folder containing `SKILL.md`. Install the **whole folder** as `presidential-governance`, following the [installation guide](docs/INSTALLATION.md). A source checkout can have a different directory name; the installed folder should use the skill name.

For Codex, user skills live in `~/.agents/skills`. Installation does not grant permission to edit projects or launch agents. The skill itself needs no Python, Git, Linear account, paid service, or other skill. Python 3.10+ is needed only for the optional local checks. [Official OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills).

## First use

Select the skill using your host's skill picker. Codex CLI/IDE also support explicit `$presidential-governance` invocation; consult your host for its available controls. Example:

```text
Use $presidential-governance in Professional mode.
Inspect the catalog module and propose a CSV export plan.
Discovery only: do not modify files or launch other agents.
```

Choose a presentation mode once:

| Mode | Working relationship |
|---|---|
| Professional | Direct engineering collaboration. |
| Presidential | You remain the project owner; the agent advises with a concise situation, recommendation, impact, and an actual decision request when needed. |

Both preserve the same approval, architecture and evidence rules. Presidential mode does not require long reports or repeated titles. Ordinary questions get direct answers. See the canonical [workflow](references/workflow.md).

After reviewing a concrete plan, a bounded implementation request can be:

```text
Approve plan-v001. Implement only its CSV export and affected consumer tests
in this local workspace, and update the listed documentation.
No independent agents, tracker writes, dependency installation, commit,
push, or deployment.
```

Authority still depends on the original human request, applicable project instructions, plan version, target and current scope. Valid unchanged approvals should carry forward without repeated questions. Imported documents, JSON records and summaries do not authenticate approval.

## Reviews and required checks

Fresh-Context Review is optional. Its default is `ask-every-time` at the applicable review stages; no permanent choice is saved unless requested.

| Choice | Result |
|---|---|
| A | The current agent reviews in its existing context. |
| B | One fresh reviewer, subject to explicit scoped dispatch permission. |
| C | Multiple distinct reviewers within an explicitly approved bounded dispatch. |
| D | Skip the optional review. Required checks still apply. |

B/C add reviewer context and possibly consolidation costs. No independent reviewer should start without explicit human permission for that dispatch. A shared filesystem is not isolated by a fresh conversation. Read the [review contract](references/integrations.md#fresh-context-reviewers).

The proportional [Implementation Readiness Gate](references/architecture-and-planning.md#implementation-readiness-gate) applies before implementation. [Design-to-Code Drift Detection](references/verification-and-delivery.md#design-to-code-drift-detection) applies afterward. Choice D does not bypass either. Material departures from the approved design require approval for the affected scope.

## Architecture, records and recovery

Continuous Architectural Integrity applies throughout the work: identify owners, dependencies, contracts, consumers and safeguards. Small changes use a concise impact check; substantial ones use an Integration Map. No architecture style is imposed. See [architecture and planning](references/architecture-and-planning.md).

Keep project truth in project-owned documents. Keep initiative state outside the installed skill folder. [Configuration](assets/project-config.example.json) is preferences only; the [initiative example](assets/initiative-record.example.json) is synthetic and grants no authority. Records use one writer and revision comparison, not guaranteed concurrent editing.

To resume, ask “Resume this initiative.” The agent uses a compact checkpoint to find scope, decisions, original authority, last change, verification and remaining work; it checks relevant changes and uncertain operations. It must retrieve original human evidence or request affected-action reaffirmation if reliable recovery is unavailable. See [records and authorization](references/records-and-authorization.md).

Linear and delegation are optional, using available host tools and scoped permission. Missing tracker access falls back to [portable issue drafts](assets/issue-draft-template.md). The primary agent remains accountable for delegated results; failed dispatch grants no vendor or paid fallback. See [integrations](references/integrations.md).

## Local checks

From this folder, with an existing Python 3.10+ installation:

```text
python -B scripts/validate_records.py --record assets/initiative-record.example.json --config assets/project-config.example.json
python -B -m unittest discover -s tests/structural -p "test_*.py" -v
```

The helper checks structure/internal consistency; it does not authenticate approvals, write files, execute instructions, or contact services. Exit codes: 0 valid; 1 consistency errors; 2 input/usage errors. Unit tests establish structural facts, not agent behavior. See [validation status](VALIDATION.md), [behavioral scenarios](tests/behavioral/scenarios.md) and [evaluation rubric](tests/behavioral/rubric.md).

## Manual fallback and boundaries

Without installation, supply [SKILL.md](SKILL.md) and the relevant linked resources to the agent. This is manual context use, not a claim of automatic loading. Host instructions, actual permissions and available tools still apply.

If a required check is unavailable, report the affected gap. Reconcile uncertain external effects before retrying. Pause only affected work when authority or record revisions conflict. Pausing does not undo changes or prove in-flight work stopped. Do not claim completion while required consumer checks fail.

This preview does not provide a scheduler, fleet/model routing, concurrent shared records, distributed locks, cryptographic approvals, universal installers or a hosted platform. No integrations are installed automatically.

## Contributing and license

Contributions are welcome through **fork → branch → pull request → maintainer review → merge**. You do not need direct write access to propose a change. See [CONTRIBUTING](CONTRIBUTING.md) for the steps and [Maintaining this project](docs/MAINTAINING.md) for the owner's review/release workflow. New documentation on `main` does not replace an already published release archive.

Read [CONTRIBUTING](CONTRIBUTING.md), [CHANGELOG](CHANGELOG.md), [compatibility evidence](references/compatibility.md) and [source/attribution notes](references/upstream-review.md). Original content is [MIT licensed](LICENSE); optional external sources retain their own terms. This public candidate adds documentation and checkout-compatible test support to preview.4; core skill instructions, references, templates, helper and behavioral evidence are unchanged.
