#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0
    for i range(x):
        try:
            print(elem[i], end=' ')
            count += 1
        except Indexerror:
             break;
    print()
    return count
