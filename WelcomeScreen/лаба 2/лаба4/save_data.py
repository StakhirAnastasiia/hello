import json
import os

def save_data(data):
    path = os.path.join(os.path.dirname(__file__), "..", "history.json")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Історію збережено!")