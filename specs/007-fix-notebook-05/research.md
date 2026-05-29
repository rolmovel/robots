# Research: Fix notebook 05 execution

**Date**: 2026-05-29
**Feature**: 007-fix-notebook-05

## Decision: Treat notebook 05 as currently healthy in the observed environment

**Rationale**: A full ordered execution of `curso/capitulo-05-breakout/notebooks/05_backtesting.ipynb` in the current VS Code notebook environment completed successfully across setup, data loading, strategy definition, backtest, trailing-stop analysis, and conclusions. No blocking error was reproduced.

**Evidence**:
- Setup cell completed and imported `curso.lib` helpers successfully.
- Data cell downloaded `GLD` history and returned 1255 rows.
- Backtest cell produced metrics plus equity and drawdown plots.
- Trailing-stop analysis cell produced a valid comparison table for ATR multipliers 2.0 to 4.0.
- Conclusions cell printed successfully.

**Alternatives considered**:
1. Assume a hidden code defect still exists and plan a code fix immediately.
   Rejected because no reproducible defect was observed in the notebook or helper code path.
2. Widen scope to audit all breakout helpers proactively.
   Rejected because it violates the minimal-change principle without evidence of a defect.
3. Base the feature on reproducible validation first.
   Chosen because it preserves rigor and keeps any future correction tightly scoped.

## Decision: Focus any future implementation on environment- or client-specific reproducibility

**Rationale**: The specification was created from a user report, but the report is not currently reproducible in the observed environment. The most defensible next step is to preserve a validated baseline and, if the issue reappears, isolate whether it depends on notebook client state, saved outputs, or a helper regression.

**Alternatives considered**:
1. Modify notebook logic preemptively.
   Rejected because there is no confirmed failing step.
2. Modify shared helpers to add defensive behavior.
   Rejected because this would add complexity and possible regressions without evidence.

## Best-practice note: Validate notebooks from a clean kernel and normalized state

**Decision**: Use a clean-kernel execution path and prefer normalized notebooks (no stale error outputs) when validating notebook health.

**Rationale**: Prior notebook incidents in this repository have been affected by stale outputs or mismatched interactive state. A clean run is the cheapest discriminating check between a content defect and a client-state problem.

**Alternatives considered**:
1. Trust saved notebook outputs as current truth.
   Rejected because saved outputs can reflect stale errors or prior environments.
2. Add broad environment handling into notebook code.
   Rejected because it expands scope before reproducing a real failure.

## Implementation-Phase Validation (T002)

**Date**: 2026-05-29 | **Environment**: VS Code notebook kernel, Python 3.12

**Procedure**: Cleared all outputs and execution counts (T001), then executed all 6 code cells sequentially from a clean kernel.

| Cell | Description | Result | Key Output |
|------|-------------|--------|------------|
| 1 | Setup/imports | ✓ | "Setup completado ✓" |
| 2 | Data download | ✓ | GLD: 1255 registros |
| 3 | Strategy definition | ✓ | DonchianBreakout class defined |
| 4 | Backtest execution | ✓ | Metrics table + equity curve + drawdown plot |
| 5 | Trailing-stop analysis | ✓ | ATR multiplier comparison (2.0–4.0) |
| 6 | Conclusions | ✓ | Template printed |

**Metrics from step 4**: Return 18.57%, Sharpe 0.256, Max DD -26.58%, 25 trades, Win Rate 36%, Profit Factor 1.439

**Trailing-stop table (step 5)**: Best Sharpe at ATR 4.0 (0.522, Return 48.6%), lowest DD at ATR 2.0 (-17.3%)

**Conclusion**: No code defect reproduced. Notebook 05 executes correctly end-to-end from a normalized, clean-kernel state.

## Conclusion

All technical-context unknowns are resolved for planning. The current implementation path is validation-first: keep the notebook content unchanged unless a clean, reproducible failure is observed during implementation.