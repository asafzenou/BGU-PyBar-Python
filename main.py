# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
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

# new workers
tom = Manager("Tom", 25)
noy = Waiter("Noy", 26)
essra = Hostess("Essra", 27)
worker_list = [essra, noy, tom]

shift = Shift(1, [], [], worker_list, {})
print(shift.get_money(tom))