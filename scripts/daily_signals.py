#!/usr/bin/env python3
"""Simple daily runner that loads a CSV (or uses example data) and writes JSON summary."""
import argparse
import json
import os
import pathlib
import pandas as pd
from curso.lib.signals import calculate_signals


def run(input_csv: str | None, out_dir: str = "out"):
    if input_csv:
        df = pd.read_csv(input_csv, parse_dates=[0], index_col=0)
    else:
        # generate tiny example
        dates = pd.date_range(end=pd.Timestamp.today(), periods=50, freq='D')
        close = pd.Series(range(50), index=dates)
        df = pd.DataFrame({'close': close, 'open': close, 'high': close, 'low': close, 'volume': 100}, index=dates)
    config = {'strategy_type': 'baseline', 'params': {'long_sma': 20, 'short_sma': 5}}
    result = calculate_signals(df, config)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"signals-{pd.Timestamp.today().date()}.json")
    with open(out_path, 'w') as f:
        json.dump(result, f, default=str)
    print('Wrote', out_path)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--input', help='CSV file with OHLCV')
    p.add_argument('--out', default='out')
    args = p.parse_args()
    run(args.input, args.out)
