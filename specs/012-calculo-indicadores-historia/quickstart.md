# Quickstart: Calculo Indicadores Historia

Ejemplo mínimo de uso (Python):

```python
from curso.lib.signals import calculate_signals, register_strategy
import pandas as pd

# load OHLCV as DataFrame with columns ['open','high','low','close','volume']
data = pd.read_csv('data/XYZ_daily.csv', parse_dates=['date'], index_col='date')

config = {
  'strategy_type': 'baseline',
  'params': {'long_sma': 200, 'short_sma': 50, 'rsi_period': 14, 'risk_pct': 0.01}
}

result = calculate_signals(data, config)
print(result['recommendation'], result['diagnostics'])
```

Registrar una estrategia personalizada:

```python
from curso.lib.signals import register_strategy

class MyStrategy:
    def compute_signals(self, data, config):
        # compute and return SignalResult-like dict
        return {...}

register_strategy('my_strategy', MyStrategy)
``` 

