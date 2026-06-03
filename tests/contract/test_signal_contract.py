import os
import pathlib


def test_contract_file_exists():
    contract_path = pathlib.Path("specs/012-calculo-indicadores-historia/contracts/signal_contract.md")
    assert contract_path.exists(), f"Contract file not found: {contract_path}"
