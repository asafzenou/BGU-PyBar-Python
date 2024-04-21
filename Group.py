import copy
from PyBarException import *


class Group:
    def __init__(self, customers_list, order_dict):
        self.customers_list = customers_list
        self.__order_dict = order_dict  # Private

        if not isinstance(customers_list, list) or len(customers_list) < 2:
            raise InvalidInputException("Invalid input, list type needed and at least two persons")
        if not isinstance(order_dict, dict):
            raise InvalidInputException("Invalid input, dict type needed")

        for key in order_dict.keys():
            if not isinstance(key, str):
                raise InvalidInputException("Invalid input, str type needed for key in order_dict")
        for val in order_dict.values():
            if not isinstance(val, int):
                raise InvalidInputException("Invalid input, int type needed for value in order_dict")

    def get_order(self):
        return copy.deepcopy(self.__order_dict)

    def get_customers_list(self):
        return copy.deepcopy(self.customers_list)

    def __str__(self):
        return f"The group has {len(self.customers_list)} members, their order: {self.__order_dict}"

    def __repr__(self):
        return f"The group has {len(self.customers_list)} members, their order: {self.__order_dict}"

    def __len__(self):
        return len(self.customers_list)

    def __lt__(self, other):
        return len(self) < len(other)

    def get_customers_string(self):
        name_list = [Customer.get_name() for Customer in self.customers_list]
        return_string = ", ".join(name_list[:-1]) + " and " + name_list[-1]
        return return_string