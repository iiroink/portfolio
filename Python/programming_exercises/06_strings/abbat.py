"""
Ohjelmointi 1: tehtävä 6.12: Montako abbaa?
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""


def count_abbas(merkkijono):
    """Laskee abbat

    :param merkkijono: str
    :return: int, montako abbaa
    """
    pituus = len(merkkijono)
    abbat = 0

    if pituus < 4:
        return abbat
    else:
        for i in range(pituus):
            if merkkijono[i:i + 4] == "abba":
                abbat += 1

        return abbat



def main():
    print(count_abbas("sd"))


if __name__ == "__main__":
    main()