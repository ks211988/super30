"""Q12: Guess a randomly selected integer from 1 to 100."""
import random
def compare_guess(guess, secret):
    if guess < secret: return "Too Low"
    if guess > secret: return "Too High"
    return "Correct"
def main():
    secret = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Guess (1-100): "))
            if not 1 <= guess <= 100: print("Choose 1 through 100"); continue
            attempts += 1
            outcome = compare_guess(guess, secret)
            print(outcome)
            if outcome == "Correct": print(f"Attempts: {attempts}"); break
        except ValueError: print("Enter an integer")
if __name__ == "__main__": main()
