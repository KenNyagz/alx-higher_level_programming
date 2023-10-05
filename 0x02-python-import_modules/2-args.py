#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    print(len(sys.argv) - 1, "argumenets:")
    for argument in sys.argv:
        print(argument)
