'''Main Test'''

import pytest
from main import calculate_and_print

@pytest.mark.parametrize("a_value, b_value, operation_string, expected_string", [
    ("7", "4", 'add', "The result of 7 add 4 is equal to 11"),
    ("9", "3", 'subtract', "The result of 9 subtract 3 is equal to 6"),
    ("5", "3", 'multiply', "The result of 5 multiply 3 is equal to 15"),
    ("16", "4", 'divide', "The result of 16 divide 4 is equal to 4"),
    ("1", "0", 'divide', "Dividing by zero is undefined. Try again"),
    ("1", "9", 'david', "Unknown operation: david"),
    ("j", "0", 'add', "j or 0 is invalid. Try again"),
    ("4", "'", 'subtract', "4 or ' is invalid. Try again"),
    ("g", "-", 'divide', "g or - is invalid. Try again")
])

def test_inputs(a_value, b_value, operation_string, expected_string, capsys):
    '''Testing all calculations'''
    calculate_and_print(a_value, b_value, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string
