#!/usr/bin/python3
'''
Docstring for python-classes.3-square
'''


class Square:
    '''
    Docstring for Square
    '''

    def __init__(self, size=0, position=(0, 0)):
        '''
                Docstring for __init__

                :param self: Description
                :param size: Description
                :param position: Description
                '''
        self.__size = size
        self.__position = position

    def area(self):
        '''
                Docstring for area

                :param self: Description
                '''
        return self.__size * self.__size

    @property
    def size(self):
        '''
                Docstring for size

                :param self: Description
                '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
                Docstring for size

                :param self: Description
                :param value: Description
                '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''
                Docstring for position

                :param self: Description
                '''
        return self.__position

    @position.setter
    def position(self, value):
        '''
                Docstring for position

                :param self: Description
                :param value: Description
                '''
        if not isinstance(value, tuple) and all(n < 0 for n in value) and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        '''
                Docstring for my_print

                :param self: Description
                '''
        if self.__size == 0:
            print()
            return
        if self.__position[1] > 0:
            for y in range(self.__position[1]):
                print()
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size - 1):
                print("#", end="")
            print("#")
