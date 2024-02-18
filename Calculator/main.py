import pygame
import sys

from Button import Button, NumberButton, OperationButton
from DisplayBar import DisplayBar

# Window Dimensions
WIDTH = 400
HEIGHT = 525
WINDOW_SIZE = (WIDTH, HEIGHT)

# Colours
WHITE = (255, 255, 255)
DARK_GREY = (169, 169, 169)
BLACK = (0, 0, 0)

MAXIMUM_LENGTH = 10


class Calculator:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Simple Calculator")

        # Icon source: https://iconduck.com/icons/183747/math
        icon = pygame.image.load("math.svg")
        pygame.display.set_icon(icon)

        # Numbers
        self.previous = "0"
        self.current = "0"
        self.operation = ""

        # Flags
        self.pressed_equals = False
        self.pressed_operation = False

        # Display Bar
        X_START = 25
        Y_START = 25

        DISPLAY_BAR_WIDTH = WIDTH - X_START * 2
        DISPLAY_BAR_HEIGHT = 100

        self.display_bar = DisplayBar(
            X_START, Y_START, DISPLAY_BAR_WIDTH, DISPLAY_BAR_HEIGHT)

        # Buttons
        BUTTON_SPACING = 25
        button_width = (DISPLAY_BAR_WIDTH - BUTTON_SPACING * 3) / 4
        button_height = button_width

        # Button y start
        buttons_row_1_Y_START = 150
        buttons_row_2_Y_START = buttons_row_1_Y_START + button_width + BUTTON_SPACING
        buttons_row_3_Y_START = buttons_row_2_Y_START + button_width + BUTTON_SPACING
        buttons_row_4_Y_START = buttons_row_3_Y_START + button_width + BUTTON_SPACING

        # Row 1 Buttons
        self.button_7 = NumberButton(pygame.Rect(
            X_START, buttons_row_1_Y_START, button_width, button_height), "7", self.handle_number, 7)
        self.button_8 = NumberButton(pygame.Rect(X_START + button_width + BUTTON_SPACING,
                                                 buttons_row_1_Y_START, button_width, button_height), "8", self.handle_number, 8)
        self.button_9 = NumberButton(pygame.Rect(X_START + 2 * (button_width + BUTTON_SPACING),
                                                 buttons_row_1_Y_START, button_width, button_height), "9", self.handle_number, 9)
        self.button_add = OperationButton(pygame.Rect(X_START + 3 * (button_width + BUTTON_SPACING),
                                                      buttons_row_1_Y_START, button_width, button_height), "+", self.handle_operation, "+")

        # Row 2 Buttons
        self.button_4 = NumberButton(pygame.Rect(
            X_START, buttons_row_2_Y_START, button_width, button_height), "4", self.handle_number, 4)
        self.button_5 = NumberButton(pygame.Rect(X_START + button_width + BUTTON_SPACING,
                                                 buttons_row_2_Y_START, button_width, button_height), "5", self.handle_number, 5)
        self.button_6 = NumberButton(pygame.Rect(X_START + 2 * (button_width + BUTTON_SPACING),
                                                 buttons_row_2_Y_START, button_width, button_height), "6", self.handle_number, 6)
        self.button_subtract = OperationButton(pygame.Rect(X_START + 3 * (button_width + BUTTON_SPACING),
                                                           buttons_row_2_Y_START, button_width, button_height), "-", self.handle_operation, "-")

        # Row 3 Buttons
        self.button_1 = NumberButton(pygame.Rect(
            X_START, buttons_row_3_Y_START, button_width, button_height), "1", self.handle_number, 1)
        self.button_2 = NumberButton(pygame.Rect(X_START + button_width + BUTTON_SPACING,
                                                 buttons_row_3_Y_START, button_width, button_height), "2", self.handle_number, 2)
        self.button_3 = NumberButton(pygame.Rect(X_START + 2 * (button_width + BUTTON_SPACING),
                                                 buttons_row_3_Y_START, button_width, button_height), "3", self.handle_number, 3)
        self.button_multiply = OperationButton(pygame.Rect(X_START + 3 * (button_width + BUTTON_SPACING),
                                                           buttons_row_3_Y_START, button_width, button_height), "x", self.handle_operation, "*")

        # Row 4 Buttons
        self.button_c = Button(pygame.Rect(
            X_START, buttons_row_4_Y_START, button_width, button_height), "c", self.perform_clear)
        self.button_0 = NumberButton(pygame.Rect(X_START + button_width + BUTTON_SPACING,
                                                 buttons_row_4_Y_START, button_width, button_height), "0", self.handle_number, 0)
        self.button_equal = Button(pygame.Rect(X_START + 2 * (button_width + BUTTON_SPACING),
                                               buttons_row_4_Y_START, button_width, button_height), "=", self.perform_calculate)
        self.button_divide = OperationButton(pygame.Rect(X_START + 3 * (button_width + BUTTON_SPACING),
                                                         buttons_row_4_Y_START, button_width, button_height), "/", self.handle_operation, "/")

        self.buttons = [self.button_0, self.button_1, self.button_2, self.button_3, self.button_4, self.button_5, self.button_6, self.button_7,
                        self.button_8, self.button_9, self.button_add, self.button_subtract, self.button_multiply, self.button_divide, self.button_c, self.button_equal]

    def run(self):
        running = True
        while running:
            self.window.fill(DARK_GREY)

            self.display_bar.draw(self.window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for button in self.buttons:
                button.draw(self.window)
                button.handle_event(event)

            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def handle_number(self, number):
        if self.pressed_equals and not self.pressed_operation:
            self.perform_clear()

        if self.current == "0":
            self.current = str(number)
        elif len(self.current) + 1 <= MAXIMUM_LENGTH:
            self.current += str(number)
        self.display_bar.update_text(self.current)

    def handle_operation(self, operation):
        self.pressed_operation = True
        self.previous = self.current
        self.operation = operation
        self.display_bar.update_text(self.current)
        self.current = "0"

    def perform_calculate(self):
        self.pressed_operation = False
        self.pressed_equals = True
        self.current = str(
            eval(f"{self.previous} {self.operation} { self.current}"))
        self.display_bar.update_text(self.current, True)

    def perform_clear(self):
        self.current = "0"
        self.previous = "0"
        self.operation = ""
        self.pressed_equals = False
        self.pressed_operation = False
        self.display_bar.update_text(self.current, True)


def main():
    calculator = Calculator()
    calculator.run()


if __name__ == "__main__":
    main()
