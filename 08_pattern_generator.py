"""Q8: Build a number triangle with nested for loops."""
def pattern(n):
    if n < 1: raise ValueError("N must be positive")
    lines = []
    for row in range(1, n + 1):
        values = []
        for column in range(1, row + 1): values.append(str(column))
        lines.append(" ".join(values))
    return lines
def main():
    try:
        for line in pattern(int(input("Rows: "))): print(line)
    except ValueError as e: print("Invalid input:", e)
if __name__ == "__main__": main()
