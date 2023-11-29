#!/usr/bin/python3
"""
Code for "5-test_indentation" module.
it prints one function, text_indentation(text).
"""


def text_indentation(text):
    """a text is split into lines along "?", ":", "." followed by 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for b in text:
        if flag == 0:
            if b == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if b == '?' or b == '.' or b == ':':
                print(b)
                print()
                flag = 0
            else:
                print(b, end="")
