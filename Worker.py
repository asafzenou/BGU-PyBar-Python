from PyBarException import *
from Person import Person
from abc import ABC, abstractmethod


class Worker(Person, ABC):

    @abstractmethod
    def __str__(self):
        name = self.get_name()
        age = self.get_age()
        return f"Name:{name},Age:{age},Job:"

    @abstractmethod
    def work(self, shift):
        pass
