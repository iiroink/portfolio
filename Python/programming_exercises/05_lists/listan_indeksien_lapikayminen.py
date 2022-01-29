"""
Ohjelmointi 1: tehtävä 5.3.2: Listan indeksien läpikäyminen
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

def main():

    list_of_numbers = []
    print("Give 5 numbers:")
    for _ in range(5):
        number = int(input("Next number: "))
        list_of_numbers.append(number)

    print("The numbers you entered, in reverse order:")
    i = len(list_of_numbers) - 1
    while i >= 0:
        print(list_of_numbers[i])
        i -= 1

if __name__ == "__main__":
    main()