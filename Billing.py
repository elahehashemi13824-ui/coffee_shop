
from Order import orders


def calculate_total():
    total = 0

    for order in orders:
        total += order["price"] * order["quantity"]

    return total


def calculate_discount(total):
    if total > 1000000:
        discount = total * 0.10
    else:
        discount = 0

    return discount


def print_invoice():
    if not orders:
        print("No orders available to print an invoice.")
        return

    total = calculate_total()
    discount = calculate_discount(total)
    final_price = total - discount

    print("\n========== Coffee Shop Invoice ==========")

    for order in orders:
        product_total = order["price"] * order["quantity"]

        print(f"Product: {order['product']}")
        print(f"Quantity: {order['quantity']}")
        print(f"Price: {product_total:,} Toman")
        print("-----------------------------------------")

    print(f"Total Amount: {total:,.0f} Toman")
    print(f"Discount: {discount:,.0f} Toman")
    print(f"Final Payment: {final_price:,.0f} Toman")

    print("=========================================")
