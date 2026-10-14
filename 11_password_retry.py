"""Q11: Allow at most three password attempts."""
def check_password(expected, attempts):
    for index, attempt in enumerate(attempts):
        if index >= 3: break
        if attempt == expected: return True
    return False
def main():
    password = "super30"  # Demonstration only; never hard-code real passwords.
    tries = 0
    while tries < 3:
        guess = input("Password: ")
        tries += 1
        if guess == password: print("Access Granted"); return
        print(f"Incorrect. Remaining attempts: {3 - tries}")
    print("Account Locked")
if __name__ == "__main__": main()
