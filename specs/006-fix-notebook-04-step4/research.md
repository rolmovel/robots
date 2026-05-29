# Research: Fix notebook 04 backtesting step 4

**Date**: 2026-05-29
**Feature**: 006-fix-notebook-04-step4

## Root Cause Analysis

### Decision: Type mismatch in `compare_strategies` invocation

**Rationale**: The step 4 cell in `04_backtesting.ipynb` passes raw `pd.Series` objects (returned by `run_backtest`) directly to `compare_strategies`, which expects `BacktestMetrics` dataclass instances.

**Evidence**:
- Error traceback in notebook output shows failure at `backtest.py:132` where `compare_strategies` tries to access `.retorno_total_pct` on a `pd.Series`.
- The function signature is `compare_strategies(results: dict[str, BacktestMetrics]) -> pd.DataFrame`.
- The notebook already imports `extract_metrics` and uses it correctly in step 3 (`metrics = extract_metrics(stats)`), but step 4 omits this conversion for both `stats` and `stats_up`.

**Alternatives considered**:
1. ~~Modify `compare_strategies` to accept both types~~: Would violate Minimal, Explicit Change and could introduce ambiguity in the library API.
2. ~~Add type coercion inside `compare_strategies`~~: Same issue — changes shared library behavior.
3. **Fix the notebook cell** (chosen): Minimal change, no library impact, consistent with how other steps use the API.

## Usage Pattern Verification

### Correct pattern (step 3 of same notebook):
```python
stats, bt = run_backtest(df, BollingerMeanReversion)
metrics = extract_metrics(stats)
print_metrics_table(metrics_to_dataframe(metrics))
```

### Broken pattern (step 4):
```python
stats_up, _ = run_backtest(df, BollingerUpperExit)
comparison = compare_strategies({'Exit BB Media': stats, 'Exit BB Superior': stats_up})
```

### Correct fix:
```python
stats_up, _ = run_backtest(df, BollingerUpperExit)
metrics_up = extract_metrics(stats_up)
comparison = compare_strategies({'Exit BB Media': metrics, 'Exit BB Superior': metrics_up})
```

Note: `metrics` is already defined in step 3 as `extract_metrics(stats)`, so it can be reused directly.

## Scope Note

Notebook 03 (`03_backtesting.ipynb`) has the same bug pattern in its comparison step, but that is out of scope for this feature per the spec's bounded scope (paso 4 del notebook 04 only).

## Conclusion

All NEEDS CLARIFICATION items resolved. The fix is a single-cell edit with no library changes. Ready for Phase 1 design.
