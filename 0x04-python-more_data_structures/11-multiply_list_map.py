#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    add = lambda x: x * number
    newlist = list(map(add, my_list))
    return newlist
