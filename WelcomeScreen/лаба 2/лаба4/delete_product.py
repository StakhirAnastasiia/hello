def delete_product(cart):
    if not cart:
        print("Кошик порожній!")
        return

    for i, item in enumerate(cart, 1):
        print(i, item["name"])

    try:
        number = int(input("Номер товару: "))
        if 1 <= number <= len(cart):
             cart.pop(number - 1)
             print("Товар видалено!")
    except ValueError:
        print("Введи число!")