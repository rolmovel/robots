# Tasks: Fix notebook 04 backtesting step 4

**Input**: Design documents from `specs/006-fix-notebook-04-step4/`

**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/

**Tests**: No automated tests requested. Validation is manual notebook execution.

**Organization**: Tasks grouped by user story for independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Include exact file paths in descriptions

---

## Phase 1: Setup

**Purpose**: No setup required — existing project structure is unchanged.

(No tasks — project structure already in place.)

---

## Phase 2: Foundational

**Purpose**: No foundational work required — all library functions are correct and unchanged.

(No tasks — `compare_strategies`, `extract_metrics`, `plot_comparison` work correctly with proper types.)

---

## Phase 3: User Story 1 - Ejecutar paso 4 sin errores (Priority: P1) 🎯 MVP

**Goal**: Fix the type mismatch in step 4 so the cell executes without errors.

**Independent Test**: Run notebook 04 cells sequentially through step 4 — no errors produced.

### Implementation for User Story 1

- [x] T001 [US1] Fix step 4 cell to use extract_metrics() before compare_strategies() in curso/capitulo-04-mean-reversion/notebooks/04_backtesting.ipynb
- [x] T002 [US1] Validate notebook 04 executes steps 1-4 without errors in curso/capitulo-04-mean-reversion/notebooks/04_backtesting.ipynb

**Checkpoint**: Step 4 cell produces comparison DataFrame and bar chart without AttributeError.

---

## Phase 4: User Story 2 - Visualizar comparación entre estrategias (Priority: P2)

**Goal**: Confirm the comparison chart displays correct labels and values for both strategies.

**Independent Test**: Verify bar chart shows "Exit BB Media" and "Exit BB Superior" with valid numeric Sharpe values.

### Implementation for User Story 2

- [x] T003 [US2] Verify comparison DataFrame contains valid metrics for both strategies after executing step 4 in curso/capitulo-04-mean-reversion/notebooks/04_backtesting.ipynb
- [x] T004 [US2] Verify plot_comparison renders bar chart with correct strategy labels in curso/capitulo-04-mean-reversion/notebooks/04_backtesting.ipynb

**Checkpoint**: Comparison visualization shows both strategies with readable, valid metric values.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Full notebook validation end-to-end

- [x] T005 Run full notebook 04 (steps 1-5) sequentially to confirm no regressions in curso/capitulo-04-mean-reversion/notebooks/04_backtesting.ipynb
- [x] T006 Run quickstart.md validation per specs/006-fix-notebook-04-step4/quickstart.md

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 3 (US1)**: No dependencies — can start immediately (single cell edit)
- **Phase 4 (US2)**: Depends on T001 completion (visualization is produced by the same fix)
- **Phase 5 (Polish)**: Depends on Phase 3 and Phase 4

### User Story Dependencies

- **User Story 1 (P1)**: No dependencies. Single cell fix.
- **User Story 2 (P2)**: Depends on US1 fix being applied — the visualization is the output of the corrected cell.

### Within Each User Story

- T001 (fix) before T002 (validate)
- T003 and T004 can run in parallel after T001

### Parallel Opportunities

- T003 and T004 (US2 verification) can run in parallel once T001 is complete
- T005 and T006 (Polish) can run in parallel once US1 and US2 are verified

---

## Parallel Example: User Story 2

```bash
# After T001 (fix applied), launch both verification tasks:
Task T003: "Verify comparison DataFrame contains valid metrics"
Task T004: "Verify plot_comparison renders bar chart with correct labels"
```

---

## Implementation Strategy

**MVP Scope**: User Story 1 only (T001 + T002). This is a 2-line fix in a single notebook cell.

**Full Delivery**: All 6 tasks. Expected total effort: minimal (single cell edit + validation runs).

**Change Summary**:
- Add `metrics_up = extract_metrics(stats_up)` after `run_backtest` call
- Change `compare_strategies({'Exit BB Media': stats, 'Exit BB Superior': stats_up})` to `compare_strategies({'Exit BB Media': metrics, 'Exit BB Superior': metrics_up})`
