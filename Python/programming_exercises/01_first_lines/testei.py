syote_hinta = input("Purchase price: ")
syote_raha = input("Paid amount of money: ")
hinta = int(syote_hinta)
raha = int(syote_raha)
vaihtoraha = raha - hinta

vaihtoraha = vaihtoraha % 10

print(vaihtoraha)
