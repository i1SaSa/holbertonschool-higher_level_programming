#!/usr/bin/python3
'''
Docstring for python-classes.3-square
'''


class Square:
    '''
    Docstring for Square
    '''

    def __init__(self, size=0):
        '''
        Docstring for __init__

        :param self: Description
        :param size: Description
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''
                Docstring for area

                :param self: Description
                '''
        return self.__size * self.__size
