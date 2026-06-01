# Research: VWAP — Volume Weighted Average Price

**Feature**: VWAP Indicator Chapter (`capitulo-09-vwap`)
**Date**: 2026-06-01
**Status**: Completed

## Research Tasks & Findings

### Task 1: VWAP Calculation Best Practices for Daily Data

**Question**: What is the standard formula for VWAP on daily candle data, and should we implement cumulative or rolling VWAP?

**Findings**:

The standard VWAP formula is:
```
VWAP = Σ(Typical Price × Volume) / Σ(Volume)
where Typical Price = (High + Low + Close) / 3
```

For **daily data**, VWAP is typically calculated cumulatively from the start of the analysis window. This is the definition used by institutional brokers (Bloomberg, Refinitiv) and is the most widely recognized form of VWAP in trading literature.

**Cumulative VWAP** (recommended for P1):
```python
cum_tp_vol = (typical_price * volume).cumsum()
cum_vol = volume.cumsum()
vwap_cumulative = cum_tp_vol / cum_vol
```

**Rolling VWAP** (supplementary for P1/P2):
```python
vwap_rolling = (typical_price * volume).rolling(window=N).sum() / volume.rolling(window=N).sum()
```

**Edge Cases**:
- **Zero volume days**: Skip or use forward-fill to avoid division by zero. In practice, markets with zero volume are extremely rare for liquid assets.
- **Missing data**: If volume is NaN for any day, the entire VWAP calculation breaks. Must handle with `ffill()` or drop NaN rows before calculation.
- **First day**: VWAP equals the typical price on the first day (single data point).

**Decision**: Implement both cumulative and rolling VWAP. Cumulative is the primary indicator; rolling (e.g., 20-day) is supplementary.

**Sources**: 
- "Technical Analysis of the Financial Markets" by John J. Murphy
- Bloomberg Professional VWAP documentation
- `pandas` cumulative operations documentation

---

### Task 2: VWAP Bounce Strategy — Entry/Exit Rules and Expected Performance

**Question**: What are the standard entry/exit rules for a VWAP mean-reversion strategy, and what performance benchmarks should we expect?

**Findings**:

VWAP is widely regarded as the "fair price" benchmark used by institutional traders. Price deviations from VWAP tend to revert, making it an effective mean-reversion reference point.

**Standard Strategy Parameters** (from practitioner literature):

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Trend filter | SMA 200 | Trade in direction of long-term trend |
| Entry trigger | Price within 0.5% of VWAP | Daily data granularity requires tolerance |
| Take profit | +2% from entry | 1:1 risk-reward with stop-loss |
| Stop-loss | -2% from entry | Protect against trend reversal |
| Timeout | 10 trading days | Prevent capital lockup |

**Expected Performance** (from backtesting studies on liquid US equities):
- Win rate: 55-65% (mean-reversion strategies typically 55%+)
- Sharpe Ratio: 0.5-1.2 (varies by market regime)
- Max Drawdown: 8-15% (lower than trend-following strategies)
- Average trade duration: 3-7 days

**Key Insight**: VWAP bounce strategies perform best in **ranging/choppy markets** and worst in **strong trending markets**. The SMA 200 filter helps avoid counter-trend bounces that fail.

**Volume Confirmation**: Some practitioners add volume confirmation (e.g., volume on the bounce day should be above average). This is noted as a potential enhancement for P3.

**Decision**: Implement the standard parameters above for P1/P2. Volume confirmation is deferred to P3.

**Sources**:
- "Evidence-Based Technical Analysis" by David Aronson
- Interactive Brokers VWAP strategy documentation
- QuantConnect community VWAP strategy discussions

---

### Task 3: Multi-Temporal VWAP Confluence Patterns

**Question**: How do VWAPs on different timeframes interact, and what confluence patterns create stronger signals?

**Findings**:

When VWAP is calculated on different timeframes (daily, weekly, monthly), each represents a different "horizon" of volume-weighted fair value:

- **Daily VWAP**: Reflects the average price weighted by volume for the entire dataset. Most sensitive.
- **Weekly VWAP**: Resampled to weekly candles, then VWAP calculated. Smoother, captures medium-term institutional positioning.
- **Monthly VWAP**: Resampled to monthly candles. Most stable, represents long-term institutional average cost.

**Confluence Detection**:
When two or more VWAP lines converge (within 1% of each other), it indicates a "super zone" where multiple timeframes agree on fair value. These zones tend to act as stronger support/resistance.

**Algorithm**:
```python
# Calculate VWAP on daily, weekly, monthly resampled data
vwap_daily = calculate_vwap(daily_data)
vwap_weekly = calculate_vwap(weekly_resampled_data)
vwap_monthly = calculate_vwap(monthly_resampled_data)

# Detect confluence
spread_daily_weekly = abs(vwap_daily - vwap_weekly) / vwap_daily
spread_daily_monthly = abs(vwap_daily - vwap_monthly) / vwap_daily
spread_weekly_monthly = abs(vwap_weekly - vwap_monthly) / vwap_weekly

confluence = (spread_daily_weekly < 0.01) | (spread_daily_monthly < 0.01) | (spread_weekly_monthly < 0.01)
```

**Signal Strength**:
- 2 VWAPs in confluence: Moderate confidence signal
- 3 VWAPs in confluence: High confidence signal

**Decision**: Implement confluence detection for P3. Use 1% threshold as default, but make it configurable.

**Sources**:
- "Trading Systems and Methods" by Perry Kaufman
- Multi-timeframe analysis discussions on Quantitative Finance Stack Exchange
- Institutional trading desk VWAP execution strategies

---

### Task 4: Data Access Patterns for the Course

**Question**: How should we fetch data and integrate with the existing course infrastructure?

**Findings**:

The course uses `curso.lib.data.download_historical` for data fetching, which wraps OpenBB/yfinance. This is consistent across all chapters.

**Pattern used in existing chapters**:
```python
from curso.lib import download_historical

df = download_historical(
    ticker="AAPL",
    start="2020-01-01",
    end="2025-12-31",
    interval="1d"
)
```

**Volume data availability**: Most liquid US equities (AAPL, MSFT, SPY, etc.) have volume data. Some obscure tickers or international markets may not. The code should handle missing volume gracefully.

**Caching**: `curso.lib.data.get_cache_path()` provides local caching to avoid repeated downloads.

**Decision**: Use existing `download_historical` pattern. Add volume availability check with SMA fallback.

**Sources**:
- Existing chapter notebooks (capitulo-01 through capitulo-08)
- `curso/lib/data.py` source code
