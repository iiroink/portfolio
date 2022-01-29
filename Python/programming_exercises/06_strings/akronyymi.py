"""
Ohjelmointi 1: tehtävä 6.7: Akronyymin muodostaminen
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673

Kääntää nimen <sukunimi, etunimi> muotoon <etunimi sukunimi>.
"""

def create_an_acronym(nimi):
    """

    :param nimi:
    :return:
    """
    sanojen_maara = nimi.count(" ") + 1

    nimi = nimi.split(" ")

    akronyymi = ""

    for i in range(sanojen_maara):
        kirjain = nimi[i].upper()
        akronyymi += kirjain[0]

    return akronyymi