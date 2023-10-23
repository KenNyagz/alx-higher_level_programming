#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    i = 0
    for element in my_list_1:
        for elem in my_list_2:
            try:
                result = element / elem
            except (TypeError):
                print("wrong type")
            except (IndexError):
                print("out of range")
            except (ZeroDivisionError):
                print("division by 0")
