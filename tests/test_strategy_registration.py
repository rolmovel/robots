import pandas as pd
from curso.lib.signals import register_strategy, calculate_signals


class DummyStrategy:
    def __init__(self, params=None):
        self.params = params or {}

    def compute_signals(self, data: pd.DataFrame, config: dict):
        return {"recommendation": "BUY", "diagnostics": {"dummy": True}}


def test_register_and_invoke_custom_strategy():
    register_strategy("dummy", DummyStrategy)
    df = pd.DataFrame({"close": [1, 2, 3, 4, 5]})
    res = calculate_signals(df, {"strategy_type": "dummy", "params": {}})
    assert res["recommendation"] == "BUY"
    assert res["diagnostics"]["dummy"] is True
