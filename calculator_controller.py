from calculator_model import CalculatorModel

"""
controller for the calculator 
handles calculator functionality 
"""
class CalculatorController:

    def __init__(self):
        self.exression = ""
        self.operator = ""
        self.calculator = CalculatorModel()

    def get_expression(self):
        return self.expression

    def add_expression(self, character):
        self.expression.append(character)

    def clear(self):
        self.calculator.clear()

    def separate_equation(self):
        ind = self.equation.find(self.operator)
        self.calculator.set_first(int(self.equation[:ind]))
        self.calculator.set_second(int(self.equation[ind+1:]))
        self.calculator.set_op(self.operator)
    
    def evaluate(self):
        solution = self.calculator.evaluate()

    

    