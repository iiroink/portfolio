"""
Ohjelmointi 1: tehtävä 6.6: Käännä nimet oikein päin
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673

Kääntää nimen <sukunimi, etunimi> muotoon <etunimi sukunimi>.
"""


def reverse_name(nimi):
    """

    :param nimi:
    :return:
    """

    if nimi.count(",") == 0:
        return nimi

    nimi = nimi.split(",")

    etunimi = nimi[1]
    etunimi = etunimi.strip()

    sukunimi = nimi[0]
    sukunimi = sukunimi.strip()

    uusi_nimi = f"{etunimi} {sukunimi}"
    uusi_nimi = uusi_nimi.strip()

    return uusi_nimi
