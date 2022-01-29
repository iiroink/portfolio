"""
Ohjelmointi 1: tehtävä 7.3: Hintalista
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673

Tells user prices of few products.
"""


GOODBYE_GREETING = "Bye!"


PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    while True:
        product = input("Enter product name: ")
        product = product.strip()

        if product in PRICES:
            print(f"The price of {product} is {PRICES[product]:.2f} e")
        elif product == "":
            break
        else:
            print(f"Error: {product} is unknown.")

    print(GOODBYE_GREETING)


if __name__ == "__main__":
    main()