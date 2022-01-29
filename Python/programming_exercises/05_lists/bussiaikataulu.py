"""
Ohjelmointi 1: tehtävä 5.7: Bussiaikataulu
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""


def time_counter(bus_times, current_time):
    """

    :param bus_times:
    :param current_time:
    :return:
    """
    if current_time > 2000:
        first_bus_index = 0
    else:
        index = 0
        while True:
            if current_time > bus_times[index]:
                index += 1
            else:
                first_bus_index = index
                break

    print("The next buses leave: ")

    length = len(bus_times)
    if first_bus_index <= (length - 3):
        print(bus_times[first_bus_index])
        print(bus_times[first_bus_index + 1])
        print(bus_times[first_bus_index + 2])

    elif first_bus_index == 4:
        print(bus_times[4])
        print(bus_times[5])
        print(bus_times[0])

    elif first_bus_index == 5:
        print(bus_times[5])
        print(bus_times[0])
        print(bus_times[1])

    else:
        print("Error.")

def main():
    bus_times = [630, 1015, 1415, 1620, 1720, 2000]

    current_time = int(input("Enter the time (as an integer): "))

    time_counter(bus_times, current_time)

if __name__ == "__main__":
    main()