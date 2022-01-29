"""
Ohjelmointi 1: tehtävä 3.6.2: Yogi Bear -laulu
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

def repeat_name(name, number_of_lines):
    """Tulostaa kysytyn määrän säkeitä valitulla nimellä.

    :param name: string, karhun nimi.
    :param number_of_lines: int, tulostettavien rivien määrä.
    """
    for _ in range(number_of_lines):
        print(f"{name}, {name} Bear")

def verse(line, bear_name):
    """
    Tulostaa yhden säkeistön laulua.

    :param line: string, muuttuva säe.
    :param bear_name: string, karhun nimi.
    """
    print(line)
    print(f"{bear_name}, {bear_name}")
    print(line)
    repeat_name(bear_name, 3)
    print(line)
    print(f"{bear_name}, {bear_name} Bear")


def main():
    verse("I know someone you don't know", "Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")

if __name__ == "__main__":
    main()
