"""Q1: Print 1..N and count even and odd numbers."""
def analyze_range(n):
    if n < 1: raise ValueError("N must be positive")
    results = [(i, "Even" if i % 2 == 0 else "Odd") for i in range(1, n + 1)]
    even = 0
    odd = 0
    for _, kind in results:
        if kind == "Even": even += 1
        else: odd += 1
    return results, even, odd

def main():
    try:
        results, even, odd = analyze_range(int(input("Enter positive N: ")))
        for number, kind in results: print(f"{number} is {kind}")
        print(f"Even: {even}; Odd: {odd}")
    except ValueError as e: print("Invalid input:", e)
if __name__ == "__main__": main()
