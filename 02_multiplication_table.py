"""Q2: Generate a multiplication table with a configurable ending."""
def table(number, end=10):
    if end < 1: raise ValueError("End must be positive")
    return [(i, number * i) for i in range(1, end + 1)]
def main():
    try:
        number = int(input("Table number: "))
        end_text = input("End multiplier (Enter for 10): ").strip()
        end = int(end_text) if end_text else 10
        for i, product in table(number, end): print(f"{number} x {i} = {product}")
    except ValueError as e: print("Invalid input:", e)
if __name__ == "__main__": main()
