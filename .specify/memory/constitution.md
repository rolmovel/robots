<!--
Sync Impact Report
- Version change: N/A (template) -> 1.0.0
- Modified principles:
	- Template Principle 1 -> I. Spec-First Delivery
	- Template Principle 2 -> II. Independent Value Slices
	- Template Principle 3 -> III. Verifiable Outcomes
	- Template Principle 4 -> IV. Traceable Artifacts
	- Template Principle 5 -> V. Minimal, Explicit Change
- Added sections:
	- Operational Constraints
	- Delivery Workflow & Quality Gates
- Removed sections:
	- None
- Templates requiring updates:
	- ✅ updated: .specify/templates/plan-template.md
	- ✅ updated: .specify/templates/spec-template.md
	- ✅ updated: .specify/templates/tasks-template.md
	- ✅ verified (no change needed): .specify/extensions/git/commands/speckit.git.commit.md
	- ✅ verified (no change needed): .specify/extensions/git/commands/speckit.git.feature.md
	- ✅ verified (no change needed): .specify/extensions/git/commands/speckit.git.initialize.md
	- ✅ verified (no change needed): .specify/extensions/git/commands/speckit.git.remote.md
	- ✅ verified (no change needed): .specify/extensions/git/commands/speckit.git.validate.md
	- ✅ verified (path not present): .specify/templates/commands/*.md
- Deferred TODOs:
	- TODO(RATIFICATION_DATE): Original adoption date is unknown; set on first confirmed governance approval.
-->

# SDD Project Constitution

## Core Principles

### I. Spec-First Delivery
Every feature MUST start from a written specification in `spec.md` before implementation
tasks are executed. The specification MUST define prioritized user stories, functional
requirements, edge cases, assumptions, and measurable outcomes.
Rationale: Shared intent reduces rework and keeps implementation aligned with user value.

### II. Independent Value Slices
Work MUST be organized as independently deliverable user stories (P1, P2, P3...). Each
story MUST be implementable and demonstrable on its own without requiring unfinished
lower-priority stories.
Rationale: Independent slices enable incremental delivery and lower integration risk.

### III. Verifiable Outcomes
Each user story MUST include an explicit independent test method and clear acceptance
scenarios using Given/When/Then behavior statements. Validation MAY be automated,
manual, or mixed, but MUST be reproducible by another contributor.
Rationale: Reproducible verification is required for objective completion decisions.

### IV. Traceable Artifacts
Plan, tasks, and implementation outputs MUST remain traceable to the originating
specification. Task descriptions MUST include concrete file paths, and each major
decision MUST be documented in the related design artifact.
Rationale: Traceability preserves context and supports fast, reliable review.

### V. Minimal, Explicit Change
Contributors MUST prefer the smallest viable change that satisfies the requirement.
Complexity, scope expansion, or architectural deviations MUST include a written
justification in the relevant planning artifact.
Rationale: Explicit tradeoffs prevent accidental complexity growth over time.

## Operational Constraints

- Repository conventions in `.github/` and `.specify/` MUST be preserved unless a
	documented migration plan is approved.
- Shell and automation guidance MUST remain cross-platform aware when scripts exist for
	both Bash and PowerShell.
- Agent and prompt artifacts MUST avoid vendor-exclusive assumptions unless explicitly
	required by integration manifests.

## Delivery Workflow & Quality Gates

1. Specification (`/speckit.specify`) MUST be completed before planning.
2. Planning (`/speckit.plan`) MUST pass Constitution Check gates before task generation.
3. Tasks (`/speckit.tasks`) MUST be grouped by user story and maintain dependency order.
4. Implementation (`/speckit.implement`) MUST execute tasks with evidence of verification.
5. Any exception to these gates MUST be documented with rationale and approver.

## Governance

This constitution supersedes conflicting workflow conventions in this repository.
Amendments require:

1. A documented proposal explaining intent, impact, and migration requirements.
2. Review by maintainers responsible for `.specify` templates and workflow files.
3. Synchronization updates for impacted templates, prompts, and command docs.

Versioning policy follows semantic versioning:

- MAJOR: Removes or materially redefines a principle or governance requirement.
- MINOR: Adds a new principle/section or materially expands existing obligations.
- PATCH: Clarifies wording, fixes errors, or improves non-semantic guidance.

Compliance review expectations:

- Every planning and review cycle MUST verify alignment with Core Principles.
- Non-compliant changes MUST include a recorded exception and remediation plan.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE): Original adoption date unknown. | **Last Amended**: 2026-05-28
