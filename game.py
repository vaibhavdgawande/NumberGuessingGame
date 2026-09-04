import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 10 attempts to guess it.")

secret_number = random.randint(1, 100)
max_attempts = 10
attempts = 0

while attempts < max_attempts:
    guess = input(f"Attempt {attempts + 1}/{max_attempts} — Enter your guess: ")
    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
else:
    print(f"Out of attempts! The number was {secret_number}.")