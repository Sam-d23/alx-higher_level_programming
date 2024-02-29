#!/usr/bin/python3
"""
   picks a peak from a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): The list of unsorted integers.

    Returns:
        int: The peak element in the list.

    Raises:
        ValueError: If the list is empty.
    """
    if not list_of_integers:
        raise ValueError("List is empty")

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
