"""
Ohjelmointi 1: tehtävä 8.12: Pisteiden laskentaa
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673

Laksee tiedoston pistetilanteen.
"""

def main():
    filename = input("Enter the name of the score file: ")

    try:
        file = open(filename, mode="r")
    except OSError:
        print("There was an error in reading the file.")
        return

    scoresheet = {}

    for line in file:
        line = line.rstrip()

        try:
            name, points = line.split()
        except ValueError:
            print("There was an erroneous line in the file:")
            print(line)
            return

        try:
            points = int(points)
        except ValueError:
            print("There was an erroneous score in the file:")
            print(points)
            return

        if name not in scoresheet:
            scoresheet[name] = points
        else:
            scoresheet[name] += points

    print("Contestant score:")

    for player in sorted(scoresheet):
        print(player, scoresheet[player])

    file.close()


if __name__ == "__main__":
    main()