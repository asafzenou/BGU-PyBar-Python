from unittest import TestCase
from PyBarException import *
from Customer import Customer
from unittest.mock import patch
from io import StringIO
from Group import Group
from Manager import Manager
from Hostess import Hostess
from Waiter import Waiter
from Shift import Shift
from Table import Table





def test_shift_day(self):
    # new workers
    tom = Manager("Tom", 25)
    noy = Waiter("Noy", 26)
    essra = Hostess("Essra", 27)
    worker_list = [essra, noy, tom]

    # new customers:
    neta = Customer("Neta", 20, 0.12)
    alon = Customer("Alon", 54, 0.2)
    tamar = Customer("Tamar", 30, 0.15)
    yuval = Customer("Yuval", 22, 0.13)
    avi = Customer("Avi", 31, 0.08)
    asaf = Customer("Asaf", 25, 0.2)
    shir = Customer("Shir", 26, 0.11)
    tal = Customer("Tal", 25, 0.14)
    adi = Customer("Adi", 24, 0.15)

    # new orders
    order1 = {"Goldstar": 2, "Pina colada": 1, "French fries": 1, "Coke": 1}
    order2 = {"White wine": 2, "Salad": 1}
    order3 = {"Goldstar": 1, "Mojito": 2, "Pizza": 1}

    # new menu
    menu = {"Goldstar": 35, "Macabi": 32, "Pina colada": 50, "Red wine": 29, "White wine": 30, "pizza": 59}

    # new groups
    group1 = Group([neta, alon, tamar, yuval], order1)
    group2 = Group([avi, asaf, shir], order2)
    group3 = Group([tal, adi], order3)
    group_list = [group3, group2, group1]
    # new tables

    table1 = Table(1, 1)
    table2 = Table(2, 2)
    table3 = Table(3, 4)
    table4 = Table(4, 2)
    tables_list = [table1, table2, table3, table4]

    # creating shift:
    shift1 = Shift(1, tables_list, group_list, worker_list, menu)
    expected_out = "Neta, Alon, Tamar and Yuval you can seat on table 3 please." \
                   "\nSorry Avi, Asaf and Shir, we don't have place for 3 people." \
                   "\nTal and Adi you can seat on table 2 please." \
                   "\n________________________________________" \
                   "\nHey Tal and Adi! My name is Noy and I'm your waiter." \
                   "\nSorry we don't have Mojito." \
                   "\nSorry we don't have Pizza.\nYour bill is:\nGoldstar..........35" \
                   "\n\nHey Neta, Alon, Tamar and Yuval! My name is Noy and I'm your waiter." \
                   "\nSorry we don't have French fries." \
                   "\nSorry we don't have Coke.\nYour bill is:" \
                   "\nGoldstar..........70\nPina colada..........50" \
                   "\n\n________________________________________" \
                   "\nThank you Tal and Adi! You paid 40.075 shekels. See you next time!" \
                   "\nThank you Neta, Alon, Tamar and Yuval! You paid 138.0 shekels. See you next time!" \
                   "\nThis is the end of the shift:" \
                   "\nShift number: 1." \
                   "\nTotal money: 155, total tip: 23.075" \
                   "\n________________________________________\n"
    with patch('sys.stdout', new=StringIO()) as real_out:
        shift1.shift_day()

test_shift_day()