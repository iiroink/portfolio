"""
Ohjelmointi 1: tehtävä 1.6.9: Kivi-paperi-sakset
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

def main():
    pelaaja1 = input("Player 1, enter your choice (R/P/S): ")
    pelaaja2 = input("Player 2, enter your choice (R/P/S): ")
    if pelaaja1 == pelaaja2:
        print("It's a tie!")
    elif pelaaja1 == "R" and pelaaja2 == "S":
        print("Player 1 won!")
    elif pelaaja1 == "P" and pelaaja2 == "R":
        print("Player 1 won!")
    elif pelaaja1 == "S" and pelaaja2 == "P":
        print("Player 1 won!")
    elif pelaaja1 == "R" and pelaaja2 == "P":
        print("Player 2 won!")
    elif pelaaja1 == "P" and pelaaja2 == "S":
        print("Player 2 won!")
    elif pelaaja1 == "S" and pelaaja2 == "R":
        print("Player 2 won!")

if __name__ == "__main__":
    main()