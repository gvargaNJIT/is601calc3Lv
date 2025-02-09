'''Calculation Definition Test'''

import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a_, b_, operation, expected", [
    (4, 3, add, 7),
    (7, 2, subtract, 5),
    (6, 3, multiply, 18),
    (81, 9, divide, 9),
    (5.5, 4.5, add, 10),
    (7.5, 4.3, subtract, 3.2),
    (1.5, 2.0, multiply, 3.0),
    (3.5, 1.75, divide, 2),
])

def test_calculations(a_, b_, operation, expected):
    '''Testing all calculations'''
    test = Calculation(a_, b_, operation)
    assert test.get_result() == expected
