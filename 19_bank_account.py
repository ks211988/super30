"""Q19: Bank mini application with balance and transaction history."""
def deposit(account, amount):
    if amount <= 0: raise ValueError("Amount must be positive")
    account["balance"] = round(account["balance"] + amount, 2)
    account["history"].append(f"Deposit ₹{amount:.2f}")
def withdraw(account, amount):
    if amount <= 0: raise ValueError("Amount must be positive")
    if amount > account["balance"]: raise ValueError("Insufficient balance")
    account["balance"] = round(account["balance"] - amount, 2)
    account["history"].append(f"Withdrawal ₹{amount:.2f}")
def check_balance(account): return account["balance"]
def transaction_history(account): return list(account["history"])
def main():
    account = {"balance": 10000.0, "history": []}
    while True:
        print("\n1 Deposit  2 Withdraw  3 Balance  4 History  5 Exit")
        choice = input("Choose: ").strip()
        if choice == "5": break
        if choice == "3": print(f"Balance: ₹{check_balance(account):.2f}"); continue
        if choice == "4":
            for entry in transaction_history(account): print(entry)
            continue
        if choice in ("1", "2"):
            try:
                amount = float(input("Amount: "))
                if choice == "1": deposit(account, amount)
                else: withdraw(account, amount)
                print("Transaction successful")
            except ValueError as e: print("Error:", e)
        else: print("Invalid option")
if __name__ == "__main__": main()
