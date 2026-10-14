"""Q6: Count English vowels, consonants, digits, spaces and symbols."""
def count_types(text):
    counts = dict(vowels=0, consonants=0, digits=0, spaces=0, special=0)
    for char in text:
        if char.lower() in "aeiou": counts["vowels"] += 1
        elif char.lower() in "abcdefghijklmnopqrstuvwxyz": counts["consonants"] += 1
        elif char.isdigit(): counts["digits"] += 1
        elif char.isspace(): counts["spaces"] += 1
        else: counts["special"] += 1
    return counts
def main():
    for name, count in count_types(input("Enter a sentence: ")).items(): print(f"{name}: {count}")
if __name__ == "__main__": main()
