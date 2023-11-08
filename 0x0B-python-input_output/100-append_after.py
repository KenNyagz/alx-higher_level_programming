#!/usr/bin/python3
"""
function that inserts a line of text to a file,
 after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file
    
    """
    with open(filename, 'r') as fle:
        lines = fle.readlines()

    with open(filename, 'w') as fle:
        for line in lines:
            fle.write(line)
            if search_string in line:
                fle.write(new_string + '\n')
