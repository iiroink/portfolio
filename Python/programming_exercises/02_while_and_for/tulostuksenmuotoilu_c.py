"""
Ohjelmointi 1: tehtävä 2.6.3: Tulosteen leveyden asettaminen
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""


def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i*j:4}", end="")
        print()

if __name__ == "__main__":
    main()
