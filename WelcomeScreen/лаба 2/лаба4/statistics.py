import numpy as np
import pandas as pd

def show_statistics(history):
    if not history:
        print("Покупок ще немає!")
        return

    totals = np.array([item["total"] for item in history])
    data = pd.DataFrame({"Суми покупок": totals})

    print(data)
    print("Загальна сума:", round(totals.sum(), 2), "грн")
    print("Середня покупка:", round(totals.mean(), 2), "грн")