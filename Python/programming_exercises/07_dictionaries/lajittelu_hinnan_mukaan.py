"""
Ohjelmointi 1: tehtävä 7.10: Tanssipelien pisteet
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673

Lajittelee sanakirjan hyötykuorman suuruusjärjestyksen mukaan.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def payload(key):
    """

    :param key:
    :return:
    """
    price = PRICES[key]
    return price


def main():
    for item in sorted(PRICES, key=payload):
        print(f"{item} {PRICES[item]:.2f}")


if __name__ == "__main__":
    main()