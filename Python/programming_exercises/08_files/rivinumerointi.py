"""
Ohjelmointi 1: tehtävä 8.6: Tiedoston rivien numerointi
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673

Numeroi annetun tiedoston rivit.
"""


def main():
    filename = input("Enter the name of the file: ")

    try:
        file = open(filename, mode="r")

    except OSError:
        print("There was an error in reading the file.")
        return

    linenumber = 1

    for line in file:
        print(linenumber, line.rstrip())
        linenumber += 1

    file.close()


if __name__ == "__main__":
    main()