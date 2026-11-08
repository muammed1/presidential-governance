# Continuous Architectural Integrity and planning

This is the canonical CAI rule set. [Workflow](workflow.md), review instructions and templates reference it rather than defining a separate architecture framework or database.

## Invariant

Integrate every component/feature/module/layer coherently with the architecture actually present. Preserve established responsibilities, contracts, safeguards, dependency boundaries and verified behavior unless an explicit approved change covers their modification. Distinguish confirmed requirements, accepted decisions, current implementation, prior verified behavior and proposals.

Extend an owner that already fits the responsibility; justify replacement or a distinct component when needed. Do not force unrelated responsibilities together or add speculative abstractions. These rules apply to layered systems, modular monoliths, microservices, event-driven systems and other styles without imposing one. Both presentation modes retain them.

## Lifecycle checkpoints

| Point | Required analysis |
|---|---|
| Before planning | Inspect relevant components, owners, boundaries, dependencies, contracts, consumers, safeguards and tests |
| Planning | Concise impact check or detailed Integration Map proportional to uncertainty/impact |
| Before implementation | Pass the mandatory Implementation Readiness Gate; check duplicates, contradictory rules, bypasses and dependency direction |
| During implementation | At meaningful changes compare actual edits with plan/map; trace consumers; assess deviations before dependent work |
| Review | Evaluate new behavior AND affected integration with appropriate regression, contract, data-integrity or dependency evidence |
| Before completion | Reconcile actual implementation, preserved guarantees, approved changes, risks and evidence limitations |

Continuous means relevant decisions/checkpoints, not a report after every edit or rereading unchanged references. Reuse current analysis and refresh affected parts. Readiness is not an automatic additional approval prompt. Delegated work carries the same obligations and needs primary-agent review.

## Implementation Readiness Gate

This existing pre-implementation checkpoint is mandatory before the first implementation action and before newly affected implementation scope. It is independent of optional review choice, in both modes. In the current plan/map/notes establish:

- Business rules, acceptance and architectural decisions are sufficiently defined; no critical unresolved decision or conflicting requirement remains for the affected work.
- Relevant owners, modules, contracts, consumers, integrations and dependencies are identified and compatible with approved project decisions. Consult the relevant knowledge-base decisions where present; otherwise use the project's existing authoritative sources, not a required new filename or competing decision store.
- Data integrity, authorization, migrations/rollback, APIs, UI and tests have been considered where applicable. Explain a material omission or non-applicability proportionately; do not impose an unrelated questionnaire.
- Original execution authority covers the actual scope/target, and appropriate verification of new behavior and affected integration is planned.

Record a concise ready or blocked assessment with source references and critical blockers in existing notes/open items. Ready is an engineering assessment, not a new record state, approval ceremony or permission grant. Critical missing decisions/conflicts block dependent implementation until resolved; independently covered work may continue only where unaffected. Skipping optional review cannot waive this gate. Reuse a current assessment until relevant changes invalidate it; scale detail to impact rather than require another report.

## Impact check or Integration Map

A lightweight check can be a few sentences: changed responsibility/behavior; existing owner; affected consumers/contracts/data/safeguards; any new or competing responsibility; appropriate verification. Escalate if complexity is material.

For nontrivial changes use:

| Field | Content |
|---|---|
| Affected responsibility | Fact, rule, effect or behavior |
| Existing owner | Component/service/module/document/system |
| References | Concrete source files, contracts, decisions and tests |
| Proposed treatment | Reuse, extension, replacement or addition |
| New responsibility | Demonstrated gap, owner and dependency direction |
| Affected consumers | Callers, downstream systems, readers/writers, operational users |
| Compatibility requirements | Guarantees, interfaces, data and historical behavior preserved or explicitly changed |
| Safeguards | Authorization, validation, integrity, retry, transaction and other protections |
| Verification strategy | Evidence for new behavior and affected integration |

Explain a plausibly relevant omitted layer if omission obscures risk. In a new project identify absent owners/contracts honestly; do not invent existing components.

For derived data/effects identify authoritative source, retained identity, owner of every write/business effect, synchronization/transaction boundaries, retry/replay rules, divergence and duplicate-effect prevention.

## Versioned plan

Include objective/outcome; scope/exclusions; confirmed requirements/decisions; assumptions/open gates; impact check/map; decomposition/dependencies; risks; acceptance/evidence; documentation/operations; requested action scopes. Use a reviewable reference such as `plan-v001`. Preserve approved versions. A new version or explicit amendment records changes; do not silently rewrite the baseline.

Keep the map with the plan, and final reconciliation with review evidence or the completion report. Use existing record plan/evidence/open-item references; CAI adds no fourth state dimension or separate architectural store.

## Conflict and deviation

Classify discoveries against the accepted outcome before adding work. A defect violating approved requirements belongs in the covered repair scope; if repair needs an uncovered material change, stop only that dependency and obtain the affected decision. An unresolved business rule is a user decision, not a routine default. An optional improvement is deferred with a short reference in the existing backlog/notes when persistence is authorized, or in the conversational handoff. Do not implement it, create an external issue, reopen completed stages or invalidate unrelated evidence merely because it was noticed. Required integration defects remain blockers; relabeling one as optional does not remove the requirement.

Identify the affected responsibility/contract/decision/safeguard, impact and consumers, reasonable alternatives, affected permissions and decision needed. Stop affected work if no safe in-scope resolution exists; independent covered work may continue. Nonmaterial implementation adjustments may be documented proportionally without new approval. Material changes to ownership, boundaries, dependency direction, safeguards, source of truth, external contracts or effect paths require affected-scope approval before dependent implementation; assess actual consequences, not every refactor as material. Follow [authorization](records-and-authorization.md) for carry-forward and renewal.

## Completion evidence

A feature is not complete solely because its own tests pass. Evaluate relevant consumers and integration. Passing isolated tests cannot override architectural conflict, missing required compatibility evidence, unapproved contract change, safeguard bypass or duplicate/divergent effects. Required missing evidence blocks the affected completion claim. [Verification and delivery](verification-and-delivery.md) owns evidence recording and reporting.
