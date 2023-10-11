#!/usr/bin/pyton3

from functools import reduce
def uniq_add(my_list=[]):
    return reduce((lambda x, y : x + y), set(element for element in my_list))
