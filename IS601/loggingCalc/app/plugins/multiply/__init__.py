from decimal import Decimal
import logging
from app.commands import Command, NumberInput
from calculator import Calculator

class MultiplyCommand(Command):
    def __init__(self):
        self.number_input = NumberInput()

    def execute(self):
        a = self.number_input.list_number(input("Number 1: "))
        if not isinstance(a, Decimal):
            return 0
        else:
           logging.info(f"{a} was entered as Number 1 for multipication operation") 
        b = self.number_input.list_number(input("Number 2: "))
        if not isinstance(b, Decimal):
            return 0
        else:
            logging.info(f"{b} was entered as Number 2 for multipication operation")
        result = Calculator.multiply(a, b)
        logging.info(f"The result is {result}")
        print(f"The result is {result}")