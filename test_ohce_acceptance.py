import subprocess, sys, os
from pathlib import Path

def test_pytest_marche():
    assert True is True

def test_miroir_simple():
    out = run_ohce("test\n")
    # On veut que "tset" apparaisse dans la sortie, peu importe la position
    assert "tset" in out