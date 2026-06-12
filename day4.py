# Day 4 - Functions
# Calculator with Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def calculate(a, operation, b):
    if operation == "+":
        return add(a, b)
    elif operation == "-":
        return subtract(a, b)
    elif operation == "*":
        return multiply(a, b)
    elif operation == "/":
        return divide(a, b)
    else:
        return "Error: Unknown operation"

# Main program
print("🧮 Python Calculator")
print("---")

while True:
    num1 = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    result = calculate(num1, op, num2)
    print("Answer:", result)
    print("---")

    again = input("Calculate again? (yes/no): ")
    if again.lower() != "yes":
        print("Goodbye! 👋")
        break