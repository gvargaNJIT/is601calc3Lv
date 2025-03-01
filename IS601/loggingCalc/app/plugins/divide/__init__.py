from decimal import Decimal
import logging
from app.commands import Command, NumberInput
from calculator import Calculator

class DivideCommand(Command):
    def __init__(self):
        self.number_input = NumberInput()

    def execute(self):
        a = self.number_input.list_number(input("Number 1: "))
        if not isinstance(a, Decimal):
            return 0
        else:
            logging.info(f"{a} was entered as Number 1 for division operation")
        b = self.number_input.list_number(input("Number 2: "))
        if b == 0 or not isinstance(b, Decimal):
            logging.error(f"The result is undefined. Exiting operation")
            print(f"The result is undefined")
            return 0
        else:
            logging.info(f"{a} was entered as Number 2 for division operation")
            result = Calculator.divide(a, b)
            logging.info(f"The result is {result}")
            print(f"The result is {result}")