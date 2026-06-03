import shutil
import subprocess
import pathlib


def test_daily_runner_writes_output(tmp_path):
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    # call the runner script
    script = pathlib.Path("scripts/daily_signals.py")
    assert script.exists()
    subprocess.check_call(["python", str(script), "--out", str(out_dir)])
    files = list(out_dir.glob("signals-*.json"))
    assert len(files) == 1