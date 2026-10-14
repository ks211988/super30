"""Q15: Return sign, parity, and primality of an integer."""
def analyze_number(number):
    sign = "positive" if number > 0 else "negative" if number < 0 else "zero"
    parity = "even" if number % 2 == 0 else "odd"
    prime = number >= 2
    if prime:
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0: prime = False; break
    return {"sign": sign, "parity": parity, "is_prime": prime}
def main():
    try:
        result = analyze_number(int(input("Integer: ")))
        for key, value in result.items(): print(f"{key}: {value}")
    except ValueError: print("Enter a valid integer")
if __name__ == "__main__": main()
