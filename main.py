from datetime import datetime
from daten_speichern import speichere_daten
from stiko_regeln import pruefe_tetanus

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
    print("Willkommen zum Impfzeit-Programm basierend auf Empfehlungen der Ständigen Impfkommission\n")
    
    name = input("Wie ist dein Name? > ").strip()

    geburtsdatum_str = input("Wann wurdest du geboren? (TT.MM.JJJJ) > ").strip()
    try:
        geburtsdatum = datetime.strptime(geburtsdatum_str, DATE_FORMAT)
    except ValueError:
        print("Ungültiges Datum. Bitte im Format TT.MM.JJJJ eingeben.")
        return None

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
                impfungen[impfung] = None
        else:
            impfungen[impfung] = None

    daten = {
        "name": name,
        "geburtsdatum": geburtsdatum.strftime(DATE_FORMAT),
        "geschlecht": geschlecht,
        "impfungen": impfungen
    }

    return daten

def auswertung_ausgeben(daten):
    print("\nImpfempfehlungen laut STIKO:\n")

    tetanus_status = pruefe_tetanus(
        daten["geburtsdatum"],
        daten["impfungen"].get("Tetanus")
    )
    print(f"Tetanus: {tetanus_status}")

def main():
    daten = frage_nutzer()
    if daten:
        speichere_daten(daten)
        auswertung_ausgeben(daten)

if __name__ == "__main__":
    main()