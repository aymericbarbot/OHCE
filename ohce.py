import sys, argparse

def mirror(s: str) -> str:
    return s[::-1]

def is_palindrome(s: str) -> bool:
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned and cleaned == cleaned[::-1]

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--mock-time", help="HH:MM (tests)", default=None)
    parser.parse_args(argv)          # on ignore l’heure pour l’instant

    for line in sys.stdin:
        txt = line.rstrip("\n")
        if is_palindrome(txt):
            print("Bien dit !")
        else:
            print(mirror(txt))

if __name__ == "__main__":
    main()