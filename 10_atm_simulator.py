"""Q10: ATM menu stays active until Exit."""
def main():
    balance = 10000.0
    while True:
        print("\n1 Check balance  2 Deposit  3 Withdraw  4 Exit")
        choice = input("Choose: ").strip()
        if choice == "4": print("Goodbye!"); break
        if choice == "1": print(f"Balance: ₹{balance:.2f}"); continue
        if choice not in ("2", "3"): print("Invalid option"); continue
        try:
            amount = float(input("Amount: "))
            if amount <= 0: print("Amount must be positive"); continue
            if choice == "2": balance += amount; print("Deposit successful")
            elif amount > balance: print("Insufficient funds")
            else: balance -= amount; print("Withdrawal successful")
        except ValueError: print("Enter a valid amount")
if __name__ == "__main__": main()
