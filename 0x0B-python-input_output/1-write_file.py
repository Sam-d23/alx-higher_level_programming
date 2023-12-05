#!/usr/bin/python3
"""A function that writes file."""


def write_file(filename="", text=""):
    """a string is written to a UTF8 text file.

    Args:
        filename (str): name of the file to be written.
        text (str): text to write to the file.
    Returns:
        number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
