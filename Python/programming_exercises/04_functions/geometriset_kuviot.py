"""
Ohjelmointi 1: tehtävä 4.8: Geometriset kuviot
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

# Import pi to be used when calculating the circle-
from math import pi


def input_checker(number):
    """Checks that the number entered is positive.

    :param number: float, number entered by the user.
    :return: bool.
    """
    return number > 0


def rectangle_circumference(side1, side2):
    """Calculates the circumference of a rectangle (or a square).

    :param side1: float, length of side 1.
    :param side2: float, length of side 2.
    :return: float, circumference of the rectangle.
    """
    circumference = 2 * side1 + 2 * side2
    return circumference


def rectangle_area(side1, side2):
    """Calculates the area of a rectangle (or a square).

    :param side1: float, length of side 1.
    :param side2: float, length of side 2.
    :return: float, area of the rectangle.
    """
    area = side1 * side2
    return area


def circle_circumference(radius):
    """Calculates the circumference of a circle.

    :param radius: float, radius of the circle.
    :return: float, circumference of the circle.
    """
    circumference = 2 * pi * radius
    return circumference


def circle_area(radius):
    """Calculates the area of a circle.

    :param radius: float, radius of the circle.
    :return: float, area of the circle.
    """
    area = pi * radius ** 2
    return area


def print_results(circ, area):
    """Prints the circumference and area of the chosen object.

    :param circ: float, circumference of the object.
    :param area: float, area of the object.
    """
    print(f"The circumference is {circ:.2f}")
    print(f"The surface area is {area:.2f}")


def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            square_side = 0
            while not input_checker(square_side):
                square_side = float(input(
                    "Enter the length of the square's side: "))

            circ = rectangle_circumference(square_side, square_side)
            area = rectangle_area(square_side, square_side)

            print_results(circ, area)

        elif answer == "r":
            side1 = 0
            side2 = 0
            while not input_checker(side1):
                side1 = float(input(
                    "Enter the length of the rectangle's side 1: "))

            while not input_checker(side2):
                side2 = float(input(
                    "Enter the length of the rectangle's side 2: "))

            circ = rectangle_circumference(side1, side2)
            area = rectangle_area(side1, side2)

            print_results(circ, area)

        elif answer == "c":
            radius = 0
            while not input_checker(radius):
                radius = float(input("Enter the circle's radius: "))

            circ = circle_circumference(radius)
            area = circle_area(radius)

            print_results(circ, area)

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()


def main():
    menu()
    print("Goodbye!")


if __name__ == "__main__":
    main()