# Quickstart: Fix Backtesting Notebook – Capítulo 01

**Feature**: 008-fix-backtesting-01
**Target file**: `curso/capitulo-01-media-movil/notebooks/01_backtesting.ipynb`

## What This Fix Does

This feature resolves two issues in `01_backtesting.ipynb`:

1. **Cell 12** – `bt.plot()` throws `ValueError` (Bokeh 3.x API incompatibility).
   Fix: wrap the call in a `try/except ValueError` block with an informative message.

2. **Cell 16** – Conclusions contain `[placeholder]` text.
   Fix: replace with the concrete backtest values observed during development.

## Prerequisites

- Project virtual environment activated (`.venv/`)
- `backtesting==0.3.3` and `bokeh==3.9.0` installed (as specified in `requirements.txt`)
- JupyterLab or VS Code with Jupyter extension

## How to Verify the Fix

```bash
# From the project root with .venv activated
jupyter nbconvert --to notebook --execute \
  curso/capitulo-01-media-movil/notebooks/01_backtesting.ipynb \
  --output 01_backtesting_executed.ipynb 2>&1 | tail -5

# Should end with:
# [NbConvertApp] Writing ... bytes to 01_backtesting_executed.ipynb

# Check for error cells
python -c "
import json
nb = json.load(open('01_backtesting_executed.ipynb'))
errs = [i for i,c in enumerate(nb['cells'])
        if any(o.get('output_type')=='error' for o in c.get('outputs',[]))]
print('Error cells:', errs if errs else 'None — all cells passed ✓')
"
```

## Expected Output After Fix

| Cell | Expected output |
|------|----------------|
| 12 | `⚠️ bt.plot() no disponible con Bokeh 3.x. Ver equity curve (celda anterior).` |
| 14 | Numeric comparison table (retorno 2.85%, B&H 39.43%, Max DD -9.05%) |
| 16 | Concrete conclusions with backtest numbers, no `[...]` placeholders |

## Known Limitation

The `bt.plot()` interactive chart is **not rendered** in this environment due to the
Bokeh 3.x / backtesting 0.3.3 incompatibility. The matplotlib equity curve (cell 10)
remains available as a visual summary. To restore full interactive plotting, either:

- Wait for a backtesting.py release that supports Bokeh 3.x, or
- Run the notebook in an isolated environment with Bokeh `<3.0`.
