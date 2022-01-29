def main():
    filename = input()

    try:
        file = open(filename, mode="r")
    except OSError:
        print("There was an error in reading the file.")
        return

    for line in file:
        line = line.rstrip()


        name, points = line.split()
        print(name, points)

    file.close()


if __name__ == "__main__":
    main()