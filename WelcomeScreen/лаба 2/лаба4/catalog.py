from rich.console import Console
from tabulate import tabulate

console = Console()

def show_catalog(products, stock):
    rows = []

    for name, price in products.items():
        rows.append([name, f"{price:.2f} грн", stock.get(name, 0)])

    console.print("\n[bold cyan]Каталог товарів[/bold cyan]")
    print(tabulate(rows, headers=["Товар", "Ціна", "Кількість"], tablefmt="grid"))