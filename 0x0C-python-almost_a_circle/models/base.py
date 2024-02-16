#!/usr/bin/python3
''' First class Base '''
import json
import csv
import turtle as t


class Base:
    ''' first class Base '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Instantiate class (class constructor) '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Convert dictionaries to json '''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' Save json to file '''
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
        ''' Load from json string '''
        if json_string is None or json_string == '[]':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' Creates new instance '''
        if dictionary != {}:
            if cls.__name__ == 'Rectangle':
                new_instance = cls(2, 3)
            else:
                new_instance = cls(2)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        ''' Load from file '''
        filename = cls.__name__+'.json'
        try:
            with open(filename, 'r') as f:
                dict_list = Base.from_json_string(f.read())
                return [cls.create(**item) for item in dict_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' save file to csv '''
        filename = cls.__name__+'.csv'
        with open(filename, 'w') as f:
            if list_objs is None or list_objs == []:
                f.write('[]')
            else:
                if cls.__name__ == 'Rectangle':
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                [writer.writerow(obj.to_dictionary()) for obj in list_objs]

    @classmethod
    def load_from_csv(cls):
        ''' Load from csv file '''
        filename = cls.__name__+'.csv'
        try:
            with open(filename, 'r') as f:
                if cls.__name__ == 'Rectangle':
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                dict_list = csv.DictReader(file, fieldnames=fieldnames)
                dict_list = [dict([key, int(value)] for key, value in dic.items())
                             for dic in dict_list]
                return [cls.create(**dic) for dic in dict_list]

        except IOError:
            return []

    @staticmethod
    def draw(x, y, width, height, is_sqr=False):
        ''' Draws the shapes '''
        turt = t.Turtle()
        turt.screen.bgcolor('black')
        turt.pensize(4)
        turt.shape('turtle')
        turt.penup()
        turt.goto(x, y)
        t.pendown()

        if is_sqr:
            turt.color('yellow')
            for i in range(4):
                turt.forward(width)
                turt.left(90)
        else:
            turt.color('blue')
            for j in range(2):
                turt.forward(width)
                turt.left(90)
                turt.forward(height)
                turt.left(90)
