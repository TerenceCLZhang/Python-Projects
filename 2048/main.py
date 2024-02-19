import copy
from Grid import Grid


def enter_command():
    while True:
        move = input("Enter Move:\n>> ").lower()

        if move in "wasd" and len(move) == 1:
            return move

        if move not in "wasd":
            print("ERROR: Invalid move. Please enter 'w', 'a', 's', or 'd'.")
        if len(move) != 1:
            print("ERROR: Please enter only one character.")


def main():
    grid = Grid()
    grid.spawn_random_two()

    print("=================")
    print("2048")
    print("=================\n")

    print("Commands:")
    print("- 'W' or 'w': Move Up")
    print("- 'S' or 's': Move Down")
    print("- 'A' or 'a': Move Left")
    print("- 'D' or 'd': Move Right\n")

    while True:
        grid.print_grid()

        if not grid.check_movable():
            print("You Lose. Better Luck Next Time")
            break

        if grid.check_grid(2048):
            print("You Win!")
            break

        previous_grid = copy.deepcopy(grid.get_grid())

        move = enter_command()

        grid.change_grid(move)

        if grid.check_changed(grid.get_grid(), previous_grid):
            grid.spawn_random_two()

    input("\nPress Enter to Exit\n")


if __name__ == "__main__":
    main()
