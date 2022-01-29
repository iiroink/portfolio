"""
Ohjelmointi 1: tehtävä 2.3.2: Kerottaulu, yli sadan
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

def main():
    numero = input("Choose a number: ")
    numero = int(numero)
    kerroin = 1
    tulos = numero

    while tulos < 100:
        tulos = kerroin * numero
        print(kerroin , "*" , numero , "=" , tulos)
        kerroin += 1

if __name__ == "__main__":
    main()