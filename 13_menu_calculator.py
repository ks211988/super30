"""Q13: Repeating six-option calculator."""
def calculate(a, b, operation):
    if operation == "1": return a + b
    if operation == "2": return a - b
    if operation == "3": return a * b
    if operation in ("4", "5") and b == 0: raise ValueError("Cannot divide or modulo by zero")
    if operation == "4": return a / b
    if operation == "5": return a % b
    raise ValueError("Unknown operation")
def main():
    while True:
        print("\n1 Add  2 Subtract  3 Multiply  4 Divide  5 Modulus  6 Exit")
        choice = input("Choose: ").strip()
        if choice == "6": break
        if choice not in ("1", "2", "3", "4", "5"): print("Invalid option"); continue
        try:
            a = float(input("First number: ")); b = float(input("Second number: "))
            print("Result:", calculate(a, b, choice))
        except ValueError as e: print("Error:", e)
if __name__ == "__main__": main()
