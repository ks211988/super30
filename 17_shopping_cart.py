"""Q17: Menu-driven cart; quantities are whole numbers."""
def add_item(cart, name, price, quantity):
    if not name.strip() or price < 0 or quantity <= 0: raise ValueError("Invalid item, price or quantity")
    # Each name identifies one product. Re-adding updates its unit price.
    old = cart.get(name, {"quantity": 0})
    cart[name] = {"price": price, "quantity": old["quantity"] + quantity}
def remove_item(cart, name):
    if name not in cart: return False
    del cart[name]
    return True
def view_cart(cart):
    if not cart: print("Cart is empty")
    for name, item in cart.items():
        print(f"{name}: {item['quantity']} x ₹{item['price']:.2f} = ₹{item['quantity'] * item['price']:.2f}")
def calculate_total(cart):
    total = 0
    for item in cart.values(): total += item["price"] * item["quantity"]
    return round(total, 2)
def checkout(cart):
    view_cart(cart)
    total = calculate_total(cart)
    print(f"Checkout total: ₹{total:.2f}")
    return total
def main():
    cart = {}
    while True:
        print("\n1 Add  2 Remove  3 View  4 Total  5 Checkout  6 Exit")
        choice = input("Choose: ").strip()
        if choice == "6": break
        if choice == "5": checkout(cart); break
        if choice == "3": view_cart(cart); continue
        if choice == "4": print(f"Total: ₹{calculate_total(cart):.2f}"); continue
        if choice == "2": print("Removed" if remove_item(cart, input("Name: ").strip()) else "Not found"); continue
        if choice == "1":
            try:
                name = input("Name: ").strip()
                price = float(input("Unit price: "))
                quantity = int(input("Quantity: "))
                add_item(cart, name, price, quantity)
                print("Added")
            except ValueError as e: print("Invalid input:", e)
        else: print("Invalid option")
if __name__ == "__main__": main()
