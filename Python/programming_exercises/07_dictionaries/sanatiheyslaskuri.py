"""
Ohjelmointi 1: tehtävä 7.3: Hintalista
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673

Laskee syötetyssä tekstissä esiintyvien sanojen esiintymiskerrat.
"""


def word_counter(teksti, sanatiheys):
    """Laskee sanojen esiintymistiehyden

    :param teksti: str, yksi rivi syötettyä tekstiä.
    """
    sanat = teksti.split(" ")

    for sana in sanat:
        if sana not in sanatiheys:
            sanatiheys[sana] = 1
        else:
            sanatiheys[sana] += 1


def print_results(sanatiheys):
    """Tulostaa sanatiheydet aakkosjärjestyksessä.

    :param sanatiheys: dict, avaimina sanat, arvoina tiheys.
    """
    for sana in sorted(sanatiheys):
        print(sana, ":", sanatiheys[sana], "times")


def main():
    sanatiheys = {}

    print("Enter rows of text for word counting. Empty row to quit.")

    while True:
        teksti = input("")

        if teksti == "":
            break
        else:
            pieni_teksti = teksti.lower()
            word_counter(pieni_teksti, sanatiheys)

    print_results(sanatiheys)


if __name__ == "__main__":
    main()