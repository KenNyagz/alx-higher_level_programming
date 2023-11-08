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

    with open(filename, 'r') as filein, open(tfilename, 'w') as fileout:
        for line in filein:
            fileout.write(line)
            if search_string in line:
                fileout.write(new_string + '\n')
