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
        if not isinstance(position, tuple) and all(n > 0 for n in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
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
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        if self.__position[1] > 0:
            for y in range(self.__position[1]):
                print()
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size - 1):
                print("#", end="")
            print("#")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) & all(n > 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")


my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
