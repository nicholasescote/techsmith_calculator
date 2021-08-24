
"""
handles data and logic 
"""

class CalculatorModel:

    def __init__(self):
        self.first = 0
        self.second = 0 
        self.operator = ""

    # setter for first number in equation
    def set_first(self, val):
        self.first = val

    # setter for second number in equation
    def set_second(self, val):
        self.second = val

    # setter for operation character that detwermines the operation to perform 
    def set_op(self, val):
        self.operator = val

    # returns the first value of the equation
    # used to continue operations on an answer 
    def get_first(self):
        return self.first

    # resets the calculator
    def clear(self):
        self.first = 0
        self.second = 0
        self.operator = ""

    # evaluates the function based on the infor passed into the calculator
    def evaluate(self):
        # solution to return 
        solution = self.first

        # returns first input if the user hits "=" button or no second input 
        if self.operator == "" or self.second == 0:
            return self.first

        # addition operation
        elif self.operator == "+":
            solution += self.second

        # subtraction operation
        elif self.operator == "-":
            solution -= self.second

        # multiplication operation
        elif self.operator == "*":
            solution *= self.second

        # division operation
        elif self.operator == "/":
            solution //= self.second

        # clears calculator and sets solution as first value to continue operation
        self.clear()
        self.first = solution

        return solution

# test cases
"""
def main():
    # test cases for addition
    calc = CalculatorModel()
    calc.set_first(1)
    calc.set_second(1)
    calc.set_op("+")
    print(calc.evaluate()) # expected value 2
    print(calc.evaluate()) # expected value 2 becuase maintains state 

    calc.clear()
    print(calc.evaluate()) # expected value 0

    # test cases for multiplication
    calc.set_first(10)
    calc.set_second(5)
    calc.set_op("*")
    print(calc.evaluate()) # expected value 50

    calc.clear()
    print(calc.evaluate()) # expected value 0
    
    #test cases for division
    calc.set_first(99)
    calc.set_second(3)
    calc.set_op("/")
    print(calc.evaluate()) # expected value 33

    calc.clear()
    print(calc.evaluate()) # expected value 0
    
    #test cases for division
    calc.set_first(150)
    calc.set_second(51)
    calc.set_op("-")
    print(calc.evaluate()) # expected value 99

    #test for continuing operationg
    calc.set_second(51)
    calc.set_op("-")
    print(calc.evaluate()) #expected value 48



if __name__ == "__main__":
    # execute only if run as a script
    main()

"""