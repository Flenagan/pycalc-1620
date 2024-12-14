# the brain of the operation contains all the logical parts.

import math
from PyQt6.QtCore import pyqtSignal, QObject


#Class containing the functionality of the entire calculator.
class CalcLogic(QObject):
    """
    A class containing the functionality of the entire calculator, refer to comments below for
    more information about this amazing brain!
    "Well it works now doesn't it!"
    """

    #updates the calculator display label.
    update_display_signal = pyqtSignal(str)

    def __init__(self) -> None:
        """
        init function for calc logic.
        """
        super().__init__()
        self.math_expression = ""

        #Max amount of char that looks good on the display
        self.max_length = 13 #Maximum characters to display

    def append_expression(self, value: str) -> None:
        """
        Appends the last inputted value to the expression.
        :param value:
        :return:
        """

        #Checking if length is less than max_length
        if len(self.math_expression) < self.max_length:
            self.math_expression += value
        self.update_display_signal.emit(self.math_expression[:self.max_length])

    def clear_expression(self) -> None:
        """
        Clears the expression and reverts back to an empty string for new input.
        :return:
        """
        #sets the expression to a empty string.
        self.math_expression = ""
        self.update_display_signal.emit(self.math_expression)

    def evaluate_expression(self) -> None:
        """
        Evaluates the expression, must replace certain characters before expression can be evaluated.
        :return:
        """
        try:
            # Replaces the calculator symbols with python compatible math symbols.
            usable_expressions = (
                self.math_expression
                .replace("×", "*")
                .replace("÷", "/")
                .replace("^", "**")
                .replace("π", str(math.pi))
                .replace("√", "math.sqrt")
            )

            result = eval(usable_expressions)
            self.math_expression = str(result)[:self.max_length]
            self.update_display_signal.emit(self.math_expression)

        except Exception as e:
            self.math_expression = "Error"
            self.update_display_signal.emit(self.math_expression)

    def parenthesis(self, paren: str) -> None:
        """
        Allows you to add parenthesis to the expression.
        :param paren:
        :return:
        """
        self.append_expression(paren)

    #Add the constant pi to expression.
    def add_pi(self) -> None:
        """
        Adds pi to the expression.
        :return:
        """
        self.append_expression("π")

    #Square root symbol, still needs closing parenthesis after inputted numbers tho, try and fix.
    def square_root(self) -> None:
        """
        Allows you to add square root symbol to the expression.
        :return:
        """
        self.append_expression("√(")

    #Caret added for powers and readability.
    def power_function(self) -> None:
        """
        Allows you to add a caret symbol for powers.
        :return:
        """
        self.append_expression("^")

    #Allows for decimal input.
    def decimal(self) -> None:
        """
        Allows you to add decimal points to the expression.
        :return:
        """
        self.append_expression(".")

    #Allows for negative input below 0.
    def minus_Sign(self) -> None:
        """
        Allows you to add minus signs to the expression.
        """
        self.append_expression("-")

    #Handles the trigonometric functions and their calculations
    def trig_function(self, function: str) -> None:
        """
        Handles the input and applies the trig functions to the expression.
        Must be pressed after the something is input. No parenthesis only raw numbers.
        Outputs only in radians, the better unit.
        :param function:
        :return:
        """

        try:
            value = eval(self.math_expression)

            if function == "sin":
                result = math.sin(value)

            elif function == "cos":
                result = math.cos(value)

            elif function == "tan":
                result = math.tan(value)

            else:
                raise ValueError

            #Sends info and changes value type
            self.math_expression = str(result)
            self.update_display_signal.emit(self.math_expression)

        except:
            self.math_expression = "Input value!"
            self.update_display_signal.emit(self.math_expression)

    #Function containing the inverse trigonometric functions and their calculations
    def inverse_trig_function(self, function: str) -> None:
        """
        Handles the input and applies the inverse trig functions to the expression.
        Must be pressed after the something is input. No parenthesis only raw numbers.
        Outputs only in radians, the better unit.
        :param function:
        """
        try:
            value = eval(self.math_expression)  # Evaluate the current input first

            #Logic for determining which function to use for input.
            if function == "arcsin":
                if -1 <= value <= 1:
                    result = math.asin(value)
                    self.math_expression = str(result)
                    self.update_display_signal.emit(self.math_expression)

                #Handles input outside domain of arcsin
                else:
                    self.math_expression = "Outside domain"
                    self.update_display_signal.emit(self.math_expression)


            elif function == "arccos":
                if -1 <= value <= 1:
                    result = math.acos(value)
                    self.math_expression = str(result)
                    self.update_display_signal.emit(self.math_expression)

                #Handles input outside domain of arccos
                else:
                    self.math_expression = "Outside domain"
                    self.update_display_signal.emit(self.math_expression)

            elif function == "arctan":
                result = math.atan(value)
                self.math_expression = str(result)
                self.update_display_signal.emit(self.math_expression)

        except:
            self.math_expression = "Input Value!"
            self.update_display_signal.emit(self.math_expression)

