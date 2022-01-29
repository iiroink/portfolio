"""
Ohjelmointi 1: tehtävä 11.2: Murtoluku
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673

Murtolukuluokka
"""


class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        """
        Simplifies the fraction to smallest form
        """
        gcd = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator // gcd
        self.__denominator = self.__denominator // gcd

    def complement(self):
        """
        Makes a new object that is the complement of self.
        :return: New object
        """
        multiplier = -1

        new_numerator = self.__numerator * multiplier

        result = Fraction(new_numerator, self.__denominator)
        return result

    def reciprocal(self):
        """
        Calculates the reciprocal.
        :return: New object
        """
        new_numerator = self.__denominator
        new_denominator = self.__numerator

        result = Fraction(new_numerator, new_denominator)
        return result

    def multiply(self, fraction2):
        """
        Multiplies self and fraction2
        :param fraction2: fraction
        :return: new object
        """
        new_numerator = self.__numerator * fraction2.__numerator
        new_denominator = self.__denominator * fraction2.__denominator

        result = Fraction(new_numerator, new_denominator)
        return result

    def divide(self, fraction2):
        """
        Divides self by fraction2
        :param fraction2: fraction
        :return: new object
        """
        multiplier = fraction2.reciprocal()

        new_numerator = self.__numerator * multiplier.__numerator
        new_denominator = self.__denominator * multiplier.__denominator

        result = Fraction(new_numerator, new_denominator)
        return result

    def add(self, fraction2):
        """
        Adds self and fraction2
        :param fraction2: fraction
        :return: new object
        """
        new_denominator = self.__denominator * fraction2.__denominator
        numerator1 = self.__numerator * fraction2.__denominator
        numerator2 = fraction2.__numerator * self.__denominator

        new_numerator = numerator1 + numerator2

        result = Fraction(new_numerator, new_denominator)
        return result

    def deduct(self, fraction2):
        """
        Deducts self and fraction2
        :param fraction2: fraction
        :return: new object
        """
        new_denominator = self.__denominator * fraction2.__denominator
        numerator1 = self.__numerator * fraction2.__denominator
        numerator2 = fraction2.__numerator * self.__denominator

        new_numerator = numerator1 - numerator2

        result = Fraction(new_numerator, new_denominator)
        return result

    def __lt__(self, other):
        numerator1 = self.__numerator * other.__denominator
        numerator2 = other.__numerator * self.__denominator

        determiner = numerator1 - numerator2
        if determiner <= 0:
            return True
        else:
            return False

    def __gt__(self, other):
        numerator1 = self.__numerator * other.__denominator
        numerator2 = other.__numerator * self.__denominator

        determiner = numerator1 - numerator2
        if determiner >= 0:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a


def main():
    # a
    frac = Fraction(-2, 4)
    print(frac.return_string())

    complement = frac.complement()
    print(complement.return_string())

    reciprocal = frac.reciprocal()
    print(reciprocal.return_string())

    # b
    frac1 = Fraction(2, 3)
    frac2 = Fraction(3, 4)

    product = frac1.multiply(frac2)
    print(product.return_string())

    product.simplify()
    print(product.return_string())

    # c
    frac1 = Fraction(4, 8)
    frac2 = Fraction(2, 1)

    quotient = frac1.divide(frac2)
    print(quotient.return_string())

    quotient.simplify()
    print(quotient.return_string())

    # d
    frac1 = Fraction(2, 3)
    frac2 = Fraction(1, 6)

    sum = frac1.add(frac2)
    print(sum.return_string())

    sum.simplify()
    print(sum.return_string())

    frac1 = Fraction(2, 3)
    frac2 = Fraction(1, 6)

    difference = frac1.deduct(frac2)
    print(difference.return_string())

    difference.simplify()
    print(difference.return_string())

    #6
    frac1 = Fraction(1, 2)
    frac2 = Fraction(2, 3)

    print(frac1 < frac2)

    print(frac1 > frac2)

    # 7
    frac = Fraction(8, 18)
    print(frac)

    frac.simplify()
    print(frac)


if __name__ == "__main__":
    main()
