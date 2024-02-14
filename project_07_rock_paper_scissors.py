import random

OPTIONS = {1: "Rock", 2: "Paper", 3: "Scissors"}


def get_player_option():
    while True:
        try:
            player_option_code = int(input("Enter an option (1-3):\n>> "))

            if 1 <= player_option_code <= 3:
                return player_option_code
            else:
                print("Error: Please enter a number between 1 and 3.")
        except ValueError:
            print("Error: Please enter a valid integer.")


def get_result(player, computer):
    if player == computer:
        return "draw"
    elif player == "Rock":
        if computer == "Paper":
            return "computer"
        return "player"
    elif player == "Paper":
        if computer == "Scissors":
            return "computer"
        return "player"
    else:
        if computer == "Rock":
            return "computer"
        return "player"


def main():
    print("====================\n"
          + "Rock Paper Scissors\n"
          + "====================")

    draw = True

    while draw:
        draw = False
        print("\nEnter Choice\n"
              + "1. Rock\n"
              + "2. Paper\n"
              + "3. Scissors")
        player_option_code = get_player_option()
        computer_option_code = random.randint(1, 3)

        player_option = OPTIONS[player_option_code]
        computer_option = OPTIONS[computer_option_code]

        print(f"\nPlayer Chose: {player_option}\n"
              + f"Computer Chose: {computer_option}\n")

        result = get_result(player_option, computer_option)
        if result == "draw":
            print("Draw")
            draw = True
        elif result == "computer":
            print("Computer Wins")
        else:
            print("Player Wins")

    input("\nPress Enter to Exit\n")


if __name__ == "__main__":
    main()
