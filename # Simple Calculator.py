# Simple Calculator
num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))
print("Choose an operation:")
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")
operation = input(": ")

if operation == "+":
    result = num1 + num2
    print(f"The result is: {result}")
elif operation == "-":
    result = num1 - num2
    print(f"The result is: {result}")
elif operation == "*":
    result = num1 * num2
    print(f"The result is: {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please try again.")