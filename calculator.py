"""
The Calculator class takes two numbers when it is created and stores them as private attributes.
It provides methods to add, subtract, multiply, and divide those numbers.
Before dividing, it checks whether the second number is zero and raises a ZeroDivisionError if it is.
"""

class Calculator:

    def __init__(self, op1: float, op2: float):
       self.__op1 = op1
       self.__op2 = op2

    def sum(self):
        return self.__op1 + self.__op2

    def subtract(self):
        return self.__op1 - self.__op2

    def multiply(self):
        return self.__op1 * self.__op2

    def divide(self):
        if self.__op2 == 0:
            raise ZeroDivisionError("Divide by zero")
        return self.__op1 / self.__op2
