"""
Ohjelmointi 1: tehtävä 4.10.1: Kolmion kulmien laskeminen
Nimi: Iiro Inkinen, Hervanta
Opiskelijanumero: 50393673
"""

def calculate_angle(angle1, angle2=90):
    """Calculates the third angle of a triangle.

    :param angle1: float, first angle of the triangle.
    :param angle2: float, second angle of the triangle.
    :return: float, the thrid angle of the triangle.
    """
    angle3 = 180 - angle1 - angle2
    return angle3