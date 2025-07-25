# The calculator app

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def get_operator(op):
    if op == '+':
        return add
    elif op == '-':
        return sub
    elif op == '*':
        return mul
    elif op == '/':
        return div
    else:
        return None

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter an operation (+, -, *, /): ")

operation = get_operator(op)
if operation:
    result = operation(a, b)
    print(f"Result: {result}")
else:
    print("Invalid operation! Please use one of: +, -, *, /")
