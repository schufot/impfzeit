import json

def speichere_daten(daten, dateiname="impfstatus.json"):
    try:
        with open(dateiname, "w", encoding="utf-8") as f:
            json.dump(daten, f, indent=4, ensure_ascii=False)
        print(f"\nDeine Daten wurden erfolgreich in '{dateiname}' gespeichert.")
    except Exception as e:
        print(f"Fehler beim Speichern: {e}")
