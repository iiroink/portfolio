"""
Ohjelmointi 1: tehtävä 6.10: Viestin tallentaminen
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



def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("The same, shouting:")
    for rivi in msg:
        print(rivi.upper())


if __name__ == "__main__":
    main()