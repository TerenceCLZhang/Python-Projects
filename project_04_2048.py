import random
import copy


class Grid:
    def __init__(self):
        self.GRID_WIDTH = 4
        self.GRID_HEIGHT = 4

        self.grid = [['X' for _ in range(self.GRID_HEIGHT)]
                     for _ in range(self.GRID_WIDTH)]

    def set_grid(self, new_grid):
        self.grid = new_grid

    def get_grid(self):
        return self.grid

    def spawn_random_two(self):
        if self.check_grid("X"):
            while True:
                pos_x = random.randint(0, self.GRID_WIDTH - 1)
                pos_y = random.randint(0, self.GRID_HEIGHT - 1)

                if self.grid[pos_x][pos_y] == "X":
                    self.grid[pos_x][pos_y] = 2
                    return

    def print_grid(self):
        col_widths = [max(map(len, map(str, col))) for col in zip(*self.grid)]

        for row in self.grid:
            for item, width in zip(row, col_widths):
                print(f"{item:>{width}}", end="  ")
            print()

    def shift_up(self):
        for i in range(1, len(self.grid)):
            for j in range(len(self.grid[i])):
                current_index = i
                while current_index > 0:
                    if self.grid[current_index - 1][j] == "X":
                        self.grid[current_index -
                                  1][j] = self.grid[current_index][j]
                    elif self.grid[current_index - 1][j] == self.grid[current_index][j]:
                        self.grid[current_index -
                                  1][j] = self.grid[current_index][j] * 2
                    else:
                        break

                    self.grid[current_index][j] = "X"
                    current_index -= 1

    def shift_down(self):
        for i in range(len(self.grid) - 2, -1, -1):
            for j in range(len(self.grid[i])):
                current_index = i
                while current_index < len(self.grid) - 1:
                    if self.grid[current_index + 1][j] == "X":
                        self.grid[current_index +
                                  1][j] = self.grid[current_index][j]
                    elif self.grid[current_index + 1][j] == self.grid[current_index][j]:
                        self.grid[current_index +
                                  1][j] = self.grid[current_index][j] * 2
                    else:
                        break

                    self.grid[current_index][j] = "X"
                    current_index += 1

    def shift_left(self):
        for i in range(len(self.grid)):
            for j in range(1, len(self.grid[i])):
                current_index = j
                while current_index > 0:
                    if self.grid[i][current_index - 1] == "X":
                        self.grid[i][current_index -
                                     1] = self.grid[i][current_index]
                    elif self.grid[i][current_index - 1] == self.grid[i][current_index]:
                        self.grid[i][current_index -
                                     1] = self.grid[i][current_index] * 2
                    else:
                        break

                    self.grid[i][current_index] = "X"
                    current_index -= 1

    def shift_right(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i]) - 2, -1, -1):
                current_index = j
                while current_index < len(self.grid[i]) - 1:
                    if self.grid[i][current_index + 1] == "X":
                        self.grid[i][current_index +
                                     1] = self.grid[i][current_index]
                    elif self.grid[i][current_index + 1] == self.grid[i][current_index]:
                        self.grid[i][current_index +
                                     1] = self.grid[i][current_index] * 2
                    else:
                        break

                    self.grid[i][current_index] = "X"
                    current_index += 1

    def check_movable(self):
        if self.check_grid("X"):
            return True

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i]) - 1):
                if self.grid[i][j] == self.grid[i][j + 1]:
                    return True

        for i in range(len(self.grid) - 1):
            for j in range(len(self.grid[i]) - 1):
                if self.grid[i][j] == self.grid[i + 1][j]:
                    return True

    def check_grid(self, value):
        for row in self.grid:
            if value in row:
                return True
        return False

    def check_changed(self, old_grid, new_grid):
        return old_grid != new_grid

    def change_grid(self, move):
        if move == 'w':
            self.shift_up()
        if move == 's':
            self.shift_down()
        if move == 'a':
            self.shift_left()
        if move == 'd':
            self.shift_right()


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

    input("\nPress Any Key to Exit\n")


if __name__ == "__main__":
    main()
