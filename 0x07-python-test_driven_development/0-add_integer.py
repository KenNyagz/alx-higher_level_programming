#!/usr/bin/python3


def add_integer(a, b=98):
    """
    add_integer(a, b=98):
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        if not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")

        a = int(a)
        b = int(b)
        return a + b

    Adds two integers or wholesome floats

    >>>add_integer(2, 3)
    5

    >>>add(2)
    100

    >>>add_integer(2, 3.0)
    5

    >>>add_integer(2, "d")
    Traceback (most recent call last):
      File "./0-add_integer.py", line 30, in <module>
        add_integer(2, "b")
      File "./0-add_integer.py", line 24, in add_integer
        raise TypeError("b must be an integer")
    TypeError: b must be an integer

    >>>add_integer("a", 2)
    Traceback (most recent call last):
      File "./0-add_integer.py", line 35, in <module>
        add_integer(2, "b")
      File "./0-add_integer.py", line 43, in add_integer
        raise TypeError("a must be an integer")
    TypeError: a must be an integer

    >>>add_integer("a", "b")
    Traceback (most recent call last):
      File "./0-add_integer.py", line 30, in <module>
        add_integer(2, "b")
      File "./0-add_integer.py", line 24, in add_integer
        raise TypeError("b must be an integer")
    TypeError: b must be an integer

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
