from Worker import Worker
from Table import Table
from PyBarException import *

class Hostess(Worker):
    def __str__(self):
        name = self.get_name()
        age = self.get_age()
        return f"Name:{name},Age:{age},Job:Hostess"

    def work(self, shift):
        group_list_with_order = shift.group_list
        groups = sorted(group_list_with_order, reverse=True)  # groups from the big to the small
        tables = sorted(shift.table_list, reverse=True)
        dont_check_more_then_one = 0
        for group in groups:
            check_if_seated = 0
            for table in tables[dont_check_more_then_one:]:
                if len(group) <= len(table):
                    dont_check_more_then_one += 1
                    check_if_seated += 1
                    table_names = group.get_customers_string()
                    print(f"{table_names} you can seat on table {table.number} please.")
                    table.seat(group)
                    break
            if check_if_seated == 0:
                table_names = group.get_customers_string()
                print(f"Sorry {table_names}, we don't have place for {len(group)} people.")

