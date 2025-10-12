from datetime import datetime
from save_data import save_data
from stiko_rules import (
    check_tetanus,
    check_diphtheria,
    check_pertussis,
    check_measles,
)

DATE_FORMAT = "%d.%m.%Y"

VACCINATIONS = [
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

def get_user_input():
    print("Willkommen zum Impfzeit-Programm basierend auf Empfehlungen der Ständigen Impfkommission (STIKO)\n")
    
    name = input("Wie ist dein Name? > ").strip()

    birthday_str = input("Wann wurdest du geboren? (TT.MM.JJJJ) > ").strip()
    try:
        birthday = datetime.strptime(birthday_str, DATE_FORMAT)
    except ValueError:
        print("Ungültiges Datum. Bitte im Format TT.MM.JJJJ eingeben.")
        return None

    sex = input("Geschlecht (männlich/weiblich/divers) > ").strip().lower()

    vaccinations = {}
    print("\nBitte gib das Datum deiner letzten Impfung ein (TT.MM.JJJJ). Wenn unbekannt, einfach leer lassen.")
    
    for vaccine in VACCINATIONS:
        date_input = input(f"{vaccine}: ").strip()
        if date_input:
            try:
                date_parsed = datetime.strptime(date_input, DATE_FORMAT).strftime(DATE_FORMAT)
                vaccinations[vaccine] = date_parsed
            except ValueError:
                print("Ungültiges Datum – überspringe diese Impfung.")
                vaccinations[vaccine] = None
        else:
            vaccinations[vaccine] = None

    user_data = {
        "name": name,
        "birthday": birthday.strftime(DATE_FORMAT),
        "sex": sex,
        "vaccinations": vaccinations
    }

    return user_data

def print_evaluation(data):
    print("\nImpfempfehlungen laut STIKO:\n")

    print(f"Tetanus: {check_tetanus(data['birthday'], data['vaccinations'].get('Tetanus'))}")
    print(f"Diphtherie: {check_diphtheria(data['birthday'], data['vaccinations'].get('Diphtherie'))}")
    print(f"Pertussis: {check_pertussis(data['birthday'], data['vaccinations'].get('Pertussis'))}")
    print(f"Masern: {check_measles(data['birthday'], data['vaccinations'].get('Masern'))}")
    print(f"Poliomyelitis: {check_polio(data['birthday'], data['vaccinations'].get('Poliomyelitis'))}")
    print(f"Hepatitis B: {check_hepatitis_b(data['birthday'], data['vaccinations'].get('Hepatitis B'))}")
    print(f"HPV: {check_hpv(data['birthday'], data['vaccinations'].get('HPV'))}")
    print(f"Meningokokken C: {check_meningo_c(data['birthday'], data['vaccinations'].get('Meningokokken C'))}")
    print(f"Mumps: {check_mumps(data['birthday'], data['vaccinations'].get('Mumps'))}")
    print(f"Röteln: {check_rubella(data['birthday'], data['vaccinations'].get('Röteln'))}")
    print(f"Varizellen: {check_varicella(data['birthday'], data['vaccinations'].get('Varizellen'))}")
    print(f"Pneumokokken: {check_pneumococcal(data['birthday'], data['vaccinations'].get('Pneumokokken'))}")
    print(f"Herpes Zoster: {check_herpes_zoster(data['birthday'], data['vaccinations'].get('Herpes Zoster'))}")
    print(f"Influenza: {check_influenza(data['birthday'], data['vaccinations'].get('Influenza'))}")
    print(f"COVID-19: {check_covid19(data['birthday'], data['vaccinations'].get('COVID-19'))}")
    print(f"RSV: {check_rsv(data['birthday'], data['vaccinations'].get('RSV (Respiratorische Synzytial-Viren)'))}")


def main():
    data = get_user_input()
    if data:
        save_data(data)
        print_evaluation(data)

if __name__ == "__main__":
    main()
