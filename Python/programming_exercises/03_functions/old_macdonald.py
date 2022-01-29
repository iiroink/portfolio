"""
Ohjelmointi 1: tehtävä 3.6.1: Old MacDonald Had a Farm -laulu
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

def print_verse(animal, sound):
    """Tulostaa Piippolan Vaari -laulun.

    :param animal: string, tietyn säkeistön eläin.
    :param sound: string, säkeistön eläimen ääni.
    """
    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print(f"And on his farm he had a {animal}")
    print("E-I-E-I-O")
    print(f"With a {sound} {sound} here")
    print(f"And a {sound} {sound} there")
    print(f"Here a {sound}, there a {sound}")
    print(f"Everywhere a {sound} {sound}")
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")


def main():
    print_verse("cow", "moo")
    print()
    print_verse("pig", "oink")
    print()
    print_verse("duck", "quack")
    print()
    print_verse("horse", "neigh")
    print()
    print_verse("lamb", "baa")

if __name__ == "__main__":
    main()