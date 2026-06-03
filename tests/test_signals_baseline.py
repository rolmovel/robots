import pandas as pd
import numpy as np
from curso.lib.signals import calculate_signals


def make_synthetic_series(n: int = 250):
    dates = pd.date_range(end=pd.Timestamp.today(), periods=n, freq="D")
    # create an upward trending close series with noise
    close = np.linspace(100, 150, n) + np.random.normal(scale=0.5, size=n)
    high = close + np.abs(np.random.normal(scale=0.5, size=n))
    low = close - np.abs(np.random.normal(scale=0.5, size=n))
    open_ = close + np.random.normal(scale=0.2, size=n)
    volume = np.random.randint(100, 1000, size=n)
    df = pd.DataFrame({"open": open_, "high": high, "low": low, "close": close, "volume": volume}, index=dates)
    return df


def test_calculate_signals_returns_keys():
    df = make_synthetic_series()
    config = {"strategy_type": "baseline", "params": {"long_sma": 200, "short_sma": 50}}
    result = calculate_signals(df, config)
    expected_keys = [
        "trend",
        "short_sma",
        "long_sma",
        "sma_cross",
        "rsi",
        "vwap",
        "vwap_distance",
        "atr",
        "stop_loss",
        "target",
        "position_size",
        "recommendation",
        "diagnostics",
    ]
    for k in expected_keys:
        assert k in result
