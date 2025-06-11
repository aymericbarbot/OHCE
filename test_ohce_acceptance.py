import subprocess, sys, os
from pathlib import Path
SCRIPT = Path(__file__).parent / "ohce.py"

def run_ohce(inputs: str = ""):
    out = run_ohce("test\n")
    # On veut que "tset" apparaisse dans la sortie, peu importe la position
    assert "tset" in out

def test_pytest_marche():
    assert True is True

