#!/usr/bin/python3
"""
    function that prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    newline_flag = True
    for char in text:
        if newline_flag and char.isspace():
            continue

        print(char, end='')
        if char in ['.', '?', ':']:
            print("\n")
            newline_flag = True
        else:
            newline_flag = False
