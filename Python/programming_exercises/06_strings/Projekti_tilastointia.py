"""
Ohjelmointi 1: tehtävä 6.2: Projekti: Tilastointia
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673

Laskee syötetyn aineiston keskiarvon ja -hajonnan, sekä piirtää histogrammin
hajonnasta.
"""

# Tuodaan neliöjuurifunktio kirjastosta.
from math import sqrt


def datan_syotto(datalista):
    """Lukee käyttäjältä syötteitä ja lisää ne float-muotoisina listaan, kunnes
    käyttäjä syöttää tyhjän rivin.

    :param datalista: list, sisältää käyttäjän syöttämät arvot.
    :return:
    """
    while True:
        # Liitetään käyttäjän antama luku muuttujaan.
        arvo = input()

        # Keskeyttää arvojen lukemisen, kun annetaan tyhjä rivi.
        if arvo == "":
            break
        # Muutetaan arvo desimaaliluvuksi ja lisätään se listaan.
        else:
            desimaaliarvo = float(arvo)
            datalista.append(desimaaliarvo)


def keskiarvo_laskuri(datalista):
    """Laskee annetun listan alkioiden keskiarvon.

    :param datalista: list, sisältää käyttäjän syöttämät arvot.
    :return: float, keskiarvo listan alkioista.
    """
    # Määritetään apumuuttuja alkioiden määrälle ja alustetaan muuttuja summa.
    alkioiden_maara = len(datalista)
    summa = 0

    # Lasketaan yhteen kaikki listan alkiot.
    for alkio in datalista:
        summa += alkio

    # Keskiarvo saadaan jakamalla summa alkioiden määrällä.
    keskiarvo = summa / alkioiden_maara

    # Palautetaan keskiarvo.
    return keskiarvo


def keskihajonta_laskuri(datalista, keskiarvo):
    """Laskee listan alkoiden keskihajonnan. (Ja varianssin, mutta sitä ei
    toistaiseksi käytetä.)

    :param datalista: list, sisältää käyttäjän syöttämät arvot.
    :param keskiarvo: float, listan alkioiden keskiarvo.
    :return: float, listan alkioiden keskihajonta.
    """
    # Määritetään apumuuttuja alkioiden määrälle ja alustetaan muuttuja summa.
    alkioiden_maara = len(datalista)
    summa = 0

    # Lasketaan varianssi.
    for alkio in datalista:
        etaisyys = (alkio - keskiarvo) ** 2
        summa += etaisyys

    varianssi = (1 / (alkioiden_maara - 1)) * summa

    # Keskihajonta on varianssin neliöjuuri.
    keskihajonta = sqrt(varianssi)

    # Palautetaan keskihajonta. Myös varianssi olisi helppo palauttaa, jos sitä
    # tarvittaisiin.
    return keskihajonta


def histogrammin_piirtaja(datalista, keskiarvo, keskihajonta):
    """Piirtää histogrammin käyttäjän antaman datan keskihajonnasta.

    :param datalista: list, sisältää käyttäjän syöttämät arvot.
    :param keskiarvo: float, listan alkioiden keskiarvo.
    :param keskihajonta: float, listan alkioiden keskihajonta.
    :return:
    """
    # Luodaan uusi lista, johon lasketaan alkuperäisen listan alkioiden
    # hajonta-arvot.
    hajonta_lista = []

    for alkio in datalista:
        etaisyys = abs(alkio - keskiarvo)
        hajonta_lista.append(etaisyys)

    # Laskee histogrammiin tulevien kuuden gategorian ala- ja ylärajat.
    for kategorian_numero in range(0, 6):
        alaraja = kategorian_numero * 0.5 * keskihajonta
        ylaraja = (kategorian_numero + 1) * 0.5 * keskihajonta

        # Alustetaan muuttuja summa.
        summa = 0

        # Tarkastetaan hajonta_listan jokaisen alkion kohdalla, kuuluuko se
        # kyseiseen väliin. Kahden kategorian rajalla oleva alkio kuuluu
        # suurempaan kategoriaan.
        for alkio in hajonta_lista:
            if alaraja <= alkio < ylaraja:
                # Summa kertoo välillä olevien alkioiden määrän.
                summa += 1

        # Histogrammiin tulostettava palkki.
        palkki = summa * "*"

        # Tulostaa yhden rivin histogrammiin.
        print(f"Values between std. dev. ", end="")
        print(f"{alaraja:0.2f}-{ylaraja:0.2f}: {palkki}")


def main():
    # Tulostaa ohjetekstin käyttäjälle.
    print("Enter the data, one value per line.")
    print("End by entering empty line.")

    # Luodaan tyhjä lista, johon käyttäjän syöttämät arvot lisätään funktiossa.
    datalista = []
    datan_syotto(datalista)

    # Luodaan apumuuttuja listan alikoiden määrälle.
    alkioiden_maara = len(datalista)

    # Tarkistaa, että listassa on vähintään kaksi arvoa.
    if alkioiden_maara < 2:
        print("Error: needs two or more values.")
    else:
        # Laskee keskiarvon funktiossa ja tulostaa sen kahden desimaalin
        # tarkkuudella.
        keskiarvo = keskiarvo_laskuri(datalista)
        print(f"The mean of given data was: {keskiarvo:0.2f}")

        # Laskee keskihajonnan funktiossa ja tulostaa sen kahden desimaalin
        # tarkkuudella.
        keskihajonta = keskihajonta_laskuri(datalista, keskiarvo)
        print(f"The standard deviation of given data was: {keskihajonta:0.2f}")

        # Tarkastaa, onko keskihajonta nolla.
        if keskihajonta == 0:
            print("Deviation is zero.")
        # Kutsuu funktiota, joka piirtää histogrammin.
        else:
            histogrammin_piirtaja(datalista, keskiarvo, keskihajonta)


if __name__ == "__main__":
    main()