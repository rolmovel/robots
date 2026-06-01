# Data Model: Fourier Transform Indicators

## Overview

This document defines the data structures used by the Fourier transform indicators
chapter. All data is in-memory; no new persistent storage or database is required.

## Entities

### PriceDataFrame

The input data structure — a pandas DataFrame with daily price data.

| Field     | Type       | Description                          |
|-----------|------------|--------------------------------------|
| index     | datetime   | Trading date (index, named "date")   |
| Open      | float      | Opening price                        |
| High      | float      | Highest price during the period      |
| Low       | float      | Lowest price during the period       |
| Close     | float      | Closing price (primary analysis target)|
| Volume    | int/float  | Trading volume                       |

**Source**: `curso.lib.data.download_historical()` — fetched via OpenBB/yfinance, cached locally.

**Preprocessing**: Gaps interpolated via `pandas.interpolate(method='linear')` before FFT.

---

### FFTSpectrum

The output of the FFT computation — frequency domain representation of the price series.

| Field       | Type    | Description                                      |
|-------------|---------|--------------------------------------------------|
| frequencies | ndarray | Array of frequencies in cycles per day           |
| power       | ndarray | Power spectrum: `|FFT_coeffs|² / N`              |
| periods     | ndarray | Derived: `252 / frequencies` (annualized → days) |

**Computation**:
```python
import numpy as np
fft_coeffs = np.fft.rfft(close_prices)
power = np.abs(fft_coeffs) ** 2 / len(close_prices)
frequencies = np.fft.rfftfreq(len(close_prices))
```

**Usage**: Identify dominant cycles by finding local maxima in the power spectrum within
a configurable frequency range (default: 5–120 trading days).

---

### DominantCycle

A single dominant cycle extracted from the power spectrum.

| Field     | Type   | Description                              |
|-----------|--------|------------------------------------------|
| period    | float  | Cycle length in trading days             |
| power     | float  | Power (amplitude²) at this frequency     |
| frequency | float  | Frequency in cycles per day              |
| rank      | int    | Rank by power (1 = strongest)            |

**Source**: Top-N peaks from `scipy.signal.find_peaks` on the power spectrum, sorted by power.

---

### FilteredSignal

The reconstructed price series containing only the selected dominant frequency components.

| Field     | Type       | Description                          |
|-----------|------------|--------------------------------------|
| index     | datetime   | Same index as original PriceDataFrame|
| filtered  | ndarray    | Reconstructed signal (same shape as Close) |

**Computation**:
```python
import numpy as np

# Zero out unwanted frequency bins
fft_filtered = fft_coeffs.copy()
fft_filtered[keep_mask] = 0  # keep only dominant cycle bins

# Inverse FFT to reconstruct
filtered_signal = np.fft.irfft(fft_filtered, n=len(close_prices))
```

**Usage**: Generate trading signals via crossover with original price:
- Buy: Price crosses above filtered signal
- Sell: Price crosses below filtered signal

---

### BacktestResult

Output from the `backtesting` library — performance metrics for the Fourier-based strategy.

| Metric          | Type   | Description                              |
|-----------------|--------|------------------------------------------|
| EquityFinal     | float  | Final portfolio value                    |
| Returns         | float  | Total return percentage                  |
| SharpeRatio     | float  | Sharpe ratio (annualized)                |
| SortinoRatio    | float  | Sortino ratio (annualized)               |
| MaxDrawdown     | float  | Maximum drawdown percentage              |
| WinRate         | float  | Percentage of winning trades             |
| ProfitFactor    | float  | Gross profit / gross loss                |
| TotalTrades     | int    | Number of executed trades                |
| AvgTradeDuration| float  | Average trade duration in days           |

**Source**: `backtesting.Backtest` object after `.run()`.

---

## Data Flow

```
PriceDataFrame (Close column)
    │
    ├──► interpolate_gaps() ──► Clean price series
    │
    ├──► np.fft.rfft() ──► FFTSpectrum
    │       │
    │       ├──► find_peaks() ──► List[DominantCycle]
    │       │
    │       └──► Zero out bins ──► Inverse FFT ──► FilteredSignal
    │
    └──► Crossover(Price, FilteredSignal) ──► TradingSignals
            │
            └──► Backtest(TradingSignals) ──► BacktestResult
```

## Constraints

- All data is in-memory; no persistent storage beyond the existing cache mechanism.
- FFT requires zero-padding to next power of 2 for optimal performance.
- Interpolation is required before FFT to avoid spectral leakage from gaps.
- Frequency range for cycle detection: 5–120 trading days (configurable).
- Data frequency: Daily closes only (not intraday).
