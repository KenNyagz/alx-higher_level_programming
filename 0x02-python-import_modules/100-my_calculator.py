#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    if sys.argv[2] == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif sys.argv[2] == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif op == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif sys.argv[2] == "/":
        if b == 0:
            print("Error: Division by zero")
            sys.exit(1)
        else:
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
