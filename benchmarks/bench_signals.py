import time
import pandas as pd
import numpy as np
from curso.lib.signals import calculate_signals


def make_series(n=10000):
    dates = pd.date_range(end=pd.Timestamp.today(), periods=n, freq='T')
    close = np.linspace(100, 200, n) + np.random.normal(scale=0.5, size=n)
    df = pd.DataFrame({'open': close, 'high': close*1.001, 'low': close*0.999, 'close': close, 'volume': 1000}, index=dates)
    return df


if __name__ == '__main__':
    df = make_series(5000)
    config = {'strategy_type': 'baseline', 'params': {'long_sma': 200, 'short_sma': 50}}
    t0 = time.time()
    res = calculate_signals(df, config)
    t1 = time.time()
    print('Elapsed:', t1-t0)
    print(res['recommendation'])
