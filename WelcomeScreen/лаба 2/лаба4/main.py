from art import text2art
from colorama import init, Fore
import emoji

from catalog import show_catalog
from add_product import add_product
from delete_product import delete_product
from show_cart import show_cart
from buy import buy
from admin import admin
from history import show_history

init(autoreset=True)


def main():
    print(Fore.CYAN + text2art("MY SHOP"))
    print(emoji.emojize("Welcome to my store :shopping_bags:"))
    products = {
        "Хліб": 25.50,
        "Молоко": 42.00,
        "Шоколад": 65.90,
        "Сік": 55.50,
        "Печиво": 38.75
    }

    stock = {
         "Хліб": 10,
         "Молоко": 8,
         "Шоколад": 5,
         "Сік": 7,
         "Печиво": 6
    }

    cart = []
    history = []

    while True:
        print("\n1. Каталог товарів")
        print("2. Додати товар у кошик")
        print("3. Видалити товар із кошика")
        print("4. Переглянути кошик")
        print("5. Купити товари")
        print("6. Адміністрування")
        print("7. Історія покупок")
        print("0. Вихід")

        choice = input("Вибери дію: ")

        if choice == "1":
            show_catalog(products, stock)

        elif choice == "2":
            add_product(products, stock, cart)

        elif choice == "3":
            delete_product(cart)

        elif choice == "4":
           show_cart(cart)

        elif choice == "5":
            buy(products, stock, cart, history)

        elif choice == "6":
           admin(stock)

        elif choice == "7":
           show_history(history)

        elif choice == "0":
            print("Дякую за покупку!")
            break

        else:
            print(Fore.RED + "Неправильний вибір!")
if __name__ == "__main__":
    main()