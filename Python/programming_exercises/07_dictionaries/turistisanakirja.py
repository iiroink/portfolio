"""
Ohjelmointi 1: tehtävä 7.3: Hintalista
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673

Simple english-spanish dictionary.
"""


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    sort_dict = sorted(english_spanish)
    contents = ", ".join(sort_dict)
    print("Dictionary contents:")
    print(contents)


    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")

            else:
                print(
                    f"The word {word} could not be found from the dictionary.")

        elif command == "A":
            english = input("Give the word to be added in English: ")
            spanish = input("Give the word to be added in Spanish: ")

            english_spanish[english] = spanish

            sort_dict = sorted(english_spanish)
            contents = ", ".join(sort_dict)
            print("Dictionary contents:")
            print(contents)

        elif command == "R":
            word = input("Give the word to be removed: ")
            if word in english_spanish:
                del english_spanish[word]
            else:
                print(
                    f"The word {word} could not be found from the dictionary.")

        elif command == "P":
            print()
            print("English-Spanish")

            for sana in sorted(english_spanish):
                print(sana, english_spanish[sana])

            print()
            print("Spanish-English")

            spanish_english = {}
            for enkku in english_spanish:
                spanish_english[english_spanish[enkku]] = enkku

            for sana in sorted(spanish_english):
                print(sana, spanish_english[sana])

            print()

        elif command == "T":
            sentence = input("Enter the text to be translated into Spanish: ")
            sentence = sentence.split(" ")

            spanish_sentence = []

            for single in sentence:
                if single in english_spanish:
                    spanish_sentence.append(english_spanish[single])
                else:
                    spanish_sentence.append(single)

            print("The text, translated by the dictionary:")

            for i in spanish_sentence:
                print(i, end = " ")

            print()

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()