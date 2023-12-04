#!/usr/bin/python3
"""writes a class that inherits another"""


class MyList(list):
    """Inherits a class"""

    def print_sorted(self):
        """prints sorted list"""

        print(sorted(self))
