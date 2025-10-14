import json

def convert_dates_to_str(data):
    result = data.copy()
    result["birthday"] = data["birthday"].strftime(DATE_FORMAT)
    result["vaccinations"] = {
        k: v.strftime(DATE_FORMAT) if v else None
        for k, v in data["vaccinations"].items()
    }
    return result

def save_data(data, filename="vaccination_status.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(convert_dates_to_str(data), f, indent=4, ensure_ascii=False)
        print(f"\nDaten gespeichert in '{filename}'")
    except Exception as e:
        print(f"Fehler beim Speichern: {e}")
