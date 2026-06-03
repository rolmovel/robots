"""curso.lib.signals
====================

Módulo de señales y estrategia pluggable.

API principal
- ``register_strategy(name, cls_or_callable)`` — registrar estrategias personalizadas.
- ``calculate_signals(data, config)`` — calcular señales usando la estrategia seleccionada.

`calculate_signals` espera:
- ``data``: ``pandas.DataFrame`` con columnas ``open, high, low, close, volume`` (al menos ``close``).
- ``config``: ``dict`` con clave ``strategy_type`` (str) y ``params`` (dict) con parámetros específicos.

Retorna un ``dict`` serializable con claves: ``trend, short_sma, long_sma, sma_cross, rsi, vwap, vwap_distance, atr, stop_loss, target, position_size, recommendation, diagnostics``.

La implementación inicial registra la estrategia ``baseline`` por defecto.
"""
from __future__ import annotations

from typing import Any, Callable, Dict
import pandas as pd
import numpy as np

# Prefer to use existing indicators implementation when available
try:
    from curso.lib import indicators as _indicators
except Exception:  # optional dependency
    _indicators = None

Registry: Dict[str, Callable] = {}


class StrategyInterface:
    def compute_signals(self, data: pd.DataFrame, config: Dict[str, Any]) -> Dict[str, Any]:
        """Compute signals for the given data and config.

        Must return a JSON-serializable dict following the SignalResult contract.
        """
        raise NotImplementedError()


def register_strategy(name: str, cls_or_callable: Callable) -> None:
    Registry[name] = cls_or_callable


def _sma(series: pd.Series, period: int) -> pd.Series:
    return series.rolling(window=period, min_periods=1).mean()


def _rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    up = delta.clip(lower=0).fillna(0)
    down = -1 * delta.clip(upper=0).fillna(0)
    ma_up = up.ewm(alpha=1 / period, adjust=False).mean()
    ma_down = down.ewm(alpha=1 / period, adjust=False).mean()
    rs = ma_up / (ma_down + 1e-8)
    return 100 - (100 / (1 + rs))


def _atr(df: pd.DataFrame, period: int = 14) -> pd.Series:
    high = df["high"] if "high" in df.columns else df["High"]
    low = df["low"] if "low" in df.columns else df["Low"]
    close = df["close"] if "close" in df.columns else df["Close"]
    tr1 = high - low
    tr2 = (high - close.shift()).abs()
    tr3 = (low - close.shift()).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    return tr.rolling(window=period, min_periods=1).mean()


def _vwap(df: pd.DataFrame) -> pd.Series:
    # typical price * volume cumulative / volume cumulative
    price = df.get("close") if "close" in df.columns else df.get("Close")
    vol = df.get("volume") if "volume" in df.columns else df.get("Volume")
    tp = price * vol
    return tp.cumsum() / (vol.cumsum().replace(0, np.nan))


