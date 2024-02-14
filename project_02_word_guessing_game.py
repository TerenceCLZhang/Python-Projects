import random

WORD_LIST = ["apple", "banana", "orange", "grape", "kiwi",
             "lemon", "peach", "pear", "plum", "watermelon"]
NUM_ROUNDS = 12


def get_unique_chars(word):
    unique_chars = {char: False for char in word}
    return unique_chars


def display(random_word, chars, round, guessed_chars):
    print()
    for char in random_word:
        if not chars[char]:
            print("_", end=" ")
        else:
            print(char, end=" ")
    print(
        f"\nYou have {NUM_ROUNDS - round} {'guess' if NUM_ROUNDS - round == 1 else 'guesses'} left.")
    print(
        f"Guessed Letters: {', '.join([guessed_char for guessed_char in guessed_chars])}\n")


def get_guess(guessed_chars):
    while True:
        guess = input("Enter Letter:\n>> ").strip().lower()

        if guess.isalpha() and len(guess) == 1 and guess not in guessed_chars:
            return guess

        if not guess.isalpha():
            print("ERROR: Please enter a valid letter (A-Z).")

        if len(guess) != 1:
            print("ERROR: Please enter only one letter.")

        if guess in guessed_chars:
            print("ERROR: You've already guessed that letter.")


def main():
    print("===================")
    print("Word Guessing Game")
    print("===================")

    random_word = random.choice(WORD_LIST)
    chars = get_unique_chars(random_word)
    guessed_chars = []

    print(random_word)

    for round in range(NUM_ROUNDS):
        display(random_word, chars, round, guessed_chars)

        guess = get_guess(guessed_chars)

        if guess in random_word:
            chars[guess] = True

        guessed_chars.append(guess)

        if all(value for value in chars.values()):
            print(f"\nYou Win. The word was {random_word}.")
            break

    if not all(value for value in chars.values()):
        print(f"\nThe word was {random_word}. Better luck next time.")

    input("\nPress Enter to Exit\n")


if __name__ == "__main__":
    main()
