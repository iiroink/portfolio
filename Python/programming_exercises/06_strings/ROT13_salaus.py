"""
Ohjelmointi 1: tehtävä 6.6: Käännä nimet oikein päin
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

def encrypt(kirjain):
    """

    :param kirjain:
    :return:
    """
    regular_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                     "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    if kirjain.isupper():
        pieni_kirjain = kirjain.lower()
        i = regular_chars.index(pieni_kirjain)
        salattu_pieni = encrypted_chars[i]
        salattu_kirjain = salattu_pieni.upper()
        return salattu_kirjain
    elif kirjain.islower():
        i = regular_chars.index(kirjain)
        return encrypted_chars[i]
    else:
        return kirjain


def row_encryption(teksti):
    """

    :param teksti:
    :return:
    """
    salattu_teksti = ""
    for kirjain in teksti:
        salattu_kirjain = encrypt(kirjain)
        salattu_teksti += salattu_kirjain

    return salattu_teksti



def main():
    print(row_encryption("Happy, happy, joy, joy!"))


if __name__ == "__main__":
    main()