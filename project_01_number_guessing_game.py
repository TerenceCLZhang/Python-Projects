import random
import math


def get_range():
    while True:
        try:
            lower_range_number = int(
                input("Enter Lower Range Number:\n>> "))
            upper_range_number = int(
                input("Enter Upper Range Number:\n>> "))

            if lower_range_number < upper_range_number:
                return lower_range_number, upper_range_number
            else:
                print(
                    "ERROR: Upper range number must be greater than lower range number.")
        except ValueError:
            print("ERROR: Please enter valid integers for the range.")


def guessing(lower_range_number, upper_range_number, random_number, current_number_guesses):
    GUESS_RESULT_DICT = {"win": "You Win.",
                         "low": "Try Again! You guessed too low.",
                         "high": "Try Again! You guessed too high."}

    while current_number_guesses > 1:
        current_number_guesses -= 1

        print(
            f"\nYou have {current_number_guesses} {'guess' if current_number_guesses == 1 else 'guesses'} left.")

        guess = get_guess(lower_range_number, upper_range_number)

        result = check_guess(guess, random_number)
        if result != "win" and current_number_guesses == 1:
            print(f"The number was {random_number}.\nBetter luck next time.")
            return

        print(GUESS_RESULT_DICT[result])
        if result == "win":
            return


def get_guess(lower_range_number, upper_range_number):
    while True:
        try:
            guess = int(input("Enter Guess:\n>> "))

            if lower_range_number <= guess <= upper_range_number:
                return guess
            else:
                print(
                    f"ERROR: Guess must be within the specified range of {lower_range_number} and {upper_range_number} inclusive.")
        except ValueError:
            print("ERROR: Please enter a valid integer for the guess.")


def check_guess(guess, random_number):
    if guess == random_number:
        return "win"

    if guess < random_number:
        return "low"

    if guess > random_number:
        return "high"


def main():
    print("======================")
    print("Number Guessing Game")
    print("======================")

    lower_range_number, upper_range_number = get_range()

    random_number = random.randint(
        lower_range_number, upper_range_number + 1)

    max_number_guesses = math.ceil(
        math.log(upper_range_number - lower_range_number + 1, 2))

    current_number_guesses = max_number_guesses

    guessing(lower_range_number, upper_range_number,
             random_number, current_number_guesses)

    input("\nPress Enter to Exit\n")


if __name__ == "__main__":
    main()
