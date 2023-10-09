#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    boollst = []
    i = 0
    while i < len(my_list):
        if my_list[i] % 2 == 0:
            boollst.append(True)
        else:
            boollst.append(False)
        i += 1
    return boollst
