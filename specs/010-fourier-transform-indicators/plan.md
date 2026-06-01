# Implementation Plan: Fourier Transform Indicators for Investment Strategy

**Branch**: `010-fourier-transform-indicators` | **Date**: 2026-06-01 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/010-fourier-transform-indicators/spec.md`

## Summary

Add a new educational chapter (`capitulo-08-fourier-transform`) to the course that introduces Fourier transform analysis as a technical indicator for investment strategies. The chapter will include two Jupyter notebooks: (1) spectral decomposition and cycle identification using FFT, and (2) a Fourier-based trading strategy with backtesting. The implementation reuses the existing `curso.lib.data` module for data fetching, `curso.lib.backtest` for backtesting, and follows the same notebook structure as previous chapters.

## Technical Context

**Language/Version**: Python 3.11+ (project venv kernel at `.venv-3/`)

**Primary Dependencies**: 
- `numpy>=1.24` — FFT computation (`numpy.fft`)
- `scipy>=1.11` — Signal processing (`scipy.signal`, `scipy.fft`)
- `pandas>=2.0` — Time series manipulation
- `matplotlib>=3.7` — Static visualizations (consistent with existing notebooks)
- `plotly>=5.18` — Interactive plots (used in some existing chapters)
- `yfinance>=0.2.28` — Market data provider (via OpenBB wrapper)
- `backtesting==0.3.3` — Backtesting engine (consistent with existing chapters)

**Storage**: Local CSV/Parquet cache via `curso.lib.data.get_cache_path()` in `data/` directory. Jupyter notebooks in `curso/capitulo-08-fourier-transform/notebooks/`.

**Testing**: Manual notebook execution via `jupyter nbconvert --execute` or VS Code notebook cell execution. Zero error-type output cells is the pass criterion. Visual validation of FFT spectra and backtest charts.

**Target Platform**: JupyterLab 4 / VS Code Jupyter extension, macOS (M-series or Intel)

**Project Type**: Educational Jupyter notebook material — course chapters with strategy notebooks

**Performance Goals**: N/A — interactive single-user notebook; FFT on ~5 years of daily data (~1250 points) completes in <1 second

**Constraints**: 
- Must reuse existing `curso.lib.data` module for data fetching (no direct OpenBB calls in notebooks)
- Must follow the same notebook structure as existing chapters: `01_analysis.ipynb` (FFT + spectrum + cycles) and `02_strategy.ipynb` (filtering + signals + backtest)
- Must handle non-power-of-2 time series lengths via zero-padding
- Must interpolate data gaps before FFT to avoid spectral artifacts
- Must use `from curso.lib import download_historical` pattern for data access

**Scale/Scope**: One new chapter (`capitulo-08-fourier-transform`) with 2 notebooks, 1 README, 1 spec. No modifications to existing chapters or library code. Uses existing backtesting infrastructure.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Spec-First Delivery**: `spec.md` includes three prioritized stories, nine functional
  requirements, edge cases, assumptions, and measurable outcomes (SC-001..005).
- [x] **Independent Value Slices**: P1 (FFT + spectrum visualization), P2 (Fourier filtering +
  backtesting), P3 (multi-asset spectral comparison) are independently implementable and
  testable.
- [x] **Verifiable Outcomes**: Each story has Given/When/Then acceptance scenarios and an
  independent test method (notebook execution, visual validation, Sharpe comparison).
- [x] **Traceable Artifacts**: All changes map to `curso/capitulo-08-fourier-transform/` with
  concrete file paths.
- [x] **Minimal, Explicit Change**: New chapter only; no modifications to existing chapters,
  library code, or project configuration. Complexity justified by educational value of
  introducing signal processing to quantitative finance.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- Spec-First Delivery: `spec.md` includes prioritized stories, requirements, assumptions,
  edge cases, and measurable outcomes.
- Independent Value Slices: User stories are independently implementable and testable.
- Verifiable Outcomes: Each story has acceptance scenarios and a reproducible validation method.
- Traceable Artifacts: Planned work maps directly to stories and target file paths.
- Minimal, Explicit Change: Added complexity includes documented rationale in this plan.

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
curso/
├── capitulo-08-fourier-transform/          # NEW: Fourier transform chapter
│   ├── README.md                            # Chapter overview and theory
│   ├── spec.md                              # Chapter-specific strategy spec
│   └── notebooks/
│       ├── 01_fft_analysis.ipynb            # FFT, power spectrum, cycle extraction
│       └── 02_fourier_strategy.ipynb        # Filtering, signals, backtesting, comparison
```

**Structure Decision**: Single project — educational Jupyter notebook chapter. No new library code required; FFT computation and filtering implemented directly in notebooks using `numpy.fft` and `scipy.signal`, reusing `curso.lib.data` for data fetching and `curso.lib.backtest` for backtesting.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | No constitutional violations identified | — |

## Implementation Phases

### Phase 0: Research (No NEEDS CLARIFICATION items)

All technical decisions are resolved from the spec:
- FFT via `numpy.fft.rfft` (real-valued FFT, most efficient for price series)
- Power spectrum: `np.abs(fft_coeffs)**2 / N`
- Cycle extraction: argmax of power spectrum in frequency range [5, 120] days
- Filtering: zero out unwanted frequency bins, inverse FFT via `numpy.fft.irfft`
- Gap handling: linear interpolation before FFT (consistent with `curso.lib.data.interpolate_gaps`)
- Padding: zero-pad to next power of 2 for optimal FFT performance

**Output**: No `research.md` needed — all decisions are standard signal processing practices with no open questions.

### Phase 1: Design Artifacts

#### 1. Data Model

The feature operates on existing data models:
- **Price DataFrame**: Index=`datetime`, Columns=`Open, High, Low, Close, Volume` (from `curso.lib.data.download_historical`)
- **FFT Spectrum**: Two arrays — frequencies (Hz or cycles/day) and power (magnitude²)
- **Cycles**: List of tuples `(period_days, power, frequency)` for dominant cycles
- **Filtered Signal**: Same shape as price series, containing only selected frequency components

No new database or persistent storage required. All computations are in-memory.

#### 2. Contracts

No external API contracts required. This is an educational notebook chapter that:
- Consumes data via existing `curso.lib.data` (internal library)
- Produces Jupyter notebook outputs (visualizations, backtest results)
- Does not expose any new interfaces to other systems

#### 3. Quickstart

See `quickstart.md` (generated below).

#### 4. Agent Context Update

Update `.github/copilot-instructions.md` to reference this plan.

## Re-evaluated Constitution Check (Post-Design)

- [x] **Spec-First Delivery**: Plan faithfully implements all spec requirements.
- [x] **Independent Value Slices**: P1 → `01_fft_analysis.ipynb`; P2 → `02_fourier_strategy.ipynb`; P3 → multi-asset extension in `02_fourier_strategy.ipynb`.
- [x] **Verifiable Outcomes**: Each notebook cell has clear expected output; backtest metrics are measurable.
- [x] **Traceable Artifacts**: All file paths documented above.
- [x] **Minimal, Explicit Change**: Only new chapter created; zero changes to existing code.
