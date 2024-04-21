from unittest import TestCase
import Group
from Group import *
from PyBarException import *
from Customer import Customer


class TestGroup(TestCase):
    def test__init__group(self):
        # checking if len is less than two:
        order = {"Goldstar" : 3 , "Red Wine" : 1, "French fries" :1}
        order_group= ["yakov"]
        self.assertRaises(InvalidInputException, Group, order_group, order)

        # checking if the order isn't dict
        order4 = [{"Goldstar" : 3 }, {"Red Wine" : 1}, {"French fries" :1}]
        order_group4 = ["yakov", "Shlomi"]
        self.assertRaises(InvalidInputException, Group, order_group4, order4)

        # checking if the key isn't str
        order2 = {1 : 3 , "Red Wine" : 1, "French fries" :1}
        order_group2 = ["yakov", "Shlomi"]
        self.assertRaises(InvalidInputException, Group, order_group2, order2)

        # checking if the val isn't int
        order3 = {"Goldstar" : 3 , "Red Wine" : 1, "French fries" :"Goldstar"}
        order_group3 = ["yakov", "Shlomi"]
        self.assertRaises(InvalidInputException, Group, order_group3, order3)

    def test_get_order_customers_list(self):
        # checking string func
        order_group5 = ["mor", "asaf", "skipi"]
        order5 = {"Suhsi" : 3 , "Humos" : 1, "salami" :1}
        group5 = Group(order_group5, order5)
        self.assertEqual({"Suhsi" : 3 , "Humos" : 1, "salami" :1}, group5.get_order())
        self.assertEqual(["mor", "asaf", "skipi"], group5.get_customers_list())

    def test_str_repr(self):
        order_group6 = ["elon", "asaf", "itay"]
        order6 = {"lafa": 3, "Humos": 1, "salami_with_besily": 1}
        group6 = Group(order_group6, order6)
        self.assertEqual(f"The group has {len(order_group6)} members, their order: {order6}", str(group6))
        self.assertEqual(f"The group has {len(order_group6)} members, their order: {order6}", repr(group6))

    def test_len_lt(self):
        order_group7 = ["victor", "tali", "gal", "neta", "asaf"]
        order7 = {"lafa": 3, "Humos": 1, "hotdog": 1, "swarma": 2, "falafel": 2}
        group7 = Group(order_group7, order7)
        group8 = ["asi", "mosh", "gdosh"]
        self.assertEqual(5, len(group7))
        self.assertEqual(False, group7.__lt__(group8))

    def test_get_cus_string(self):
        order9 = {"lafa": 3, "Humos": 1, "hotdog": 1, "swarma": 2, "corn": 2}
        cus1 = Customer("dani", 20, 10)
        cus2 = Customer("kobi", 20, 10)
        cus3 = Customer("yossi", 20, 10)
        cus4 = Customer("ali", 20, 10)
        order_group9 = [cus1, cus2, cus3, cus4]
        group9 = Group(order_group9, order9)
        print(group9.get_customers_string())