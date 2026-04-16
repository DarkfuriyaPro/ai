import sys

if len(sys.argv) != 4:
    print("Usage: python app.py <command> <a> <b>")
    exit()

command = sys.argv[1]
try:
    a = int(sys.argv[2])
    b = int(sys.argv[3])
except ValueError:
    print("Numbers must be integers")
    exit()

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

if command == "add":
    result = add(a, b)

elif command == "sub":
    result = sub(a, b)

elif command == "mul":
    result = mul(a, b)

elif command == "div":
    result = div(a, b)

else:
    result = "Unknown operation"

print(f"Result: {result}")