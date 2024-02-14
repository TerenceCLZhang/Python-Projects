import pyscreenshot as ImageGrab
import time
from datetime import datetime


def get_time_delay():
    while True:
        try:
            num_seconds = int(
                input("Enter number of seconds (0-60) delay.\n>> "))

            if 0 <= num_seconds <= 60:
                return num_seconds
            else:
                print("Error: Please enter a number between 0 and 60.")
        except ValueError:
            print("Error: Please enter a valid integer.")


def get_save():
    while True:
        try:
            print("1. Save\n"
                  + "2. Retake")
            option = int(
                input("Enter an option (1-2):\n>> "))

            if option == 1:
                return True
            elif option == 2:
                return False
            else:
                print("Error: Please enter 1 or 2.")
        except ValueError:
            print("Error: Please enter a valid integer.")


def get_time_string():
    current_datetime = datetime.now()
    datetime_string = current_datetime.strftime("%Y%m%d%H%M%S")
    return datetime_string


def main():
    print("======================\n"
          + "Screenshot\n"
          + "======================")

    while True:
        num_seconds = get_time_delay()

        time.sleep(num_seconds)

        image = ImageGrab.grab()
        datetime_string = get_time_string()

        image.show()

        if get_save():
            filename = datetime_string + ".png"
            image.save(filename)
            break

    input("\nPress Enter to Exit")


if __name__ == "__main__":
    main()
