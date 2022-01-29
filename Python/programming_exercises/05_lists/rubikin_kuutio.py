"""
Ohjelmointi 1: tehtävä 5.5.3: Rubikin kuutio -kilpailut
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""


def time_counter(list_of_times):
    """Removes the maximum and minimum numbers and counts the average for
    5 times.

    :param list_of_times: list
    :return: list
    """
    maximum = max(list_of_times)
    minimum = min(list_of_times)

    list_of_times.remove(maximum)
    list_of_times.remove(minimum)

    time1 = list_of_times[0]
    time2 = list_of_times[1]
    time3 = list_of_times[2]

    competition_time = (time1 + time2 + time3) / 3

    return competition_time


def main():
    list_of_times = []
    for count in range(1, 6):
        time = float(input(f"Enter the time for performance {count}: "))
        list_of_times.append(time)

    competition_time = time_counter(list_of_times)
    print(f"The official competition score is {competition_time:.2f} seconds.")


if __name__ == "__main__":
    main()
