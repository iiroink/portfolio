"""
Ohjelmointi 1: tehtävä 4.11.1: Paranneltu ruudun tulostus
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""


def print_box(width, height, border_mark="#", inner_mark=" "):
    """Prints a box.

    :param width: int, width of the box.
    :param height: int, height of the box.
    :param border_mark: string, character used in the borders.
    :param inner_mark: string, character used in the filling.
    """
    print(width * border_mark)
    for _ in range(height - 2):
        print(f"{border_mark}{(width - 2) * inner_mark}{border_mark}")
    print(width * border_mark)
    print()


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)

if __name__ == "__main__":
    main()