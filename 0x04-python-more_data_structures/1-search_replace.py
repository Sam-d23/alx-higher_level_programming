#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if search == y else y for y in my_list]
