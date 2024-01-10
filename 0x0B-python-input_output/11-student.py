#!/usr/bin/python3
''' Class that defines a student '''


class Student:
    ''' Class that defines a student
    '''

    def __init__(self, first_name, last_name, age) -> None:
        ''' Initialization

        Args:
            first_name (str): first name
            last_name (str): last name
            age: age
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None) -> dict:
        ''' Retrieves dictionary representation
        '''
        if (type(attrs) == list and
            all(type(item) == str for item in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

        return self.__dict__

    def reload_from_json(self, json):
        ''' Replaces all attributes of a student object
        '''

        for key, value in json.items():
            setattr(self, key, value)
