#!/usr/bin/python3
"""
function that inserts a line of text to a file,
 after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file

    """
    tfilename = filename + ".tmp"

    with open(filename, 'r+') as fle:
        lines = fle.readlines()
        newlines = []

        for line in lines:
            if search_string in line:
                newlines.append(line)
                newlines.append(new_string)
            else:
                newlines.append(line)

        fle.seek(0)
        fle.truncate()
        fle.writelines(newlines)
