# Quickstart: VWAP Indicator Chapter

**Feature**: VWAP Indicator Chapter (`capitulo-09-vwap`)
**Date**: 2026-06-01

## Prerequisites

- Python 3.11+ installed
- Project virtual environment activated: `source .venv-3/bin/activate`
- All dependencies installed: `pip install -r curso/requirements.txt`

## Step 1: Activate the Virtual Environment

```bash
cd /Users/rolmov/Documents/github/sdd-project
source .venv-3/bin/activate
```

## Step 2: Install Dependencies (if not already installed)

```bash
pip install -r curso/requirements.txt
```

Required packages:
- `pandas>=2.0`
- `numpy>=1.24`
- `matplotlib>=3.7`
- `plotly>=5.18`
- `yfinance>=0.2.28`
- `backtesting==0.3.3`

## Step 3: Run Notebook 1 — VWAP Analysis

Open and execute `curso/capitulo-09-vwap/notebooks/01_vwap_analysis.ipynb` in JupyterLab or VS Code.

This notebook covers:
1. Downloading historical data for AAPL, MSFT, and SPY
2. Calculating typical price and cumulative VWAP
3. Calculating rolling VWAP (20-day window)
4. Comparing VWAP vs SMA visualizations
5. Identifying price-VWAP divergence zones

**Expected output**: Three subplots per asset showing price, VWAP, and SMA overlaid. A table of VWAP divergence statistics.

## Step 4: Run Notebook 2 — VWAP Strategy

Open and execute `curso/capitulo-09-vwap/notebooks/02_vwap_strategy.ipynb` in JupyterLab or VS Code.

This notebook covers:
1. Generating VWAP bounce signals (BUY/SELL) with trend filter (SMA 200)
2. Simulating trades with take-profit, stop-loss, and timeout rules
3. Running backtests for AAPL, MSFT, and SPY
4. Comparing VWAP strategy vs buy & hold
5. Comparing VWAP strategy vs SMA cross and RSI momentum (from previous chapters)

**Expected output**: Trade log table, equity curve chart, performance metrics table comparing VWAP strategy against benchmarks.

## Step 5: Validate Results

Each notebook should execute without errors. Verify:

1. **Notebook 1**: VWAP line is visible on price charts, positioned between price extremes. SMA 200 is smoother than VWAP.
2. **Notebook 2**: VWAP strategy generates 10-50 trades per asset over the test period. Sharpe Ratio is between 0.3 and 1.5. Max Drawdown is under 20%.

## Troubleshooting

### ImportError: No module named 'curso.lib'

Ensure you're running from the project root directory:
```bash
cd /Users/rolmov/Documents/github/sdd-project
```

### No volume data for ticker

Some tickers may not have volume data. The notebooks will display a warning and fall back to SMA-based analysis for those tickers.

### Jupyter kernel not found

Select the Python 3.11 kernel:
- In VS Code: `Ctrl+Shift+P` → "Python: Select Interpreter" → Choose `.venv-3`
- In JupyterLab: Kernel → Change Kernel → Python 3.11

### Data download fails

Check your internet connection. The notebooks use yfinance (via OpenBB wrapper) to download data. If downloads are slow, the notebooks cache data locally in the `data/` directory.
