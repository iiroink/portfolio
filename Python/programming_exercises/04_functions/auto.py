"""
Ohjelmointi 1: tehtävä 4.14: Auto
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

from math import sqrt


def menu():
    """
    This is a text-based menu. You should ONLY TOUCH TODOs inside the menu.
    TODOs in the menu call functions that you have implemented and take care
    of the return values of the function calls.
    """

    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas, x, y = drive(x, y, new_x, new_y, gas, gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")


def fill(tank_size, to_fill, gas):
    """
    This function has three parameters which are all FLOATs:
      (1) the size of the tank
      (2) the amount of gas that is requested to be filled in
      (3) the amount of gas in the tank currently

    The parameters have to be in this order.
    The function returns one FLOAT that is the amount of gas in the
    tank AFTER the filling up.

    The function does not print anything and does not ask for any
    input.
    """
    if gas + to_fill >= tank_size:
        return tank_size
    else:
        return gas + to_fill


def drive(x, y, new_x, new_y, gas, gas_consumption):
    """
    This function has six parameters. They are all floats.
      (1) The current x coordinate
      (2) The current y coordinate
      (3) The destination x coordinate
      (4) The destination y coordinate
      (5) The amount of gas in the tank currently
      (6) The consumption of gas per 100 km of the car

    The parameters have to be in this order.
    The function returns three floats:
      (1) The amount of gas in the tank AFTER the driving
      (2) The reached (new) x coordinate
      (3) The reached (new) y coordinate

    The return values have to be in this order.
    The function does not print anything and does not ask for any
    input.
    """
    travel_x = abs(new_x - x)
    travel_y = abs(new_y - y)
    travel_distance = diagonal_distance(travel_x, travel_y)
    maximum_distance = consumption_counter(gas, gas_consumption)
    if travel_distance > maximum_distance:
        new_x, new_y = possible_distance_counter(maximum_distance, x, y,
                                                 travel_distance, new_x, new_y)
        gas = 0
    else:
        gas = gas - gas_consumption / 100 * travel_distance

    return gas, new_x, new_y



def diagonal_distance(dx, dy):
    """Calculates the length of hypotenuse when the other sides are dx and dy.

    :param dx: float, distance travelled on x-axis.
    :param dy: float, distance travelled on y-axis.
    :return: float, the hypotenuse.
    """
    return sqrt(dx ** 2 + dy ** 2)


def consumption_counter(gas, gas_consumption):
    """Calculates how far can be travelled with the gas in the tank.

    :param gas: float, gas in the tank.
    :param gas_consumption: float, gas consumption.
    :return: float, the possible distance to travel
    """
    return gas / gas_consumption * 100

def possible_distance_counter(maximum_distance, x, y, travel_distance,
                              new_x, new_y):
    """Calculates where the car will end up if it runs out of gas.
    
    :param maximum_distance: float, the possible distance to travel with gas.
    :param x: float, the current x-coordinate.
    :param y: float, the current y-coordinate.
    :param travel_distance: float, the attempted distance to travel.
    :param new_x: float, the attempted new x-coordinate.
    :param new_y: float, the attempted new y-coordinate.
    :return: float, the new x and y coordinates.
    """
    possible_x = maximum_distance / travel_distance * abs(new_x - x)
    possible_y = maximum_distance / travel_distance * abs(new_y - y)
    if new_x < x:
        possible_x = -possible_x
    if new_y < y:
        possible_y = -possible_y
    new_x = x + possible_x
    new_y = y + possible_y

    return new_x, new_y


def read_number(prompt, error_message="Incorrect input!"):
    """
    DO NOT TOUCH THIS FUNCTION.
    This function reads input from the user.
    Also, don't worry if you don't understand it.
    """

    try:
        return float(input(prompt))

    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


if __name__ == "__main__":
    main()
