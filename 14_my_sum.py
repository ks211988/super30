"""Q14: Reimplement sum() with a loop."""
def my_sum(numbers):
    total = 0
    for number in numbers: total += number
    return total
def main():
    try:
        values = [float(x) for x in input("Numbers: ").split()]
        print("Sum:", my_sum(values))
    except ValueError: print("Please enter valid numbers")
if __name__ == "__main__": main()
