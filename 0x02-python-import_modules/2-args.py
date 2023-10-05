#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    if len(sys.argv) - 1 == 0:
         print("0 arguments.")
    elif len(sys.argv) - 1 == 1:
         print("1 argument")
    else:
         print(len(sys.argv) - 1, "argumenets:")

    for idx in range(1, len(sys.argv)):
         print("{}: {}".format(idx, sys.argv[idx]))
