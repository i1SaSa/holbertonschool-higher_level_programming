#!/usr/bin/env python3
'''
Docstring for python-abc.task_00_abc
'''
from abc import ABC, abstractmethod


class Animal(ABC):
    '''
    Docstring for Animal
    '''
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"
