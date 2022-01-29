"""
Ohjelmointi 1: tehtävä 5.5.1: Funktio listan alkioiden yhtäsuuruusvertailuun
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""


def are_all_members_same(given_list):
    """Checks if all alkiot are the same in a list.

    :param given_list: list
    :return: bool, true, if all alkiot are the same.
    """
    if not given_list:
        return True

    first_number = given_list[0]
    if given_list.count(first_number) == len(given_list):
        return True
    else:
        return False
