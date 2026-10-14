"""Q4: Find extremes without max() or min()."""
def extremes(numbers):
    if not numbers: raise ValueError("List cannot be empty")
    largest = smallest = numbers[0]
    for number in numbers[1:]:
        if number > largest: largest = number
        if number < smallest: smallest = number
    return largest, smallest
def main():
    try:
        values = [float(x) for x in input("Numbers: ").split()]
        largest, smallest = extremes(values)
        print(f"Largest: {largest:g}; Smallest: {smallest:g}")
    except ValueError as e: print("Invalid input:", e)
if __name__ == "__main__": main()
