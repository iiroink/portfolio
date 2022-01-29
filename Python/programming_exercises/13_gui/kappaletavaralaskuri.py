"""
Ohjelmointi 1: tehtävä 13.5: Kappaletavaralaskuri
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673

Kappaletavaralaskuri ja graafinen käyttöliittymä
"""


from tkinter import *


class Counter:
    def __init__(self):

        self.__main_window = Tk()
        self.__number = 0

        self.__current_value_label = Label(self.__main_window, text=self.__number)
        self.__current_value_label.grid(row=0, column=0, columnspan=2, sticky=E+W)

        self.__increase_button = Button(self.__main_window, text="Increase", command=self.increase)
        self.__increase_button.grid(row=1, column=1, sticky=N+E+S+W)

        self.__decrease_button = Button(self.__main_window, text="Decrease", command=self.decrease)
        self.__decrease_button.grid(row=1, column=0, sticky=N+E+S+W)

        self.__reset_button = Button(self.__main_window, text="Reset", command=self.reset)
        self.__reset_button.grid(row=2, column=0, sticky=N+E+S+W)

        self.__quit_button = Button(self.__main_window, text="Quit", command=self.quit)
        self.__quit_button.grid(row=2, column=1, sticky=N+E+S+W)

        self.__main_window.mainloop()

    def increase(self):
        self.__number += 1
        self.__current_value_label.configure(text=self.__number)

    def decrease(self):
        self.__number -= 1
        self.__current_value_label.configure(text=self.__number)

    def reset(self):
        self.__number = 0
        self.__current_value_label.configure(text=self.__number)

    def quit(self):
        self.__main_window.destroy()


def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()


if __name__ == "__main__":
    main()
