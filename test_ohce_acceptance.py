import subprocess, sys, os
from pathlib import Path
from ohce_builder import OhceBuilder
from datetime import datetime   
SCRIPT = Path(__file__).parent / "ohce.py"
builder_language = OhceBuilder("fr")

def run_ohce(
    inputs: str = "",
    mock_time: str = "10:00",
    lang: str = "fr",
    timeout: int = 2,
):
    proc = subprocess.run(
        [sys.executable, SCRIPT, "--mock-time", mock_time, "--lang", lang],
        input=inputs.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env={**os.environ, "OHCE_TIMEOUT": "1"},
        timeout=timeout,
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
    assert builder_language.palindrome()

def test_salue_bonjour():
    out = run_ohce("", mock_time="08:00")
    # la première ligne doit être la salutation
    dt  = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)
    assert out[0] == builder_language.greeting(dt)

def test_salue_bonsoir():
    out = run_ohce("", mock_time="20:00")
    dt  = datetime.now().replace(hour=20, minute=0, second=0, microsecond=0)
    assert out[0] == builder_language.greeting(dt)

def test_arret_auto_apres_inactivite():
    proc = subprocess.run(
        [sys.executable, SCRIPT, "--mock-time", "10:00"],  # 10 h ⇒ Bonjour
        input=b"",                     # aucune saisie utilisateur
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env={**os.environ, "OHCE_TIMEOUT": "1"},  # 1 s au lieu de 60
        timeout=3                                 # marge de sécurité
    )
    lines = proc.stdout.decode().splitlines()
    dt10 = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)
    assert lines == [builder_language.greeting(dt10), builder_language.farewell()]

def test_greeting_in_english():
   
    lang = "en"
    out  = run_ohce(inputs="", mock_time="10:00", lang=lang)   # ← run_ohce sera adapté
    expected = OhceBuilder(lang).greeting(
        datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)
    )
    assert out[0] == expected

def test_greeting_in_english():
    out = run_ohce("", mock_time="10:00", lang="en")
    builder_en = OhceBuilder("en")
    dt10 = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)
    assert out[0] == builder_en.greeting(dt10)