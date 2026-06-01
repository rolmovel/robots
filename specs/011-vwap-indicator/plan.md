# Implementation Plan: VWAP — Volume Weighted Average Price como Indicador de Trading

**Branch**: `011-vwap-indicator` | **Date**: 2026-06-01 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/011-vwap-indicator/spec.md`

## Summary

Add a new educational chapter (`capitulo-09-vwap`) to the course that introduces VWAP (Volume Weighted Average Price) as a technical indicator and trading strategy. The chapter will include two Jupyter notebooks: (1) VWAP concept, calculation, and visualization comparing it with SMA, and (2) a VWAP bounce strategy with backtesting and comparison against other course strategies. The implementation reuses the existing `curso.lib.data` module for data fetching, `curso.lib.backtest` for backtesting, and follows the same notebook structure as previous chapters.

## Technical Context

**Language/Version**: Python 3.11+ (project venv kernel at `.venv-3/`)

**Primary Dependencies**: 
- `numpy>=1.24` — Numerical computation
- `pandas>=2.0` — Time series manipulation, cumulative calculations for VWAP
- `matplotlib>=3.7` — Static visualizations (consistent with existing notebooks)
- `plotly>=5.18` — Interactive plots (used in some existing chapters)
- `yfinance>=0.2.28` — Market data provider (via OpenBB wrapper)
- `backtesting==0.3.3` — Backtesting engine (consistent with existing chapters)

**Storage**: Local CSV/Parquet cache via `curso.lib.data.get_cache_path()` in `data/` directory. Jupyter notebooks in `curso/capitulo-09-vwap/notebooks/`.

**Testing**: Manual notebook execution via `jupyter nbconvert --execute` or VS Code notebook cell execution. Zero error-type output cells is the pass criterion. Visual validation of VWAP charts and backtest results.

**Target Platform**: JupyterLab 4 / VS Code Jupyter extension, macOS (M-series or Intel)

**Project Type**: Educational Jupyter notebook material — course chapters with strategy notebooks

**Performance Goals**: N/A — interactive single-user notebook; VWAP calculation on ~5 years of daily data (~1250 points) is instantaneous

**Constraints**: 
- Must reuse existing `curso.lib.data` module for data fetching (no direct OpenBB calls in notebooks)
- Must follow the same notebook structure as existing chapters: `01_vwap_analysis.ipynb` (VWAP concept, calculation, visualization vs SMA) and `02_vwap_strategy.ipynb` (bounce strategy, signals, backtesting, comparison)
- VWAP will be calculated on daily data only (not intraday minute-by-minute) since `curso.lib.data` provides daily candles
- Must use `from curso.lib import download_historical` pattern for data access
- If a ticker lacks volume data, fall back to SMA-based analysis with a clear warning
- Use the same test tickers as previous chapters (AAPL, MSFT, SPY) for direct comparison

**Scale/Scope**: One new chapter (`capitulo-09-vwap`) with 2 notebooks, 1 README, 1 spec. No modifications to existing chapters or library code. Uses existing backtesting infrastructure.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Spec-First Delivery**: `spec.md` includes three prioritized stories, nine functional
  requirements, edge cases, assumptions, and measurable outcomes (SC-001..005).
- [x] **Independent Value Slices**: P1 (VWAP concept + calculation), P2 (VWAP bounce strategy + backtesting), P3 (multi-temporal VWAP confluence) are independently implementable and testable.
- [x] **Verifiable Outcomes**: Each story has Given/When/Then acceptance scenarios and an
  independent test method (notebook execution, visual validation, Sharpe comparison).
- [x] **Traceable Artifacts**: All changes map to `curso/capitulo-09-vwap/` with
  concrete file paths.
- [x] **Minimal, Explicit Change**: New chapter only; no modifications to existing chapters,
  library code, or project configuration. Complexity justified by educational value of
  introducing volume-weighted analysis to quantitative finance.

## Phase 0: Research

**Status**: No unresolved NEEDS CLARIFICATION in Technical Context. All technical decisions are known from project context and existing chapter patterns.

**Research Tasks**:

1. **VWAP calculation best practices for daily data**: Confirm that cumulative VWAP formula using typical price × volume is standard for daily candle data (not intraday). Verify edge cases for cumulative vs rolling VWAP on daily data.
   - **Approach**: Review quantitative finance literature and existing VWAP implementations in Python libraries.
   - **Output**: Decision on whether to implement cumulative-only VWAP or also support rolling VWAP windows.

2. **VWAP bounce strategy literature review**: Investigate academic and practitioner literature on VWAP as support/resistance. Document typical entry/exit rules, win rates, and Sharpe ratios reported in studies.
   - **Approach**: Search for peer-reviewed papers and reputable trading blogs discussing VWAP mean-reversion strategies.
   - **Output**: Documented strategy parameters and expected performance benchmarks.

3. **Multi-temporal VWAP confluence patterns**: Research how combining VWAPs across different timeframes (daily, weekly, monthly) creates stronger confluence signals.
   - **Approach**: Analyze existing implementations and practitioner discussions on multi-timeframe VWAP strategies.
   - **Output**: Confluence detection algorithm and threshold parameters.

**Research Findings**:

### Finding 1: VWAP Calculation for Daily Data

**Decision**: Use cumulative VWAP from the start of the dataset. A rolling VWAP window (e.g., last 20 days) will also be implemented as an additional feature.

**Rationale**: 
- Cumulative VWAP is the standard definition used by institutional traders and brokers. It represents the volume-weighted average price since the beginning of the analysis window.
- Rolling VWAP provides a complementary view, showing the average price over a recent period weighted by volume.
- Both are computed using the same core formula: `cumsum(typical_price * volume) / cumsum(volume)` for cumulative, and `rolling(N).apply(lambda x: (x['typical_price'] * x['volume']).sum() / x['volume'].sum())` for rolling.

**Alternatives considered**: 
- Intraday VWAP (minute-by-minute) — rejected because `curso.lib.data` provides daily candles only.
- Session VWAP (reset daily for intraday data) — not applicable for daily data.

### Finding 2: VWAP Bounce Strategy Parameters

**Decision**: Implement a VWAP bounce strategy with the following parameters:
- Trend filter: Price > SMA(200) for long, Price < SMA(200) for short
- Entry: Price touches VWAP (within 0.5% tolerance) in the direction of the trend
- Exit: Target profit of 2% or stop-loss of -2% from entry, whichever comes first
- Timeout: Close position after 10 trading days if no exit triggered

**Rationale**:
- VWAP acts as a magnet (mean-reversion) — prices tend to revert to VWAP after deviating significantly.
- The 0.5% tolerance accounts for the discrete nature of daily data (price may gap over VWAP without touching it exactly).
- 2% target / -2% stop provides a 1:1 risk-reward ratio, consistent with mean-reversion strategies.
- 10-day timeout prevents capital from being tied up in stagnant positions.

**Alternatives considered**:
- Volume confirmation on bounce — rejected for P1/P2 as it adds complexity; can be explored in P3.
- Multiple VWAP windows as dynamic bands — too complex for initial implementation.

### Finding 3: Multi-Temporal VWAP Confluence

**Decision**: For P3, implement VWAP calculations on daily, weekly, and monthly resampled data. Confluence zones are identified when two or more VWAP lines are within 1% of each other.

**Rationale**:
- VWAP on different timeframes captures volume-weighted price levels at different horizons.
- Institutional orders often cluster around VWAP levels on multiple timeframes.
- Confluence of VWAPs from daily, weekly, and monthly creates "super zones" of support/resistance.

**Alternatives considered**:
- VWAP bands (VWAP ± standard deviation) — adds complexity; confluence approach is more intuitive for education.

## Phase 1: Design & Contracts

### Data Model

**Entity: VWAP Series**

| Field | Type | Description |
|-------|------|-------------|
| `date` | `datetime.date` | Trading date |
| `vwap_cumulative` | `float` | Cumulative VWAP value |
| `vwap_rolling` | `float` | Rolling VWAP over N-day window (optional) |
| `vwap_weekly` | `float` | VWAP resampled to weekly frequency |
| `vwap_monthly` | `float` | VWAP resampled to monthly frequency |
| `typical_price` | `float` | (High + Low + Close) / 3 |
| `volume` | `float` | Trading volume |

**Entity: VWAP Bounce Signal**

| Field | Type | Description |
|-------|------|-------------|
| `date` | `datetime.date` | Signal date |
| `signal_type` | `str` | "BUY" or "SELL" |
| `entry_price` | `float` | Price at entry |
| `vwap_at_entry` | `float` | VWAP value at entry |
| `distance_to_vwap_pct` | `float` | Percentage distance from price to VWAP |
| `trend_direction` | `str` | "UP" or "DOWN" (based on SMA 200 filter) |
| `exit_price` | `float` | Price at exit (filled when position closes) |
| `pnl_pct` | `float` | Profit/loss as percentage |
| `duration_days` | `int` | Number of days position was held |

**Entity: VWAP Confluence Zone**

| Field | Type | Description |
|-------|------|-------------|
| `date` | `datetime.date` | Date of confluence detection |
| `vwap_daily` | `float` | Daily VWAP value |
| `vwap_weekly` | `float` | Weekly VWAP value |
| `vwap_monthly` | `float` | Monthly VWAP value |
| `confluence_pct` | `float` | Maximum percentage spread between VWAP lines |
| `signal_type` | `str` | "BUY" if price above all VWAPs and bouncing, "SELL" if below |

### Interface Contracts

No external API contracts required. This is an educational notebook chapter with no external service interfaces.

### Quickstart

See `quickstart.md` for step-by-step instructions to run the notebooks.

## Project Structure

### Documentation (this feature)

```text
specs/011-vwap-indicator/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (consolidated from research above)
├── data-model.md        # Phase 1 output (entity definitions from above)
├── quickstart.md        # Phase 1 output (step-by-step run instructions)
├── contracts/           # Phase 1 output (empty — no external interfaces)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
curso/
├── capitulo-09-vwap/                          # NEW: VWAP chapter
│   ├── README.md                               # Chapter overview and VWAP theory
│   ├── spec.md                                 # Chapter-specific strategy spec
│   └── notebooks/
│       ├── 01_vwap_analysis.ipynb              # VWAP concept, calculation, visualization vs SMA
│       └── 02_vwap_strategy.ipynb              # Bounce strategy, signals, backtesting, comparison
```

**Structure Decision**: Single project — educational Jupyter notebook chapter. No new library code required; VWAP computation implemented directly in notebooks using `pandas` cumulative/rolling operations, reusing `curso.lib.data` for data fetching and `curso.lib.backtest` for backtesting.

## Complexity Tracking

No additional complexity beyond the spec. All technical decisions are resolved. No unknowns remain.
