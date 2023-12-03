#!/usr/bin/python3
"""
   Ancestor class Base
"""
import json
import csv


class Base:
    """
       Ancestor Base class
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
        # update(self, *args, **kwargs)
        inst = cls(**dict(dictionary))
        return inst

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open("{}.json".format(cls.__name__, "r")) as fle:
                json_string = fle.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        filename = f"{cls._name_}.csv"
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls._name_ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height,
                                     obj.x, obj.y])
                elif cls._name_ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        filename = f"{cls._name_}.csv"
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls._name_ == "Rectangle":
                        dictionary = {'id': int(row[0]), 'width': int(row[1]),
                                      'height': int(row[2]), 'x': int(row[3]),
                                      'y': int(row[4])}
                    elif cls._name_ == "Square":
                        dictionary = {'id': int(row[0]), 'size': int(row[1]),
                                      'x': int(row[2]), 'y': int(row[3])}
                    instances.append(cls.create(**dictionary))
                return instances
        except FileNotFoundError:
            return []
