#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    if not my_list:

        return 0
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end=' ')
            count += 1
        except Indexerror:
            break
    print()
    return count
