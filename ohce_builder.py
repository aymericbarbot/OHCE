from datetime import datetime


class OhceBuilder:
    _DATA = {
        "fr": {
            "greeting_day": "Bonjour !",
            "greeting_night": "Bonsoir !",
            "farewell": "Au revoir !",
            "palindrome": "Bien dit !",
        },
        "en": {
            "greeting_day": "Good morning!",
            "greeting_night": "Good evening!",
            "farewell": "Goodbye!",
            "palindrome": "Well said!",
        },
    }

    def __init__(self, lang: str = "fr"):
        self.lang = lang if lang in self._DATA else "fr"
        self.data = self._DATA[self.lang]

    # ---------- chaînes dépendant de l'heure et/ou du contexte ----------
    def greeting(self, dt: datetime) -> str:
        return (
            self.data["greeting_day"]
            if 5 <= dt.hour <= 16
            else self.data["greeting_night"]
        )

    def farewell(self) -> str:
        return self.data["farewell"]

    def palindrome(self) -> str:
        return self.data["palindrome"]