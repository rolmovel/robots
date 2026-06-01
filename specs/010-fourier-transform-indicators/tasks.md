---

description: "Task list for Fourier Transform Indicators chapter"
---

# Tasks: Fourier Transform Indicators for Investment Strategy

**Input**: Design documents from `/specs/010-fourier-transform-indicators/`

**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md (required), quickstart.md (required)

**Tests**: No automated tests requested — each user story validated via notebook execution and visual inspection.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Single project: `curso/` at repository root
- Chapter: `curso/capitulo-08-fourier-transform/`
- Notebooks: `curso/capitulo-08-fourier-transform/notebooks/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the new chapter directory structure

- [ ] T001 Create chapter directory structure at `curso/capitulo-08-fourier-transform/` and `curso/capitulo-08-fourier-transform/notebooks/`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Chapter scaffolding that MUST be complete before any notebook content can be written

**⚠️ CRITICAL**: No notebook implementation can begin until this phase is complete

- [ ] T002 Create chapter README at `curso/capitulo-08-fourier-transform/README.md` with Fourier theory overview (FFT explanation, power spectrum, cycle detection, filtering concepts)
- [ ] T003 Create chapter strategy spec at `curso/capitulo-08-fourier-transform/spec.md` (adapted from feature spec with chapter-specific rules, parameters, and metrics)
- [ ] T004 Create notebook cell templates — verify `curso.lib` import path pattern (`sys.path.insert(0, '../..')`) works from notebooks directory

**Checkpoint**: Foundation ready — notebook content implementation can begin in parallel

---

## Phase 3: User Story 1 — Spectral Decomposition of Prices (Priority: P1) 🎯 MVP

**Goal**: Build `01_fft_analysis.ipynb` that downloads price data, computes FFT, generates power spectrum, identifies dominant cycles, and reconstructs the filtered signal.

**Independent Test**: Execute all cells in `01_fft_analysis.ipynb` end-to-end — verify power spectrum chart displays, dominant cycles are listed with periods in days, and reconstructed filtered signal is plotted alongside original price.

### Implementation for User Story 1

- [ ] T005 [P] [US1] Create notebook file `curso/capitulo-08-fourier-transform/notebooks/01_fft_analysis.ipynb` with markdown header cell (title, chapter reference, objective)
- [ ] T006 [P] [US1] Add setup/import cell: `sys.path.insert(0, '../..')`, import `numpy`, `pandas`, `matplotlib.pyplot`, `scipy.signal`, `curso.lib.data.download_historical`
- [ ] T007 [P] [US1] Add cell to download historical price data for AAPL (5 years, via `curso.lib.data.download_historical`)
- [ ] T008 [US1] Add cell to preprocess data: interpolate gaps, extract Close column, convert to numpy array
- [ ] T009 [US1] Add cell to compute FFT using `numpy.fft.rfft` and power spectrum using `np.abs(fft_coeffs)**2 / N`
- [ ] T010 [US1] Add cell to compute frequencies via `numpy.fft.rfftfreq` and derive periods in trading days (`252 / frequencies`)
- [ ] T011 [US1] Add cell to plot power spectrum chart: x-axis = periods (days), y-axis = power, highlight top-5 dominant cycles
- [ ] T012 [US1] Add cell to identify dominant cycles using `scipy.signal.find_peaks` with configurable parameters (min_distance, prominence)
- [ ] T013 [US1] Add cell to display dominant cycles as a table: rank, period (days), power, frequency
- [ ] T014 [US1] Add cell to construct frequency-domain filter: zero out bins outside selected dominant cycle bands
- [ ] T015 [US1] Add cell to reconstruct filtered signal using `numpy.fft.irfft` and plot overlay: original Close price vs. filtered signal
- [ ] T016 [US1] Add cell with educational commentary: explain what the filtered signal represents, how cycle periods relate to trading opportunities, and limitations of FFT for non-stationary financial data

**Checkpoint**: User Story 1 is complete — `01_fft_analysis.ipynb` runs end-to-end with power spectrum, cycle identification, and filtered signal reconstruction.

---

## Phase 4: User Story 2 — Fourier-Based Trading Strategy (Priority: P2)

**Goal**: Build `02_fourier_strategy.ipynb` that uses FFT filtering to generate crossover trading signals and runs a backtest with performance metrics.

**Independent Test**: Execute all cells in `02_fourier_strategy.ipynb` end-to-end — verify trading signals are generated, backtest runs without errors, and performance metrics table displays Sharpe, Sortino, Max Drawdown, Win Rate, and Profit Factor.

### Implementation for User Story 2

- [ ] T017 [P] [US2] Create notebook file `curso/capitulo-08-fourier-transform/notebooks/02_fourier_strategy.ipynb` with markdown header cell (title, chapter reference, objective)
- [ ] T018 [P] [US2] Add setup/import cell: `sys.path.insert(0, '../..')`, import `numpy`, `pandas`, `matplotlib.pyplot`, `scipy.signal`, `backtesting`, `curso.lib.data.download_historical`, `curso.lib.backtest.run_backtest`, `curso.lib.backtest.BacktestMetrics`
- [ ] T019 [US2] Add cell to download and preprocess price data (same pattern as US1 notebook)
- [ ] T020 [US2] Add cell to compute FFT and identify dominant cycles (reuse US1 logic, parameterized as a function)
- [ ] T021 [US2] Add cell to implement Fourier filter function: takes price series and dominant cycle periods, returns filtered signal
- [ ] T022 [US2] Add cell to generate crossover trading signals: buy when price crosses above filtered signal, sell when price crosses below
- [ ] T023 [US2] Add cell to plot chart: price, filtered signal, buy/sell markers on the time series
- [ ] T024 [US2] Add cell to prepare backtest data: create OHLCV DataFrame with signals as `Position` column for `backtesting.py`
- [ ] T025 [US2] Add cell to define backtesting.py Strategy class that implements Fourier crossover logic (for comparison with pre-computed signals)
- [ ] T026 [US2] Add cell to execute backtest using `curso.lib.backtest.run_backtest()` with pre-computed signals
- [ ] T027 [US2] Add cell to display performance metrics table: Sharpe Ratio, Sortino Ratio, Max Drawdown, Win Rate, Profit Factor, Total Trades, CAGR
- [ ] T028 [US2] Add cell to plot backtest equity curve comparing Fourier strategy vs. Buy & Hold
- [ ] T029 [US2] Add cell with educational commentary: explain how Fourier filtering reduces noise vs. traditional SMA, discuss regime-dependent performance

**Checkpoint**: User Story 2 is complete — `02_fourier_strategy.ipynb` runs end-to-end with signal generation, backtest execution, and comparative performance analysis.

---

## Phase 5: User Story 3 — Multi-Asset Spectral Comparison (Priority: P3)

**Goal**: Add multi-asset spectral comparison section to `02_fourier_strategy.ipynb` (or as a separate section) to rank assets by cyclical stability.

**Independent Test**: Execute the multi-asset section in `02_fourier_strategy.ipynb` — verify spectral comparison chart displays for 3-5 tickers, assets are ranked by cycle stability, and the comparison is visually interpretable.

### Implementation for User Story 3

- [ ] T030 [P] [US3] Add cell to download historical data for multiple tickers (AAPL, MSFT, GOOGL, AMZN, META) using `curso.lib.data.download_multiple()`
- [ ] T031 [US3] Add cell to compute power spectrum for each ticker and extract dominant cycles
- [ ] T032 [US3] Add cell to create comparison chart: power spectrum overlay for all tickers (different colors)
- [ ] T033 [US3] Add cell to create cycle stability ranking table: ticker, dominant period, power, stability score (coefficient of variation of top-3 cycle powers)
- [ ] T034 [US3] Add cell with educational commentary: explain how cyclical stability relates to predictability, discuss which assets are better suited for Fourier-based strategies

**Checkpoint**: User Story 3 is complete — multi-asset spectral comparison adds universe selection capability based on objective cyclical properties.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final validation, documentation, and consistency checks

- [ ] T035 Update `.github/copilot-instructions.md` to reference `specs/010-fourier-transform-indicators/plan.md` (if not already updated)
- [ ] T036 Update `curso/README.md` to include Chapter 08 in the course structure listing
- [ ] T037 Validate both notebooks execute without errors: run `jupyter nbconvert --execute curso/capitulo-08-fourier-transform/notebooks/01_fft_analysis.ipynb --to notebook --execute` and same for `02_fourier_strategy.ipynb`
- [ ] T038 Review and clean up all markdown cells: ensure consistent Spanish language tone matching existing chapters, verify all math equations render correctly
- [ ] T039 Verify all cell outputs are clear and readable (charts fit within viewport, tables are well-formatted)
- [ ] T040 Update `specs/010-fourier-transform-indicators/checklists/requirements.md` to mark spec implementation as complete

---

## Dependencies

```
Phase 1 (Setup)
    └── Phase 2 (Foundational)
            ├── Phase 3 (US1: FFT Analysis) ───┐
            ├── Phase 4 (US2: Strategy) ───────┤
            └── Phase 5 (US3: Multi-Asset) ────┘
                                                    │
                                            Phase 6 (Polish)
