
"""
handles data and logic 
"""
import tkinter


class CalculatorModel(self):

    def __init__(self):
        self.first = 0
        self.second = 0 
        self.operator = ""

    def set_first(self, val):
        self.first = val

    def set_second(self, val):
        self.second = val

    def get_first(self):
        return self.first

    def operate(self):
        if self.operation == "+":
            self.first += self.second
            return self.first + self.second

        elif self.operation == "-":
            return self.first - self.second

        elif self.operation == "*":
            return self.first * self.second

        elif self.operation == "/":
            return 
