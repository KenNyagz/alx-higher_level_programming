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

    with open(filename, 'r+', encoding='utf-8') as fle:
        st = ""
        for line in fle:
            st += line
            if search_string in line:
                st += new_string

        fle.seek(0)
        fle.write(st)
