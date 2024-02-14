import random


def get_player_guess(initial):
    if initial:
        message = "I have a four digit number. Enter your choice of numbers.\n>> "
    else:
        message = "Enter your next choice of numbers.\n>> "

    while True:
        try:
            guess = int(input(message))

            if len(str(guess)) == 4:
                print()
                return guess
            else:
                print("ERROR: Please enter a 4-digit number.")

        except ValueError:
            print("ERROR: Please enter a valid integer.")


def display_digit(guess, random_num):
    for digit_guess, digit_random in zip(guess, random_num):
        if digit_guess != digit_random:
            print("X", end=" ")
        else:
            print(digit_random, end=" ")
    print()


def get_correct_count(guess, random_num):
    num_correct = 0
    for digit in guess:
        if digit in random_num:
            num_correct += 1
    return num_correct


def main():
    print("===============")
    print("Mastermind")
    print("===============")

    random_num = str(random.randint(1000, 10000))
    player_tries = 0

    guess = str(get_player_guess(initial=True))

    if guess == random_num:
        print("Great! You guessed the number in just one try! You're a mastermind!")
        return

    while True:
        player_tries += 1
        num_correct = 0

        num_correct = get_correct_count(guess, random_num)

        display_digit(guess, random_num)

        if guess == random_num:
            print("You've become a mastermind.")
            print(f"It only took you {player_tries} tries")

            input("\nPress Enter to Exit\n")
            return
        else:
            print(
                f"Not quite the number. But you did get {num_correct} {'digit' if num_correct == 1 else 'digits'} correct!")
            guess = str(get_player_guess(initial=False))


if __name__ == "__main__":
    main()
