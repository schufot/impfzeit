import json
from datetime import datetime

DATE_FORMAT = "%d.%m.%Y"

impfstoffe = [
    "Tetanus",
    "Diphtherie",
    "Pertussis",
    "Poliomyelitis",
    "Hepatitis B",
    "HPV",
    "Meningokokken C",
    "Masern",
    "Mumps",
    "Röteln",
    "Varizellen",
    "Pneumokokken",
    "Herpes Zoster",
    "Influenza",
    "COVID-19",
    "RSV (Respiratorische Synzytial-Viren)"
]

def frage_nutzer():
    print("Willkommen zum Impfcheck-Programm der STIKO (basierend auf RKI-Empfehlungen)\n")
    name = input("Wie ist dein Name? > ").strip()

    geburtsdatum_str = input("Wann wurdest du geboren? (TT.MM.JJJJ) > ").strip()
    try:
        geburtsdatum = datetime.strptime(geburtsdatum_str, DATE_FORMAT)
    except ValueError:
        print("Ungültiges Datum. Bitte im Format TT.MM.JJJJ eingeben.")
        return

    geschlecht = input("Geschlecht (männlich/weiblich/divers) > ").strip().lower()

    impfungen = {}

    print("\nBitte gib das Datum deiner letzten Impfung ein (TT.MM.JJJJ). Wenn unbekannt, einfach leer lassen.")
    for impfung in impfstoffe:
        datum = input(f"{impfung}: ").strip()
        if datum:
            try:
                datum = datetime.strptime(datum, DATE_FORMAT).strftime(DATE_FORMAT)
                impfungen[impfung] = datum
            except ValueError:
                print("Ungültiges Datum – überspringe diese Impfung.")
        else:
            impfungen[impfung] = None

    daten = {
        "name": name,
        "geburtsdatum": geburtsdatum.strftime(DATE_FORMAT),
        "geschlecht": geschlecht,
        "impfungen": impfungen
    }

    return daten

def speichere_daten(daten, dateiname="impfstatus.json"):
    try:
        with open(dateiname, "w", encoding="utf-8") as f:
            json.dump(daten, f, indent=4, ensure_ascii=False)
        print(f"\nDeine Daten wurden erfolgreich in '{dateiname}' gespeichert.")
    except Exception as e:
        print(f"Fehler beim Speichern: {e}")

def main():
    daten = frage_nutzer()
    if daten:
        speichere_daten(daten)

if __name__ == "__main__":
    main()
