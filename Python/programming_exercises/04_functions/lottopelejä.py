"""
Ohjelmointi 1: tehtävä 4.7: Lottopelejä
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

from math import factorial

def input_checker(total_balls, drawn_balls):
    """
    Checks that both inputs are greater than zero and that total number of
    balls is bigger or equal to the number of balls drawn.

    :param total_balls: int, number of balls in the lottery.
    :param drawn_balls: int, number of balls drawn.
    :return: bool.
    """
    difference = total_balls >= drawn_balls
    positivity = total_balls > 0 and drawn_balls > 0
    return difference, positivity

def lottery_probability(total_balls, drawn_balls):
    """
    Calculates the number of different draws.

    :param total_balls: int, the size of the poll.
    :param drawn_balls: int, number of balls drawn.
    :return: string, the number of possible draws.
    """
    osoittaja = factorial(total_balls)
    nimittaja = factorial(total_balls - drawn_balls) * factorial(drawn_balls)
    probability = int(osoittaja / nimittaja)
    return probability

def main():
    # Ask the desired number of balls.
    total_balls = int(input("Enter the total number of lottery balls: "))
    drawn_balls = int(input("Enter the number of the drawn balls: "))

    # Run input_checker to check the validity of the inputs.
    difference, positivity = input_checker(total_balls, drawn_balls)

    if not positivity:
        print("The number of balls must be a positive number.")
    elif not difference:
        print("At most the total number of balls can be drawn.")
    else:
        probability = lottery_probability(total_balls, drawn_balls)
        print(f"The probability of guessing all {drawn_balls}", end =" ")
        print(f"balls correctly is 1/{probability}")

if __name__ == "__main__":
    main()