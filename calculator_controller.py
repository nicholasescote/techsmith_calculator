from calculator_model import CalculatorModel

"""
controller for the calculator 
handles calculator functionality 
"""
class CalculatorController:

    def __init__(self):
        self.expression = ""
        self.operator = ""
        self.calculator = CalculatorModel()

    # returns expression value 
    def get_expression(self):
        return self.expression
    
    # returns operator 
    def get_op(self):
        return self.operator

    # sets operator for equation
    def set_op(self, value):
        self.operator = value

    # adds character to expresion on button press
    def add_expression(self, character):
        self.expression += character
    
    # sets expression as a whole
    def set_expression(self, expression):
        self.expression = expression

    # clears calculator
    def clear(self):
        self.calculator.clear()
        self.expression= ""
        self.operator = ""

    # seperates parts of expression to pass to calculate to operate 
    def separate_equation(self):
        # separate if the there are two numbers and an operator  
        if self.operator != "" and self.expression[-1] not in '+-/*':
            ind = self.expression.find(self.operator)
            # edit here for decimals 
            self.calculator.set_first(int(self.expression[:ind]))
            # issue here if operator not found (returns -1)
            self.calculator.set_second(int(self.expression[ind+1:]))
            self.calculator.set_op(self.operator)
        # returns first number if there is no second number
        elif self.expression[-1] in '+-/*':
            self.calculator.set_first(int(self.expression[:-1]))
            self.set_op("")
        else:
            self.calculator.set_first(int(self.expression))

    # evaluates the function using the calculator class 
    def evaluate(self):
        solution = self.calculator.evaluate()
        self.expression = str(solution)

    

    