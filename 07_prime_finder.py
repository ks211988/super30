"""Q7: Prime numbers in an inclusive range using nested loops."""
def primes_between(start, end):
    if start > end: raise ValueError("Start must not exceed end")
    primes = []
    for number in range(start, end + 1):
        if number < 2: continue
        is_prime = True
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime: primes.append(number)
    return primes
def main():
    try:
        start = int(input("Start: ")); end = int(input("End: "))
        print("Prime numbers:", *primes_between(start, end))
    except ValueError as e: print("Invalid input:", e)
if __name__ == "__main__": main()
