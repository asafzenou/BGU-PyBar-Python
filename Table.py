import Group
from Group import *
from PyBarException import *


class Table:
    def __init__(self, number, max_capacity=None):
        self.number = number
        self.max_capacity = max_capacity
        self.group = None  # Important
        self.bill = {}

        if (not isinstance(number, int)) or (not isinstance(max_capacity, int)) or (max_capacity < 0) or (number < 0):
            raise InvalidInputException("Invalid input. Number and max_capacity most be int and more then 0.")

    def __str__(self):
        return f"Table number {self.number} has {self.max_capacity} seats."

    def __repr__(self):
        return f"Table number {self.number} has {self.max_capacity} seats."

    def __len__(self):
        return self.max_capacity

    def __lt__(self, other):
        return len(self) < len(other)

    def is_empty(self):
        if self.group is None:  # from =
            return True
        else:
            return False

    def seat(self, group):  # self - Table(2,4), group -  Group([cust1, cust2], {"Macabi": 1, "Negev": 1, "Cake":2})
        if not isinstance(group, Group):  # most be type Group.
            raise InvalidInputException("Invalid input, group most be a type from Group class")
        if not self.is_empty():
            raise OccupiedTableException("Occupied table")
        if len(group) > self.max_capacity:
            raise TooSmallTableException("Too small table")
        self.group = group  # Table(2,4) = Group([cust1, cust2], {"Macabi": 1, "Negev": 1, "Cake":2})

    def order(self, menu):  # self - Table(2,4), menu - {"Macabi": 30, "Negev": 30, "Red Whine": 29, "Salad": 30, "Sandwich": 50}
        if not isinstance(menu, dict):
            raise InvalidInputException("Invalid input, menu must be a dict.")
        if self.group is None:  # from =
            raise EmptyTableException("Empty table")
        table_the_order = self.group.get_order()  # all the order, exp-{"Macabi": 1, "Negev": 1, "Cake":2}
        table_product_order = [product for product in table_the_order.keys()]  # only the product, exp-["Macabi", "Negev", "Cake"]
        menu_products = [product for product in menu.keys()]
        for product_order in table_product_order:
            count_product = 0
            for me_product in menu_products:
                if product_order == me_product:
                    count_product += 1
                    break
            if count_product != 0:
                self.bill[product_order] = menu[product_order] * table_the_order[product_order]
            else:
                print(f"Sorry we don't have {product_order}.")

        print("Your bill is:")
        bill_keys = [key for key in self.bill.keys()]  # {name:price, ..}
        bill_values = [val for val in self.bill.values()]
        for an_item in range(len(bill_values)):
            print(f"{bill_keys[an_item]}..........{bill_values[an_item]}")

    def pay(self):
        if self.group == None:
            raise EmptyTableException("Empty table")
        payment = 0
        val_pay = [a_val for a_val in self.bill.values()]
        for val in val_pay:
            payment += val
        amount_of_dinners = len(self.group)    # Group.__len__()
        split_bill = payment / amount_of_dinners
        collect_tip = 0
        for cus in self.group.get_customers_list():
            get_cus_tip = cus.tip
            collect_tip += (get_cus_tip * split_bill)
        return payment, round(collect_tip, 3)
