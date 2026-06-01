"""
Curso de Inversión en Bolsa — Utilidades compartidas.

Módulos disponibles:
- data: Descarga y cache de datos de mercado vía OpenBB
- indicators: Wrappers de indicadores técnicos (pandas-ta)
- backtest: Helpers para ejecutar backtesting.py y extraer métricas
- reporting: Visualizaciones estándar (equity curve, drawdown, tablas)
"""

from curso.lib.data import download_historical
from curso.lib import data, indicators, backtest, reporting

__all__ = ["download_historical", "data", "indicators", "backtest", "reporting"]
