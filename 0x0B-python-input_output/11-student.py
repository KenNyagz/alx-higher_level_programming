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


"""
Class Student with two names and age attrs +
method that gets dict repr of obj
"""


class Student:
    """
       defines a student by and age
    """
    def __init__(self, first_name, last_name, age):
        """Initialisaation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return class_to_json(self)
        elif isinstance(attrs, list) and all(isinstance(attr, str)
                                             for attr in attrs):
            return {att: class_to_json(getattr(self, att)) for att in attrs}

        else:
            raise TypeError("attrs must be a list of strings or None")

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
