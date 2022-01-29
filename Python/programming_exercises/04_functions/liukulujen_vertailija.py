"""
Ohjelmointi 1: tehtävä 4.6.1: Liukulukujen (desimaalilukujen) vertaileminen
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

def compare_floats(float_1, float_2, EPSILON):
    """
    Compares two

    :param float_1: float,
    :param float_2:
    :param EPSILON:
    :return: bool,
    """
    absolute = abs(float_1 - float_2)

    return absolute < EPSILON

