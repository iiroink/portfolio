"""
Ohjelmointi 1: tehtävä 3.6.3: Tulostetaan ruutu
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

def print_box(wid, heig, drawing_mark):
    """
    Prints a box with given width, height and symbol.

    :param wid: int, width of the box.
    :param heig: int, height of the box.
    :param drawing_mark: string, drawing symbol.
    """
    for _ in range(heig):
        print(wid * drawing_mark)

def main():
    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
