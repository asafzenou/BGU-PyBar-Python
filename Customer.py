from PyBarException import *
from Person import *


class Customer(Person):
    def __init__(self, name, age, tip):
        super().__init__(name, age)
        self.tip = tip  # Round the tip

        if not isinstance(tip, float) and not isinstance(tip, int) or tip < 0 :
            raise InvalidInputException("Invalid Input, int/float type needed")

    def __str__(self):
        name = self.get_name()
        age = self.get_age()
        tip = int(self.tip * 100)
        return f"Name:{name},Age:{age},Tip:{tip}%"

    def cus_tip(self):
        return self.tip


