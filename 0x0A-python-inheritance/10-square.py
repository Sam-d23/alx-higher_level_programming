#!/usr/bin/python3
"""Rectangle with subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of a square."""

    def __init__(self, size):
        """Initializes a new square.

        Args:
            size (int): size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
