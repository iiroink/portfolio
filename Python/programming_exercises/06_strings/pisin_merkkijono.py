"""
Ohjelmointi 1: tehtävä 6.13: Pisin järjestetty alimerkkijono
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""


def longest_substring_in_order(merkkijono):
    """Selvittää pisimmän järjestetyn alimerkkijonon

    :param merkkijono: str
    :return: str, pisin merkkijono
    """
    pituus = len(merkkijono)
    osapituus = 0
    pisin_osuus = ""
    pisin_pituus = 0

    if pituus <= 1:
        return merkkijono

    for i in range(pituus - 1):
        if merkkijono[i] < merkkijono[i + 1]:
            if osapituus > pisin_pituus:
                pisin_osuus = merkkijono[i - osapituus: i + 2]
                pisin_pituus = osapituus
            osapituus += 1
        else:
            osapituus = 0

    if pisin_pituus == 0:
        pisin_osuus = merkkijono[0]

    return pisin_osuus

def main():
    print(longest_substring_in_order("x"))


if __name__ == "__main__":
    main()