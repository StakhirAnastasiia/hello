import json
import os
def load_data():
    path = os.path.join(os.path.dirname(file), "..", "history.json")


    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    return []