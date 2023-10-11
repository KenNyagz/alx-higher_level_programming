#!/usr/bin/python3


def uniq_add(my_list=[]):
    uniques = set(element for element in my_list)
    return sum(uniques)
