#!/usr/bin/python3
def complex_delete(a_dictionary, value):
        temp = a_dictionary.copy()
    for j, x in temp.items():
        if value == x:
            a_dictionary.pop(j)
    return a_dictionary
