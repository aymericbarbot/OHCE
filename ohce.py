import sys, argparse, os, threading 
from datetime import datetime

DEFAULT_TIMEOUT = int(os.getenv("OHCE_TIMEOUT", "60"))

def mirror(s: str) -> str:
    return s[::-1]

def is_palindrome(s: str) -> bool:
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned and cleaned == cleaned[::-1]

def greeting(dt=None) -> str:
    dt = dt or datetime.now()
    return "Bonjour !" if 5 <= dt.hour <= 16 else "Bonsoir !"

def farewell() -> str:
    return "Au revoir !"

def _parse_dt(arg):
    if not arg:
        return None
    h, m = map(int, arg.split(":"))
    return datetime.now().replace(hour=h, minute=m, second=0, microsecond=0)

def _timeout_exit(stop_event: threading.Event):
    """
    Attend DEFAULT_TIMEOUT secondes ; si aucun input n’arrive,
    dit « Au revoir ! » puis coupe net le processus.
    """
    if not stop_event.wait(DEFAULT_TIMEOUT):
        print(farewell())
        os._exit(0) 

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--mock-time", help="HH:MM (tests)", default=None)
    args = parser.parse_args(argv)

    dt = _parse_dt(args.mock_time)
    print(greeting(dt))                       # salutation affichée avant la boucle

    stop = threading.Event()
    threading.Thread(target=_timeout_exit, args=(stop,), daemon=True).start()
    try:
        for line in sys.stdin:
            stop.set()                              # une saisie ⇒ on annule
            text = line.rstrip("\n")

            if is_palindrome(text):
                print("Bien dit !")
            else:
                print(mirror(text))

            # relance un nouveau compte-à-rebours après chaque input
            stop = threading.Event()
            threading.Thread(target=_timeout_exit, args=(stop,), daemon=True).start()
    except KeyboardInterrupt:
        pass

    print(farewell())

if __name__ == "__main__":
    main()