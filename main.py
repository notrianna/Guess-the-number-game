from art import logo
import random

print(logo)

numbers = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
    22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
    60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78,
    79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97,
    98, 99, 100
]

randomized_num = random.choice(numbers)

print(
    "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100."
)

cheat_sheet = print(f"Pssst, the correct answer is {randomized_num}")

diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if diff == 'hard':
    print("You have 5 attempts remaining to guess the number. ")
else:
    print("You have 10 attempts remaining to guess the number.")

attempts_remaining_hard = 5
if diff == 'hard':
    for guess in range(5):
        user_guess = int(input("Make a guess: "))
        if user_guess > randomized_num:
            print("Too High.\nGuess again.")
        elif user_guess < randomized_num:
            print("Too Low.\nGuess again.")
        elif user_guess == randomized_num:
            print(f"You got it! The answer was {randomized_num}")
        attempts_remaining_hard -= 1
        print(
            f"You have {attempts_remaining_hard} attempts remaining to guess the number."
        )

attempts_remaining_easy = 10
if diff == 'easy':
    for guess in range(10):
        user_guess = int(input("Make a guess: "))
        if user_guess > randomized_num:
            print("Too High.\nGuess again.")
        elif user_guess < randomized_num:
            print("Too Low.\nGuess again.")
        elif user_guess == randomized_num:
            print(f"You got it! The answer was {randomized_num}")
        attempts_remaining_easy -= 1
        print(
            f"You have {attempts_remaining_easy} attempts remaining to guess the number."
        )
