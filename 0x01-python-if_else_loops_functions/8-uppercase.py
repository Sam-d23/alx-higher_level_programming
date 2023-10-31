#!/usr/bin/python3
def upper(char):
    if ord(char) >= 97 and ord(char) <= 122:
        return (ord(char) - 32)
    else:
        return ord(char)


def uppercase(str):
    str_new = ""
    for char in str:
        str_new += "%c" % upper(char)
    print("{:s}".format(str_new))
