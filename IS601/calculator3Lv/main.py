'''Main File of Calculator for Users'''

import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation

def calculate_and_print(a, b, operation_name):
    operation_mappings = {
        'add' : Calculator.add,
        'subtract' : Calculator.subtract,
        'multiply' : Calculator.multiply,
        'divide': Calculator.divide
    }
    try:
        a_decimal, b_decimal = map(Decimal, [a,b])
        result = operation_mappings.get(operation_name)
        if result:
            print(f"The result of {a} {operation_name} {b} is equal to {result(a_decimal, b_decimal)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"{a} or {b} is invalid. Try again")
    except ValueError as e:
        if str(e) == "Undefined":
            print(f"Dividing by zero is undefined. Try again")
        else:
            print(f"{e} is an unexpected error. Try again")

def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator-> python main.py <number1> <number2> <operation>")
        sys.exit(1)
    
    _, a, b, operation =sys.argv
    calculate_and_print(a, b, operation)


if __name__ == '__main__':
    main()