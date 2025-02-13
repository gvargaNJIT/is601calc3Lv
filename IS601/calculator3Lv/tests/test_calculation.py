'''Calculation Definition Test'''


from calculator.calculation import Calculation


def test_calculations(a, b, operation, expected):
    '''Testing all calculations'''
    test = Calculation(a, b, operation)
    assert test.get_result() == expected
