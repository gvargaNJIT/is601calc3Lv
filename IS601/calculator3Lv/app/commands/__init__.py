from abc import ABC, abstractmethod
from decimal import Decimal

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Commandlist:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"{command_name} is not a valid operation")

class NumberInput:
    def __init__(self):
        self.numbers = {}
        
    def list_number(self, a: Decimal):
        try:
            return Decimal(a)
        except Exception as e:
            print(f"{a} is not a valid number")
            return 1

            

