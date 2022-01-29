"""
Ohjelmointi 1: tehtävä 5.4.1: Montako löytyy?
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""


def input_to_list(number_count):
    """Asks the user to input set amount of numbers and converts them into a
    list.

    :param number_count: int, the number of numbers wanted in the list.
    :return: list, contains the inputted numbers.
    """
    number_list = []
    print(f"Enter {number_count} numbers:")
    for _ in range(number_count):
        integer = int(input())
        number_list.append(integer)

    return number_list


def main():

    number_count = int(input("How many numbers do you want to process: "))
    number_list = input_to_list(number_count)

    searched_number = int(input("Enter the number to be searched: "))

    how_many_times = number_list.count(searched_number)

    if how_many_times == 0:
        print(f"{searched_number} is not among the numbers you have entered.")
    else:
        print(f"{searched_number} shows up {how_many_times} times among the "
              f"numbers you have entered.")


if __name__ == "__main__":
    main()