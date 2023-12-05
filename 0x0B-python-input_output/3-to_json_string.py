#!/usr/bin/python3
"""string-to-JSON function."""
import json


def to_json_string(my_obj):
    """JSON representation of a string object is returned."""
    return json.dumps(my_obj)
