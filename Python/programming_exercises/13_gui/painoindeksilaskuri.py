"""
Ohjelmointi 1: tehtävä 13.7: Painoindeksilaskuri
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673

Painoindeksilaskuri ja graafinen käyttöliittymä
"""

from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()

        self.__weight_text = Label(self.__mainwindow, text="Weight (kg):")
        self.__height_text = Label(self.__mainwindow, text="Height (cm):")

        # TODO: Create an Entry-component for the weight.
        self.__weight_value = Entry(self.__mainwindow)

        # TODO: Create an Entry-component for the height.
        self.__height_value = Entry(self.__mainwindow)
        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        #       the default colour.
        self.__calculate_button = Button(self.__mainwindow, text="Calculate BMI", background="lime green",
                                         command=self.calculate_BMI)

        # TODO: Create a Label that will show the decimal value of the BMI
        #      after it has been calculated.
        self.__result_text = Label(self.__mainwindow, text="0")

        # TODO: Create a Label that will show a verbal description of the BMI
        #       after the BMI has been calculated.
        self.__explanation_text = Label(self.__mainwindow, text="-")

        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow, text="Quit", background="OrangeRed", command=self.stop)

        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!
        self.__weight_text.grid(row=0, column=0)
        self.__height_text.grid(row=0, column=1)
        self.__weight_value.grid(row=1, column=0)
        self.__height_value.grid(row=1, column=1)
        self.__calculate_button.grid(row=2, column=0, columnspan=2)
        self.__stop_button.grid(row=5, column=0, columnspan=2)
        self.__result_text.grid(row=3, column=0, columnspan=2)
        self.__explanation_text.grid(row=4, column=0, columnspan=2)

    # TODO: Implement this method.

    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """

        error_value = "Error: height and weight must be numbers."
        error_negative = "Error: height and weight must be positive."

        try:
            weight = float(self.__weight_value.get())
        except ValueError:
            self.reset_fields(error_value)
            return

        try:
            height_cm = float(self.__height_value.get())
        except ValueError:
            self.reset_fields(error_value)
            return

        if weight < 0:
            self.reset_fields(error_negative)
            return

        if height_cm < 0:
            self.reset_fields(error_negative)
            return

        height_m = height_cm / 100

        bmi = weight / (height_m ** 2)

        self.__result_text.configure(text=f"{bmi:.2f}")

        if bmi < 18.5:
            message = "You are underweight."

        elif bmi <= 25:
            message = "Your weight is normal."

        else:
            message = "You are overweight."

        self.__explanation_text.configure(text=message)

    def reset_fields(self, error_prompt):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """

        self.__weight_value.delete(0, END)
        self.__weight_value.insert(0, "")
        self.__height_value.delete(0, END)
        self.__height_value.insert(0, "")
        self.__result_text.configure(text="")
        self.__explanation_text.configure(text=error_prompt)

    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()



"""    def get_values(self):

        error_value = "Error: height and weight must be numbers."
        error_negative = "Error: height and weight must be positive."

        try:
            weight = float(self.__weight_value.get())
        except ValueError:
            self.__explanation_text.configure(text=error_value)
            return self.reset_fields()

        try:
            height = float(self.__height_value.get())
        except ValueError:
            self.__explanation_text.configure(text=error_value)
            return self.reset_fields()

        if weight < 0:
            self.__explanation_text.configure(text=error_negative)
            return self.reset_fields()

        if height < 0:
            self.__explanation_text.configure(text=error_negative)
            return self.reset_fields()

        return weight, height
        """
    # TODO: Implement this method.

def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
