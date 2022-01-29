"""
Ohjelmointi 1: tehtävä 10.4: Tuote
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673

Product price and sale calculator.
"""


class Product:
    """
    This class defines a simplified product for sale in a store.
    """

    def __init__(self, name, price, discount=0.0):
        """
        Each product is initialized with name, prize and discount.

        :param name: str, name of the product
        :param price: float, price of the product
        :param discount: float, discount 0.0 as default
        """

        self.__name = name
        self.__price = price
        self.__discount = discount

    def printout(self):
        """
        Prints
        name: <name>
          price: <price>
          sale%: <discount>
        """

        print(self.__name)
        print(f"  price: {self.__price:.2f}")
        print(f"  sale%: {self.__discount:.2f}")

    def set_sale_percentage(self, discount):
        """
        Calculates the discounted price.
        :param discount: float
        """

        self.__discount = discount

    def get_price(self):
        """

        :return: The price
        """
        return (1 - (0.01 * self.__discount)) * self.__price


def main():
    ################################################################
    #                                                              #
    #  You can use the main-function to test your Product class.   #
    #  The automatic tests will not use the main you submitted.    #
    #                                                              #
    #  Voit käyttää main-funktiota Product-luokkasi testaamiseen.  #
    #  Automaattiset testit eivät käytä palauttamaasi mainia.      #
    #                                                              #
    ################################################################

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
