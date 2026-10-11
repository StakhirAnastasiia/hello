def show_cart(cart):
    if not cart:
        print("Кошик порожній!")
        return

    for item in cart:
        print(item["name"], "-", item["quantity"], "шт.")