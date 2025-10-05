from datetime import datetime
from daten_speichern import speichere_daten
from stiko_regeln import pruefe_tetanus, pruefe_diphtherie

DATE_FORMAT = "%d.%m.%Y"

vaccinations = [
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

def ask_user():
    print("Willkommen zum Impfzeit-Programm basierend auf Empfehlungen der Ständigen Impfkommission\n")
    
    name = input("Wie ist dein Name? > ").strip()

    birthday_str = input("Wann wurdest du geboren? (TT.MM.JJJJ) > ").strip()
    try:
        birthday = datetime.strptime(birthday_str, DATE_FORMAT)
    except ValueError:
        print("Ungültiges Datum. Bitte im Format TT.MM.JJJJ eingeben.")
        return None

    sex = input("Geschlecht (männlich/weiblich/divers) > ").strip().lower()

    vaccines = {}
    print("\nBitte gib das Datum deiner letzten Impfung ein (TT.MM.JJJJ). Wenn unbekannt, einfach leer lassen.")
    
    for vaccine in vaccinations:
        datum = input(f"{vaccine}: ").strip()
        if datum:
            try:
                datum = datetime.strptime(datum, DATE_FORMAT).strftime(DATE_FORMAT)
                vaccines[vaccine] = datum
            except ValueError:
                print("Ungültiges Datum – überspringe diese Impfung.")
                vaccines[vaccine] = None
        else:
            vaccines[vaccine] = None

    data = {
        "name": name,
        "birthday": birthday.strftime(DATE_FORMAT),
        "sex": sex,
        "vaccinations": vaccines
    }

    return data

def auswertung_ausgeben(data):
    print("\nImpfempfehlungen laut STIKO:\n")

    tetanus_status = pruefe_tetanus(
        data["birthday"],
        data["impfungen"].get("Tetanus")
    )
    print(f"Tetanus: {tetanus_status}")

    diphtherie_status = pruefe_diphtherie(
        data["birthday"],
        data["impfungen"].get("Diphtherie")
    )
    print(f"Diphtherie: {diphtherie_status}")

def main():
    data = ask_user()
    if data:
        speichere_data(data)
        auswertung_ausgeben(data)

if __name__ == "__main__":
    main()