from tabulate import tabulate
def show_history(history):
    if not history:
        print("Історія покупок порожня!")
        return

    rows = [[i + 1, item["total"]] for i, item in enumerate(history)]
    print(tabulate(rows, headers=["№", "Сума (грн)"], tablefmt="grid"))