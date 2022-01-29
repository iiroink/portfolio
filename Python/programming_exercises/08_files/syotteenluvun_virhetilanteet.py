"""
Ohjelmointi 1: tehtävä 8.4: Syötteenluvun virhetilanteet
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673


"""


def read_input(inp):
    """
    Checks that the entered number is an integer and greater than zero.

    :param inp: int, number entered by the user.
    :return: int, the number entered, when greater than zero.
    """
    do_the_loop = True
    while do_the_loop:
        try:
            number = int(input(inp))
            if number > 0:
                do_the_loop = False
        except ValueError:
            do_the_loop = True

    return number


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
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()