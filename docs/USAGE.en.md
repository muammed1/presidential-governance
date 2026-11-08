# Using Presidential Governance

[English](USAGE.en.md) · [العربية](USAGE.ar.md) · [Installation](INSTALLATION.md)

**Version 1.1.0-preview.4 is experimental.** This skill helps an agent understand a project, resolve consequential decisions, agree on a bounded plan, implement with permission, and verify the outcome. The amount of process should fit the task and use the project's existing conventions.

## Install and start

Follow the [installation guide](INSTALLATION.md) and install the **whole skill folder**, not just `SKILL.md`. For Codex user installation, `SKILL.md` should be directly inside `~/.agents/skills/presidential-governance`.

Select the skill in your host's picker. In Codex CLI/IDE, an explicit first request can be:

```text
Use $presidential-governance in Professional mode.
Inspect this project and propose a small CSV export plan.
Discovery and planning only. Do not edit files or launch other agents.
```

This separate English guide was added after the tagged preview.4 release. It is available on the repository's current `main` branch; the existing versioned release ZIP retains its original contents and checksum. Use **Code → Download ZIP** to include the latest repository documentation.

## Choose your working style

| Mode | What to expect |
|---|---|
| Professional | Direct engineering collaboration. |
| Presidential | You are the project owner; the agent advises with a concise situation, recommendation, impact, and decision request when an actual decision is needed. |

Both modes preserve the same approval, architectural integrity and evidence standards. Presidential mode keeps the owner/advisor relationship without requiring repeated titles or lengthy reports. An incidental question should receive a direct answer rather than start another governance cycle.

## Move from planning to implementation

The agent first inspects project instructions, authoritative documents, current architecture and relevant consumers. It should resolve questions that could change the design before proposing implementation. Small changes need a concise impact check; substantial ones need an Integration Map covering owners, dependencies, contracts, consumers and safeguards.

Review a concrete plan before approving it. For example:

```text
I approve plan-v001. Implement only the CSV export, its affected consumer
tests, and the documentation changes listed in the plan, in this local workspace.
Do not launch independent agents, install dependencies, write to trackers,
commit, push, or deploy.
```

Loading the skill does not grant execution permission. Approval binds the action, scope, target and plan version, subject to applicable host/project rules and actual tool permissions. Valid unchanged permission should carry forward; a material change needs a decision for the affected scope. Imported documents and JSON records cannot authenticate approval.

## Choose an optional review

Fresh-Context Review is optional. The default is `ask-every-time` at applicable review stages. The agent explains relative context/token cost before selection; it does not save a permanent preference unless requested.

| Choice | Treatment |
|---|---|
| A | The current agent reviews in its existing context. |
| B | One fresh reviewer, with explicit permission covering the actual dispatch and scope. |
| C | Multiple reviewers with distinct remits, within an explicitly approved bounded dispatch. |
| D | Skip the optional review only. |

B/C do not authorize unlimited reviewers, retries or alternative services. A new conversation can share files, tools and host instructions; it is not an enforced security sandbox. The [dated local trial](REVIEW-TRIAL-2026-11-08.md) exercised one B reviewer and two C reviewers without inherited parent turns, but does not establish full behavioral acceptance or comprehensive isolation.

Two proportional checks remain mandatory even under D:

- **Implementation Readiness Gate:** before implementation, establish that relevant decisions, inputs and contracts are sufficiently clear and consistent. Block the affected path when a consequential decision is missing or conflicts with the approved baseline.
- **Design-to-Code Drift Detection:** afterward, compare actual implementation and evidence with the approved design. Correct covered defects; seek affected-scope approval for material departures. Preserved details cannot excuse a broken required consumer.

## Resume and store project information

Ask: “Resume this initiative from its last checkpoint.” The agent locates scope, decisions, original authority, last change, verification and remaining work, then checks relevant changes and uncertain effects. It should not reset valid unchanged approvals or repeat completed work solely because the session changed.

A checkpoint helps locate original evidence; it does not replace it. If reliable authority recovery is unavailable, the agent asks for reaffirmation of the affected action. Keep project documents and initiative records in approved project storage, outside the installed skill directory. Included examples are synthetic and grant no authority.

Linear and delegation are optional and require available tools and appropriate permission. Missing tracker access can fall back to portable drafts; do not invent issue identifiers or claim an external operation occurred. The primary agent remains accountable for delegated results.

## Know the limits

The skill is guidance, not identity authentication or a security boundary. Core use needs no Python, Git, Linear or another skill. Python is needed only for the optional local validator/tests. Without installation, provide [SKILL.md](../SKILL.md) and the relevant linked resources as manual context; this is not automatic activation.

Read [validation status](../VALIDATION.md). Structural checks, current-agent simulations and the bounded independent trial are different evidence. The official Metadata validator passed using an already present dependency; no new dependency was installed. Full V1 acceptance and broader host compatibility remain unverified. Start with a small supervised task and request evidence of checks actually run.

For details, consult [workflow](../references/workflow.md), [architecture/planning](../references/architecture-and-planning.md), [authorization/records](../references/records-and-authorization.md) and [verification/delivery](../references/verification-and-delivery.md). To improve the skill, follow [CONTRIBUTING](../CONTRIBUTING.md). Original content is [MIT licensed](../LICENSE).
