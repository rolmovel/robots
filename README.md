# sdd-project

Se añadió el módulo `curso.lib.signals` que provee una API pluggable para calcular señales basadas en indicadores técnicos.

Quickstart

```python
from curso.lib.signals import calculate_signals
import pandas as pd

df = pd.DataFrame(...)  # DataFrame con columnas ['open','high','low','close','volume']
config = {'strategy_type': 'baseline', 'params': {'long_sma': 200, 'short_sma': 50}}
result = calculate_signals(df, config)
print(result['recommendation'], result['diagnostics'])
```

Más detalles en `specs/012-calculo-indicadores-historia/quickstart.md` y `specs/012-calculo-indicadores-historia/spec.md`.
