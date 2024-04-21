from Group import *
from Manager import *
from Worker import *
from Group import Group #NEWADD
from Waiter import Waiter
from Hostess import Hostess
from PyBarException import *


class Shift:
    def __init__(self, shift_number, table_list, group_list, workers_list, menu):
        self.shift_number = shift_number
        self.table_list = table_list
        self.group_list = group_list
        self.workers_list = workers_list
        self.menu = menu
        self.__total_money = 0
        self.__total_tip = 0

        if shift_number < 0:
            raise InvalidInputException("shift number positive")
        if (not isinstance(workers_list, list)) or len(workers_list) != 3:
            raise InvalidInputException("Only 3 workers in a shift")
        if (not isinstance(workers_list[0], Hostess)) or (not isinstance(workers_list[1], Waiter) or (not isinstance(workers_list[2], Manager))):
            raise InvalidInputException("Need to be in a order of Hostess, Waiter and Manager")

    def __str__(self):
        return f"Shift number: {self.shift_number}."

    def __repr__(self):
        return f"Shift number: {self.shift_number}."

    def add_money(self, money):
        if money < 0:
            raise InvalidInputException("Invalid input, money must be positive")
        else:
            self.__total_money += money

    def add_tip(self, tip):
        if tip < 0:
            raise InvalidInputException("Invalid input, money must be positive")
        else:
            self.__total_tip += tip

    def get_money(self, manager):
        if not isinstance(manager, Manager):
            raise AccessDeniedException("Only a manager can access the money")
        else:
            return self.__total_money

    def get_tip(self, manager):
        if not isinstance(manager, Manager):
            raise AccessDeniedException("Only a manager can access the tip")
        return self.__total_tip

    def get_table_list(self):
        return self.table_list()

    def get_shift_number(self):
        return self.shift_number()

    def shift_day(self):
        for worker in self.workers_list:
            worker.work(self)
            print("__________"*4)


