a = float(input("Enter first number: ")) # taking input from user
b = float(input("Enter second number: "))  #tale input from user

operator = input("Enter operator: ")  # enter the operator

if operator == "+":  # addition
    print("Result:", a + b)

elif operator == "-": #subtraction
    print("Result:", a - b)

elif operator == "*": # multipication
    print("Result:", a * b)

elif operator == "/": #division
        print("Result:", a / b)
else:
    print("Invalid operator")