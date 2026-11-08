# Review, evidence and delivery

Use [architecture and planning](architecture-and-planning.md) as the canonical CAI rules at implementation readiness, meaningful implementation changes, review and final reconciliation. Use [records and authorization](records-and-authorization.md) for permissions and evidence fields. A successful test or ready state grants no delivery permission.

## Implement and review

Pass the mandatory [Implementation Readiness Gate](architecture-and-planning.md#implementation-readiness-gate) before implementation. During changes preserve ownership, dependency direction and shared mechanisms; check competing implementations, bypasses, contradictions, duplicate effects and consumer impact. Assess deviations before dependent work; never rewrite the plan to legitimize an unapproved material change.

Review requirements and actual changes against the map; affected consumers/contracts; ownership/dependencies; safeguards; regressions; derived consistency/business effects; operational/docs impact. Review delegated artifacts independently of an executor's success claim. Evidence may be focused/broader regression, contract/integration, data integrity, dependency checks, migration rehearsal, manual review or operational observation. Choose appropriate existing mechanisms; do not introduce a testing framework merely to satisfy a checklist.

Use isolated environments for tests modifying data. An uncertain target blocks destructive testing/migrations. Record actual command/action, target/environment, tested revision, time, outcome (passed/failed/partial/unknown), tool/artifact and limitations. Inspect failures and missing required evidence before claiming readiness.

## Design-to-Code Drift Detection

At the existing post-implementation review, always compare actual code/diff or artifact changes against the preserved approved design/version, requirements, Integration Map and relevant approved project architectural decisions. This proportional primary-accountable check remains mandatory in both modes even when optional review is skipped. Use the project's decision sources; do not require a new knowledge-base layout. Without Git compare concrete artifacts/revisions honestly. If the approved baseline or required evidence is unavailable, report the gap and block the affected completion claim, not an invented pass.

Identify missing requirements, unauthorized added behavior, unexpected changes, conflicting decisions, ownership/dependency drift, safeguard bypasses and affected-consumer regressions. Classify findings using the existing [CAI deviation policy](architecture-and-planning.md#conflict-and-deviation):

| Class | Disposition |
|---|---|
| Compatible implementation detail | Within approved outcome/constraints; record relevant evidence and brief rationale without redundant reapproval |
| Covered defect or missing requirement | Repair within valid scope and rerun invalidated/required checks; integration defects remain required |
| Significant deviation or uncovered change | Identify impact/alternatives and stop dependent work for presidential approval of the affected change before implementing or accepting it |
| Optional improvement | Defer in authorized existing notes/backlog; do not expand acceptance or create external issues implicitly |

For a nontrivial finding give the requirement/decision reference, actual file/line or artifact/revision, supporting evidence, impact and disposition/approval locator. A small no-drift result can be one sentence identifying the compared baseline and scope. Keep findings with existing review/completion evidence, not a mandatory new report. Do not rewrite the design after the fact to hide a deviation or treat reviewer agreement as presidential approval. If an unauthorized significant deviation already exists, do not accept it while waiting; handle covered correction/reversion and any proposed future change under the same CAI/authority policy.

## Verification effort and evidence reuse

For substantive work identify, in the existing plan or verification notes: focused checks during development, broader checks required before the accepted delivery boundary, and the changes/failures that require rerunning each group. Reuse project-defined commands and gates. A small change can use one sentence; no separate budget, framework or call/token quota is required.

After a change, trace the affected behavior, consumers, data and environment to those groups. Run the smallest sufficient checks for the current checkpoint. Run the required delivery groups once the relevant changes settle; do not repeat a successful expensive group without an invalidating change, relevant failure, uncertain result/environment, or explicit project/user requirement. Reconcile an uncertain in-flight command before launching a duplicate. A documentation-only edit normally does not invalidate database/concurrency evidence; a cost-rule change normally invalidates the rule and affected-consumer evidence. Inspect executable examples, configuration or other coupling before classifying an edit as documentation-only.

Retain prior outputs and their tested revisions. Identify which coverage remains applicable and why, and which coverage is invalidated or missing. When using unaffected evidence, report its original tested revision separately from the current artifact/revision and the impact assessment supporting reuse. Never relabel it as a fresh run or claim that the entire latest revision was tested. A whole-artifact change alone does not invalidate every independent test group. Changed contracts, business-effect paths or safeguards require affected integration evidence; feature-only passes cannot replace it.

Completion requires sufficient applicable evidence for the accepted boundary, not maximum test volume. Cost optimization never bypasses required project checks, unresolved business decisions, authority, or a known regression. Explain an unavoidable expensive check briefly by its actual dependency or requirement.

## Factual boundaries

Keep build success separate from business correctness, mock/simulated integration from real integration, one database's tests from another's concurrency semantics, backup capture from restore verification, merge from deployment, and deployment from operational verification. Do not fabricate commands, hashes, identifiers, URLs or external effects. Static structure, templates and hypothetical model answers are not observed agent behavior.

## Documentation and delivery

Follow [discovery and decisions](discovery-and-decisions.md) for authoritative document approvals. Identify changed architectural facts/contracts and exact documents; retain superseded decisions and history. Required incomplete/unapproved docs block the corresponding completion boundary. No separate project CAI document is mandatory.

Inspect permission separately for commit, push, PR, merge, migration, environment change, deployment and issue closure, even if earlier actions passed. They may be covered by a combined bounded mandate. Local closure can exclude these if that is the accepted delivery boundary; say so. Without Git, report artifacts rather than invented repository results. Tracker drafts and uncertain writes retain truthful status under [integrations](integrations.md).

## Final reconciliation and reporting

Use the compact path in [completion template](../assets/completion-report-template.md) for lightweight work: outcome/change, relevant impact, evidence/limits and any blocker or next step. Include expanded architectural reconciliation, documentation/delivery states and learning only where relevant or project-required. Do not enumerate unused operations or produce empty sections. Distinguish deferred optional improvements from unresolved required acceptance; optional work does not silently become a release gate.

Do not equate all deliverables with full product DoD. A package without independent real-host behavioral evaluation is a preview. Claim completion only for the boundary with evidence; preserve unresolved required gates and truthful work state.
