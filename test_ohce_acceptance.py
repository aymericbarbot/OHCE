import subprocess, sys, os
from pathlib import Path
SCRIPT = Path(__file__).parent / "ohce.py"

def run_ohce(inputs: str = "", mock_time: str = "10:00", timeout: int = 2):
    proc = subprocess.run(
        [sys.executable, SCRIPT, "--mock-time", mock_time],
        input=inputs.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env={**os.environ, "OHCE_TIMEOUT": "1"},  # timeout court pour ne jamais bloquer
        timeout=timeout
    )
    return proc.stdout.decode().splitlines()

def test_miroir_simple():
    out = run_ohce("test\n")
    # On veut que "tset" apparaisse dans la sortie, peu importe la position
    assert "tset" in out

def test_pytest_marche():
    assert True is True

def test_palindrome_declenche_message():
    out = run_ohce("kayak\n")
    assert "Bien dit !" in out

def test_salue_bonjour():
    out = run_ohce("", mock_time="08:00")
    # la première ligne doit être la salutation
    assert out[0] == "Bonjour !"

def test_salue_bonsoir():
    out = run_ohce("", mock_time="20:00")
    assert out[0] == "Bonsoir !"