# Tasks: Fix notebook 05 execution

**Input**: Design documents from `specs/007-fix-notebook-05/`

**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/

**Tests**: No automated tests requested. Validation is manual clean-kernel notebook execution.

**Organization**: Tasks grouped by user story for independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

---

## Phase 1: Setup

**Purpose**: No project setup required — existing structure is unchanged.

(No tasks — project structure already in place.)

---

## Phase 2: Foundational

**Purpose**: No foundational work required — research confirmed notebook 05 executes without blocking errors in the current environment.

(No tasks.)

---

## Phase 3: User Story 1 - Ejecutar el notebook 05 sin bloqueos (Priority: P1) 🎯 MVP

**Goal**: Normalize the notebook and validate a clean end-to-end execution without blocking errors.

**Independent Test**: Run all code cells of notebook 05 from a clean kernel and confirm all complete without errors.

### Implementation for User Story 1

- [x] T001 [US1] Clear stale outputs and execution counts from curso/capitulo-05-breakout/notebooks/05_backtesting.ipynb to produce a normalized baseline
- [x] T002 [US1] Execute notebook 05 end-to-end from a clean kernel and confirm all cells complete without errors in curso/capitulo-05-breakout/notebooks/05_backtesting.ipynb

**Checkpoint**: All code cells execute without blocking errors and produce expected outputs.

---

## Phase 4: User Story 2 - Identificar con claridad el paso fallido (Priority: P2)

**Goal**: Document the reproduced (or non-reproduced) state with evidence so any future failure is quickly isolable.

**Independent Test**: Confirm that research.md and this tasks file record the outcome of the validation run with enough detail for a reviewer to repeat.

### Implementation for User Story 2

- [x] T003 [US2] Record validation evidence (cell execution order, output summary, environment) in specs/007-fix-notebook-05/research.md if not already present

**Checkpoint**: A reviewer can identify, in under 5 minutes, whether the notebook has a reproducible code defect or not.

---

## Phase 5: User Story 3 - Conservar el valor didactico del analisis (Priority: P3)

**Goal**: Confirm that the analytical outputs (metrics, plots, comparison table) remain present and interpretable after normalization.

**Independent Test**: After T001 normalization and T002 re-execution, verify that backtest metrics, equity/drawdown plots, and trailing-stop table are generated.

### Implementation for User Story 3

- [x] T004 [US3] Verify backtest metrics, equity curve, drawdown plot, and trailing-stop comparison table are all generated after executing notebook 05 in curso/capitulo-05-breakout/notebooks/05_backtesting.ipynb

**Checkpoint**: All analytical outputs from the spec are present and readable.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final validation per quickstart.md

- [x] T005 Run quickstart.md validation per specs/007-fix-notebook-05/quickstart.md

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 3 (US1)**: No dependencies — can start immediately
- **Phase 4 (US2)**: Depends on T002 outcome (needs execution evidence)
- **Phase 5 (US3)**: Depends on T002 outcome (needs generated outputs)
- **Phase 6 (Polish)**: Depends on all prior phases

### Within Each User Story

- T001 before T002 (normalize before executing)
- T003 after T002 (record evidence from the run)
- T004 after T002 (check outputs from the run)

### Parallel Opportunities

- T003 and T004 can run in parallel after T002 completes

---

## Implementation Strategy

**MVP Scope**: User Story 1 only (T001 + T002). Normalize the notebook and validate clean execution.

**Full Delivery**: All 5 tasks. Expected total effort: minimal (notebook normalization + one validation run + evidence recording).

**Change Summary**:
- Clear stale outputs/execution counts from notebook 05
- Run all cells from clean kernel
- Record outcome in research artifact
- Confirm analytical outputs remain intact
