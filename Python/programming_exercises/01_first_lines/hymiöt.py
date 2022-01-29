"""
Ohjelmointi 1: tehtävä 1.6.8: Hymiöt
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

def main():
    arviointi = input("How do you feel? (1-10) ")
    tunnetila = float(arviointi)
    if tunnetila < 1 or tunnetila > 10:
        print("Bad input!")
    else:
        if tunnetila == 10:
            smiley = ":-D"
        elif tunnetila > 7:
            smiley = ":-)"
        elif tunnetila >= 4:
            smiley = ":-|"
        elif tunnetila == 1:
            smiley = ":'("
        else:
            smiley = ":-("
        print("A suitable smiley would be" , smiley)
if __name__ == "__main__":
    main()