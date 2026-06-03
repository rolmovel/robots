# Tasks: Calculo Indicadores Historia

**Input**: Design documents in `specs/012-calculo-indicadores-historia/`

## Phase 1: Setup (Shared Infrastructure)

- [X] T001 [P] Create new module `curso/lib/signals.py` with package exports
- [X] T002 [P] Export `signals` module from `curso/lib/__init__.py` (update import map)
- [X] T003 [P] Add test folder and pytest config: create `tests/` and `pytest.ini`
- [X] T004 Create example script `examples/calc_signals.py` that loads data and calls `calculate_signals()`

---

## Phase 2: Foundational (Blocking Prerequisites)

- [X] T005 Implement `StrategyInterface` and registry in `curso/lib/signals.py`
- [X] T006 Implement `baseline` strategy class in `curso/lib/signals.py` (uses `curso/lib/indicators.py`)
- [X] T007 Implement public API `calculate_signals(data, config)` in `curso/lib/signals.py`
- [X] T008 [P] Add unit tests skeleton `tests/test_signals_baseline.py` verifying API shape and basic output keys
- [X] T009 Add contract test placeholder in `tests/contract/test_signal_contract.py` referencing `specs/012-calculo-indicadores-historia/contracts/signal_contract.md`

**Checkpoint**: Foundation complete — core API and baseline strategy available for story work

---

## Phase 3: User Story 1 - Calcular señales para un activo (Priority: P1) 🎯 MVP

**Goal**: Provide `calculate_signals()` which returns `SignalResult` (trend, sma cross, rsi, vwap_distance, atr, stop/target, position_size, recommendation, diagnostics)

**Independent Test**: Run `tests/test_signals_baseline.py` which asserts `calculate_signals()` returns all keys in `SignalResult` for synthetic OHLCV input.

- [X] T010 [P] [US1] Implement integration with `curso/lib/indicators.py` inside `curso/lib/signals.py` (wrap indicator calls)
- [X] T011 [US1] Add unit test `tests/test_signals_baseline.py::test_signal_result_keys()` asserting keys and types
- [X] T012 [US1] Add example usage in `specs/012-calculo-indicadores-historia/quickstart.md` showing `calculate_signals()` invocation
- [ ] T013 [US1] Add documentation of inputs/outputs in `curso/lib/signals.py` docstring and update repo README

**Checkpoint**: User Story 1 should be independently testable and demoable

---

## Phase 4: User Story 2 - Workflow diario (Priority: P2)

**Goal**: Enable daily execution and logging of results for review

**Independent Test**: `tests/integration/test_daily_workflow.py` runs `examples/calc_signals.py` over a slice of real/synthetic data and asserts output file/summary exists

- [X] T014 [P] [US2] Add a simple runner script `scripts/daily_signals.py` to load data, call `calculate_signals()` and write JSON summary to `out/signals-<date>.json`
- [ ] T015 [US2] Add integration test `tests/integration/test_daily_workflow.py` that runs the script on sample data
- [X] T016 [US2] Add logging and basic CSV/JSON output formatting support in `curso/lib/signals.py` or `scripts/daily_signals.py`

---

## Phase 5: User Story 3 - Configuración parametrizable y estrategias (Priority: P3)

**Goal**: Allow selecting strategy via `config.strategy_type` and registering custom strategies

**Independent Test**: `tests/test_strategy_registration.py` registers a trivial custom strategy and asserts `calculate_signals(..., config={'strategy_type':'custom'})` invokes it

- [ ] T017 [P] [US3] Implement `config` validation logic in `curso/lib/signals.py` (ensure `strategy_type` exists and params match expected keys)
- [X] T018 [US3] Implement runtime `register_strategy(name, cls_or_callable)` helper in `curso/lib/signals.py`
- [X] T019 [US3] Add test `tests/test_strategy_registration.py` demonstrating custom strategy registration and invocation
- [X] T020 [US3] Document strategy types and example `config` schemas in `specs/012-calculo-indicadores-historia/quickstart.md`
 - [X] T017 [P] [US3] Implement `config` validation logic in `curso/lib/signals.py` (ensure `strategy_type` exists and params match expected keys)
 - [X] T018 [US3] Implement runtime `register_strategy(name, cls_or_callable)` helper in `curso/lib/signals.py`
 - [X] T019 [US3] Add test `tests/test_strategy_registration.py` demonstrating custom strategy registration and invocation
 - [X] T020 [US3] Document strategy types and example `config` schemas in `specs/012-calculo-indicadores-historia/quickstart.md`

---

## Phase N: Polish & Cross-Cutting Concerns

- [ ] T021 [P] Add comprehensive README section and docstrings for `curso/lib/signals.py` and `specs/012-calculo-indicadores-historia/quickstart.md`
- [ ] T022 [P] Add CI job or local test script to run the new tests (`pytest tests/test_signals*`)
- [ ] T023 [P] Add small performance benchmark script `benchmarks/bench_signals.py` (optional)
- [X] T024 [P] Ensure `specs/012-calculo-indicadores-historia/tasks.md` references contract file `specs/012-calculo-indicadores-historia/contracts/signal_contract.md`
 - [X] T021 [P] Add comprehensive README section and docstrings for `curso/lib/signals.py` and `specs/012-calculo-indicadores-historia/quickstart.md`
 - [X] T022 [P] Add CI job or local test script to run the new tests (`pytest tests/test_signals*`)
 - [X] T023 [P] Add small performance benchmark script `benchmarks/bench_signals.py` (optional)
 - [X] T024 [P] Ensure `specs/012-calculo-indicadores-historia/tasks.md` references contract file `specs/012-calculo-indicadores-historia/contracts/signal_contract.md`
---

## Dependencies & Execution Order

- Phase 1 → Phase 2 → Phase 3 (US1) → Phase 4 (US2) → Phase 5 (US3) → Polish
- Many file-creation tasks marked `[P]` can be implemented in parallel by different developers.

## Parallel Opportunities

- Files creation tasks (`T001`, `T002`, `T003`, `T004`) can run in parallel
- Unit tests for different stories can be implemented in parallel (`T008`, `T011`, `T015`, `T019`)
- Strategy registration and config validation (`T017`, `T018`) can be implemented in parallel with documentation (`T020`)

## Implementation Strategy (MVP first)

1. Implement Foundation (Phase 1 & 2): `curso/lib/signals.py` with `StrategyInterface`, `baseline`, and `calculate_signals()` (T001..T007)
2. Implement and test User Story 1 (T010..T013) — this is the MVP to validate core behavior
3. Add Workflow support (T014..T016)
4. Add Strategy registration and config validation (T017..T020)
5. Polish, docs, CI and benchmarks (T021..T024)


## Notes

- All tasks include exact file paths where possible
- Each User Story phase includes at least one test task to validate independence
- Tasks prefixed with [P] are parallelizable

