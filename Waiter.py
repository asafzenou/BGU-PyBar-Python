from PyBarException import *
from Worker import Worker
from Group import Group
from Table import Table


class Waiter(Worker):

    def __str__(self):
        name = self.get_name()
        age = self.get_age()
        return f"Name:{name},Age:{age},Job:Waiter"

    def work(self, shift):
        table_list_from_shift_waiter = shift.table_list
        for any_table in table_list_from_shift_waiter:
            if any_table.is_empty():
                continue
            hey_from_waiter = f"Hey {any_table.group.get_customers_string()}! My name is {self.get_name()} and I'm your waiter."
            print(hey_from_waiter)
            any_table.order(shift.menu)
            print("")


