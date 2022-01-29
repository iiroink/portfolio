"""
Ohjelmointi 1: tehtävä 5.6.1: Arvosanojen korvaus
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

def convert_grades(grades):
    """Converts all numbers except zeroes to sixes.

    :param grades: list, grades
    :return: 
    """
    length = len(grades)

    if length > 0:
        for single_grade in grades:
            if single_grade != 0:
                grades[grades.index(single_grade)] = 6


def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()