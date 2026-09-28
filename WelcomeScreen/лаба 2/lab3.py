products = {
    "Хліб":25.50,
    "Молоко":42.00,
    "Шоколад":65.90,
    "Сік":55.50,
    "Печево":38.75
}

stock = {
    "Хліб":10,
    "Молоко":8,
    "Шоколад":5,
    "Сік":7,
    "Печево":6
}
cart = []

def show_catalog():
    print("\n--- КАТАЛОГ ТОВАРІВ---")

    for item,price in products.items():
        print(f"{item} - {price:.2f} грн")

def add(cart,*args, **kwards):
    for item in args:
        item = item.strip().title()

        if item in products and stock.get(item, 0)>0:
            cart.extend([item])
            stock.update({item:stock[item]-1})
            print(item,"додано в кошик")
        else:
            print("такого товару немає")

def remove(cart,*args):
    for item in args:
        item = item.strip().title()

        if item in cart:
            cart.remove(item)
            stock[item]+= 1
            print(item,"видалено з кошика")
        else:
            print("такого товару немає в кошику")

def show_cart():
    if not cart:
        print("\nкошик порожній")
        return

    cart.sort()
    print("\n---КОШИК---")
    for item in cart:
        print(item,"-",f"{products.get(item,0):.2f} грн")

    total = sum(map(lambda item:products.get(item,0),cart))
    print("Разом:",f"{total:.2f} грн")

def buy():
    if not cart:
        print("Кошик порожній")
        return

    total = sum(map(lambda item: products.get(item, 0), cart))
    print("Покупка успішна!")
    print("До сплати:", f"{total:.2f} грн")
    cart.clear()

def admin(**kwargs):
    login = input("Логін: ").strip()
    password = input("Пароль: ").strip()

    if login == "admin" and password == "1234":
        print("\n--- ЗАЛИШКИ ---")
        for item, amount in stock.items():
            print(item, "-", amount, "шт.")
    else:
        print("Неправильний логін або пароль")

def main():
    while True:
        print("\n===== МІНІ-МАГАЗИН =====")
        print("1 - Каталог")
        print("2 - Додати товар")
        print("3 - Видалити товар")
        print("4 - Кошик")
        print("5 - Купити")
        print("6 - Адміністратор")
        print("7 - Вихід")

        choice = input("Виберіть дію: ").strip()

        if choice == "1":
            show_catalog()

        elif choice == "2":
            item = input("Введіть товар: ")
            add(cart, item)

        elif choice == "3":
            item = input("Введіть товар: ")
            remove(cart, item)

        elif choice == "4":
            show_cart()

        elif choice == "5":
            buy()

        elif choice == "6":
            admin()

        elif choice == "7":
            break

        else:
            print("Невірний вибір")
    pass

if __name__ == "__main__":
    main()