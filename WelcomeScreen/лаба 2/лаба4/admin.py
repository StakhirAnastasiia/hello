def admin(stock):
    print("\nСклад товарів:")

    for name, quantity in stock.items():
        print(name, "-", quantity, "шт.")

    name = input("Товар для зміни кількості: ").strip().capitalize()

    if name in stock:
        try:
            stock[name] = int(input("Нова кількість: "))
            print("Кількість змінено!")
        except ValueError:
            print("Введи число!")
    else:
        print("Товар не знайдено!")