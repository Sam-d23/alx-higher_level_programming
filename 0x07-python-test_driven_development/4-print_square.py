#!/usr/bin/python3
"""
Code for "4-print_square" module.
It supplies one function, print_square(size).
"""


def print_square(size):
    """a square is printed using "#"'s that has a length of size"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
