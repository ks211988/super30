"""Q5: Count every character, including spaces."""
def frequencies(text):
    counts = {}
    for char in text: counts[char] = counts.get(char, 0) + 1
    return counts
def main():
    for char, count in frequencies(input("Enter text: ")).items():
        print(f"{char!r}: {count}")
if __name__ == "__main__": main()
