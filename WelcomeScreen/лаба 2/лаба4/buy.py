from receipt import create_receipt
from save_data import save_data
def buy(products, stock, cart, history):
    if not cart:
        print("Кошик порожній!")
        return

    total = sum(products[item["name"]] * item["quantity"]
                for item in cart)

    print(f"Сума покупки: {total:.2f} грн")
    answer = input("Підтвердити покупку? (так/ні): ")

    if answer.lower() == "так":
        history.append({"total": total})
        create_receipt(total)
        save_data(history)
        cart.clear()
        print("Покупку оформлено!")