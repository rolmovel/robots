# Quickstart: Fourier Transform Indicators

## Overview

This chapter introduces Fourier transform analysis as a technical indicator for investment strategies. You will learn how to decompose price series into their frequency components, identify dominant market cycles, and build a trading strategy based on filtered signals.

## Prerequisites

- Python 3.11+ with the project virtual environment activated
- JupyterLab or VS Code Jupyter extension
- All project dependencies installed (`pip install -r curso/requirements.txt`)

## Installation

No new dependencies required. The chapter uses:
- `numpy` — FFT computation (`numpy.fft`)
- `scipy` — Signal processing utilities
- `pandas` — Time series handling
- `matplotlib` / `plotly` — Visualization
- `yfinance` — Market data (via OpenBB wrapper)
- `backtesting` — Backtesting engine

## Getting Started

### Step 1: Activate the Environment

```bash
source .venv-3/bin/activate
```

### Step 2: Run the FFT Analysis Notebook

Open `curso/capitulo-08-fourier-transform/notebooks/01_fft_analysis.ipynb` and execute all cells. This notebook will:

1. Download historical price data for a selected ticker (default: AAPL)
2. Compute the Fast Fourier Transform (FFT) of the price series
3. Generate and display the power spectrum
4. Identify the dominant market cycles
5. Reconstruct the price using only the dominant frequency components

### Step 3: Run the Fourier Strategy Notebook

Open `curso/capitulo-08-fourier-transform/notebooks/02_fourier_strategy.ipynb` and execute all cells. This notebook will:

1. Build a Fourier-based filter using the dominant cycles identified in Step 2
2. Generate trading signals from crossovers between price and filtered signal
3. Execute a backtest using the `backtesting` library
4. Calculate and display performance metrics (Sharpe, Sortino, Max Drawdown, Win Rate)
5. Compare Fourier-based strategy performance against buy & hold
6. (Optional) Compare spectral analysis across multiple tickers

## Expected Output

After running both notebooks, you should see:

- **Power spectrum chart** showing frequency peaks corresponding to dominant cycles
- **Price vs. filtered signal chart** showing the smoothed cyclical component
- **Backtest equity curve** comparing Fourier strategy vs. buy & hold
- **Performance metrics table** with Sharpe Ratio, Max Drawdown, Win Rate, etc.

## Troubleshooting

- **Import errors**: Ensure the project virtual environment is activated and `curso` package is installed (`pip install -e .`)
- **Data download errors**: Check your internet connection; the notebook uses yfinance via OpenBB
- **FFT visualization issues**: If the power spectrum looks noisy, try increasing the lookback period (default: 5 years)
- **Backtesting errors**: Ensure `backtesting==0.3.3` is installed; Bokeh 3.x compatibility is handled in existing notebooks

## Next Steps

After completing this chapter, you can:

- Experiment with different tickers and time periods
- Adjust the number of dominant cycles retained in the filter
- Compare Fourier-based signals with traditional indicators (SMA, RSI, MACD)
- Combine Fourier filtering with other strategies for multi-indicator approaches
