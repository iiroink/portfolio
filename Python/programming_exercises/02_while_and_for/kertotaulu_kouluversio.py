"""
Ohjelmointi 1: tehtävä 2.3.1: Kerottaulu, kouluversio
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

def main():
    numero = input("Choose a number: ")
    numero = int(numero)

    i = 1
    while i <= 10:
        print(i , "*" , numero , "=" , i * numero)
        i += 1


if __name__ == "__main__":
    main()