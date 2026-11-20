
from Menu import menu

orders = []


def add_order():
    product = input("Enter product name: ").lower().strip()

    if product not in menu:
        print("Sorry! This product is not available.")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        order = {
            "product": product,
            "price": menu[product],
            "quantity": quantity
        }

        orders.append(order)

        print("Order added successfully!")

    except ValueError:
        print("Please enter a valid number.")


def show_orders():
    if not orders:
        print("No orders have been registered yet.")
        return

    print("\n========== Your Orders ==========")

    for order in orders:
        print(f"Product: {order['product']}")
        print(f"Price: {order['price']:,} Toman")
        print(f"Quantity: {order['quantity']}")
        print("---------------------------------")
