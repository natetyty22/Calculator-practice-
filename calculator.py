#testing out pull requests
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# Ask the user
print("Simple Calculator")
print("Choose operation: +, -, *, /")
operation = input("Operation: ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Perform the operation
if operation == '+':
    result = add(a, b)
elif operation == '-':
    result = subtract(a, b)
elif operation == '*':
    result = multiply(a, b)
elif operation == '/':
    result = divide(a, b)
else:
    result = "Invalid operation"

print("Result:", result)

