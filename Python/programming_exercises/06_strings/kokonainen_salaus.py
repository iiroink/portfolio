"""
Ohjelmointi 1: tehtävä 6.11: Kokonainen salaus
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""


def read_message():
    """Lukee käyttäjältä syötteitä ja lisää ne str-muotoisina listaan, kunnes
    käyttäjä syöttää tyhjän rivin.

    :param datalista: list, sisältää käyttäjän syöttämät arvot.
    :return:
    """
    message = []
    while True:
        # Liitetään käyttäjän antama luku muuttujaan.
        teksti = input()

        # Keskeyttää arvojen lukemisen, kun annetaan tyhjä rivi.
        if teksti == "":
            break
        else:
            message.append(teksti)

    return message


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
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("ROT13:")
    for rivi in msg:
        print(row_encryption(rivi))


if __name__ == "__main__":
    main()