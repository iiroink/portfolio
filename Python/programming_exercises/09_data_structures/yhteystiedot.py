"""
Ohjelmointi 1: tehtävä 9.7: Yhteystiedot
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673

Luo sanakirjan sisäisen sanakirjan ihmisten yhteystiedoista.
"""


def read_file(file):
    """Luo sanakirjan sisäisen sanakirjan ihmisten yhteystiedoista.

    :param file: csv file, has to have ";" as separator.
    :return:
    """

    try:
        open_file = open(file, mode="r")

    except OSError:
        return

    first_keys = open_file.readline()
    first_keys = first_keys.rstrip()
    first_keys = first_keys.split(";")

    phonebook = {}

    for line in open_file:
        pure_line = line.rstrip()
        contents = pure_line.split(";")

        phonebook[contents[0]] = {}

        length = len(contents)

        for ind in range(length):
            phonebook[contents[0]][first_keys[ind]] = contents[ind]

    open_file.close()

    return phonebook
