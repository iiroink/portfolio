"""
Ohjelmointi 1: tehtävä 9.5: TV-sarjan valitseminen
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673

Read genres and tv-series from a file into a dict.
Print a list of the genres in alphabetical order
and list tv-series by given genre on user's command.
"""


def read_file(filename):
    """
    Reads and saves the series and their genres from the file.
    :param filename: file containing the series and their genres.
    :return: dict, genres are keys, series in them are sublists.
    """

    try:
        file = open(filename, mode="r")

        recommender = {}

        for row in file:

            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            name, genres = row.rstrip().split(";")

            genres = genres.split(",")

            for one_genre in genres:
                if one_genre not in recommender.keys():
                    recommender[one_genre] = []
                recommender[one_genre].append(name)

        file.close()
        return recommender

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)

    genre_selection = ", ".join(sorted(genre_data))

    print("Available genres are:", genre_selection)

    while True:
        genre = input("> ")

        if genre == "exit":
            return

        else:
            if genre in genre_selection:
                shows = genre_data[genre]
                for show in sorted(shows):
                    print(show)


if __name__ == "__main__":
    main()
