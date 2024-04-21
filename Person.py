import copy
from PyBarException import *
from abc import ABC, abstractmethod



class Person(ABC):
    #@abstractmethod
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

        if not isinstance(name, str) or len(name) == 0:
            raise InvalidInputException("Invalid Input, need type str")
        if not isinstance(age, int) or age < 18:
            raise InvalidInputException("Invalid Input, need type int")

    def get_name(self):
        name = self.__name
        return name

    def get_age(self):
        age = self.__age
        return age

    @abstractmethod
    def __str__(self):
        name = self.get_name()
        age = self.get_age()
        return f"Name:{name},Age:{age}"





