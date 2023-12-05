#!/usr/bin/python3
"""A Python class-to-JSON function."""


def class_to_json(obj):
    """the dictionary represntation of a simple data structure is returned."""
    return obj.__dict__
