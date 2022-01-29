"""
Ohjelmointi 1: tehtävä 5.3.1: Listan alkioiden läpikäyminen
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

def main():

    list_of_numbers = []
    print("Give 5 numbers:")
    for _ in range(5):
        number = int(input("Next number: "))
        list_of_numbers.append(number)

    print("The numbers you entered that were greater than zero were:")
    for given_number in list_of_numbers:
       if given_number > 0:
           print(given_number)

if __name__ == "__main__":
    main()