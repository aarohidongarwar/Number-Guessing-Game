import random

print("🎯 Welcome to the Number Guessing Game!\n")

# Take range input from the player
low = int(input("Enter the lowest number in the range: "))
high = int(input("Enter the highest number in the range: "))

# Generate a random number within the user's range
right_number = random.randint(low, high)

print(f"\nI've picked a number for you to guess between {low} and {high}.\n")

# Initialize score counter
attempts = 0

# Take the first guess
guessed_number = int(input("Enter your guess: "))
attempts += 1

# Continue until the player guesses correctly
while guessed_number != right_number:
    if guessed_number < low or guessed_number > high:
        print(f"Invalid guess! Please enter a number between {low} and {high}.")
    elif guessed_number > right_number:
        print("\nYour guess is too high. Try a lower number!\n")
    else:
        print("\nYour guess is too low. Try a higher number!\n")

    guessed_number = int(input("Enter your guess again: "))
    attempts += 1

# Player guessed correctly
print(f"\n✅ Correct guess! The number was {right_number}.")
print(f"🎉 You won in {attempts} attempts. Thanks for playing!\n")
