#!/usr/bin/python3
"""class Student."""


class Student:
    """Representation of a student."""

    def __init__(self, first_name, last_name, age):
        """A new Student is initialized.

        Args:
            first_name (str): The student's first name.
            last_name (str): The  student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Fetches a dictionary representation of the Student.

        If attrs is a list of strings, represents only those attributes
        in the list.

        Args:
            attrs (list): (Optional)  attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
