#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        my_listcp = my_list[:]
        my_listcp[idx] = element
        return my_listcp
