# Lifecycle and proportional workflow

This resource owns interaction lifecycle and work progression. [Records and authorization](records-and-authorization.md) owns permission/evidence semantics; [architecture and planning](architecture-and-planning.md) owns CAI. Neither state nor a stage number grants permission.

## Activation and ordinary use

Activate only on explicit invocation or a clear request for this governance workflow with supported host selection. Discussion about the skill or reviewing an idea is not implementation authorization and must not create a persistent initiative. Identify objective and scope; follow [first-use discovery](discovery-and-decisions.md). No activation side effects are authorized implicitly.

Use one initiative for related follow-ups. Answer ordinary questions directly without a new record, rigor announcement or ceremonial briefing. Professional is the default: direct engineering collaboration. Presidential retains an owner/advisor relationship: brief the owner on the situation, recommendation and impact, and surface the decision actually needed. Use chosen titles naturally and sparingly; avoid repeated honorifics, preambles or long reports merely because this mode is selected. Roles never prove authority. Mode switches preserve progress, approvals and identical verification/CAI obligations.

Progress updates state the relevant discovery, remaining uncertainty and what the next action will resolve. A decision request in either mode is needed only when reliable existing authority does not already cover the action. Do not impose an extra approval step to maintain a Presidential role or briefing format.

## Reuse project process

Map these checkpoints onto the project's existing instructions, plans, decisions and approval artifacts. Reuse the same artifact when it already satisfies a checkpoint; add only missing information. Do not require a second plan, sign-off, report or storage location for the skill. Project requirements remain applicable: efficiency preferences do not waive a mandated check or user decision. An existing user-authorized exception remains applicable within its scope.

When a pause or permission request is actually necessary, identify the missing action/decision and its source: project instruction, a specific skill rule, or tool permission. Cite the relevant file/rule or tool rejection. Distinguish an implementation recommendation from a mandatory gate; check existing original approval before asking again.

## Optional review choice

Fresh-Context Review is always optional. Default to `ask-every-time`: at each existing substantive plan/design or implementation review stage, ask once before its optional review. Do not add stages at every CAI checkpoint, minor edit or ordinary question. A manual review request can use the same choice at any point with a bounded objective.

Before the choices explain relative token cost: same-agent review reuses current context; one fresh reviewer adds one context/review; several add their approved contexts and consolidation; skipping adds no optional-reviewer context. Do not invent numerical estimates without measured usage for the relevant work.

| Choice | Treatment |
|---|---|
| A — Same-Agent Review | Current agent reviews with its existing context; no independent agent |
| B — Single Fresh-Context Reviewer | One independent conversation under explicit presidential review/dispatch approval |
| C — Multiple Fresh-Context Reviewers | Present the minimal useful count and distinct responsibilities; obtain explicit approval covering them before launch |
| D — Skip Optional Review | Skip only optional review; mandatory readiness, drift, security, testing, approvals and verification continue |

An absent choice, silence or approval of a plan alone grants no independent-review dispatch permission. Follow [delegation](integrations.md#fresh-context-reviewers) for B/C and unavailable-isolation fallbacks. While a choice is pending, do not dispatch or report optional review complete; independently authorized work and mandatory primary checks may continue.

A choice covers only its named stage/task scope. Ask again at the next review stage by default; honor an explicit task-wide duration and allow switching. Do not save a selection as a permanent preference unless expressly requested; even a saved preference does not grant dispatch authority. Preserve unchanged valid scoped permission on resume using original evidence, not a checkpoint's claim. A material scope change requires reassessing affected permission, not automatic additional reviewers.

## Rigor

| Level | Trigger | Treatment |
|---|---|---|
| Lightweight | Clear bounded behavior, limited impact | Short plan, concise impact check, focused verification, completion reconciliation |
| Standard | Multiple components, contracts, consumers | Written plan, Integration Map, acceptance criteria, compatibility/regression review |
| High impact | Migration, security boundary, architecture replacement, production or broad integration risk | Alternatives, dependency/operational analysis, explicit affected-change authorization, deeper evidence |

Choose the level early for substantive work and give a one-sentence reason in the existing plan or briefing. Its treatment in the table sets the necessary outputs; existing artifacts or a concise inline impact check can satisfy them. Do not generate empty sections or a separate rigor document. Reconsider only when actual consequences, uncertainty or integration change; elevate the affected part rather than restarting every stage. A high-impact financial operation can contain a small UI adjustment with focused treatment when its business path is unaffected. Trace that impact rather than inferring safety from file type.

CAI remains mandatory at every level. One bounded mandate may cover multiple actions; proportionality never silently decides an unresolved business rule or removes project gates.

## Interaction state

`inactive` → `active`; user pause → `suspended`; explicit resume → `active`; user termination → `terminated`. Reactivation is explicit and reuses normal recovery checks. Interaction state is separate from work progress.

On suspension stop launching work, preserve recoverable progress only within authorized storage, report in-flight operations and supported stopping actions. Confirm an actual stop before claiming it occurred. Suspension does not undo completed effects or automatically revoke every mandate.

On resume use the compact checkpoint in [records and authorization](records-and-authorization.md). Revalidate identity, applicable instructions, current plan/revision and newer human decisions; inspect changed sources and affected architecture. Reuse references already read and still current instead of rereading the whole project or every skill reference. If freshness is uncertain or project instructions require rereading, inspect the necessary sources. Retrieve original authority before approval-dependent work; the checkpoint is only a locator. Reconcile uncertain operations before retries and preserve unaffected scope/evidence with stated limits. Do not reset all permissions or re-execute completed work merely because the session changed.

Default recovery handoff is a compact checkpoint/delta: current scope, any changed decision/authority, last verified state and next step. Do not reproduce the whole approved plan, policy catalogue or conversation chronology. Keep source locators and supporting detail as references; expand into a detailed audit only when explicitly requested or needed to resolve a material conflict. Retrieve only the original conversation context needed to establish scope and newer decisions; exclude unrelated tool outputs and respect the host's advertised request limits.

Termination ends the interaction. It does not close/cancel the initiative, issues or PRs; delete records; roll back effects; or revoke unrelated mandates. Report unfinished state accurately. Future action requires reactivation and valid scoped permission.

## Work state

| State | Meaning |
|---|---|
| draft | Discovery/planning incomplete |
| planned | Reviewable plan exists; approval not implied |
| executing | Authorized implementation underway |
| reviewing | Results under review/verification |
| ready_for_closure | Required implementation, review, evidence and docs satisfied |
| closed | Authorized delivery boundary reconciled and reported |
| blocked | Specific dependency prevents progress; preserve prior state |
| cancelled | User explicitly cancelled |

Normal progression: `draft → planned → executing → reviewing → ready_for_closure → closed`.
Also allow `planned → draft`, `reviewing → executing` for covered corrections, and `ready_for_closure → reviewing` for a new relevant failure. Any unfinished state may become blocked with `blocked_from` and a reason, or cancelled on explicit instruction. Resolve a blocker back to its retained prior state, then proceed through normal transitions. Closed/cancelled work must not silently resume: obtain explicit reopening or a linked follow-up. These transitions are structural descriptions, not authorization checks.

## Milestones

Report implemented, reviewed, verified, merged, deployed and operationally verified separately. Close only the agreed delivery boundary; local completion may exclude merge/deployment. Unresolved required acceptance or integration evidence blocks that completion claim, while independent authorized work can continue. See [verification and delivery](verification-and-delivery.md).