```

**Story Completion Order**: US1 (MVP) → US2 → US3

## Parallel Execution Examples

- **Phase 2**: T002 (README), T003 (spec.md), T004 (import validation) can run in parallel
- **Phase 3**: T005-T006 (notebook skeleton + imports) → T007-T016 (sequential content cells)
- **Phase 4**: T017-T018 (notebook skeleton + imports) → T019-T029 (sequential content cells)
- **Phase 5**: T030 (data download) → T031-T034 (sequential comparison cells)

## Implementation Strategy

1. **MVP (US1)**: Create `01_fft_analysis.ipynb` — delivers standalone educational value (FFT theory, spectrum visualization, cycle extraction). This is the minimum viable deliverable.
2. **Core Strategy (US2)**: Create `02_fourier_strategy.ipynb` — delivers the trading strategy with backtesting, the primary value proposition.
3. **Enhancement (US3)**: Add multi-asset comparison — enhances the strategy by enabling objective asset selection based on spectral properties.
4. **Polish (Phase 6)**: Validate, document, and ensure consistency with existing course material.

## Success Criteria Mapping

| Criterion | Task(s) |
|-----------|---------|
| SC-001: Spectrum visualization in <5 min | T005-T016 (US1 notebook runs end-to-end) |
| SC-002: Sharpe comparable to existing strategies | T026-T028 (backtest execution and comparison) |
| SC-003: Multi-asset comparison (5 tickers) | T030-T033 (multi-asset download and ranking) |
| SC-004: Error-free notebook execution | T037 (nbconvert validation) |
| SC-005: Clear visualizations | T038-T039 (review and cleanup) |
