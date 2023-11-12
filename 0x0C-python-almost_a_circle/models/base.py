#!/usr/bin/python3
"""Ancestor class Base
"""
import json


class Base:
    """Ancestor Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if (list_dictionaries is None) or len(list_dictionaries) == 0:
            return str([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        # list_dicts = [obj.to_dictionary() for obj in list_objs]
        # stringjson = cls.to_json_string(list_dicts)
        obls = []
        for obj in list_objs:
            ob = obj.to_dictionary()
            obls.append(ob)
        stringjson = cls.to_json_string(obls)

        with open("{}.json".format(cls.__name__), "w") as fle:
            fle.write(stringjson)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        inst = cls(**dict(dictionary))
        return inst
