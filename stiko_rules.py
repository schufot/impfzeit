# Vaccination rules based on the STIKO calendar
# https://www.rki.de/DE/Themen/Infektionskrankheiten/Impfen/Staendige-Impfkommission/Empfehlungen-der-STIKO/Empfehlungen/Impfkalender.pdf

from datetime import datetime, timedelta

DATE_FORMAT = "%d.%m.%Y"

def parse_date(date_str):
    return datetime.strptime(date_str, DATE_FORMAT)

def check_tetanus(birthday_str, last_vaccination_str):
    if not last_vaccination_str:
        return "Auffrischimpfung empfohlen (kein Datum vorhanden)."
    last_vaccination = parse_date(last_vaccination_str)
    now = datetime.now()
    delta = now - last_vaccination
    if delta.days > 365 * 10:
        return "Auffrischimpfung fällig (letzte Impfung >10 Jahre her)."
    else:
        return "Auffrischimpfung nicht fällig."

def check_diphtheria(birthday_str, last_vaccination_str):
    return check_tetanus(birthday_str, last_vaccination_str)

def check_pertussis(birthday_str, last_vaccination_str):
    if not last_vaccination_str:
        return "Auffrischimpfung empfohlen (kein Datum vorhanden)."
    last_vaccination = parse_date(last_vaccination_str)
    now = datetime.now()
    delta = now - last_vaccination
    if delta.days > 365 * 10:
        return "Auffrischimpfung fällig (letzte Impfung >10 Jahre her)."
    else:
        return "Auffrischimpfung nicht fällig."

def check_measles(birthday_str, last_vaccination_str):
    birthday = parse_date(birthday_str)
    born_after_1970 = birthday.year >= 1970

    if not born_after_1970:
        return "Keine Impfung empfohlen (vor 1970 geboren)."

    if not last_vaccination_str:
        return "MMR-Impfung empfohlen (kein Impfnachweis vorhanden)."

    return "Impfstatus für Masern ausreichend laut STIKO-Empfehlung."

def check_polio(birthday_str, last_vaccination_str):
    if not last_vaccination_str:
        return "Auffrischimpfung empfohlen (kein Datum vorhanden)."
    
    last_vaccination = parse_date(last_vaccination_str)
    now = datetime.now()
    delta = now - last_vaccination

    if delta.days > 365 * 10:
        return "Auffrischimpfung fällig (letzte Impfung >10 Jahre her)."
    else:
        return "Auffrischimpfung nicht fällig."

def check_hepatitis_b(birthday_str, last_vaccination_str):
    if not last_vaccination_str:
        return "Impfung empfohlen bei beruflichem/gesundheitlichem Risiko (kein Nachweis vorhanden)."
    return "Impfung liegt vor – prüfen, ob vollständige Grundimmunisierung erfolgt ist."

def check_hpv(birthday_str, last_vaccination_str):
    birthday = parse_date(birthday_str)
    today = datetime.now()
    age = (today - birthday).days // 365

    if age > 17:
        return "Impfung nicht mehr empfohlen (älter als 17 Jahre)."
    elif not last_vaccination_str:
        return "HPV-Impfung empfohlen (nicht nachgewiesen)."
    else:
        return "HPV-Impfung liegt vor – prüfen, ob vollständig."
