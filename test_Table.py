from unittest import TestCase
from Table import Table
from Customer import Customer
from PyBarException import *
from io import StringIO
from unittest.mock import patch
from Group import Group

class Test(TestCase):
    def test_table(self):
        # check str
        Tablet1 = Table(5,6)
        self.assertEqual("Table number 5 has 6 seats.", str(Tablet1))
        # check repr
        Table3 = Table(2,3)
        self.assertEqual("Table number 2 has 3 seats.", repr(Table3))
        # check len
        self.assertEqual(6, len(Tablet1))
        # check is_empty
        Tablet2 = Table(2,3)
        self.assertEqual(True, Tablet2.is_empty())

        self.assertEqual(True, Tablet2.__lt__(Tablet1))

        self.assertRaises(InvalidInputException, Table, (11.5, 3))
        self.assertRaises(InvalidInputException, Table, (11, 3.5))
        self.assertRaises(InvalidInputException, Table, (-11, 3))
        self.assertRaises(InvalidInputException, Table, (11, -3))


    # Test is empty
    def test_is_empty(self):
        Tablet4 = Table(4, 3)
        self.assertEqual(True, Tablet4.is_empty())

    def test_seat(self):
        customer1 = Customer("yosef", 25, 2)
        customer2 = Customer("Alex", 29, 3)
        group1 = Group([customer1, customer2], {"Macabi": 1, "Negev": 1, "Cake": 2})
        Tablet7 = Table(7, 3)

        # checking isinstance/invalid input Exception
        self.assertRaises(InvalidInputException, Tablet7.seat, customer1)

        # checking occupied table Exception
        Tablet7.seat(group1)  # seating group 1
        customer3 = Customer("mor", 23, 10)
        customer4 = Customer("asaf", 24, 8)
        group2 = Group([customer3, customer4], {"Macabi": 1, "Sushi": 1, "Cake": 2})
        self.assertRaises(OccupiedTableException, Tablet7.seat, group2)

        # checking too small table Exception
        Tablet8 = Table(8,1)
        self.assertRaises(TooSmallTableException, Tablet8.seat, group2)


   # Testing def order
    def test_order_table(self):
        menu = {"Macabi": 30, "Negev": 30, "Red Whine": 29, "Salad": 30, "Sandwich": 50}
        table1 = Table(1,2)
        self.assertRaises(EmptyTableException,table1.order,menu)
        table2 = Table(2,4)
        cust1 = Customer("Avi", 22, 0.1)
        cust2 = Customer("Joseph", 27, 0.2)
        group1 = Group([cust1, cust2], {"Macabi": 1, "Negev": 1, "Cake":2})
        table2.seat(group1)
        expected_out1 = "Sorry we don't have Cake.\nYour bill is:\nMacabi..........30\nNegev..........30\n"
        with patch('sys.stdout', new = StringIO()) as real_out1:
            table2.order(menu)
            self.assertEqual(expected_out1, real_out1.getvalue())
        table3 = Table(3,3)
        table3.seat(group1)  # Table 3 is seating
        expected_out2 = "Sorry we don't have Macabi.\nSorry we don't have Negev.\nSorry we don't have Cake.\nYour " \
                        "bill is:\n"
        with patch('sys.stdout', new=StringIO()) as real_out2:
            table3.order({})
            self.assertEqual(expected_out2, real_out2.getvalue())

    def test_order_expction(self):
        menu2 = ["macbi", "goldstar"]
        cus11 = Customer("Moly", 22, 0.1)
        cus12 = Customer("Ofek", 27, 0.2)
        group4 = Group([cus11, cus12], {"malca": 2, "shelo": 1})
        Table12 = Table(12, 3)
        Table12.seat(group4)
        self.assertRaises(InvalidInputException, Table12.order, menu2)

    def test_pay(self):
        Table9 = Table(9, 3)
        cust9 = Customer("johnatan", 22, 0.1)
        cust10 = Customer("omer", 27, 0.2)
        menu = {"Sushi": 25, "Malaca": 18, "thi food": 29, "Cake": 33, "beef Sandwich": 50}
        group3 = Group([cust9, cust10], {"Sushi": 1, "Malaca": 2, "Cake": 1, "taco bell": 2})
        Table9.seat(group3)
        Table9.order(menu)
        self.assertEqual((94, 14.1),Table9.pay())
        Table10 = Table(10, 3)
        self.assertRaises(EmptyTableException, Table10.pay)


