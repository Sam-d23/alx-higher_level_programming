#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        error_message = "Exception: Cannot print non-integer value"
        print(error_message, file=sys.stderr)
        return False
