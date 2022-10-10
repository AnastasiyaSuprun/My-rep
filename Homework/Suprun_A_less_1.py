# Calculator

num_1 = float(input("Enter first number: "))
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

input()
