#!/usr/bin/python3
"""
 function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    def read_file(filename=""):
    """
    with open(filename, 'r', encoding='utf-8') as data:
        for line in data:
            print(line, end='')
