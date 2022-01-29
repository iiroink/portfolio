"""
Ohjelmointi 1: tehtävä 1.6.10: Vaihtorahat
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

def main():
    syote_hinta = input("Purchase price: ")
    syote_raha = input("Paid amount of money: ")
    hinta = int(syote_hinta)
    raha = int(syote_raha)
    vaihtoraha = raha - hinta

    if vaihtoraha <= 0:
        print("No change")
    else:
        print("Offer change:")
        if vaihtoraha // 10 >= 1:
            print(vaihtoraha // 10, "ten-euro notes")
            vaihtoraha = vaihtoraha % 10
        if vaihtoraha // 5 >= 1:
            print(vaihtoraha // 5, "five-euro notes")
            vaihtoraha = vaihtoraha % 5
        if vaihtoraha // 2 >= 1:
            print(vaihtoraha // 2, "two-euro coins")
            vaihtoraha = vaihtoraha % 2
        if vaihtoraha >= 1:
            print(vaihtoraha // 1, "one-euro coins")

if __name__ == "__main__":
    main()