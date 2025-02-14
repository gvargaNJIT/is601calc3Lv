'''Calculator Test'''

from calculator import Calculator

def test_addition():
    '''Testing addition'''
    assert Calculator.add(2.0,2.0) == 4.0

def test_subtraction():
    '''Testing subtraction'''
    assert Calculator.subtract(3.0,1.0) == 2.0

def test_multiply():
    '''Testing multiplication'''
    assert Calculator.multiply(3.0,4.0) == 12.0

def test_divide():
    '''Testing division'''
    assert Calculator.divide(4.0,2.0) == 2.0
