menu = {
    "coffee": 80000,
    "tea": 50000,
    "cake": 120000,
    "latte": 100000,
    "hot chocolate": 90000
}

def show_menu():
    print("\n========== Coffee Menu ==========")

    for product, price in menu.items():
        print(f"{product} : {price:,} Toman")

    print("=================================")
    