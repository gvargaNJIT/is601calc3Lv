#Operation Definitions/Classes

class Calculator:
    @staticmethod
    def add(a,b):
        calculation = a + b
        return calculation
    @staticmethod
    def subtract(a,b):
        calculation = a - b
        return calculation
    @staticmethod
    def multiply(a,b):
        calculation = a * b
        return calculation
    @staticmethod
    def divide(a,b):
        if b == 0:
            return print("Undefined")
        else:
            calculation = a / b
            return calculation
