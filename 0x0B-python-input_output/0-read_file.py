#!/usr/bin/python3
"""Defines a function that reads text file."""


def read_file(filename=""):
    """the contents of a UTF8 text file are printed to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
