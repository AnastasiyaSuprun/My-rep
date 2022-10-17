# Calculator

class MyError(Exception):
    """This class warns that my calculator can't raise numbers to a power"""

    def __init__(self, err):
        self.err = err


my_err = MyError("I can't raise a number to a power!!!")


while True:
    try:
        num_1 = float(input("Enter first number: "))
    except ValueError:
        print("Please enter numbers, not strings!!!")
    else:
        try:
            operation = input("Enter operation: ")
            num_2 = float(input("Enter second number: "))
            if operation == "+":
                print("Result: ", num_1 + num_2)
            elif operation == "-":
                print("Result: ", num_1 - num_2)
            elif operation == "*":
                print("Result: ", num_1 * num_2)
            elif operation == "/":
                print("Result: ", num_1 / num_2)
            elif operation == "**":
                print(my_err)
                continue
            else:
                print("Wrong operator!!!")
                continue
        except ZeroDivisionError:
            print("You can't divide by zero!!!")
        except ValueError as error:
            print("Please, enter only numbers, not strings!!!")
        else:
            print("No errors found!!!")





