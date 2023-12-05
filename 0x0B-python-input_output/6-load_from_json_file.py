#!/usr/bin/python3
"""A function that reads a JSON file."""
import json


def load_from_json_file(filename):
    """A Python object is created from a JSON file."""
    with open(filename) as f:
        return json.load(f)
