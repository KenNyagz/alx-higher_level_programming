#!/usr/bin/python3


def common_elements(set_1, set_2):
    commons = []
    for elem in set_1:
        for elemn in set_2:
            if elem == elemn:
                commons.append(elem)
    return commons
