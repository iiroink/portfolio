"""
Ohjelmointi 1: tehtävä 2.8.1: Onko tylsää? (parannettu versio)
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""


def main():
    tylsaa = True
    while tylsaa:
        tylsyys = input("Bored? (y/n) ")
        if tylsyys == "y" or tylsyys == "Y":
            tylsaa = False
        elif tylsyys == "n" or tylsyys == "N":
            tylsaa = True
        else:
            print("Incorrect entry.")

    print("Well, let's stop this, then.")


if __name__ == "__main__":
    main()