#!/usr/bin/env python3
'''
Docstring for python-abc.task_01_duck_typing
'''
from abc import *
from math import *


class Shape(ABC):
    '''
        Docstring for Shape
        '''
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    '''
        Docstring for Circle
        '''

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return pi*(self.__radius * self.__radius)

    def perimeter(self):
        return 2 * pi * self.__radius


class Rectangle(Shape):
    '''
        Docstring for Rectangle
        '''

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__height + self.__width)


def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