class BaselineStrategy(StrategyInterface):
    def __init__(self, params: Dict[str, Any] | None = None):
        params = params or {}
        self.long = int(params.get("long_sma", 200))
        self.short = int(params.get("short_sma", 50))
        self.rsi_period = int(params.get("rsi_period", 14))
        self.rsi_overbought = float(params.get("rsi_overbought", 70))
        self.rsi_oversold = float(params.get("rsi_oversold", 30))
        self.risk_pct = float(params.get("risk_pct", 0.01))
        self.capital = float(params.get("capital", 10000.0))

    def compute_signals(self, data: pd.DataFrame, config: Dict[str, Any]) -> Dict[str, Any]:
        df = data.copy()
        # normalize column names to lowercase for convenience
        df.columns = [c if c.islower() else c.lower() for c in df.columns]

        close = df.get("close")
        if close is None:
            raise ValueError("DataFrame must contain a 'close' column")

        # Use existing indicators implementations if available
        if _indicators is not None:
            df_ind = df.copy()
            df_ind.columns = [c.capitalize() for c in df_ind.columns]
            try:
                short_sma = _indicators.sma(df_ind, length=self.short, column="Close")
                long_sma = _indicators.sma(df_ind, length=self.long, column="Close")
                rsi = _indicators.rsi(df_ind, length=self.rsi_period, column="Close")
                atr = _indicators.atr(df_ind, length=14)
            except Exception:
                # fallback to local implementations
                short_sma = _sma(close, self.short)
                long_sma = _sma(close, self.long)
                rsi = _rsi(close, self.rsi_period)
                atr = _atr(df, period=14)
            vwap = _vwap(df)
        else:
            short_sma = _sma(close, self.short)
            long_sma = _sma(close, self.long)
            rsi = _rsi(close, self.rsi_period)
            atr = _atr(df, period=14)
            vwap = _vwap(df)

        # take last two values for cross detection
        idx = -1
        prev = -2 if len(df) >= 2 else -1

        short_now = float(short_sma.iloc[idx])
        long_now = float(long_sma.iloc[idx])
        short_prev = float(short_sma.iloc[prev])
        long_prev = float(long_sma.iloc[prev])
        rsi_now = float(rsi.iloc[idx])
        atr_now = float(atr.iloc[idx])
        vwap_now = float(vwap.iloc[idx])
        close_now = float(close.iloc[idx])

        trend = "UP" if close_now > long_now else "DOWN"

        sma_cross = "NONE"
        if short_prev <= long_prev and short_now > long_now:
            sma_cross = "BULL"
        elif short_prev >= long_prev and short_now < long_now:
            sma_cross = "BEAR"

        vwap_distance = (close_now - vwap_now) / (vwap_now + 1e-8)

        # risk calculations
        stop_loss = close_now - 1.5 * atr_now
        target = close_now + 2.0 * atr_now
        position_size = 0.0
        price_risk = abs(close_now - stop_loss)
        if price_risk > 0:
            position_size = (self.risk_pct * self.capital) / price_risk

        recommendation = "HOLD"
        diagnostics = {
            "trend_filter": trend == "UP",
            "sma_cross": sma_cross,
            "rsi": rsi_now,
            "vwap_distance": vwap_distance,
        }

        # simple decision rule: trend UP + bull cross + not overbought => BUY
        if trend == "UP" and sma_cross == "BULL" and rsi_now < self.rsi_overbought:
            recommendation = "BUY"
        # trend DOWN and bear cross => SELL
        if trend == "DOWN" and sma_cross == "BEAR" and rsi_now > self.rsi_oversold:
            recommendation = "SELL"

        result = {
            "trend": trend,
            "short_sma": short_now,
            "long_sma": long_now,
            "sma_cross": sma_cross,
            "rsi": rsi_now,
            "vwap": vwap_now,
            "vwap_distance": vwap_distance,
            "atr": atr_now,
            "stop_loss": stop_loss,
            "target": target,
            "position_size": position_size,
            "recommendation": recommendation,
            "diagnostics": diagnostics,
        }

        return result


def calculate_signals(data: pd.DataFrame, config: Dict[str, Any]) -> Dict[str, Any]:
    """Public API: calculate signals using selected strategy.

    Args:
        data: OHLCV DataFrame (must include at least `close` column).
        config: dict with `strategy_type` and `params`.
    """
    if not isinstance(config, dict):
        raise ValueError("config must be a dict with 'strategy_type' and optional 'params'.")

    # Basic validation
    strategy_type = config.get("strategy_type", "baseline")
    if not isinstance(strategy_type, str):
        raise ValueError("'strategy_type' must be a string")

    params = config.get("params", {}) or {}
    if not isinstance(params, dict):
        raise ValueError("'params' must be a dict of strategy parameters")

    # If baseline, validate allowed params keys (warn or raise on unexpected keys)
    if strategy_type == "baseline":
        allowed = {"long_sma", "short_sma", "rsi_period", "rsi_overbought", "rsi_oversold", "risk_pct", "capital"}
        unexpected = set(params.keys()) - allowed
        if unexpected:
            raise ValueError(f"Unexpected params for baseline strategy: {unexpected}")

    strategy_cls = Registry.get(strategy_type)
    if strategy_cls is None:
        if strategy_type == "baseline":
            strategy = BaselineStrategy(params)
        else:
            raise ValueError(f"Unknown strategy_type: {strategy_type}")
    else:
        # instantiate if class, or call if callable
        if isinstance(strategy_cls, type):
            strategy = strategy_cls(params)
        else:
            strategy = strategy_cls

    return strategy.compute_signals(data, config)


# register baseline by default
register_strategy("baseline", BaselineStrategy)
