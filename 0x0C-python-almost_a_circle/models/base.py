#!/usr/bin/python3

""" Base class """
import json


class Base:
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert dictionaries to JSON """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__+'.json'
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write('[]')
            else:
                dict_list = []
                for obj in list_objs:
                    dict_list.append(obj.to_dictionary())
                f.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """ Returns a list of JSON string representation """
        if json_string is None or json_string == '[]':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Creates a new instance from a dictionary """
        if dictionary != {}:
            # check if class is rectangle
            if cls.__name__ == 'Rectangle':
                # Create dummy rectangle instance
                new_instance = cls(4, 6)
            else:
                # Create dummy square instance
                new_instance = cls(4)
            new_instance.update(**dictionary)

            return new_instance
