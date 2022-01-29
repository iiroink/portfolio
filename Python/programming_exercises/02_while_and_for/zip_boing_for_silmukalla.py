"""
Ohjelmointi 1: tehtävä 2.5.1: Lukusarjapeli zip boing for-silmukalla
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

def main():
    suurin_luku = int(input("How many numbers would you like to have? "))
    juokseva_luku = 1

    for juokseva_luku in range(juokseva_luku,suurin_luku+1):
        if juokseva_luku % 21 == 0:
            print("zip boing")
        elif juokseva_luku % 3 == 0:
            print("zip")
        elif juokseva_luku % 7 == 0:
            print("boing")
        else:
            print(juokseva_luku)



if __name__ == "__main__":
    main()