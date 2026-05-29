# Tasks: Fix notebook 04 execution at step 2

**Input**: Design documents from `specs/005-fix-notebook-04/`

**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/bollinger-bands.md

**Tests**: Not requested. Each user story includes a reproducible validation task.

**Organization**: Tasks grouped by user story for independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Exact file paths included in descriptions

---

## Phase 1: Setup

**Purpose**: No project initialization needed — existing codebase, single file fix.

- [X] T001 Confirm reproducibility: run notebook `curso/capitulo-04-mean-reversion/notebooks/04_estrategia.ipynb` steps 0→1→2 and capture `KeyError: 'upper'`

---

## Phase 2: Foundational

**Purpose**: Fix the library wrapper that blocks the notebook step 2.

**⚠️ CRITICAL**: User story validation cannot proceed until this is complete.

- [X] T002 Normalize column names in `bollinger_bands()` in `curso/lib/indicators.py` — rename `pandas_ta` output columns to `['lower', 'middle', 'upper', 'bandwidth', 'percent']`
- [X] T003 Update docstring of `bollinger_bands()` in `curso/lib/indicators.py` to document the stable column names returned

**Checkpoint**: Library fix applied — notebook step 2 should now execute without `KeyError`.

---

## Phase 3: User Story 1 — Ejecutar notebook 04 sin bloqueo en paso 2 (Priority: P1) 🎯 MVP

**Goal**: The notebook completes step 2 without errors when run in a prepared environment.

**Independent Test**: Restart kernel, run cells 1→2→3 (setup → data → Bollinger+ATR), confirm no error and signal counts printed.

### Validation for User Story 1

- [X] T004 [US1] Verify `bollinger_bands()` returns correct columns via CLI: `python -c "from curso.lib.indicators import bollinger_bands; ..."` per `specs/005-fix-notebook-04/quickstart.md`
- [X] T005 [US1] Restart kernel and execute notebook `curso/capitulo-04-mean-reversion/notebooks/04_estrategia.ipynb` steps 0→1→2 — confirm step 2 completes and prints signal count
- [X] T006 [US1] Execute remaining notebook steps (3: visualization) to confirm no regression in downstream cells

**Checkpoint**: User Story 1 complete — notebook 04 runs through step 2 without blocking errors.

---

## Phase 4: User Story 2 — Entender rápidamente una precondición incumplida (Priority: P2)

**Goal**: When a precondition for step 2 is missing, the user gets a clear error instead of an opaque `KeyError`.

**Independent Test**: Remove/rename the `Close` column from the DataFrame and confirm the error message names the missing column rather than raising a confusing internal error.

### Implementation for User Story 2

- [X] T007 [US2] Add a precondition check at the top of `bollinger_bands()` in `curso/lib/indicators.py` that raises a clear `KeyError` message when the target `column` is missing from `df`
- [X] T008 [US2] Verify the improved error message by calling `bollinger_bands()` with a DataFrame missing `Close` and confirming the message names the column

**Checkpoint**: Precondition failures surface a clear, actionable message.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and cleanup.

- [X] T009 [P] Clear cached error outputs from `curso/capitulo-04-mean-reversion/notebooks/04_estrategia.ipynb` so the committed notebook shows clean state
- [X] T010 Run quickstart.md full validation sequence per `specs/005-fix-notebook-04/quickstart.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — reproduces the bug.
- **Foundational (Phase 2)**: Depends on Setup — BLOCKS all user stories.
- **User Story 1 (Phase 3)**: Depends on Foundational (T002).
- **User Story 2 (Phase 4)**: Depends on Foundational (T002); independent of US1.
- **Polish (Phase 5)**: Depends on US1 and US2 completion.

### User Story Dependencies

- **User Story 1 (P1)**: Can start immediately after Foundational — no dependency on US2.
- **User Story 2 (P2)**: Can start immediately after Foundational — no dependency on US1.

### Parallel Opportunities

- T004, T005, T006 are sequential (kernel state dependent).
- T007 and T008 are sequential (implement then verify).
- T009 and T010 can run in parallel.
- US1 and US2 can run in parallel after Phase 2.

---

## Parallel Example: After Phase 2

```text
# Both user stories can begin in parallel after T002+T003:
Stream A: T004 → T005 → T006  (US1 validation)
Stream B: T007 → T008          (US2 implementation + verify)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Reproduce bug (T001)
2. Complete Phase 2: Apply library fix (T002, T003)
3. Complete Phase 3: Validate US1 (T004, T005, T006)
4. **STOP and VALIDATE**: Notebook 04 step 2 works ✓
5. Merge if ready — US2 is enhancement, not blocker.

### Incremental Delivery

1. T001 → T002 → T003 → Foundation ready
2. T004 → T005 → T006 → US1 validated (MVP!)
3. T007 → T008 → US2 validated (better error messages)
4. T009 → T010 → Polish complete
