# Research: Fix notebook 04 step 2

**Feature**: 005-fix-notebook-04 | **Date**: 2026-05-29

## Root Cause

**Reproduced error**: `KeyError: 'upper'` at `04_estrategia.ipynb` cell 6 (step "2. Calcular Bollinger Bands + ATR").

The notebook calls:

```python
bb = bollinger_bands(df, length=BB_PERIOD, std=BB_STD)
df['BB_upper'] = bb['upper']
df['BB_middle'] = bb['middle']
df['BB_lower'] = bb['lower']
```

But `bollinger_bands()` in `curso/lib/indicators.py` returns the raw output of
`pandas_ta.bbands()`, whose columns are parameter-encoded:

| pandas_ta column | Expected by notebook |
|------------------|---------------------|
| `BBU_20_2.0`     | `upper`             |
| `BBM_20_2.0`     | `middle`            |
| `BBL_20_2.0`     | `lower`             |
| `BBB_20_2.0`     | (not used)          |
| `BBP_20_2.0`     | (not used)          |

The column names change with different `length`/`std` parameters, making it
impossible for callers to predict names without inspecting the result at runtime.

## Decision

- **Chosen fix**: Normalize column names inside `bollinger_bands()` to return
  `upper`, `middle`, `lower`, `bandwidth`, `percent` — stable names independent
  of the parameters passed.
- **Rationale**: The wrapper's purpose is to shield callers from `pandas_ta`
  internals. The docstring already promises standardized names but the
  implementation omits the rename. Fixing the wrapper is a single-point change
  and prevents every consumer from re-discovering the mismatch.
- **Alternative rejected**: Changing the notebook to use raw column names — this
  would leak library internals into educational content and break if parameters change.

## Blast Radius

| File | Uses `bollinger_bands()` | Accesses columns directly | Affected |
|------|--------------------------|---------------------------|----------|
| `curso/capitulo-04-mean-reversion/notebooks/04_estrategia.ipynb` | ✅ | ✅ (`upper`, `middle`, `lower`) | **Yes** |
| `curso/capitulo-04-mean-reversion/notebooks/04_backtesting.ipynb` | ❌ (inlines its own BB calc) | N/A | No |
| `curso/capitulo-07-agente-autonomo/notebooks/07_estrategia.ipynb` | ✅ (import only, not called for columns) | ❌ | No |

## Verification

After applying the fix, the following must pass:

1. `python -c "from curso.lib.indicators import bollinger_bands; import pandas as pd; df = pd.DataFrame({'Close': range(30)}); bb = bollinger_bands(df); print(list(bb.columns))"` → `['lower', 'middle', 'upper', 'bandwidth', 'percent']`
2. Notebook `04_estrategia.ipynb` executes steps 0 → 1 → 2 without error.
3. CI smoke tests continue to pass.
