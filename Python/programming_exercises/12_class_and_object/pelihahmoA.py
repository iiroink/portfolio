"""
Ohjelmointi 1: tehtävä 12.3: Pelihahmo A
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673

Yksinkertainen luokka pelihahmolle ja hänen tavaroilleen
"""


class Character:
    """
    This class represents the inventory of a character.
    """
    def __init__(self, name):
        """
        Constructor
        """
        self.__name = name
        self.__inventory = {}

    def give_item(self, item):
        """
        Adds item into the inventory
        :param item: str, the item
        """
        if item not in self.__inventory:
            self.__inventory[item] = 1
        else:
            self.__inventory[item] += 1

    def remove_item(self, item):
        """
        Removes item from inventory
        :param item: str, the item
        """
        if item in self.__inventory:
            self.__inventory[item] -= 1
        if self.__inventory[item] == 0:
            self.__inventory.pop(item)

    def printout(self):
        """
        Standard printout:
        Name: <name>
          amount item
          amount item
          ...
        """
        print(f"Name: {self.__name}")
        if self.__inventory == {}:
            print("  --nothing--")

        for item in sorted(self.__inventory):
            print(f"  {self.__inventory[item]} {item}")

    def get_name(self):
        """
        :return: str, the name of the character
        """
        return self.__name

    def has_item(self, item):
        """
        :param item: str, item to test
        :return: bool, true if character has item
        """
        if item in self.__inventory:
            return True
        else:
            return False

    def how_many(self, item):
        """
        Returns the amount of item in inventory
        :param item: str, the item
        :return: int, the amount of the item
        """
        if item in self.__inventory:
            return self.__inventory[item]
        else:
            return 0


def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
