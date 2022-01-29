"""
Ohjelmointi 1: tehtävä 5.5.2: Funktio listan suuruusjärjestyksen tarkasteluun
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

    sorted_list = sorted(given_list)
    if given_list == sorted_list:
        return True
    else:
        return False
