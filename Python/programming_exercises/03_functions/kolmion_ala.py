"""
Ohjelmointi 1: tehtävä 3.8.1: Kolmion pinta-ala
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

from math import sqrt

def area(r1,r2,r3):
    """
    Calculates the area of a triangle from the length of the sides.

    :param r1: float, length of side one.
    :param r2: float, length of side two.
    :param r3: float, length of side three.
    :return: float, area of the triangle.
    """
    #Calculate half of the perimeter
    s = (r1 + r2 + r3) / 2

    #Calculate and return the area
    return sqrt(s*(s-r1)*(s-r2)*(s-r3))


def main():
    radius_1 = float(input("Enter the length of the first side: "))
    radius_2 = float(input("Enter the length of the second side: "))
    radius_3 = float(input("Enter the length of the third side: "))

    print(f"The triangle's area is{area(radius_1, radius_2, radius_3): .1f}")


if __name__ == "__main__":
    main()
