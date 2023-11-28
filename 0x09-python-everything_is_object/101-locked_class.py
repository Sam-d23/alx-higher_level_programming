#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevents instantiation of new LockedClass attributes
    which are not called 'first_name'.
    """
    __slots__ = ["first_name"]
