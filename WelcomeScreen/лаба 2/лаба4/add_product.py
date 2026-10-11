def add_product(products, stock, cart):
    name = input("Назва товару: ").strip().capitalize()

    if name not in products:
       print("Товар не знайдено!")
       return

    try:
       quantity = int(input("Кількість: "))

       if 0 < quantity <= stock[name]:
           cart.append({"name": name, "quantity": quantity})
           stock[name] -= quantity
           print("Товар додано!")
       else:
           print("Недостатня кількість!")
    except ValueError:
        print("Введи число!")