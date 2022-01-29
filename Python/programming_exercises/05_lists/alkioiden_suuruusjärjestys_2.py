"""
Ohjelmointi 1: tehtävä 5.5.2: Funktio listan suuruusjärjestyksen tarkasteluun.2
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""


def is_the_list_in_order(given_list):
    """Checks if the list is in order.

    :param given_list: list
    :return: bool, true, if the list is in order.
    """
    if not given_list:
        return True

    for i in range(len(given_list) - 1):
        if given_list[i] > given_list[i + 1]:
            return False

    return True

def main():
    print(is_the_list_in_order([1,2,3,4,5,4]))

if __name__ == "__main__":
    main()
