"""
Ohjelmointi 1: tehtävä 10.10: Mölkyn pisteiden laskentaa
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673

Mölkky score counter.
"""


class Player:
    """
    Class for persons points in mölkky. The attributes are:
    - player's name
    - points of the player
    - "won" bool, true if 50 points
    - number of throws
    - totalpoints, all points gotten with no penalties
    - hits scored successfully
    """

    def __init__(self, player):
        """
        Initializes object player.

        :param player: str, name of the player
        """
        self.__name = player
        self.__points = 0
        self.__won = False
        self.__throws = 0
        self.__totalpoints = 0
        self.__hits = 0

    def get_name(self):
        """
        :return: str, name of the player
        """
        return self.__name

    def get_points(self):
        """
        :return: int, points of the player
        """
        return self.__points

    def add_points(self, points):
        """
        Adds points to players score.

        :param points: int, points to add
        """
        if points > 0:
            self.__hits += 1

        self.__totalpoints += points
        self.__points += points

        if self.__points > 50:
            print(f"{self.__name} gets penalty points!")
            self.__points = 25

        if 40 <= self.__points <= 49:
            needed_points = 50 - self.__points
            print(f"{self.__name} needs only {needed_points} points. It's "
                  "better to avoid knocking down the pins with higher points.")

        self.__throws += 1

    def has_won(self):
        """
        Determines if the player has won i.e. has exactly 50 points.

        :return: bool, True if the player has won.
        """
        if self.__points == 50:
            self.__won = True

        return self.__won

    def average_counter(self):
        """
        Counts the average of previous throws.

        :return: float, average.
        """
        average = self.__totalpoints / self.__throws

        return average

    def hit_percentage(self):
        """
        Calculates the hit percentage of the player.
        :return: float, the hp
        """
        if self.__throws == 0:
            return 0.0

        hit_percentage = self.__hits / self.__throws * 100
        return hit_percentage


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        if in_turn.average_counter() < pts:
            print(f"Cheers {in_turn.get_name()}!")

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p,",
              f"hit percentage {player1.hit_percentage():.1f}")
        print(player2.get_name() + ":", player2.get_points(), "p,",
              f"hit percentage {player2.hit_percentage():.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()
