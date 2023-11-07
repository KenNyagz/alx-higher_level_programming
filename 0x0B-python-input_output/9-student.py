#!/usr/bin/python3
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

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return {
                "fisrt_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
               }
