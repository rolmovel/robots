"""
Módulo de backtesting — Helpers para ejecutar backtesting.py y extraer métricas.

Proporciona funciones para ejecutar backtests, extraer métricas estándar
del curso y comparar múltiples estrategias.
"""

from dataclasses import dataclass

import pandas as pd
from backtesting import Backtest, Strategy


@dataclass
class BacktestMetrics:
    """Métricas estándar de un backtest (alineado con data-model.md)."""

    retorno_total_pct: float
    retorno_anualizado_pct: float
    sharpe_ratio: float
    sortino_ratio: float
    max_drawdown_pct: float
    num_operaciones: int
    win_rate_pct: float
    profit_factor: float
    buy_and_hold_pct: float


def run_backtest(
    data: pd.DataFrame,
    strategy_class: type[Strategy],
    cash: float = 10_000,
    commission: float = 0.002,
    exclusive_orders: bool = True,
    **kwargs,
) -> tuple[pd.Series, "Backtest"]:
    """
    Ejecuta un backtest y devuelve resultados.

    Args:
        data: DataFrame OHLCV con index datetime.
        strategy_class: Clase Strategy de backtesting.py.
        cash: Capital inicial.
        commission: Comisión por operación (0.2% default).
        exclusive_orders: Si True, cierra posición antes de abrir nueva.
        **kwargs: Parámetros adicionales para el Backtest.

    Returns:
        Tuple (stats Series, Backtest instance para plot).
    """
    bt = Backtest(
        data,
        strategy_class,
        cash=cash,
        commission=commission,
        exclusive_orders=exclusive_orders,
        **kwargs,
    )
    stats = bt.run()
    return stats, bt


def extract_metrics(stats: pd.Series) -> BacktestMetrics:
    """
    Extrae métricas estándar del curso desde los resultados de backtesting.py.

    Args:
        stats: Serie de resultados devuelta por Backtest.run().

    Returns:
        BacktestMetrics con los valores extraídos.
    """
    return BacktestMetrics(
        retorno_total_pct=float(stats.get("Return [%]", 0)),
        retorno_anualizado_pct=float(stats.get("Return (Ann.) [%]", 0)),
        sharpe_ratio=float(stats.get("Sharpe Ratio", 0)),
        sortino_ratio=float(stats.get("Sortino Ratio", 0)),
        max_drawdown_pct=float(stats.get("Max. Drawdown [%]", 0)),
        num_operaciones=int(stats.get("# Trades", 0)),
        win_rate_pct=float(stats.get("Win Rate [%]", 0)),
        profit_factor=float(stats.get("Profit Factor", 0)),
        buy_and_hold_pct=float(stats.get("Buy & Hold Return [%]", 0)),
    )


def metrics_to_dataframe(metrics: BacktestMetrics) -> pd.DataFrame:
    """Convierte BacktestMetrics a un DataFrame legible para reporting."""
    data = {
        "Métrica": [
            "Retorno Total (%)",
            "Retorno Anualizado (%)",
            "Sharpe Ratio",
            "Sortino Ratio",
            "Max Drawdown (%)",
            "Nº Operaciones",
            "Win Rate (%)",
            "Profit Factor",
            "Buy & Hold (%)",
        ],
        "Valor": [
            f"{metrics.retorno_total_pct:.2f}",
            f"{metrics.retorno_anualizado_pct:.2f}",
            f"{metrics.sharpe_ratio:.3f}",
            f"{metrics.sortino_ratio:.3f}",
            f"{metrics.max_drawdown_pct:.2f}",
            str(metrics.num_operaciones),
            f"{metrics.win_rate_pct:.2f}",
            f"{metrics.profit_factor:.3f}",
            f"{metrics.buy_and_hold_pct:.2f}",
        ],
    }
    return pd.DataFrame(data)


def compare_strategies(
    results: dict[str, BacktestMetrics],
) -> pd.DataFrame:
    """
    Compara métricas de múltiples estrategias en una tabla.

    Args:
        results: Dict {nombre_estrategia: BacktestMetrics}.

    Returns:
        DataFrame comparativo con una fila por estrategia.
    """
    rows = []
    for name, m in results.items():
        rows.append(
            {
                "Estrategia": name,
                "Retorno (%)": m.retorno_total_pct,
                "CAGR (%)": m.retorno_anualizado_pct,
                "Sharpe": m.sharpe_ratio,
                "Sortino": m.sortino_ratio,
                "Max DD (%)": m.max_drawdown_pct,
                "Trades": m.num_operaciones,
                "Win Rate (%)": m.win_rate_pct,
                "Profit Factor": m.profit_factor,
                "B&H (%)": m.buy_and_hold_pct,
            }
        )
    return pd.DataFrame(rows).set_index("Estrategia")


def optimize_strategy(
    data: pd.DataFrame,
    strategy_class: type[Strategy],
    maximize: str = "Sharpe Ratio",
    cash: float = 10_000,
    commission: float = 0.002,
    **param_ranges,
) -> tuple[pd.Series, "Backtest"]:
    """
    Optimiza parámetros de una estrategia.

    Args:
        data: DataFrame OHLCV.
        strategy_class: Clase Strategy.
        maximize: Métrica a maximizar.
        cash: Capital inicial.
        commission: Comisión.
        **param_ranges: Rangos de parámetros (ej. n1=range(5,50,5)).

    Returns:
        Tuple (stats optimizados, Backtest instance).
    """
    bt = Backtest(
        data,
        strategy_class,
        cash=cash,
        commission=commission,
        exclusive_orders=True,
    )
    stats = bt.optimize(maximize=maximize, **param_ranges)
    return stats, bt
