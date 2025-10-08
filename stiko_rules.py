# Vaccination rules based on the STIKO calendar
# https://www.rki.de/DE/Themen/Infektionskrankheiten/Impfen/Staendige-Impfkommission/Empfehlungen-der-STIKO/Empfehlungen/Impfkalender.pdf

from datetime import datetime

DATE_FORMAT = "%d.%m.%Y"

def check_auffrischimpfung(birthdate_str, last_vaccination_str):
    today = datetime.today()

    if is_empty_or_none(last_vaccination_str):
        return "Keine Angabe zur letzten Diphtherie-Impfung – bitte beim Arzt prüfen."

    try:
        last_vaccination = datetime.strptime(last_vaccination_str, DATE_FORMAT)
    except ValueError:
        return "Ungültiges Impfdatum für Diphtherie."

    difference = today - last_vaccination
    years_since = difference.days / 365.25

    if years_since > 10:
        return f"Diphtherie-Auffrischung empfohlen – letzte Impfung liegt über {int(years_since)} Jahren zurück."
    else:
        return f"Diphtherie-Impfung in Ordnung – letzte Impfung vor {int(years_since)} Jahren."

def is_empty_or_none(value):
    return value is None or value.strip() == ""
