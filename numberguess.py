import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

number = random.randint(1, 100)
guesses = 0

while True:
    guess = int(input("Enter your guess: "))
    guesses += 1

    if guess < number:
        print("Your guess is too low. Try again.")
    elif guess > number:
        print("Your guess is too high. Try again.")
    else:
        print(f"Congratulations! You guessed the number in {guesses} guesses.")
        break
