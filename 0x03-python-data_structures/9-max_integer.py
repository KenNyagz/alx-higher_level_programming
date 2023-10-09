#!/usr/bin/python3


def max_integer(my_list=[]):
    if not my_list:
        return None
    maxno = my_list[0]
    for elem in my_list:
        if elem > maxno:
            maxno = elem

    return maxno
