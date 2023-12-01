#!/usr/bin/python3
"""function that adds integers"""


def add_integer(a, b=98):
    """
    Checks if int and returns sum
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return a + b
