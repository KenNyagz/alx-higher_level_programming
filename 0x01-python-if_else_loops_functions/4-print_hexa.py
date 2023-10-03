#!/usr/bin/python3

for i in range(0, 99):
    print("0x", end='')
    print("{:.0f}".format(i / 16), end='')
    
    match i % 16:
        case 10:
            print("a")
        case 11:
            print("b")
        case 12:
            print("c")
        case 13:
            print("d")
        case 14:
            print("e")
        case 15:
            print("f")
        case _: 
            print("{:.0f}".format(i % 16))
