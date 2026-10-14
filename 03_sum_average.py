"""Q3: Total and average using a loop, not sum()."""
def total_average(numbers):
    if not numbers: raise ValueError("List cannot be empty")
    total = 0
    for number in numbers: total += number
    return total, total / len(numbers)
def main():
    try:
        numbers = [float(x) for x in input("Numbers separated by spaces: ").split()]
        total, average = total_average(numbers)
        print(f"Total: {total:g}; Average: {average:g}")
    except ValueError as e: print("Invalid input:", e)
if __name__ == "__main__": main()
