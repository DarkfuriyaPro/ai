first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

def addition(a, b):
    return a+b
def subtraction(a, b):
    return a-b
def multiplication(a, b):
    return a*b
def division(a, b):
    if b == 0:
        return "Immpossible"
    else:
        return a/b

if operation == "+":
    result =  addition(first, second)
elif operation == "-":
    result = subtraction(first, second)
elif operation == "*":
    result = multiplication(first, second)
elif operation == "/":
    result = division(first, second)
else:
    result = None
    print("Unknown command.")

print(f"Result: {result}")