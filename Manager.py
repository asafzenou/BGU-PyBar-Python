from Worker import Worker
from Group import Group
from Table import Table
from PyBarException import *


class Manager(Worker):

    def __str__(self):
        name = self.get_name()
        age = self.get_age()
        return f"Name:{name},Age:{age},Job:Manager"

    def work(self, shift):
        table_list_from_shift_manager = shift.table_list
        for any_table in table_list_from_shift_manager:
            if any_table.is_empty():
                continue
            go_to_table = any_table.pay()
            thank_you_group = any_table.group.get_customers_string()
            thank_you = f"Thank you {thank_you_group}! You paid {sum(go_to_table)} shekels. See you next time!"
            print(thank_you)
            shift.add_money(go_to_table[0])
            shift.add_tip(go_to_table[1])
        print(f"This is the end of the shift:\nShift number: {shift.shift_number}.")
        total_money = shift.get_money(self)
        total_tip = shift.get_tip(self)
        print(f"Total money: {total_money}, total tip: {total_tip}")




