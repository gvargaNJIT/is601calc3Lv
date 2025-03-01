import logging
import sys
from app.commands import Command

class ExitCommand(Command):
    def execute(self):
        logging.info("~Exiting Calculator~")
        print(f"~Exiting Calculator~")
        sys.exit()