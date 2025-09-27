# Impfregeln basierend auf dem STIKO-Kalender
# https://www.rki.de/DE/Themen/Infektionskrankheiten/Impfen/Staendige-Impfkommission/Empfehlungen-der-STIKO/Empfehlungen/Impfkalender.pdf?__blob=publicationFile&v=6

from datetime import datetime, timedelta

DATE_FORMAT = "%d.%m.%Y"

def pruefe_tetanus(geburtsdatum_str, letztes_datum_str):
    heute = datetime.today()

    if nicht_datum(letztes_datum_str):
        return "Keine Angabe zur letzten Tetanus-Impfung – bitte beim Arzt prüfen."

    try:
        letztes_datum = datetime.strptime(letztes_datum_str, DATE_FORMAT)
    except ValueError:
        return "Ungültiges Impfdatum für Tetanus."

    differenz = heute - letztes_datum
    jahre_seit_impfung = differenz.days / 365.25

    if jahre_seit_impfung > 10:
        return f"Tetanus-Auffrischung empfohlen – letzte Impfung liegt über {int(jahre_seit_impfung)} Jahren zurück."
    else:
        return f"Tetanus-Impfung in Ordnung – letzte Impfung vor {int(jahre_seit_impfung)} Jahren."

def nicht_datum(wert):
    return wert is None or wert.strip() == ""

def pruefe_diphtherie(geburtsdatum_str, letztes_datum_str):
    heute = datetime.today()

    if nicht_datum(letztes_datum_str):
        return "Keine Angabe zur letzten Diphtherie-Impfung – bitte beim Arzt prüfen."

    try:
        letztes_datum = datetime.strptime(letztes_datum_str, DATE_FORMAT)
    except ValueError:
        return "Ungültiges Impfdatum für Diphtherie."

    differenz = heute - letztes_datum
    jahre_seit_impfung = differenz.days / 365.25

    if jahre_seit_impfung > 10:
        return f"Diphtherie-Auffrischung empfohlen – letzte Impfung liegt über {int(jahre_seit_impfung)} Jahren zurück."
    else:
        return f"Diphtherie-Impfung in Ordnung – letzte Impfung vor {int(jahre_seit_impfung)} Jahren."
