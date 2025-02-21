from app.commands import Commandlist
from app.commands.exit import ExitCommand
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

class App:
    def __init__(self):
        self.command_list = Commandlist()

    def start(self):
        self.command_list.register_command("add", AddCommand())
        self.command_list.register_command("subtract", SubtractCommand())
        self.command_list.register_command("multiply", MultiplyCommand())
        self.command_list.register_command("divide", DivideCommand())
        self.command_list.register_command("exit", ExitCommand())

        print("Welcome to the Calculator! Enter an operation or type 'exit' to leave the program")
        while True:
            self.command_list.execute_command(input(">>> ").strip())