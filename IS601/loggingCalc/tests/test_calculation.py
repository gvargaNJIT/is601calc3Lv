'''Calculation Definition Test'''

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import divide


def test_calculations(a, b, operation, expected):
    '''Testing all calculations'''
    test = Calculation(a, b, operation)
    assert test.get_result() == expected

def test_undefined():
    '''Testing dividing by zero'''
    division_zero = Calculation(Decimal('3'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Undefined"):
        division_zero.get_result()
