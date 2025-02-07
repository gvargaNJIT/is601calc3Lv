#Calculator Test
from calculator import Calculator

def test_addition():
    #Testing addition
    assert Calculator.add(2,2) == 4

def test_subtraction():
    #Testing subtraction
    assert Calculator.subtract(3,1) == 2

def test_multiply():
    #Testing multiplication
    assert Calculator.multiply(3,4) == 12

def test_divide():
    #Testing division
    assert Calculator.divide(4,2) == 2

def test_undefined(capsys):
    #Testing dividing by zero
    Calculator.divide(2,0)
    captured = capsys.readouterr()
    assert captured.out == "Undefined\n"
