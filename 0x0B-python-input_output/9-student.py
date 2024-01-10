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

    def to_json(self) -> dict:
        ''' Retrieves dictionary representation
        '''

        return self.__dict__
