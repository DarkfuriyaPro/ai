import sys

first = int(sys.argv[1])
op = sys.argv[2]
second = int(sys.argv[3])

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Impossible"
    return a / b

if op == "+":
    result = add(first, second)

elif op == "-":
    result = sub(first, second)

elif op == "*":
    result = mul(first, second)

elif op == "/":
    result = div(first, second)

else:
    result = "Unknown operation"

print(f"Result: {result}")