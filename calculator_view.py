from tkinter import *
from tkinter.ttk import *
from calculator_controller import CalculatorController

"""
handles ui elements of calculator
resources:
https://stackoverflow.com/questions/34366068/python-tkinter-rowspan-not-resizing-elements-correctly

"""
class CalculatorView:
    
    def __init__(self, view, controller):
        # initializing conroller to use calculator logic
        self.controller = controller
        # establishing tkinter object to use for UI
        self.view = view
        # set title and fixed size of calculator
        view.title("Calculator")
        view.geometry("280x320")
          


        # define button styles depending on button type 
        number_style = Style() 
        operator_style = Style()
        label_style = Style()

        # sets the style attributes
        number_style.configure('W.TButton', bg=100, height=6, width=4, sticky=E+W+S+N)
        label_style.configure('W.TLabel', rowspan=1, columnspan=4, bd=2,sticky=E+W+S+N)
        

        # initializing Tkinter string object to be displayed in the calculator 
        self.display_text = StringVar()

        # set equal to variable in conroller 
        self.display_text.set(self.controller.get_expression())   
        self.display = Label(master=self.view, style='W.TLabel', textvariable=self.display_text)
        self.label = Label(view, text="Total:")

        #initializing all the buttons of the calculator 
        self.one_button = Button(view, text="1", style='W.TButton', command= lambda: self.button_press("1"))
        self.two_button = Button(view, text="2", style='W.TButton', command= lambda: self.button_press("2"))
        self.three_button = Button(view, text="3", style='W.TButton', command= lambda: self.button_press("3"))
        self.four_button = Button(view, text="4", style='W.TButton', command= lambda: self.button_press("4"))
        self.five_button = Button(view, text="5", style='W.TButton', command= lambda: self.button_press("5"))
        self.six_button = Button(view, text="6", style='W.TButton', command= lambda: self.button_press("6"))
        self.seven_button = Button(view, text="7", style='W.TButton', command= lambda: self.button_press("7"))
        self.eight_button = Button(view, text="8", style='W.TButton', command= lambda: self.button_press("8"))
        self.nine_button = Button(view, text="9", style='W.TButton', command= lambda: self.button_press("9"))
        self.zero_button = Button(view, text="0", style='W.TButton', command= lambda: self.button_press("0"))

        self.add_button = Button(view, text="+", style="W.TButton", command= lambda: self.button_operator("+"))
        self.subtract_button = Button(view, text="-", style="W.TButton", command= lambda: self.button_operator("-"))
        self.multiply_button = Button(view, text="*", style="W.TButton", command= lambda: self.button_operator("*"))
        self.divide_button = Button(view, text="/", style="W.TButton", command= lambda: self.button_operator("/"))

        self.equal_button = Button(view, text="=", style="W.TButton", command= lambda: self.button_equal())
        self.clear_button = Button(view, text="C", style="W.TButton", command=lambda: self.button_clear())


        #layout below this comment 


        # placing the buttons on the tkinter grid
        self.label.grid(row=0, column=0, sticky=W)
        self.display.grid(row=0, column=1, sticky=W)

        self.one_button.grid(row=4, column=0)
        self.two_button.grid(row=4, column=1)
        self.three_button.grid(row=4, column=2)
        self.four_button.grid(row=3, column=0)
        self.five_button.grid(row=3, column=1)
        self.six_button.grid(row=3, column=2)
        self.seven_button.grid(row=2, column=0)
        self.eight_button.grid(row=2, column=1)
        self.nine_button.grid(row=2, column=2)
        self.zero_button.grid(row=5, column=1)

        self.add_button.grid(row=1, column=3)
        self.subtract_button.grid(row=2, column=3)
        self.multiply_button.grid(row=3, column=3)
        self.divide_button.grid(row=4, column=3)
        self.equal_button.grid(row=5, column=3)
        self.clear_button.grid(row=1, column=2)

    # functions for button press 
    # adds passed in value to the expression
    def button_press(self, value):
        self.controller.add_expression(value)
        self.display_text.set(self.controller.get_expression())
        # could change to add character to first or second depensing if operator exists
        # this helps with clear/AC

    # functon for any operator button press
    def button_operator(self,value):
        #prevents users from replacing number with operator 
        if self.controller.get_op() != "" and self.controller.get_expression()[-1] not in '+-/*':
            return None
        # allows user to to use operation button only if there is a first parameter 
        if self.controller.get_op() == "" and self.controller.get_expression() != "":
            self.button_press(value)
        # user can change the operation if operation is the last thing they clicked 
        elif self.controller.get_expression()[-1] in '+-/*':
            self.controller.set_expression(self.controller.get_expression()[:-1] + value)
            self.display_text.set(self.controller.get_expression())
        self.controller.set_op(value)

    # operation for clear button
    def button_clear(self):
        self.controller.clear()
        self.display_text.set(self.controller.get_expression()) 

    # operation for equals button
    def button_equal(self):
        self.controller.separate_equation()
        self.controller.evaluate()
        self.display_text.set(self.controller.get_expression()) 


# runs the calculator
root = Tk()
controller = CalculatorController()
my_gui = CalculatorView(root, controller)
root.mainloop()
