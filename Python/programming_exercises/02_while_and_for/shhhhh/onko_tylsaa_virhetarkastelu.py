"""
Ohjelmointi 1: tehtävä 2.2.2: Onko tylsää? (virhetarkastelu)
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

def main():
    tylsaa = True
    while tylsaa:
        tylsaa = input("Answer Y or N: ")
        if tylsaa == "y" or tylsaa == "n" or tylsaa == "Y" or tylsaa == "N":
            print("You answered" , tylsaa)
            tylsaa = False
        else:
            print("Incorrect entry.")

if __name__ == "__main__":
    main()

