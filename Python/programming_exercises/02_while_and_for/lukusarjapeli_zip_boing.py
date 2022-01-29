"""
Ohjelmointi 1: tehtävä 2.4.1: Lukusarjapeli zip boing
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

def main():
    viimeinen_luku = input("How many numbers would you like to have? ")
    viimeinen_luku = int(viimeinen_luku)
    juokseva_luku = 1

    while viimeinen_luku >= juokseva_luku:
        if juokseva_luku % 21 == 0:
            print("zip boing")
        elif juokseva_luku % 3 == 0:
            print("zip")
        elif juokseva_luku % 7 == 0:
            print("boing")
        else:
            print (juokseva_luku)
        juokseva_luku += 1

if __name__ == "__main__":
    main()