#!/usr/bin/python3
'''
    Docstring for python-more_classes.1-rectangle
    '''


class Rectangle:
    '''
        Docstring for Rectangle
        '''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2*(self.__width + self.__height)

    def print(self):
        if self.__height == 0 or self.__width == 0:
            return " "
        for x in range(self.height):
            print("#", end="")
            for i in range(self.width):
                print("#", end="")
            print()
        return ""

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return " "
        for x in range(self.height):
            print("#", end="")
            for i in range(self.width):
                print("#", end="")
            print()
        return ""
