#!/usr/bin/python3
'''
    Docstring for python-inheritance.10-square
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
        Docstring for Square
        '''

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
