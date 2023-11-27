#!/usr/bin/python3
"""Definition of a Rectangle class."""


class Rectangle:
    """Represention of a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialization of a new Rectangle.
        Args:
            width (int):  width of new rectangle.
            height (int): height of new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns a printable representation of the Rectangle.

        Represents the rectangle using # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for x in range(self.__height):
            [rectangle.append('#') for j in range(self.__width)]
            if x != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))
