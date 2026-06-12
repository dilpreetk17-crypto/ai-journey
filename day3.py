# Day 3 - Conditions & Loops
# Number Guessing Game

secret_number = 7
attempts = 0
max_attempts = 3

print("🎮 Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 10")
print("You have 3 attempts")
print("---")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess == secret_number:
        print("🎉 CORRECT! You got it in", attempts, "attempt(s)!")
        break
    elif guess < secret_number:
        print("📉 Too low! Try higher.")
    else:
        print("📈 Too high! Try lower.")

    # Tell them how many attempts are left
    attempts_left = max_attempts - attempts
    if attempts_left > 0:
        print("Attempts left:", attempts_left)

# This runs after the loop ends
if guess != secret_number:
    print("❌ Out of attempts! The number was", secret_number)