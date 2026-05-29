# Tasks: Fix `curso` import (pkg_resources)

**Input**: Design documents from `specs/004-fix-curso-import/`

**Prerequisites**: plan.md ✅, spec.md ✅, research.md ✅, data-model.md ✅, contracts/installation.md ✅

**Tests**: No automated tests requested. Each user story includes a reproducible validation task.

**Organization**: Single user story (P1) — tasks are sequential with some parallel opportunities.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[US1]**: User Story 1 — Import `curso` works when running notebooks

---

## Phase 1: Setup

**Purpose**: No new project structure needed; existing `pyproject.toml` and `setup.cfg` already in place.

- [X] T001 Verify existing packaging files are correct in pyproject.toml and setup.cfg

---

## Phase 2: Foundational (Dependency Fix)

**Purpose**: Pin `setuptools<72` to restore `pkg_resources` availability for `pandas_ta`

**⚠️ CRITICAL**: The notebook import chain fails until this phase is complete

- [X] T002 Add `setuptools<72` constraint to curso/requirements.txt
- [X] T003 [P] Pin setuptools in upgrade step in scripts/setup_env.sh (change `pip install --upgrade pip setuptools wheel` to `pip install --upgrade pip "setuptools<72" wheel`)
- [X] T004 [P] Remove pkg_resources shim workaround from scripts/setup_env.sh (lines 40-51)

**Checkpoint**: After this phase, `pkg_resources` is importable in any fresh venv created by `setup_env.sh`

---

## Phase 3: User Story 1 - Import `curso` works when running notebooks (Priority: P1) 🎯 MVP

**Goal**: Students and reviewers can execute notebook cells that import `curso.lib.*` without `ModuleNotFoundError`

**Independent Test**: Run `./scripts/setup_env.sh python3 .venv && source .venv/bin/activate && python -c "from curso.lib.indicators import sma; print('OK')"`

### Validation for User Story 1

- [X] T005 [US1] Recreate venv using scripts/setup_env.sh and verify `import pkg_resources` works
- [X] T006 [US1] Verify `from curso.lib.indicators import sma` succeeds (validates pandas_ta loads)
- [X] T007 [US1] Execute chapter 01 notebook first cell to confirm no ModuleNotFoundError in curso/capitulo-01-media-movil/notebooks/01_estrategia.ipynb

**Checkpoint**: User Story 1 is fully functional — notebooks execute without import errors

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Documentation and CI alignment

- [X] T008 [P] Update specs/004-fix-curso-import/quickstart.md with final verification commands
- [X] T009 [P] Verify CI workflows pass (ci-install-check.yml and ci-notebook-smoke.yml)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — verification only
- **Foundational (Phase 2)**: Depends on Setup — BLOCKS user story validation
- **User Story 1 (Phase 3)**: Depends on Foundational (Phase 2) — validate the fix
- **Polish (Phase 4)**: Depends on User Story 1 passing

### Within Phase 2

- T002 is the core fix (requirements.txt)
- T003 and T004 can run in parallel (both edit `setup_env.sh` but different sections)
- T003 + T004 together ensure the setup script produces a correct venv

### Parallel Opportunities

```text
Phase 2 (after T002):
  T003 [P] Pin setuptools in setup_env.sh upgrade step
  T004 [P] Remove pkg_resources shim from setup_env.sh

Phase 4:
  T008 [P] Update quickstart docs
  T009 [P] Verify CI workflows
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Verify packaging files (T001)
2. Complete Phase 2: Pin setuptools + cleanup (T002, T003, T004)
3. Complete Phase 3: Validate fix works end-to-end (T005, T006, T007)
4. **STOP and VALIDATE**: Run notebook chapter 01 — no errors
5. Complete Phase 4: Docs + CI (T008, T009)

### Suggested MVP Scope

The entire feature IS the MVP — all 9 tasks deliver the single user story. Estimated scope: requirements edit + script edit + validation.
