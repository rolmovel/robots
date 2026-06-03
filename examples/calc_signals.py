import pandas as pd
from curso.lib.signals import calculate_signals

# example: create minimal synthetic data
if __name__ == '__main__':
    dates = pd.date_range(end=pd.Timestamp.today(), periods=250, freq='D')
    import numpy as _np
    close = pd.Series(_np.linspace(100, 150, 250), index=dates)
    df = pd.DataFrame({'close': close, 'open': close*0.99, 'high': close*1.01, 'low': close*0.98, 'volume': 1000}, index=dates)
    config = {'strategy_type': 'baseline', 'params': {'long_sma': 200, 'short_sma': 50}}
    result = calculate_signals(df, config)
    print(result)
