"""
Ohjelmointi 1: tehtävä 2.8.2: Vuoden päivämäärät
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

def main():
    kuukausi = 1

    while kuukausi <= 12:
        paiva = 1
        if kuukausi == 2:
            vika_paiva = 28
        elif kuukausi == 4 or kuukausi == 6 or kuukausi == 9 or kuukausi == 11:
            vika_paiva = 30
        else:
            vika_paiva = 31

        for paiva in range(paiva , vika_paiva + 1):
            print(f"{paiva}.{kuukausi}.")

        kuukausi += 1

if __name__ == "__main__":
    main()