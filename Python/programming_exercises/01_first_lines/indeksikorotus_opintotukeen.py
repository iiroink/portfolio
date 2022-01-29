"""
Ohjelmointi 1: tehtävä 1.6.4: Indeksikorotus opintotukeen
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

syöte = input("Enter the amount of the study benefits: ")
opintotuki = float(syöte)
indeksikorotus = 1.0117
korotettu_tuki_1 = (opintotuki * indeksikorotus)
print("If the index raise is 1.17 percent, the study benefit,")
print("after a raise, would be" , korotettu_tuki_1 , "euros")
korotettu_tuki_2 = (korotettu_tuki_1 * indeksikorotus)
print("and if there was another index raise, the study")
print("benefits would be as much as" , korotettu_tuki_2 , "euros")