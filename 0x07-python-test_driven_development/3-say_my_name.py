#!/usr/bin/python3
"""
   Module contains a function that takes two strings and
   prints them out. Does not return anything
"""


def say_my_name(first_name, last_name=""):
    """
       first_name is meant to be a string with user's first name
       last_name is string with user's last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
