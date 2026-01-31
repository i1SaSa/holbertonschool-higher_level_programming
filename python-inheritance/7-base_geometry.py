#!/usr/bin/python3
'''
Docstring for python-inheritance.5-base_geometry
'''


class BaseGeometry():
    '''
        Docstring for BaseGeometry
        '''

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")





bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)
