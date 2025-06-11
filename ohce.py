import sys, argparse
from datetime import datetime

def mirror(s: str) -> str:
    return s[::-1]

def is_palindrome(s: str) -> bool:
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned and cleaned == cleaned[::-1]

def greeting(dt=None) -> str:
    dt = dt or datetime.now()
    return "Bonjour !" if 5 <= dt.hour <= 16 else "Bonsoir !"

def _parse_dt(arg):
    if not arg:
        return None
    h, m = map(int, arg.split(":"))
    return datetime.now().replace(hour=h, minute=m, second=0, microsecond=0)

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--mock-time", help="HH:MM (tests)", default=None)
    args = parser.parse_args(argv)

    dt = _parse_dt(args.mock_time)
    print(greeting(dt))                       # salutation affichée avant la boucle

    for line in sys.stdin:
        txt = line.rstrip("\n")
        if is_palindrome(txt):
            print("Bien dit !")
        else:
            print(mirror(txt))

if __name__ == "__main__":
    main()