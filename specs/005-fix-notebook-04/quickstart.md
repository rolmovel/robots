# Quickstart: Verify notebook 04 fix

**Feature**: 005-fix-notebook-04 | **Date**: 2026-05-29

## Prerequisites

- Python 3.11+ with the course virtual environment activated (`./scripts/setup_env.sh`).
- Repository installed in editable mode (`pip install -e .`).

## Verify the library fix

```bash
python -c "
from curso.lib.indicators import bollinger_bands
import pandas as pd
import numpy as np

df = pd.DataFrame({'Close': np.random.randn(50).cumsum() + 100})
bb = bollinger_bands(df, length=20, std=2.0)
assert list(bb.columns) == ['lower', 'middle', 'upper', 'bandwidth', 'percent'], \
    f'Unexpected columns: {list(bb.columns)}'
print('bollinger_bands() columns OK:', list(bb.columns))
"
```

Expected output:

```
bollinger_bands() columns OK: ['lower', 'middle', 'upper', 'bandwidth', 'percent']
```

## Verify the notebook

1. Open `curso/capitulo-04-mean-reversion/notebooks/04_estrategia.ipynb` in JupyterLab or VS Code.
2. Restart the kernel and run all cells.
3. Step 2 ("Calcular Bollinger Bands + ATR") should complete without errors and print signal counts.

## CI validation

The existing CI smoke test (`ci-notebook-smoke.yml`) will execute the notebook
headlessly. Confirm the workflow passes after the fix is merged.
