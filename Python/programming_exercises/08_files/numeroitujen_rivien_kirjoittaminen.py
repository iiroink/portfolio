"""
Ohjelmointi 1: tehtävä 8.9: Numeroitujen rivien kirjoittaminen tiedostoon
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673

Numeroi syötetyt rivit ja tallentaa ne annettuun tiedostoon.
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
    filename = input("Enter the name of the file: ")

    try:
        file = open(filename, mode="w")
    except OSError:
        print(f"Writing the file {filename} was not successful.")
        return

    print("Enter rows of text. Quit by entering an empty row.")
    msg = read_message()

    number = 1

    for line in msg:
        print(number, line, file=file)
        number += 1

    file.close()

    print(f"File {filename} has been written.")


if __name__ == "__main__":
    main()