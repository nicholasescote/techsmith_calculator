from tkinter import *
from calculator_controller import CalculatorController

"""
handles ui elements of calculator
"""
class CalculatorView:
    
    def __init__(self, view, controller):
        self.controlller = controller
        self.view = view
        view.title("Calculator")
        view.geometry("320x568")
        view.resizable(0,0)        

    def button_press(self, value):
        self.controlller.add_expression(value)

    def button_operator(self,value):
        self.button_press(value)
        self.controlller.set_op

    def button_clear(self):
        self.controlller.clear()

    def button_equal(self):
        self.controlller.separate_equation()
        self.controlller.evaluate()

root = Tk()
controller = CalculatorController()
my_gui = CalculatorView(root)
root.mainloop()
