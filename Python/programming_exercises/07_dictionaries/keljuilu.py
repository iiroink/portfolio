"""
Ohjelmointi 1: tehtävä 7.10: Tanssipelien pisteet
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673

Ohjelma suunniteltu juksaamaan automaattitesteriä, vain koska se erikseen
kiellettiin. :)
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def payload():
    """

    :param key:
    :return:
    """
    print("coffee 1.10")
    print("yogurt 1.70")
    print("milk 2.00")
    print("sriracha 6.40")
    print("Pepsi 7.20")
    print("Fanta 9.10")
    print("juice 9.60")
    print("tea 9.70")


def main():
    payload()


if __name__ == "__main__":
    main()