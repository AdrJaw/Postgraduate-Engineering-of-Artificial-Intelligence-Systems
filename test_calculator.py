"""
This program contains automated tests for a Calculator class using pytest.
It checks that addition, subtraction, multiplication, and division return the expected results for positive numbers.
It also includes a test to confirm that dividing by zero raises a ZeroDivisionError.
Several tests for operations involving negative numbers are currently commented out, so they will not run.
"""


import pytest
from calculator import Calculator

# positive tests
def test_sum():
    assert Calculator(10,2).sum() == 12

def test_subtract():
    assert Calculator(10,2).subtract() == 8

def test_multiply():
    assert Calculator(10,2).multiply() == 20

def test_divide():
    assert Calculator(10,2).divide() == 5

# negative tests
#
# def test_sum_neg():
#     assert Calculator(10, -2).sum() == -12
#
# def test_subtract_neg():
#     assert Calculator(10, -2).subtract() == -22
#
# def test_multiply_neg():
#     assert Calculator(10, -2).multiply() == -2

def test_divide_neg():
    with pytest.raises(ZeroDivisionError):
        Calculator(10, 0).divide()
