"""
Ohjelmointi 1: tehtävä 6.4: Vokaalit ja konsonantit
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673

Laskee syötetyn sanan vokaalit ja konsonantit.
"""


def vokaali_laskuri(sana):
    """

    :param sana:
    :return:
    """
    vokaaleja = 0
    konsonantteja = 0

    for kirjain in sana:
        if kirjain == "a" or kirjain == "e" or kirjain == "i" or kirjain == "o"\
                or kirjain == "u" or kirjain == "y":
            vokaaleja += 1
        else:
            konsonantteja += 1

    print(f'The word "{sana}" contains {vokaaleja} vowels and {konsonantteja}'
          f' consonants.')


def main():
    sana = input("Enter a word: ")

    vokaali_laskuri(sana)


if __name__ == "__main__":
        main()