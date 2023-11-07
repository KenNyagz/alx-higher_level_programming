#!/usr/bin/python3
"""
function that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for JSON serialization of obj
"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    for JSON serialization of object
    """
    if isinstance(obj, (list, dict, int, str, bool)):
        return obj
    elif isinstance(obj, (tuple, set)):
        return list(obj)
    elif hasattr(obj, '__dict__'):
        return {key: class_to_json(val) for key, val in obj.__dict__.items()}
    else:
        raise TypeError("Object of type {} is not JSON serializable".
                        format(type(obj).__name__))
