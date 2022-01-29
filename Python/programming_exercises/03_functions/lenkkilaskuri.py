"""
Ohjelmointi 1: tehtävä 3.3: Lenkkilaskuri
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""


def main():
    # Kysytään seurattavien päivien määrä.
    paivien_maara = int(input("Enter the number of days: "))

    # Juokseva luku, tarkasteltava päivä.
    paiva = 1
    # Perättäisten lepopäivien määrä.
    lepopaiva = 0
    # Käyttäjän päivittäisten juoksulenkkien keskiarvo.
    keskipituus = 0

    # Kysytään käyttäjältä päivän juoksumäärää, kunnes saavutetaan käyttäjän
    # antama päivien määrä tai kolme peräkkäistä lepopäivää.
    while paiva <= paivien_maara:
        lenkin_pituus = float(input(f"Enter day {paiva} running length: "))

        # Lasketaan peräkkäisten lepopäivien määrä. Jos päästään kolmeen,
        # liputetaan toisto.
        if lenkin_pituus == 0:
            lepopaiva += 1
        else:
            lepopaiva = 0
        if lepopaiva == 3:
            break

        # Lasketaan jokaisen päivän osuus keskiarvosta valmiiksi, jolloin
        # keskipituus on vain summa
        keskipituus += lenkin_pituus / paivien_maara

        paiva += 1

    # Tulostetaan ensin tyhjä rivi, sitten haluttu yhteenveto
    print()
    # Kolme peräkkäistä lepopäivää.
    if lepopaiva == 3:
        print("You had too many consecutive lazy days!")
    # Keskimääräinen juoksumatka alle 3km päivässä.
    elif keskipituus < 3:
        print(f"Your running mean of {keskipituus:.2f} km was too low!")
    # Keskimääräinen juoksumatka 3km tai enemmän päivässä.
    else:
        print(
            f"You were persistent runner! With a mean of {keskipituus:.2f} km.")


if __name__ == "__main__":
    main()