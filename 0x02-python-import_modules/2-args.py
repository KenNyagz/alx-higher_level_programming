#!/usr/bin/python3
def print_arg(argv):
    n = len(argv) - 1
    if n == 0:
        print("{:d} argument.".format(n))
        return
